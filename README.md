# Daily 3D Science Video Skill

一个面向多种大语言模型的交互式 Skill，用于把日常用品、家用电器和生活现象，转化为**写实电影级 3D 科普视频**。

## 目标

帮助创作者完成从选题到成片的完整策划与制作：
- 选题判断与传播角度
- 科学原理检索、事实核验
- 视频脚本、旁白与字幕
- 分镜与镜头设计
- 3D 结构演示、AI 视频素材与后期方案
- 成片质量检查与发布复盘

## 设计原则

1. **智能混合式交互**：关键节点征求用户意见，次要决策由模型提出合理默认值；不把流程变成冗长问卷。
2. **质量优先**：AI 负责提效，人负责事实审核、审美判断和最终剪辑。
3. **科学准确**：不把模型生成内容当作事实；结构、数值、工作机制必须核验。
4. **分工明确**：精确结构和物理过程优先使用 Blender 等 3D 工具；人物、环境和生活化镜头可使用 AI 视频模型。
5. **跨模型可用**：不依赖特定厂商 API、插件或私有工具。

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
- `references/content-strategy.md`：选题定位与传播策略
- `references/fact-checking.md`：科学事实核验
- `references/script-storyboard.md`：脚本与分镜设计
- `references/visual-production.md`：3D、AI 视频与后期制作规范
- `references/publishing-review.md`：发布、合规与数据复盘
- `templates/production-templates.md`：可复用生产模板
- `skills/3d-camera-cinematography/SKILL.md`：专业 3D 电影镜头设计与执行 Skill
- `skills/3d-camera-cinematography/references/`：镜头语言、Blender 执行、AI 视频提示词规范
- `templates/3d-shot-execution-card.md`：单镜头执行卡
- `templates/3d-shot-plan-template.json`：结构化镜头计划示例
- `scripts/validate_shot_plan.py`：镜头计划结构与时长校验脚本

## 专业 3D 镜头 Skill

当任务涉及景别、机位、焦距、运镜、构图、Blender 摄像机执行或多镜头连续性时，读取 `skills/3d-camera-cinematography/SKILL.md`。它负责把已批准的分镜转化为可执行的 Blender / AI 视频 / 混合制作镜头方案；不替代主 Skill 的选题、科学核验和脚本决策。

镜头硬性规则保持一致：每个独立镜头时长大于 0 秒且不超过 15 秒。可使用 `python scripts/validate_shot_plan.py templates/3d-shot-plan-template.json` 检查结构化镜头计划。

## 推荐内容定位

聚焦普通人每天接触、却不一定理解其原理的物品和现象。优先考虑安全提醒、亲子解释、避免误用/浪费、关心家人等分享动机。单条视频只讲清楚一个核心原理。

## 许可

当前仓库未附加开源许可证。除非仓库所有者另行添加许可证，使用者不应默认拥有复制、修改或再分发本项目内容的权利。
