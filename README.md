# SkillHub - AI 智能体技能商店

欢迎来到 SkillHub！这是一个 AI 智能体技能包的托管仓库，所有技能包都可以直接下载使用。

## 技能列表

### OpenClaw 系列

> OpenClaw 系列技能基于智谱 AI 服务构建

| 技能名称 | 简介 | 下载地址 |
|---------|------|---------|
| zhipu-toolkit | 智谱 AI 工具集：整合文件解析、文档布局解析、网页阅读、网络搜索四大能力。Use when: (1) 解析 PDF/Word/Excel/PPT 等文件提取文本，(2) 解析文档布局结构识别表格/公式/图片，(3) 读取指定网页 URL 内容，(4) 进行网络搜索检索信息。支持多种搜索引擎和输出格式。 | [下载](https://skillhub.feixing.io/openclaw/zhipu-toolkit.skill) |
| zhipu-web-reader | 智谱网页内容读取服务。使用智谱AI的Reader API读取并解析指定URL的网页内容，支持Markdown/Text格式、图片保留、摘要选项。Use when: (1) 读取特定网页URL、解析网页内容，(2) 提取网页正文、获取网页标题和描述。NOT for: 用户需要进行网络搜索（使用zhipu-web-search）。 | [下载](https://skillhub.feixing.io/openclaw/zhipu-web-reader.skill) |
| audio-transcription | 录音转文字服务，使用火山引擎豆包大模型进行语音识别。 触发场景： - 用户想要将音频文件转换为文字 - 用户提到"录音转文字"、"语音转文字"、"音频转录"、"语音识别" - 用户需要转写会议录音、访谈录音、课程录音等 - 支持格式：mp3、wav、ogg、raw - 本地文件自动上传云端，转写完成自动删除 | [下载](https://skillhub.feixing.io/openclaw/audio-transcription.skill) |
| zhipu-web-search | 智谱网络搜索服务：使用智谱 AI 的 Web Search API 进行网络搜索，支持多搜索引擎（智谱基础版、智谱高阶版、搜狗、夸克）。Use when: (1) 需要进行网络搜索、网页搜索、信息检索，(2) 查找网上资料、搜索最新新闻，(3) 用户明确要求使用智谱搜索。NOT for: 用户只想读取特定网页内容（使用 zhipu-web-reader）。 | [下载](https://skillhub.feixing.io/openclaw/zhipu-web-search.skill) |
| zhipu-layout-parsing | 智谱文档布局解析服务：使用 GLM-OCR 模型解析文档和图片的布局结构，识别文本、表格、公式、图片等元素，返回 Markdown 格式结果和详细布局信息。Use when: (1) 解析文档布局、提取文档结构，(2) 识别表格、公式、图片，(3) 分析 PDF 布局，(4) 提取扫描件内容。NOT for: 用户只需要简单文字 OCR（使用 zhipu-ocr）。 | [下载](https://skillhub.feixing.io/openclaw/zhipu-layout-parsing.skill) |
| zhipu-file-parser | 智谱文件解析服务。使用智谱AI的文件解析API解析多种文件格式（PDF、DOCX、DOC、XLS、XLSX、PPT、PPTX、图片等），提取文本内容。支持同步解析，返回结构化结果。 | [下载](https://skillhub.feixing.io/openclaw/zhipu-file-parser.skill) |


### Claude Code 系列

> Claude Code 系列技能专为 Claude Code CLI 工具设计

| 技能名称 | 简介 | 下载地址 |
|---------|------|---------|
| openclaw-skill-creator | 创建、编辑、改进或打包 OpenClaw 技能。用于：(1) 创建新的 OpenClaw 技能，(2) 编辑或改进现有的 OpenClaw 技能，(3) 将技能打包为 .skill 文件，(4) 了解 OpenClaw 技能结构和规范。需要 OpenClaw 环境。 | [下载](https://skillhub.feixing.io/claude-code/openclaw-skill-creator.skill) |
| pdf-book-generator | 使用 Markdown 撰写技术书籍/文档并生成专业排版的 PDF。支持多章节分文件管理、中文排版。触发短语："我想写一本书"、"帮我生成 PDF 电子书"、"写一份技术教程"、"多章节文档怎么管理"。 | [下载](https://skillhub.feixing.io/claude-code/pdf-book-generator.skill) |
| product-review | AI产品创意多专家评审系统。输入产品创意，获得5位专家的多维度评审报告和毒舌劝退建议。 | [下载](https://skillhub.feixing.io/claude-code/product-review.skill) |
| list-cli | 列出当前电脑中已安装的 CLI 软件工具。当用户想查看有哪些命令行工具、忘记安装了什么 CLI、或者想整理/盘点 CLI 工具时使用。支持按包管理器分类，过滤系统命令，输出美观的表格格式。 | [下载](https://skillhub.feixing.io/claude-code/list-cli.skill) |
| list-github-repo | 扫描本地 Git 仓库并按类型分类输出。当你想查看本地有哪些 Git 仓库、它们的远程地址是什么、哪些是你自己的项目、哪些是从别人那里克隆的时候使用此技能。触发短语包括："查看本地仓库"、"列出我的 git 仓库"、"有哪些 github 仓库"、"本地项目列表"。 | [下载](https://skillhub.feixing.io/claude-code/list-github-repo.skill) |
| setup-sound-notifications | 为 Claude Code 设置或卸载声音通知。在等待用户确认时播放进度循环音，任务完成时播放庆祝音。适用于用户需要音频提醒、声音通知、音频反馈，或想要卸载/禁用声音通知的场景。仅支持 macOS。 | [下载](https://skillhub.feixing.io/claude-code/setup-sound-notifications.skill) |


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

1. 将 `.skill` 文件放入对应的分类文件夹（如 `openclaw/` 或 `claude-code/`）
2. 提交并推送到 GitHub
3. GitHub Actions 会自动更新 README

如果需要添加新的分类文件夹，请：
1. 创建新文件夹并添加 `.gitkeep` 文件
2. 手动在 README 中添加新分类的表格

---

## 许可证

MIT License
