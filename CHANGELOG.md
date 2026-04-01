# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

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
