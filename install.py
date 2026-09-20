#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
xiaodai-illustrations 多 Agent 一键安装与同步脚本
支持平台:
  - antigravity: Google Antigravity 全局技能目录 (~/.gemini/config/skills/xiaodai-illustrations)
  - claude: Claude Code 技能目录 (~/.claude/skills/xiaodai-illustrations)
  - custom: 用户指定目录 (--path)

安装模式:
  - link (默认推荐): 创建软链接或目录连接 (Windows Junction)，修改仓库源码实时生效。
  - copy: 完整拷贝技能文件副本到目标目录。
"""

import argparse
import os
import platform
import shutil
import subprocess
import sys
from pathlib import Path

# 确保在 Windows 控制台下的 UTF-8 兼容性
if sys.stdout and hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

# 仓库中技能主目录
REPO_ROOT = Path(__file__).resolve().parent
SKILL_SOURCE_DIR = REPO_ROOT / "xiaodai-illustrations"

DEFAULT_TARGETS = {
    "antigravity": Path.home() / ".gemini" / "config" / "skills" / "xiaodai-illustrations",
    "claude": Path.home() / ".claude" / "skills" / "xiaodai-illustrations",
}


def is_junction_or_symlink(path: Path) -> bool:
    """判断路径是否是软链接或 Windows Junction"""
    if not path.exists() and not path.is_symlink():
        return False
    if path.is_symlink():
        return True
    # Windows Junction 检测
    if platform.system() == "Windows":
        try:
            return bool(os.readlink(str(path)))
        except (OSError, ValueError):
            pass
    return False


def get_link_target(path: Path) -> str:
    """获取软链接或 Junction 指向的目标"""
    try:
        return str(os.readlink(str(path)))
    except Exception:
        return "未知"


def check_status():
    """检查各宿主环境下的安装状态"""
    print("\n=== xiaodai-illustrations 安装状态检查 ===")
    print(f"源码目录: {SKILL_SOURCE_DIR}")
    if not SKILL_SOURCE_DIR.exists():
        print("  [ERROR] 源码目录不存在，请检查仓库完整性！")
        return

    for name, target_path in DEFAULT_TARGETS.items():
        print(f"\n[{name.upper()}] 目标路径: {target_path}")
        if not target_path.exists():
            print("  状态: 未安装")
        else:
            if is_junction_or_symlink(target_path):
                link_to = get_link_target(target_path)
                is_current_repo = str(SKILL_SOURCE_DIR).lower() in link_to.lower()
                status_desc = "已链接至当前仓库 (实时更新)" if is_current_repo else f"链接至其他路径: {link_to}"
                print(f"  状态: [Junction/Symlink] {status_desc}")
            else:
                print("  状态: [物理拷贝副本] 独立目录 (更新需重新同步)")
            
            # 校验核心文件
            skill_md = target_path / "SKILL.md"
            platforms_ag = target_path / "platforms" / "antigravity.md"
            platforms_agents = target_path / "platforms" / "AGENTS.md"
            status_skill = "[OK]" if skill_md.exists() else "[MISSING]"
            status_ag = "[OK]" if platforms_ag.exists() else "[MISSING]"
            status_agents = "[OK]" if platforms_agents.exists() else "[MISSING]"
            print(f"  核心文件: SKILL.md {status_skill}, antigravity.md {status_ag}, AGENTS.md {status_agents}")


def remove_target(target_path: Path, dry_run: bool = False):
    """安全移除目标目录或链接"""
    if not target_path.exists() and not target_path.is_symlink():
        return

    print(f"正在清理旧目标: {target_path}")
    if dry_run:
        print("  [Dry-run] 跳过实际删除")
        return

    if is_junction_or_symlink(target_path):
        if platform.system() == "Windows":
            try:
                os.rmdir(target_path)
            except OSError:
                subprocess.run(["cmd", "/c", "rmdir", str(target_path)], check=True)
        else:
            target_path.unlink()
    else:
        shutil.rmtree(target_path)


def install_link(source_dir: Path, target_path: Path, dry_run: bool = False):
    """使用链接模式安装（Windows Junction 或 Unix Symlink）"""
    print(f"链接模式: {source_dir} -> {target_path}")
    if dry_run:
        print("  [Dry-run] 跳过实际创建")
        return

    target_path.parent.mkdir(parents=True, exist_ok=True)
    remove_target(target_path, dry_run=False)

    if platform.system() == "Windows":
        # Windows 使用 mklink /J 创建目录连接（无需管理员权限）
        cmd = ["cmd", "/c", "mklink", "/J", str(target_path), str(source_dir)]
        res = subprocess.run(cmd, capture_output=True, text=True)
        if res.returncode != 0:
            print(f"  [WARN] mklink /J 失败: {res.stderr.strip()}，尝试标准 symlink...")
            try:
                os.symlink(source_dir, target_path, target_is_directory=True)
            except OSError as e:
                print(f"  [ERROR] 创建链接失败: {e}")
                print("  建议回退至 copy 模式: python install.py --mode copy")
                sys.exit(1)
        else:
            print("  成功创建 Windows 目录连接 (Junction)")
    else:
        os.symlink(source_dir, target_path, target_is_directory=True)
        print("  成功创建符号链接 (Symlink)")


def install_copy(source_dir: Path, target_path: Path, dry_run: bool = False):
    """使用完整复制模式安装"""
    print(f"复制模式: {source_dir} -> {target_path}")
    if dry_run:
        print("  [Dry-run] 跳过实际复制")
        return

    target_path.parent.mkdir(parents=True, exist_ok=True)
    remove_target(target_path, dry_run=False)
    shutil.copytree(source_dir, target_path)
    print("  成功复制全部技能文件")


def main():
    parser = argparse.ArgumentParser(description="xiaodai-illustrations 多 Agent 一键安装与同步工具")
    parser.add_argument(
        "--target",
        choices=["antigravity", "claude", "custom"],
        default="antigravity",
        help="目标 Agent 环境 (默认: antigravity)",
    )
    parser.add_argument(
        "--path",
        type=Path,
        default=None,
        help="当 --target custom 时指定目标路径",
    )
    parser.add_argument(
        "--mode",
        choices=["link", "copy"],
        default="link",
        help="安装模式: link (Junction/软链接，源码实时生效) 或 copy (物理复制，独立副本)",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="检查当前各平台安装与链接状态",
    )
    parser.add_argument(
        "--uninstall",
        action="store_true",
        help="卸载指定 target 的技能",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="演练模式，仅打印动作不执行",
    )

    args = parser.parse_args()

    if args.check:
        check_status()
        return

    # 确定目标目录
    if args.target == "custom":
        if not args.path:
            print("[ERROR] 当 --target 为 custom 时，必须通过 --path 指定路径！")
            sys.exit(1)
        target_path = args.path.resolve()
    else:
        target_path = DEFAULT_TARGETS[args.target]

    if args.uninstall:
        print(f"正在从 [{args.target}] 卸载技能: {target_path}")
        remove_target(target_path, dry_run=args.dry_run)
        print("卸载完成。")
        return

    print(f"=== 开始部署 xiaodai-illustrations 到 [{args.target}] ===")
    if not SKILL_SOURCE_DIR.exists():
        print(f"[ERROR] 源目录不存在: {SKILL_SOURCE_DIR}")
        sys.exit(1)

    if args.mode == "link":
        install_link(SKILL_SOURCE_DIR, target_path, dry_run=args.dry_run)
    else:
        install_copy(SKILL_SOURCE_DIR, target_path, dry_run=args.dry_run)

    print("\n部署完成！校验结果:")
    check_status()


if __name__ == "__main__":
    main()
