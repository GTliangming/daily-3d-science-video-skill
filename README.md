# Daily 3D Science Video

一个包含**视频策划 Skill**与**视频生产 Agent Skill**的双模式项目，用于把日常用品、家用电器和生活现象转化为写实电影级 3D 科普视频。

## 两种工作模式

### A. 视频策划 Skill（原有能力）

负责选题、科学研究、事实核验、脚本、旁白、分镜、视觉设计和制作方案。它的交付物是经过确认的策划包，不会把“写出提示词”说成“已经生成视频”。

### B. 视频生产 Agent Skill（新增）

负责把已确认的策划包变成真实视频产物：镜头任务拆解、素材生成、Blender 3D 制作、音频、FFmpeg 合成、自动质检、返工和 MP4 交付。

## 如何选择

将本仓库提供给支持 Skill 的 AI 助手，并让它读取根目录 `SKILL.md`。

开始时可以直接说：
- “使用视频策划模式，帮我策划一期吹风机工作原理。”
- “使用视频生产 Agent 模式，根据这份分镜实际生成视频。”
- “先策划，再进入视频生产。”

如果用户没有明确选择，入口 Skill 应询问使用哪种模式。

## 生产模式的技术原则

- **Blender**：精确结构、剖切、爆炸图、机械运动和物理过程示意。
- **AI 视频**：人物、家庭环境、产品使用场景和电影化过场。
- **AI 图片/授权素材**：参考图、背景和静态插入素材。
- **FFmpeg**：视频拼接、音频混合、字幕和交付编码。
- **Python**：任务状态、素材清单、校验、自动化和审计。
- **Provider Adapter**：统一模型服务接口，避免把单一厂商写死。

首个版本提供标准化项目/镜头数据、任务状态管理、项目校验和生产规范；暂不声称已经内置 MiniMax、可灵或 TTS 的可用 API 集成。实际接入前必须核实当前 API、凭证、价格和输出格式。所有付费生成默认需要用户确认。

## 目录

```text
.
├── SKILL.md                         # 双模式入口 + 原视频策划工作流
├── references/                      # 原有策划参考
├── templates/                       # 原有策划模板
└── video-production-agent/
    ├── SKILL.md                      # 视频生产 Agent 主流程
    ├── references/
    │   ├── pipeline.md
    │   ├── provider-contract.md
    │   └── quality-control.md
    ├── schemas/
    │   ├── video-project.schema.json
    │   └── shot-task.schema.json
    ├── templates/
    │   ├── project.example.json
    │   └── shot-task.example.json
    └── scripts/
        ├── validate_project.py
        └── task_manager.py
```

## 本地运行生产脚本

仅需 Python 3.10+，当前基础脚本使用 Python 标准库，不需要 Docker、数据库或第三方 Python 包。

验证项目清单：

```bash
python video-production-agent/scripts/validate_project.py video-production-agent/templates/project.example.json
```

查看任务状态：

```bash
python video-production-agent/scripts/task_manager.py status path/to/project.json
```

认领镜头任务：

```bash
python video-production-agent/scripts/task_manager.py claim path/to/project.json SHOT_001
```

任务完成时，必须提供真实存在且非空的素材文件：

```bash
python video-production-agent/scripts/task_manager.py complete path/to/project.json SHOT_001 --artifact path/to/shot.mp4
```

标记失败或重试：

```bash
python video-production-agent/scripts/task_manager.py fail path/to/project.json SHOT_001 --reason "provider timeout"
python video-production-agent/scripts/task_manager.py retry path/to/project.json SHOT_001 --reason "retry after provider recovery"
```

## 重要限制

- 项目未附带可默认继承的第三方模型 API 额度或密钥。
- 生产 Agent 需要在实际运行环境中具备 Blender、FFmpeg 和所选 Provider Adapter；缺少时必须报告阻塞。
- 自动化检查不能替代科学事实审核、视觉连续性审核和最终人工验收。
- 对素材、字体、音乐、人物肖像及平台 AI 内容标识要求，必须在交付前单独核查。

## 许可

当前仓库未附加开源许可证。除非仓库所有者另行添加许可证，使用者不应默认拥有复制、修改或再分发本项目内容的权利。
