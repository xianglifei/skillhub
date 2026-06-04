# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed - 2026-06-05

- 合并目录结构：将 `claude-code/`、`openclaw/`、`minimax/` 统一迁移至 `skills/` 目录
- 同名技能加后缀区分：`zhipu-web-reader-cc`/`zhipu-web-reader-oc`、`zhipu-web-search-cc`/`zhipu-web-search-oc`

### Added - 2026-06-05

- **wechat-cover-art** - 微信公众号文章配图技能（基于 dreamina CLI）
  - 自动按微信规范生成头条封面（21:9 高清）、正文插图、次条封面
  - Prompt 安全区增强，确保朋友圈裁切后效果 OK

### Changed - 2026-06-02

- 重构 README 技能列表：取消按 Agent 分类，改为统一表格
  - 新增「分类」列标注功能性分类（办公/开发/搜索）
  - 所有技能按名称首字母排序

### Added - 2026-06-02

- **zhihu-research** - 知乎全能研究助手（从本地技能迁入）
  - 集成全网搜索、站内搜索、热榜、知达 AI 问答与深度研究编排
  - 深度研究模式自动协同知达+双路搜索
  - 需配置 ZHIHU_ACCESS_SECRET 环境变量
  - 新增「分类」列标注功能性分类（办公/开发）
  - 所有技能按名称首字母排序

### Added - 2026-06-02

#### MiniMax Code 系列

- **setup-custom-llm** - 新增第三方 LLM Provider 配置技能
  - 支持 Anthropic 和 OpenAI 两种协议
  - Anthropic 协议可获得 Prompt Caching 和推理过程展示
  - 包含自动合并配置的 Python 脚本（merge_provider.py）
  - 触发场景：添加模型、配置大模型、接入 DeepSeek/OpenAI/Qwen/GLM、自定义 LLM

### Added - 2026-06-02

#### OpenClaw 系列

- **image-compress** - 新增图片压缩技能（从 my-openclaw-skills 仓库迁移）
  - 支持 PNG/JPG/GIF/SVG 所有常见图片格式
  - 默认无损压缩，压缩率和 ImageOptim 完全一致
  - 可自定义压缩级别（lossless/medium/high）、是否保留 EXIF 信息
  - 原始时间线：
    - 2026-03-22：初始提交，image-compress 图片压缩技能 v1.0
    - 2026-06-02：迁移至 SkillHub

- **md-to-xiaohongshu** - 新增 Markdown/飞书文档转小红书卡片图片技能（从 my-openclaw-skills 仓库迁移）
  - 支持本地 Markdown 文件和飞书文档转换为小红书风格卡片图片
  - 自动分页、多种 Markdown 格式和飞书特殊格式
  - 生成图片直接发送到聊天窗口，发送后自动清理本地文件
  - 原始时间线：
    - 2026-03-25 08:56：新增 md 转小红书卡片图片工具技能
    - 2026-03-25 09:16：升级支持飞书文档输入、callout 格式，自动发消息并清理本地文件
    - 2026-03-25 10:36：修复 emoji 显示问题，优化字体支持
    - 2026-03-25 12:17：设置 Notion 风格为默认主题
    - 2026-03-25 12:33：修复分页截断 bug，增加内容冗余空间
    - 2026-03-25 12:45：新增飞书 lark-table 格式解析支持
    - 2026-06-02：迁移至 SkillHub

### Updated - 2026-04-01

#### Claude Code 系列

- **setup-sound-notifications** - 更新声音通知技能
  - 内置音频文件，无需从外部下载
  - 包含 progress_loop.wav 和 celebration.wav 音效
  - 简化安装流程，开箱即用

### Added - 2026-04-01

#### Claude Code 系列

- **pdf-book-generator** - 新增 PDF 书籍生成技能
  - 使用 Markdown 撰写技术书籍/文档
  - 支持多章节分文件管理
  - 一键生成专业排版的 PDF（基于 MiniMax PDF）
  - 支持中文排版
  - 自动创建项目结构和写作规范
  - 触发场景：写书、写教程、生成 PDF 电子书、多章节文档管理

### Added - 2026-03-31

#### OpenClaw 系列

- **audio-transcription** - 新增录音转文字技能
  - 基于火山引擎豆包大模型录音文件识别 API
  - 支持本地音频文件自动上传到云端
  - 转写完成后自动删除云端临时文件
  - 支持多种音频格式：mp3、wav、ogg、raw
  - 支持说话人分离、情绪检测、性别检测、语种识别
  - 首次使用提示配置 API Key，保存到本地配置文件
  - 无需任何 Cloudflare 配置，开箱即用
  - 多语言支持：中文普通话、英语、粤语、日语、韩语等

---

## Version History

| 日期 | 版本 | 变更内容 |
|------|------|----------|
| 2026-06-05 | - | 合并目录结构至 skills/，新增 wechat-cover-art 技能 |
| 2026-06-02 | - | 迁移 image-compress 和 md-to-xiaohongshu 技能（从 my-openclaw-skills 仓库） |
| 2026-03-31 | - | 新增 audio-transcription 录音转文字技能 |
| 2026-03-30 | - | 初始化 SkillHub 仓库，添加智谱系列技能 |

---

## 技能详情

### audio-transcription

**功能特性：**
- 本地音频文件一键转写
- 自动上传云端，转写完成自动清理
- API Key 安全存储（本地配置文件，权限 600）
- 无需依赖，仅需 curl 命令

**技术架构：**
- 转写引擎：火山引擎豆包大模型录音文件识别 API
- 文件存储：Cloudflare R2
- 公开上传：通过 Worker 实现无鉴权上传

**配置要求：**
- 火山引擎 API Key（首次使用时配置）

**使用示例：**
```bash
# 本地文件转写
python scripts/transcribe.py --file ./meeting.mp3 --output transcript.md

# 启用说话人分离
python scripts/transcribe.py --file ./interview.wav --output result.md --speaker-info
```

### pdf-book-generator

**功能特性：**
- 使用 Markdown 撰写技术书籍/文档
- 多章节分文件管理，每章一个 .md 文件
- 一键合并章节生成专业排版的 PDF
- 支持中文排版（STSong-Light 字体）
- 自动创建项目结构和写作规范（CLAUDE.md）
- 多种文档类型模板（editorial、report、proposal 等）

**技术架构：**
- PDF 生成：MiniMax PDF 技能
- 字体支持：STSong-Light（华文宋体）
- 文档模板：editorial（推荐）、report、proposal、minimal、academic

**项目结构：**
```
my-book/
├── .claude/CLAUDE.md    # 写作规范
├── chapters/            # 章节目录
├── images/              # 图片目录
├── output/              # 输出目录
└── scripts/build.sh     # 构建脚本
```

**使用示例：**
```bash
# 初始化项目
bash scripts/init-project.sh my-book

# 生成 PDF
bash scripts/build.sh "我的技术教程" editorial
```
