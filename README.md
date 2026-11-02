# Daily 3D Science Video Skill

一个面向多种大语言模型的交互式 Skill，用于把日常用品、家用电器和生活现象，转化为**写实电影级 3D 科普视频**。

## 目标

帮助创作者完成从选题到成片的完整策划与制作：
- 选题判断与传播角度
- 科学原理检索、事实核验
- 中文视频脚本、普通话旁白、人物对白与中文字幕
- 分镜、电影镜头与 3D 场景设计
- 3D 结构演示、AI 视频素材与后期方案
- 成片质量检查与发布复盘

## 设计原则

1. **智能混合式交互**：关键节点征求用户意见，次要决策由模型提出合理默认值；不把流程变成冗长问卷。
2. **质量优先**：AI 负责提效，人负责事实审核、审美判断和最终剪辑。
3. **科学准确**：不把模型生成内容当作事实；结构、数值、工作机制必须核验。
4. **分工明确**：精确结构和物理过程优先使用 Blender 等 3D 工具；人物、环境和生活化镜头可使用 AI 视频模型。
5. **中文成片**：默认所有旁白、对白、字幕、标题和画面标签均使用简体中文；语言轻松有趣，但不牺牲科学准确性。
6. **跨模型可用**：不依赖特定厂商 API、插件或私有工具。

## 快速使用

将本仓库作为 Skill 提供给支持技能/指令文件的 AI 助手，并让它读取根目录的 `SKILL.md`。

开始时只需告诉 AI 一个主题，例如：
- 吹风机为什么能吹出热风？
- 电热毯为什么能发热？
- 微波炉为什么能加热食物？
- 保温杯为什么能保温？

AI 会先分析主题并给出可选切入角度，再在选题、事实、脚本、分镜等关键节点与你确认。

## 目录

- `SKILL.md`：Skill 主入口和完整工作流
- `references/`：选题策略、科学核验、脚本分镜、视觉制作、发布复盘等主流程参考
- `skills/3d-camera-cinematography/SKILL.md`：专业 3D 电影镜头设计与执行 Skill
- `skills/3d-camera-cinematography/references/`：镜头语言、Blender 执行、AI 视频提示词规范
- `skills/3d-scene-composition/SKILL.md`：专业 3D 场景构建、空间布局与连续性 Skill
- `skills/3d-scene-composition/references/scene-layout-patterns.md`：产品、剖切、物理过程、人物场景和竖屏布局参考
- `skills/3d-lighting-materials/SKILL.md`：专业灯光、材质、纹理、反射与渲染一致性
- `skills/3d-lighting-materials/references/lighting-setups.md`：产品棚拍、生活场景、微距及常见材质布光参考
- `skills/3d-animation-motion/SKILL.md`：产品机构、科学过程、人物动作与 Blender 动画执行
- `skills/3d-animation-motion/references/animation-patterns.md`：产品启动、旋转机构、爆炸图、气流、热量和人物交互动画参考
- `skills/3d-asset-modeling/SKILL.md`：资产拆解、下载/改造/自建决策、建模质量与授权核验
- `skills/3d-asset-modeling/references/asset-sourcing-inspection.md`：模型来源、格式、导入检查与许可档案参考
- `templates/3d-asset-brief.md`：单项 3D 资产需求说明模板
- `templates/asset-register.example.json`：资产登记 JSON 示例
- `scripts/validate_asset_manifest.py`：资产登记字段与授权状态完整性校验脚本
- `templates/3d-shot-execution-card.md`：单镜头执行卡
- `templates/3d-shot-plan-template.json`：结构化镜头计划示例
- `scripts/validate_shot_plan.py`：镜头计划结构与时长校验脚本

## 专业 3D 制作模块

- **场景构建**：把分镜变成空间布局、主体/道具清单、前中后景、灯光材质基准和 Blender 场景结构。
- **镜头设计**：把场景变成明确的景别、机位、焦距、运镜路径、焦点与连续性方案。
- **灯光与材质**：建立可信的产品表面、反射、光影层次和跨镜头渲染基准。
- **动画与运动**：将已核验的工作过程转化为关键帧、约束或模拟，确保动作有因果、可读且可复现。
- **模型与资产制作**：从分镜反推资产清单，决定下载、改造或自建，并检查模型质量、拆件能力和商业授权。
- **AI 视频翻译**：将镜头设计转成模型可执行提示词，并定义参考图、首尾帧和负面约束。

每个独立镜头时长必须大于 0 秒且不超过 15 秒。可使用 `python scripts/validate_shot_plan.py templates/3d-shot-plan-template.json` 检查结构化镜头计划。可使用 `python scripts/validate_asset_manifest.py templates/asset-register.example.json` 检查资产登记信息完整性（不构成法律许可判断或模型几何检查）。

## 中文成片规范

默认成片使用简体中文：
- 所有旁白、人物对白和口播均为普通话中文。
- 所有字幕、标题、标签、图注和信息图文字均为正确简体中文。
- 旁白风格轻松、有画面感、适度幽默，避免说明书腔、尬梗和低幼化。
- 对汉字生成不稳定的视频模型，画面中不生成复杂文字，统一在后期添加校对后的中文字幕和图形标签。
- 技术对象名、文件名、代码字段可使用英文，不影响成片中文要求。

## 推荐内容定位

聚焦普通人每天接触、却不一定理解其原理的物品和现象。优先考虑安全提醒、亲子解释、避免误用/浪费、关心家人等分享动机。单条视频只讲清楚一个核心原理。

## 许可

当前仓库未附加开源许可证。除非仓库所有者另行添加许可证，使用者不应默认拥有复制、修改或再分发本项目内容的权利。
