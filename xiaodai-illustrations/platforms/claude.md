# Claude Code 平台适配指南

本文档是 `xiaodai-illustrations` 在 **Claude Code** 或基于终端的 Agent CLI 环境下的执行契约。

---

## 1. 生图工具调用

在 Claude Code 环境中，通常通过以下方式之一触发图像生成：
1. **配置好的生图 MCP Server**（如 `mcp-server-imagen`、`dall-e` 等工具）；
2. **本地脚本或命令行工具**（如调用 Python 包装脚本生成并保存至本地）；
3. **纯提示词输出模式**：若未配置自动化生图工具，则输出标准英文生图 Prompt 与中文说明，供用户复制到 Midjourney / DALL-E / Web 端生成。

## 2. 参考图处理

- 若使用的生图 MCP 工具支持参考图（Image Input / Character Reference / IP-Adapter），请上传或传入本仓库中的 `assets/standard-xiaodai.png` 作为角色基准。
- 若工具不支持参考图输入，提示词中必须格外强调角色硬约束（单体火焰剪影、无独立躯干、两只微小白点眼睛）。

## 3. 文件输出与组织

- 生成的图片统一保存至用户工作目录下的：
  ```text
  outputs/<article-slug>-illustrations/
  ```
- 命名按顺序组织：
  ```text
  01-topic-name.png
  02-topic-name.png
  ```
- 在终端向用户输出交付清单，包含：
  - 场景模式与画幅
  - 图片保存的绝对/相对路径
  - 核心隐喻与对应文章段落建议
