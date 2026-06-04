#!/usr/bin/env python3
"""
自动更新 README.md 中的技能列表
扫描所有 .skill 文件并更新统一的技能表格

设计原则：
1. 所有技能放在一张表格中，按名称首字母排序
2. 表格包含：技能名称、分类、简介、下载地址
3. 增量更新：只添加新增技能，保留已有技能的简介和分类
4. 新技能才从 SKILL.md 提取 description
"""

import os
import zipfile
import re
from pathlib import Path

BASE_URL = "https://skillhub.feixing.io"

# 技能描述映射（新增技能的默认中文描述，优先级最高）
SKILL_DESCRIPTIONS = {
    "zhipu-file-parser": "智谱文件解析服务。使用智谱AI的文件解析API解析多种文件格式（PDF、DOCX、DOC、XLS、XLSX、PPT、PPTX、图片等），提取文本内容。支持同步解析，返回结构化结果。",
    "zhipu-ocr": "智谱OCR服务。使用智谱AI的OCR API识别图片中的文字，支持手写体识别、多语言识别。",
    "zhipu-web-search-cc": "智谱网络搜索服务（Claude Code 版）。使用智谱AI的Web Search API进行网络搜索，集成 Python 脚本。",
    "zhipu-web-search-oc": "智谱网络搜索服务（OpenClaw 版）。使用智谱AI的Web Search API进行网络搜索，基于 curl/jq 实现。",
    "zhipu-web-reader-cc": "智谱网页内容读取服务（Claude Code 版）。使用智谱AI的Reader API读取并解析网页内容，集成 Python 脚本。",
    "zhipu-web-reader-oc": "智谱网页内容读取服务（OpenClaw 版）。使用智谱AI的Reader API读取并解析网页内容，基于 curl/jq 实现。",
    "zhipu-layout-parsing": "智谱文档布局解析服务。使用GLM-OCR模型解析文档和图片的布局结构。",
    "wechat-cover-art": "微信公众号文章配图技能。基于 dreamina CLI，自动按微信规范生成头条封面、正文插图、次条封面。",
    "ima": "IMA 笔记与知识库操作技能。支持上传文件到知识库、添加网页、搜索知识库内容、搜索/浏览/创建/编辑笔记。",
}

# 技能功能分类映射（优先级最高）
SKILL_CATEGORIES = {
    "audio-transcription": "办公",
    "image-compress": "办公",
    "ima": "办公",
    "list-cli": "开发",
    "list-github-repo": "开发",
    "md-to-xiaohongshu": "办公",
    "openclaw-skill-creator": "开发",
    "pdf-book-generator": "办公",
    "product-review": "办公",
    "setup-custom-llm": "开发",
    "setup-sound-notifications": "开发",
    "wechat-cover-art": "办公",
    "zhihu-research": "搜索",
    "zhipu-file-parser": "办公",
    "zhipu-layout-parsing": "办公",
    "zhipu-toolkit": "办公",
    "zhipu-web-reader-cc": "办公",
    "zhipu-web-reader-oc": "办公",
    "zhipu-web-search-cc": "办公",
    "zhipu-web-search-oc": "办公",
}

# 扫描的目录
SKILL_DIRS = ['skills']


def extract_existing_table(readme_path):
    """从现有 README 中提取已有技能的信息（名称→分类+简介）"""
    existing = {}

    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 匹配表格行：| skill-name | category | description | [下载](url) |
    pattern = r'\|\s*([a-zA-Z0-9_-]+)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*\[下载\]'
    matches = re.findall(pattern, content)

    for skill_name, category, description in matches:
        existing[skill_name] = {
            'category': category.strip(),
            'description': description.strip(),
        }

    return existing


