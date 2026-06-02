# SkillHub - AI 智能体技能商店

欢迎来到 SkillHub！这是一个 AI 智能体技能包的托管仓库，所有技能包都可以直接下载使用。

## 技能列表

| 技能名称 | 分类 | 简介 | 下载地址 |
|---------|------|------|---------|
| audio-transcription | 办公 | 录音转文字服务，使用火山引擎豆包大模型进行语音识别。触发场景：录音转文字、语音转文字、音频转录、语音识别。支持 mp3/wav/ogg/raw 格式，本地文件自动上传云端，转写完成自动删除。 | [下载](https://skillhub.feixing.io/openclaw/audio-transcription.skill) |
| image-compress | 办公 | 图片压缩技能，支持 PNG/JPG/GIF/SVG 格式无损/有损压缩，压缩率和 ImageOptim 完全一致。触发场景：压缩图片、减小图片大小、图片优化。 | [下载](https://skillhub.feixing.io/openclaw/image-compress.skill) |
| list-cli | 开发 | 列出当前电脑中已安装的 CLI 软件工具。支持按包管理器分类，过滤系统命令，输出美观的表格格式。 | [下载](https://skillhub.feixing.io/claude-code/list-cli.skill) |
| list-github-repo | 开发 | 扫描本地 Git 仓库并按类型分类输出，区分自己的项目、他人的仓库和本地仓库。触发短语：查看本地仓库、列出 git 仓库、本地项目列表。 | [下载](https://skillhub.feixing.io/claude-code/list-github-repo.skill) |
| md-to-xiaohongshu | 办公 | Markdown/飞书文档转小红书卡片图片工具。支持自动分页、多种 Markdown 和飞书特殊格式，生成图片直接发送到聊天窗口，发送后自动清理本地文件。 | [下载](https://skillhub.feixing.io/openclaw/md-to-xiaohongshu.skill) |
| openclaw-skill-creator | 开发 | 创建、编辑、改进或打包技能。用于：创建新技能、编辑或改进现有技能、将技能打包为 .skill 文件、了解技能结构和规范。 | [下载](https://skillhub.feixing.io/claude-code/openclaw-skill-creator.skill) |
| pdf-book-generator | 办公 | 使用 Markdown 撰写技术书籍/文档并生成专业排版的 PDF。支持多章节分文件管理、中文排版。触发短语：写书、生成 PDF 电子书、技术教程、多章节文档管理。 | [下载](https://skillhub.feixing.io/claude-code/pdf-book-generator.skill) |
| product-review | 办公 | AI 产品创意多专家评审系统。输入产品创意，获得 5 位专家的多维度评审报告和毒舌劝退建议。 | [下载](https://skillhub.feixing.io/claude-code/product-review.skill) |
| setup-custom-llm | 开发 | 配置第三方 LLM Provider，支持 Anthropic 和 OpenAI 两种协议，包含自动合并配置的 Python 脚本。触发场景：添加模型、配置大模型、接入 DeepSeek/OpenAI/Qwen/GLM、自定义 LLM。 | [下载](https://skillhub.feixing.io/minimax/setup-custom-llm.skill) |
| setup-sound-notifications | 开发 | 设置或卸载声音通知。等待用户确认时播放进度循环音，任务完成时播放庆祝音。仅支持 macOS。 | [下载](https://skillhub.feixing.io/claude-code/setup-sound-notifications.skill) |
| zhipu-file-parser | 办公 | 智谱文件解析服务，解析 PDF/DOCX/DOC/XLS/XLSX/PPT/PPTX/图片等格式，提取文本内容，支持同步解析，返回结构化结果。 | [下载](https://skillhub.feixing.io/openclaw/zhipu-file-parser.skill) |
| zhipu-layout-parsing | 办公 | 智谱文档布局解析服务，使用 GLM-OCR 模型识别文本、表格、公式、图片等元素，返回 Markdown 格式结果和详细布局信息。 | [下载](https://skillhub.feixing.io/openclaw/zhipu-layout-parsing.skill) |
| zhipu-toolkit | 办公 | 智谱 AI 工具集：整合文件解析、文档布局解析、网页阅读、网络搜索四大能力，支持多种搜索引擎和输出格式。 | [下载](https://skillhub.feixing.io/openclaw/zhipu-toolkit.skill) |
| zhipu-web-reader | 办公 | 智谱网页内容读取服务，读取并解析指定 URL 的网页内容，支持 Markdown/Text 格式、图片保留、摘要选项。 | [下载](https://skillhub.feixing.io/openclaw/zhipu-web-reader.skill) |
| zhipu-web-search | 办公 | 智谱网络搜索服务，使用 Web Search API 进行网络搜索，支持多搜索引擎（智谱基础版/高阶版、搜狗、夸克）。 | [下载](https://skillhub.feixing.io/openclaw/zhipu-web-search.skill) |


---

## 如何使用

1. 点击技能对应的「下载」链接，下载 `.skill` 文件
2. 在 Claude Code 中使用该技能文件

## 技能格式说明

每个 `.skill` 文件都是一个独立的技能包，包含了技能定义、脚本和配置信息。

---

## 自动更新机制

本仓库使用 GitHub Actions 自动维护 README 中的技能列表。

### 工作原理

每次推送新的 `.skill` 文件到仓库时，GitHub Actions 会自动：
1. 扫描所有 `.skill` 文件
2. 解析技能元数据
3. 更新 README.md 中的技能列表

### 如何添加新技能

1. 将 `.skill` 文件放入对应的目录（如 `openclaw/`、`claude-code/`、`minimax/`）
2. 提交并推送到 GitHub
3. GitHub Actions 会自动更新 README

---

## 许可证

MIT License
