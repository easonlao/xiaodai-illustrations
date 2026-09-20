---
AIGC:
    Label: "1"
    ContentProducer: 001191110102MACQD9K64018705
    ProduceID: 367649822881267_0-data_volume/7646052380831695119-files/所有对话/主对话/skills/xiaodai-illustrations/README.md
    ReservedCode1: ""
    ContentPropagator: 001191110102MACQD9K64028705
    PropagateID: 367649822881267#1781401824828
    ReservedCode2: ""
---
# 小呆配图 Skill

围绕小呆角色生成纯白手绘、低科技隐喻感的内容配图，并补一个最小竖版适配层。

小呆 IP（小火人形态） | 纯白手绘 | 少量红橙蓝批注 | Agent Skill / Prompt Pack

## 这个仓库是什么

这个仓库的定位，是一套围绕小呆角色展开的配图 skill。

当前重点有两件事：

- 把小呆角色本体锁稳
- 在现有配图能力上补一个最小竖版适配层

它不是要从零发明一整套全新的多场景角色系统，也不是要把每个 scene mode 都重做成独立范式。

默认视觉 IP 是「小呆」：纯手绘亮红色火焰形状实体剪影小人，脸上有一对白色小圆点眼睛，四肢为纤细的黑色火柴人线条。小呆不是吉祥物，不是贴纸，也不是站在角落里的装饰物，而是正在认真参与系统运转的荒诞工作者。

一句话：**先把小呆角色锁稳，再让这套 skill 产出清爽、怪诞、可复用的内容配图，并谨慎补竖版能力。**

## 适合谁用

特别适合：
- 做知识型内容、方法论内容、AI 工作流内容的人
- 想要一种比 PPT 信息图更轻、更怪、更有个人识别度的配图风格的人
- 用 Agent 做内容生产，希望稳定复用同一套视觉语言的人

不适合：
- 想要商业插画、品牌 KV 或精致扁平插画的人
- 想要传统 PPT 信息图、复杂架构图或流程图的人
- 想要儿童卡通、可爱 IP、表情包风格的人
- 想把大量正文、长段解释或完整课程页塞进一张图里的人
- 需要严格可编辑矢量源文件的人

## 当前提供什么

默认输出：
- 小呆角色规则
- 统一的视觉和配图框架
- 一套强调角色稳定性的提示词约束
- 一个最小的 vertical 适配层

默认不输出：
- 一整套重做后的全新场景系统
- 商业海报或封面 KV
- 大段文字型信息图

## 当前边界

当前这套 skill 会定义：

- 小呆角色规则
- 统一的视觉语言
- 最小必要的角色硬约束
- 最小必要的竖版适配规则

当前这套 skill 不会主动去做：

- 把每个场景都重做成独立系统
- 为了追求“严格角色系统”而牺牲原版配图可用性

## 视觉风格

- 纯白背景，不要纸纹、米色、阴影、渐变
- 黑色手绘线稿，细线，轻微抖动
- 大量留白，主体只占画面约 40%-60%
- 少量红色、橙色、蓝色中文手写批注
- 一张图只表达一个核心动作、结构、状态或隐喻
- 小呆必须参与核心动作，不能只是装饰
- 怪诞、有创意、清爽，但不幼稚、不卖萌

## 参考图说明

`xiaodai-illustrations/assets/examples/` 存放 14 张内部风格校准图，用来帮助理解留白、线条密度、颜色克制和隐喻方向。

这些参考图里包含早期角色版本的案例，只能用于观察风格，不要直接模仿角色外形，也不要照抄旧案例的物件和构图。

## 目录结构

```
.
├── README.md                  # 项目说明
├── LICENSE                    # MIT 开源许可
├── NOTICE.md                  # 版权与声明
├── install.py                 # 跨平台多 Agent 一键安装与同步脚本
├── .gitignore
├── xiaodai-illustrations/      # 技能主目录
│   ├── SKILL.md                  # 技能定义与核心指令
│   ├── agents/
│   │   └── openai.yaml            # Agent 接口配置
│   ├── platforms/                 # 宿主平台适配层
│   │   ├── antigravity.md         # Google Antigravity 原生适配指引
│   │   └── claude.md              # Claude Code / 终端 Agent 适配指引
│   ├── assets/                    # 参考图资源
│   │   └── standard-xiaodai.png   # 小呆 IP 标准参考图
│   │   └── examples/              # 14 张风格校准参考图
│   └── references/                # 技能参考文档
│       ├── style-dna.md           # 风格 DNA
│       ├── user-ip.md             # 小呆 IP 定义
│       ├── composition-patterns.md # 构图模式
│       ├── scene-modes.md         # 最小场景适配约束
│       ├── prompt-template.md     # 生图提示词模板
│       └── qa-checklist.md        # 检查清单
├── LICENSE                    # MIT 开源许可
└── NOTICE.md                  # 版权与声明
```

## 多 Agent 支持与一键安装

本项目设计为**跨平台 Agent 技能**。通过根目录的 `install.py`，可以一键将技能部署或软链接至不同 Agent 环境中：