def extract_skill_metadata(skill_path, existing_info):
    """从 .skill 文件中提取技能元数据，优先使用已有信息"""
    skill_name = Path(skill_path).stem

    category = "办公"  # 默认分类
    description = "AI 智能体技能包"

    # 优先级1：使用 README 中已有的信息
    if skill_name in existing_info:
        category = existing_info[skill_name]['category']
        description = existing_info[skill_name]['description']
        return skill_name, category, description

    # 优先级2：使用预设的分类
    if skill_name in SKILL_CATEGORIES:
        category = SKILL_CATEGORIES[skill_name]

    # 优先级2：使用预设的中文描述
    if skill_name in SKILL_DESCRIPTIONS:
        description = SKILL_DESCRIPTIONS[skill_name]
        return skill_name, category, description

    # 优先级3：从 SKILL.md 提取 description
    try:
        with zipfile.ZipFile(skill_path, 'r') as zf:
            for name in zf.namelist():
                if name.endswith('SKILL.md'):
                    content = zf.read(name).decode('utf-8')

                    # 尝试提取描述 - 支持多种 YAML 格式
                    desc_match = re.search(r'description:\s*"([^"]+)"', content)
                    if desc_match:
                        description = desc_match.group(1).strip()
                    else:
                        desc_match = re.search(r'description:\s*\|\s*\n((?:[ \t]+.+\n)+)', content)
                        if desc_match:
                            lines = desc_match.group(1).strip().split('\n')
                            description = ' '.join(line.strip() for line in lines)
                        else:
                            desc_match = re.search(r'description:\s*([^\n|]+)\n', content)
                            if desc_match:
                                description = desc_match.group(1).strip()

                    # 去除 TRIGGER 和 DO NOT trigger 部分
                    description = re.split(r'\s*TRIGGER when:', description)[0].strip()
                    break
    except Exception as e:
        print(f"Warning: Could not extract metadata from {skill_path}: {e}")

    return skill_name, category, description


def scan_skills(base_dir, existing_info):
    """扫描所有目录中的技能，返回按名称排序的列表"""
    skills = []

    for dir_name in SKILL_DIRS:
        category_dir = Path(base_dir) / dir_name
        if category_dir.is_dir():
            for skill_file in category_dir.glob('*.skill'):
                skill_name, category, description = extract_skill_metadata(skill_file, existing_info)
                download_url = f"{BASE_URL}/skills/{skill_file.name}"
                skills.append({
                    'name': skill_name,
                    'category': category,
                    'description': description,
                    'url': download_url,
                })

    # 按技能名称首字母排序
    skills.sort(key=lambda s: s['name'].lower())
    return skills


def generate_table(skills):
    """生成统一的技能表格 Markdown"""
    if not skills:
        return "| *暂无技能* | - | 敬请期待 | - |"

    lines = ["| 技能名称 | 分类 | 简介 | 下载地址 |", "|---------|------|------|---------|"]
    for skill in skills:
        lines.append(f"| {skill['name']} | {skill['category']} | {skill['description']} | [下载]({skill['url']}) |")

    return '\n'.join(lines)


def update_readme(readme_path, skills):
    """更新 README 文件中的技能表格"""
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 匹配 ## 技能列表 后面的表格区域，直到遇到 --- 或 ## 或文件结束
    table = generate_table(skills)

    pattern = r'(## 技能列表\s*\n\n)(.*?)(?=\n---|\n## |\Z)'
    replacement = rf'\1{table}\n'
    content = re.sub(pattern, replacement, content, flags=re.DOTALL)

    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print("README.md updated successfully!")


def main():
    base_dir = Path(__file__).parent.parent
    readme_path = base_dir / 'README.md'

    # 先提取现有 README 中的已有信息
    existing_info = extract_existing_table(readme_path)
    print(f"Existing skills: {list(existing_info.keys())}")

    # 扫描技能，保留已有信息
    skills = scan_skills(base_dir, existing_info)
    print(f"Found skills: {[s['name'] for s in skills]}")

    update_readme(readme_path, skills)


if __name__ == '__main__':
    main()
