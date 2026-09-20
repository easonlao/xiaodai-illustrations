# 生图提示词模板

这是小呆配图 skill 的通用模板。默认先使用最稳定、最清楚的解释型配图骨架；只有当场景明确需要时，才补最小竖版约束。每张图单独生成，不要把多张图拼在一起。

```text
Design one standalone Xiaodai illustration for the scene decision below.

Scene mode:
{scene_mode}

Format goal:
{format_goal}

Canvas ratio:
{canvas_ratio}

Subject density:
{subject_density}

Scene-specific constraints:
{scene_constraints}

Character lock:
Xiaodai must remain one single compact red flame silhouette. The red body is the whole body. There is no separate torso, no neck, no chest, no belly, and no humanoid trunk under a flame head. The black limbs must attach directly to the outer edge of the red flame silhouette. The eyes must remain strictly a level, horizontal, symmetrical pair of identical tiny circular white dots. Do NOT place one eye higher than the other. Do NOT distort or stretch the eye dots into ovals, slants, or diagonal lines. There are no pupils; gaze direction is conveyed solely by the tilt of the flame silhouette, never by moving or reshaping the eyes. Do not allow props, tools, or hands to cross or occlude the eyes. Mild deformation is allowed only if the body still reads as one uninterrupted flame shape. If the model tends to add a torso or split the body into upper and lower parts, simplify the pose instead of redesigning the body.

Reference-lock constraints:
Always match the reference image before pursuing scene creativity. Character consistency is higher priority than pose variation, metaphor complexity, or cover tension.

Visual DNA:
Pure white background. Minimalist black hand-drawn line art. Slightly wobbly pen lines. Lots of empty white space. Sparse red/orange/blue handwritten Chinese annotations. Clean absurd product-sketch feeling. No gradients, no shadows, no paper texture, no complex background, no commercial vector style, no PPT infographic look, no cute mascot poster, no children's illustration, no realistic UI.

Recurring IP character (小呆) — from reference image:
小呆, a little flame person (小火人), which is a small solid red flame-shaped silhouette character with two small white-dot eyes and thin black stick-figure limbs (arms and legs). No hair, no clothing details, no glasses, no shoes. Serious but doing something absurd, participating as the core operator in the conceptual action. Keep the character serene, focused, and slightly bizarre.
Keep the flame silhouette compact and consistent across images. The whole red body must remain one single flame silhouette, not a flame head on top of a separate torso. The two tiny white-dot eyes must remain clearly visible, identical, perfectly round, level, and symmetrical — never asymmetrical, never with one eye higher than the other, never stretched into ovals. Match the reference silhouette first and prioritize character consistency over pose variation. Do not redesign the character per scene. Do not invent a new body shape. Do not split the red body into upper and lower parts. Not a cute cartoon mascot, not a rounded chibi flame character, not a sticker-like character, not a faceless flame silhouette. Keep the limbs as thin black stick lines.

Theme:
{配图主题}

Structure type:
{结构类型：Workflow / 系统局部 / 前后对比 / 角色状态 / 概念隐喻 / 方法分层 / 地图路线 / 小漫画分镜}

Core idea:
{这张图要表达的核心意思}

Core metaphor:
{这次选用的物理隐喻}

Composition:
{具体画面：小呆在哪里、正在做什么、主要物件是什么、信息如何流动}

Suggested elements:
{元素1} / {元素2} / {元素3} / {元素4}

Chinese handwritten labels:
{标注词1} / {标注词2} / {标注词3} / {标注词4} / {可选标注词5}

Color use:
Black for main line art. Solid bright red for the character 小呆. Orange for main flow/path/arrows. Red only for key warnings/problems/results. Blue only for secondary notes or feedback/system state.

Constraints:
One image explains only one core structure. Keep the main subject around 40%-60% of the canvas. Preserve at least 35% blank white space. Use at most 2-5 short handwritten Chinese labels unless the scene truly needs more. Do not write a title in the top-left corner. Do not write the structure type on the image. Do not make it a formal diagram, course slide, or dense explainer. Prefer explanatory clarity over novelty-for-novelty's-sake. If a simple action skeleton already explains the idea clearly, keep it simple.

For article_inline specifically: avoid a centered icon-like or sticker-like composition. Do not place Xiaodai alone in the exact middle with circular swirls around the body. Preserve a horizontal reading direction, give the scene one clear external anchor or one clear side of blank breathing space, and make the image feel like a paragraph illustration rather than a logo on white paper.

If torso drift keeps happening: prefer standing, leaning, reaching, pulling, or being lightly dragged. Temporarily avoid seated, crouched, curled-up, or symmetrical front-facing poses.
```

## 使用顺序

如果用户没有给完整的场景规格，先输出一段简短的 scene decision，再填这个模板。

默认原则：

- 如果没有明确竖屏需求，优先走 `article_inline`
- 如果只是单张观点图，再在 `social_single` / `feed_cover` / `vertical_cover` 里判断
- 不要为了“更丰富”主动把正文配图任务改造成封面任务

推荐最小 decision 字段：

- `scene_mode`
- `format_goal`
- `canvas_ratio`
- `subject_density`
- `structure_type`
- `core_metaphor`

不要把 `Canvas ratio: 16:9 horizontal` 这种字段写成系统默认值；它应该是当前任务的判断结果。

字段边界：

- `scene_mode` = 使用场景
- `structure_type` = 表达结构

`scene_mode` 不要写成 `conceptual_metaphor`、`workflow`、`before_after` 这类结构词。

例如：

- `scene_mode: article_inline`
- `scene_mode: social_single`
- `scene_mode: feed_cover`
- `scene_mode: vertical_cover`
- `structure_type: conceptual_metaphor`

填写模板前，先从 `references/scene-modes.md` 里挑出对应 scene mode 的约束，填进 `{scene_constraints}`。

## 图像编辑提示

增强存在感：

```text
Regenerate this illustration with the same core meaning and simple layout, but make the red flame character 小呆 more central to the conceptual action. 小呆 should be doing the strange work that explains the idea, not standing beside the diagram. Keep it clean, sparse, hand-drawn, and not cute.
```
