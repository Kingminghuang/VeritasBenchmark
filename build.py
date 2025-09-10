import json
import os
import re


def load_paper(paper_path):
    try:
        with open(paper_path, 'r', encoding='utf-8') as f:
            full_paper_text = f.read()
        return full_paper_text
    except FileNotFoundError:
        print(f"错误: 未找到论文文件 '{paper_path}'。请确保它与此Notebook在同一目录下。")
        raise

def parse_markdown_sections(markdown_text):
    """
    Extracts section headers from a markdown document and splits the original text into structured data containing the content of each section.
    Refactored: The content of each section includes all content from its subsections.

    Args:
        markdown_text (str): The markdown-formatted text content.

    Returns:
        list: A list of dictionaries containing section information. Each dictionary includes:
            - level (int): Header level (1 for #, 2 for ##, etc.)
            - text (str): Header text content
            - content (str): All content from the header to the next header of the same level (including all subsections)
    """
    
    # 匹配markdown标题的正则表达式 (ATX风格: # Header)
    header_pattern = r'^(#{1,6})\s+(.+?)(?:\s+#*)?$'
    
    # 找到所有标题及其位置
    lines = markdown_text.split('\n')
    line_positions = []  # 记录每行的起始位置
    
    # 计算每行的起始位置
    pos = 0
    for line in lines:
        line_positions.append(pos)
        pos += len(line) + 1  # +1 for newline
    
    # 提取所有标题信息
    header_matches = []
    for i, line in enumerate(lines):
        match = re.match(header_pattern, line.strip())
        if match:
            hashes, text = match.groups()
            level = len(hashes)
            clean_text = text.strip()
            if "acknowledgments" in clean_text.lower():
                continue
            header_matches.append({
                'level': level,
                'text': clean_text,
                'line_index': i,
                'position': line_positions[i]
            })
    
    # 为每个章节分割内容，包含所有子章节
    sections = []
    references = []
    for i, header in enumerate(header_matches):
        # 确定章节内容的结束位置（下一个同级别标题之前）
        end_position = len(markdown_text)  # 默认到文档末尾
        
        # 查找下一个同级别标题
        for next_header in header_matches[i+1:]:
            if next_header['level'] == header['level']:
                end_position = next_header['position']
                break
        
        # 提取章节内容（从当前标题到结束位置）
        start_position = header['position']
        content = markdown_text[start_position:end_position]

        if "references" in header['text'].lower():
            ref_dict = {}
            for line in content.split('\n'):
                line = line.strip()
                num = re.match(r'\[(\d+)\]', line)
                ref = re.sub(r'\[\d+\]\s*', '', line).strip()
                if not num:                
                    num = re.match(r'(\d+)\.', line)
                    ref = re.sub(r'\d+\.\s*', '', line).strip()
                if num and ref:
                    ref_dict[num.group(1)] = ref
            references = [ref_dict[key] for key in sorted(ref_dict.keys(), key=int)]
        else:
            sections.append({
                'level': header['level'],
                'text': header['text'],
                'content': content
            })
    
    return sections, references

def references_extraction(chapter_text, references):
    # 提取章节文本中的所有引用编号（如 [5] 或 [1,2]）
    def extract_reference_numbers(text):
        # 匹配 [数字] 或 [数字,数字,...]
        pattern = r'\[(\d+(?:,\s*\d+)*)\]'
        matches = re.findall(pattern, text)
        ref_nums = set()
        for match in matches:
            nums = [int(num.strip()) for num in match.split(',')]
            ref_nums.update(nums)
        return sorted(ref_nums, key=int)

    ref_nums = extract_reference_numbers(chapter_text)
    extracted_references = [f"[{ref_num}] {references[ref_num-1]}" for ref_num in ref_nums]
    return "\n".join(extracted_references)


if __name__ == "__main__":
    corpus_file = "data/PubMed/corpus.json"
    src_file = "data/PubMed/A Comprehensive Review of Metabolic Syndrome.md"
    print(f"正在处理文件: {src_file}")
    full_paper_text = load_paper(src_file)
    print(f"论文总字数: {len(full_paper_text)} 字")
    sections, references = parse_markdown_sections(full_paper_text)
    with open(corpus_file, "w", encoding="utf-8") as f:
        json.dump({"sections": sections, "references": references}, f, ensure_ascii=False, indent=2)
    print(f"{len(sections)}个章节被解析。")

    veritas_dir = "data/PubMed/veritas"
    os.makedirs(veritas_dir, exist_ok=True)
    for i, section in enumerate(sections):
        if section['level'] != 3:
            continue
        with open(os.path.join(veritas_dir, f"{i+1}.json"), "w", encoding="utf-8") as f:
            section_content = section['content']
            json.dump({"section_content": section_content}, f, ensure_ascii=False, indent=2)
        