# 通用 Agent 平台适配契约 (AGENTS.md)

本文档是 `xiaodai-illustrations` 在通用 Agent 环境（如 **Claude Code**, **OpenAI/Codex**, **Cursor**, **Windsurf**, **Roo Code**, 以及基于终端的 CLI Agents）下的执行契约。

---

## 1. 生图工具调用规范

不同 Agent 环境配备的外部生图能力各不相同，Agent 遵循以下优先级调用：

1. **宿主配置的生图 MCP Server**：
   - 若环境接入了生图 MCP 工具（如 `mcp-server-imagen`、`dall-e` 等），优先调用 MCP 工具进行自动化生图。
2. **本地自动化脚本**：
   - 若宿主具备终端执行权限且配置了本地生图脚本（如 Python 包装脚本），通过终端命令调用。
3. **纯提示词交付模式 (Fallback)**：
   - 若当前 Agent 环境未接入任何自动化生图工具，Agent 应完整输出结构化的英文生图 Prompt（基于 `references/prompt-template.md` 填充）与中文场景说明，方便用户复制到 Web 端、Midjourney 或其他绘图平台中生成。

---

## 2. 参考图与 IP 一致性锁定

- **支持参考图输入的环境**（Image Input / Character Reference / IP-Adapter）：
  - 必须优先将仓库中的标准立绘 `assets/standard-xiaodai.png` 作为唯一角色参考图送入生图接口，以锁定单体火焰剪影与两点小白眼特征。
- **纯文本提示词环境**：
  - 必须在生成的 Prompt 中完整带入 `references/user-ip.md` 中的所有硬约束，特别是：
    - `The red flame silhouette is the entire body, no torso under the flame`
    - `Two tiny white-dot eyes clearly visible`
    - `Thin black stick-figure limbs attached directly to the flame silhouette edge`

---

## 3. 文件输出与交付规范

- 生成的图片统一保存至用户工作空间下的：
  ```text
  outputs/<article-slug>-illustrations/
  ```
- 命名按顺序编号：
  ```text
  01-topic-name.png
  02-topic-name.png
  ```
- 在对话中向用户交付简明清单：
  - 场景判断（`scene_mode`）与画幅建议（`canvas_ratio`）
  - 图片保存路径（绝对/相对路径）
  - 核心物理隐喻与对应文章段落建议