### 1. Google Antigravity
Antigravity 原生支持多模态看图与垫图，使用本仓库的专属适配层可获得最佳 IP 锁定效果：
```bash
# 推荐开发模式：创建软链接/Junction，修改仓库即时在 Antigravity 生效
python install.py --target antigravity --mode link

# 独立副本模式：将完整文件复制到全局技能目录 (~/.gemini/config/skills/)
python install.py --target antigravity --mode copy
```
*Antigravity 专有能力：* 自动绑定 `generate_image`、通过 `ImagePaths` 注入标准立绘防止角色变形、使用 `view_file` 跑 QA 视觉质检、以及使用 Artifacts ````carousel```` 进行长文 Shot List 轮播交付。详见 `xiaodai-illustrations/platforms/antigravity.md`。

### 2. Claude Code
```bash
python install.py --target claude --mode link
```
部署到 `~/.claude/skills/xiaodai-illustrations`，配合生图 MCP 服务或终端脚本使用。详见 `xiaodai-illustrations/platforms/claude.md`。

### 3. 安装状态检查与卸载
```bash
# 检查当前各 Agent 环境下的安装/链接状态与文件完整性
python install.py --check

# 卸载指定环境中的技能
python install.py --target antigravity --uninstall
```

## 使用方式

这个仓库更适合作为一套技能源码与提示词底座使用，而不是某个单一平台上的现成成品。

常见用法：

- 直接在支持技能触发的 Agent 环境中使用仓库里的 `xiaodai-illustrations/SKILL.md`
- 把它作为上层场景 skill 的共用底座
- 仓库内真正的技能主入口是 `xiaodai-illustrations/SKILL.md`、`xiaodai-illustrations/agents/openai.yaml` 以及对应的 `platforms/*.md`

如果你的生图平台支持 `ref_images`、character reference 或 image weight，请同时上传 `xiaodai-illustrations/assets/standard-xiaodai.png` 作为唯一角色参考图，用它来锁定小呆的外形一致性。

如果平台不支持参考图绑定，也可以使用这套提示词，但角色稳定性会低一些。

当前建议优先保持横版正文配图的稳定性；竖版只做最小适配，不把整个 skill 改造成一个完全新的多场景系统。

## 使用示例

### 只做配图规划

```text
Use $xiaodai-illustrations 先不要生图。
请分析下面这篇文章哪里值得配图，输出 5 张左右的 shot list。
每张图写清楚：
- 放在哪个段落后
- 图的主题
- 核心意思
- 结构类型
- 小呆在图里做什么
- 建议元素
- 建议中文标注词

<粘贴文章>
```

### 长文正文场景示例

```text
Use $xiaodai-illustrations 为下面这篇文章设计一组小呆配图方案。
场景：长文正文配图
画幅：16:9 横版
要求：纯白背景、黑色手绘线稿、少量红橙蓝中文手写批注。
每张图只讲一个核心结构，不要做 PPT 信息图，不要可爱卡通。

<粘贴文章>
```

### 只定场景策略

```text
Use $xiaodai-illustrations 先不要生图。
请基于这套小呆配图 skill，为这篇内容判断更适合什么场景：
- article
- feed
- vertical

然后给出建议画幅、主体占比、文字密度和 shot list。

<粘贴文章>
```

### 单个观点生成一张图

```text
Use $xiaodai-illustrations 为这个观点生成一张图：
场景：待你判断
画幅：待你根据场景建议

信任不是喊出来的，而是一块证据一块证据铺过去。

画面要怪诞但清爽，小呆必须承担核心动作。
中文标注最多 5 个，短一点。
```

理想输出顺序：

- 先给出 `scene_mode / format_goal / canvas_ratio / subject_density / structure_type / core_metaphor`
- 再给最终 prompt 或直接生成

而不是一上来就默认写死 `16:9`。

### 工作流主题

```text
Use $xiaodai-illustrations 为"把一条原始素材加工成流量、信任、转化三种内容"生成一张图。
不要画正式流程图，不要复刻一鱼多吃旧案例。
请重新发明一个新的低科技隐喻，让小呆参与核心动作。
```

### 改图：去掉标题

```text
Use $xiaodai-illustrations 帮我编辑这张图。
去掉左上角的"Workflow / 流程图"标题和下划线，其他内容保持不变。
不要新增任何文字或物件。
```

### 改图：增强小呆参与感

```text
Use $xiaodai-illustrations 这张图方向对，但小呆有点像装饰。
请保持核心意思不变，重生成一版：让小呆成为真正推动结构运转的人。
画面更怪一点，但仍然纯白、清爽、少字。
```

### 生成一组风格样片

```text
Use $xiaodai-illustrations 输出 5 个不同主题的小呆配图效果。
主题分别覆盖：信息过载、产品验证、内容复利、一人公司、信任建立。
每张单独生成，不要拼成一张。
你需要先为每个主题判断更合适的场景和画幅，再生成。
```

## License

MIT License. See LICENSE.

---
