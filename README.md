---
AIGC:
    Label: "1"
    ContentProducer: 001191110102MACQD9K64018705
    ProduceID: 367649822881267_0-data_volume/7646052380831695119-files/所有对话/主对话/skills/xiaohei-illustrations/README.md
    ReservedCode1: ""
    ContentPropagator: 001191110102MACQD9K64028705
    PropagateID: 367649822881267#1781401824828
    ReservedCode2: ""
---
# 小呆正文配图

把中文文章里的判断、流程、状态和隐喻，变成一张张纯白手绘、清爽但怪诞的正文配图。

16:9 横版 | 小呆 IP（Q版眼镜男） | 纯白手绘 | 少量红橙蓝中文批注 | Coze/Claw Skill

## 这个仓库是什么

小呆正文配图是一个 Claw Skill，用来指导 AI Agent 为中文文章、帖子、博客、方法论内容生成正文配图。

它不是通用插画 prompt，也不是 PPT 信息图模板。它的核心目标是：先理解文章里的认知锚点，再把其中一个判断、流程、结构、状态或隐喻，变成一张有记忆点的 16:9 手绘解释图。

默认视觉 IP 是「小呆」：Q版东亚男性，黑色蓬松短发发梢向右，细金框圆眼镜，宽松黑T左胸白色小火苗，盘腿坐，认真做一件荒诞但成立的事。小呆不是吉祥物，不是贴纸，也不是站在角落里的装饰物，而是正在认真参与系统运转的荒诞工作者。

一句话：**让 AI 不只是"配一张图"，而是把文章里的一个关键认知动作画出来。**

## 适合谁用

特别适合：
- 写中文文章，需要正文配图和文章插图的人
- 做知识型内容、方法论内容、AI 工作流内容的人
- 想把抽象判断画成具体隐喻的人
- 想要一种比 PPT 信息图更轻、更怪、更有个人识别度的配图风格的人
- 用 Agent 做内容生产，希望稳定复用一套视觉语言的人

不适合：
- 想要商业插画、品牌 KV 或精致扁平插画的人
- 想要传统 PPT 信息图、复杂架构图或流程图的人
- 想要儿童卡通、可爱 IP、表情包风格的人
- 想把大量正文、长段解释或完整课程页塞进一张图里的人
- 需要严格可编辑矢量源文件的人

## 它会产出什么

默认输出：
- 16:9 横版正文配图
- 一篇文章的 4-8 张 shot list
- 每张图的主题、核心意思、结构类型、小呆动作和中文标注建议
- 最终 PNG 图片

默认不输出：
- PPTX / PDF / Keynote
- SVG / HTML / Canvas 可编辑图
- 商业海报或封面 KV
- 大段文字型信息图

## 视觉风格

- 纯白背景，不要纸纹、米色、阴影、渐变
- 黑色手绘线稿，细线，轻微抖动
- 大量留白，主体只占画面约 40%-60%
- 少量红色、橙色、蓝色中文手写批注
- 一张图只表达一个核心动作、结构、状态或隐喻
- 小呆必须参与核心动作，不能只是装饰
- 怪诞、有创意、清爽，但不幼稚、不卖萌

## 示例效果

示例图片存放在 `examples/images/` 目录，用于风格校准。使用时应该从当前文章重新发明隐喻，不要照抄旧案例的物件和构图。

## 目录结构

```
.
├── README.md                  # 项目说明
├── LICENSE                    # MIT 开源许可
├── NOTICE.md                  # 版权与声明
├── .gitignore
├── assets/                    # 参考图资源
│   ├── 01-two-breakpoints.png          # 风格校准参考图
│   ├── ...
│   ├── 14-trust-bridge.png             # 风格校准参考图
│   └── ian-wechat-qr.jpg              # 原作者联系二维码
├── examples/                  # 展示示例
│   ├── images/                          # 8 张展示样例图
│   └── prompts.md                       # 使用示例 prompt
├── agents/
│   └── openai.yaml            # Agent 接口配置
└── references/                # 技能参考文档
    ├── style-dna.md           # 风格 DNA
    ├── user-ip.md             # 小呆 IP 定义
    ├── composition-patterns.md # 构图模式
    ├── prompt-template.md     # 生图提示词模板
    └── qa-checklist.md        # 检查清单
```

## 安装

在扣子（Coze）平台中，搜索并安装「小暖正文配图」技能即可使用。安装后触发方式为向 Agent 提出配图相关需求。

## License

MIT License. See LICENSE.

## 致谢

本技能基于 [helloianneo/ian-xiaohei-illustrations](https://github.com/helloianneo/ian-xiaohei-illustrations) 改编，原始项目作者 Ian。

---

> 本内容由 Coze AI 生成，请遵循相关法律法规及《人工智能生成合成内容标识办法》使用与传播。
