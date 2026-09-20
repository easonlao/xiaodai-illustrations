# Antigravity 平台适配指南

本文档是 `xiaodai-illustrations` 在 **Google Antigravity** 环境下的专有执行契约。
当 Agent 运行在 Antigravity 环境中时，涉及图像生成、质量自检、工件交付与工作区联动均以本文档为准。

---

## 1. 原生生图工具映射 (`generate_image`)

在 Antigravity 中，严禁调用虚构的 `image_gen` 或外部命令，必须统一调用原生工具 **`generate_image`**。

### 参数传入规范

| 参数名 | 类型 | 规范与取值 | 说明 |
| :--- | :--- | :--- | :--- |
| **`Prompt`** | `string` | 填入根据 `prompt-template.md` 生成的英文提示词 | 包含核心动作、隐喻、纯白手绘、中文手写标注等 |
| **`ImageName`** | `string` | **必须全部小写、下划线连接、最多 3 个英文单词** | 例如 `xiaodai_broken_cable`, `xiaodai_funnel_sort`, `xiaodai_cover_stop` |
| **`AspectRatio`** | `enum` | 严格映射场景判断结果：<br>• `article_inline` → `'16:9'` 或 `'4:3'`<br>• `social_single` → `'3:4'` 或 `'4:3'`<br>• `feed_cover` → `'3:4'`<br>• `vertical_cover` → `'3:4'` 或 `'9:16'`<br>• 单独头像/卡片 → `'1:1'` | 必须使用枚举字面值，禁止传入非规范文本 |
| **`ImagePaths`** | `array` | **强制传入标准参考图绝对路径**：<br>`["<skill_root>/assets/standard-xiaodai.png"]` | **IP 锁定的核心关键**。Antigravity 会将此图作为多模态参考送入扩散底层，彻底锁定单体火焰剪影、两点小白眼与火柴人四肢 |

> [!TIP]
> `<skill_root>` 可通过当前技能所在物理路径动态获取（如 `C:/Users/eason/.gemini/config/skills/xiaodai-illustrations/assets/standard-xiaodai.png` 或当前项目仓库对应资产路径）。

---

## 2. 视觉多模态质检闭环 (`view_file`)

Antigravity 的 Agent 原生具备多模态图像查看能力。生图完成后，**不得直接盲交**，必须执行一次快速机器质检：

1. **调用 `view_file`**：将 `generate_image` 返回的生成图片绝对路径传入 `view_file` 进行查看。
2. **对照 `references/qa-checklist.md` 进行自检**：
   - **IP 一致性**：小呆是否仍为单体火焰剪影？是否误长出脖子、胸腔或独立下躯干？脸上两个白点眼睛是否清晰可见？
   - **背景与风格**：是否为纯净白底？有无杂乱背景纹理、灰底、3D 渐变或左上角标题框？
   - **中文标注**：文字是否极简且可读，有无不可辨认的乱码？
3. **合格即通过**；若出现严重 IP 漂移（如变成卡通萌偶或水滴人），立即触发重新生成。

---

## 3. 图生图局部迭代（Image-to-Image Refinement）

若初次生成的图片主体构图合格，但存在局部微瑕（例如白点眼睛被弱化、局部线条多余、需要去除某处文字）：
- **不要从零盲抽**，使用图生图迭代：
- 调用 `generate_image` 时，将**上一轮生成的图片绝对路径**填入 `ImagePaths`（最多支持传入 3 张参考图，可同时传入标准立绘与待微调图）。
- 在 `Prompt` 中使用针对性修正指令：
  ```text
  Keep the overall hand-drawn composition, but clearly restore the two tiny white-dot eyes on Xiaodai's red flame silhouette and remove the stray strokes on the right.
  ```

---

## 4. 交付呈现与交互画廊 (Artifact + Carousel)

根据任务规模区分交付方式：

### 单张图交付
在对话中直接输出简明结果：
- 场景判断与画幅参数
- 图片 Markdown 预览：`![Image Description](file:///path/to/image.png)`
- 核心隐喻与使用建议

### 长文成套配图（Shot List 多图交付）
当一次性为长文生成 3~5 张配图时，必须在 Antigravity 脑区创建交付工件（Artifact），并使用 **`carousel`（轮播）语法** 组织：

````markdown
````carousel
![01-断点卡位](file:///C:/Users/eason/.gemini/antigravity/brain/.../xiaodai_broken_point.png)
<!-- slide -->
![02-漏斗分流](file:///C:/Users/eason/.gemini/antigravity/brain/.../xiaodai_funnel_filter.png)
<!-- slide -->
![03-杠杆撬动](file:///C:/Users/eason/.gemini/antigravity/brain/.../xiaodai_lever_push.png)
````
````

在轮播下方附带每张图的对应段落、核心动作与 Obsidian 嵌入代码，用户可在 Antigravity 右侧工件面板中无缝滑动审阅整套视觉叙事。

---

## 5. 工作区联动 (Obsidian / OrbitOS)

当工作区位于 Obsidian / OrbitOS 笔记库时：
1. **归档路径**：建议将最终确定的图片从临时目录复制到用户的文章附件目录（例如 `outputs/<article-slug>-illustrations/` 或对应项目 `assets/` 目录）。
2. **正文回填**：提供标准的 Obsidian 嵌入链接格式：
   ```markdown
   ![[01-xiaodai-broken-point.png]]
   ```
   方便用户直接将配图拖拽或粘贴进长文正文中。
