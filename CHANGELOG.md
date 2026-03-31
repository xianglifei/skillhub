# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

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
