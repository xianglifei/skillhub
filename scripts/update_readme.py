#!/usr/bin/env python3
"""
自动更新 README.md 中的技能列表
扫描所有 .skill 文件并更新对应的表格

设计原则：
1. 增量更新：只添加新增技能，保留已有技能的简介
2. 优先使用 README 中已有的中文简介
3. 新技能才从 SKILL.md 提取 description
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
    "zhipu-web-search": "智谱网络搜索服务。使用智谱AI的Web Search API进行网络搜索。",
    "zhipu-web-reader": "智谱网页内容读取服务。使用智谱AI的Reader API读取并解析指定URL的网页内容，支持Markdown/Text格式。",
    "zhipu-layout-parsing": "智谱文档布局解析服务。使用GLM-OCR模型解析文档和图片的布局结构。",
}

def extract_existing_descriptions(readme_path):
    """从现有 README 中提取已有技能的简介"""
    existing = {}

    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 匹配表格行：| skill-name | description | [下载](url) |
    pattern = r'\|\s*([a-zA-Z0-9_-]+)\s*\|\s*([^|]+?)\s*\|\s*\[下载\]'
    matches = re.findall(pattern, content)

    for skill_name, description in matches:
        existing[skill_name] = description.strip()

    return existing

def extract_skill_metadata(skill_path, existing_descriptions):
    """从 .skill 文件中提取技能元数据，优先使用已有简介"""
    skill_name = Path(skill_path).stem

    # 优先级1：使用 README 中已有的简介
    if skill_name in existing_descriptions:
        return skill_name, existing_descriptions[skill_name]

    # 优先级2：使用预设的中文描述
    if skill_name in SKILL_DESCRIPTIONS:
        return skill_name, SKILL_DESCRIPTIONS[skill_name]

    # 优先级3：从 SKILL.md 提取 description
    description = "AI 智能体技能包"

    try:
        with zipfile.ZipFile(skill_path, 'r') as zf:
            for name in zf.namelist():
                if name.endswith('SKILL.md'):
                    content = zf.read(name).decode('utf-8')

                    # 尝试提取描述 - 支持多种 YAML 格式
                    # 格式1: description: "单行描述"
                    desc_match = re.search(r'description:\s*"([^"]+)"', content)
                    if desc_match:
                        description = desc_match.group(1).strip()
                    else:
                        # 格式2: description: | 后跟多行描述
                        desc_match = re.search(r'description:\s*\|\s*\n((?:[ \t]+.+\n)+)', content)
                        if desc_match:
                            lines = desc_match.group(1).strip().split('\n')
                            description = ' '.join(line.strip() for line in lines)
                        else:
                            # 格式3: description: 单行描述（无引号）
                            desc_match = re.search(r'description:\s*([^\n|]+)\n', content)
                            if desc_match:
                                description = desc_match.group(1).strip()

                    # 去除 TRIGGER 和 DO NOT trigger 部分
                    description = re.split(r'\s*TRIGGER when:', description)[0].strip()
                    break
    except Exception as e:
        print(f"Warning: Could not extract metadata from {skill_path}: {e}")

    return skill_name, description

# 定义技能分类文件夹
SKILL_CATEGORIES = ['openclaw', 'claude-code', 'minimax']

def scan_skills(base_dir, existing_descriptions):
    """扫描所有分类文件夹中的技能"""
    skills = {}

    for category_name in SKILL_CATEGORIES:
        category_dir = Path(base_dir) / category_name
        if category_dir.is_dir():
            skills[category_name] = []

            for skill_file in category_dir.glob('*.skill'):
                skill_name, description = extract_skill_metadata(skill_file, existing_descriptions)
                download_url = f"{BASE_URL}/{category_name}/{skill_file.name}"
                skills[category_name].append({
                    'name': skill_name,
                    'description': description,
                    'url': download_url
                })

    return skills

def generate_table(skills_list):
    """生成技能表格 Markdown"""
    if not skills_list:
        return "| *暂无技能* | 敬请期待 | - |"

    lines = ["| 技能名称 | 简介 | 下载地址 |", "|---------|------|---------|"]
    for skill in skills_list:
        lines.append(f"| {skill['name']} | {skill['description']} | [下载]({skill['url']}) |")

    return '\n'.join(lines)

def update_readme(readme_path, skills):
    """更新 README 文件"""
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 定义分类信息
    categories = {
        'openclaw': {'title': 'OpenClaw 系列', 'desc': 'OpenClaw 系列技能基于智谱 AI 服务构建'},
        'claude-code': {'title': 'Claude Code 系列', 'desc': 'Claude Code 系列技能专为 Claude Code CLI 工具设计'},
        'minimax': {'title': 'MiniMax Code 系列', 'desc': 'MiniMax Code 系列技能专为 MiniMax Code 工具设计'},
    }

    for category_name, info in categories.items():
        # 查找并替换对应分类的表格
        pattern = rf'(### {info["title"]}.*?>\s*{info["desc"]}\s*\n\n)(.*?)(?=\n### |\n---|\n## |\Z)'

        table = generate_table(skills.get(category_name, []))
        replacement = rf'\1{table}\n\n'

        content = re.sub(pattern, replacement, content, flags=re.DOTALL)

    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print("README.md updated successfully!")

def main():
    base_dir = Path(__file__).parent.parent
    readme_path = base_dir / 'README.md'

    # 先提取现有 README 中的已有简介
    existing_descriptions = extract_existing_descriptions(readme_path)
    print(f"Existing descriptions: {list(existing_descriptions.keys())}")

    # 扫描技能，保留已有简介
    skills = scan_skills(base_dir, existing_descriptions)
    print(f"Found skills: {[s['name'] for cat in skills.values() for s in cat]}")

    update_readme(readme_path, skills)

if __name__ == '__main__':
    main()
