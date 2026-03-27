# SkillHub - AI 智能体技能商店

欢迎来到 SkillHub！这是一个 AI 智能体技能包的托管仓库，所有技能包都可以直接下载使用。

## 技能列表

### OpenClaw 系列

> OpenClaw 系列技能基于智谱 AI 服务构建

| 技能名称 | 简介 | 下载地址 |
|---------|------|---------|
| zhipu-file-parser | 智谱文件解析服务。使用智谱AI的文件解析API解析多种文件格式（PDF、DOCX、DOC、XLS、XLSX、PPT、PPTX、图片等），提取文本内容。支持同步解析，返回结构化结果。 | [下载](https://skillhub.feixing.io/openclaw/zhipu-file-parser.skill) |


### Claude Code 系列

> Claude Code 系列技能专为 Claude Code CLI 工具设计

| *暂无技能* | 敬请期待 | - |


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
