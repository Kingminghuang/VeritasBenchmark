import json
import os
import re
import time
from xml.dom import minidom
from openai import OpenAI
from dotenv import load_dotenv
from tqdm import tqdm

load_dotenv(override=True)
LLM_MODEL = os.getenv("llm_model")
LLM_API_KEY = os.getenv("llm_api_key")
LLM_BASE_URL = os.getenv("llm_base_url")
print(f"LLM_MODEL: {LLM_MODEL}")
print(f"LLM_API_KEY: {LLM_API_KEY[:4]}***")
print(f"LLM_BASE_URL: {LLM_BASE_URL}")
llm_client = OpenAI(api_key=LLM_API_KEY, base_url=LLM_BASE_URL)


def pretty_print_xml(xml_string):
    try:
        # 清理可能存在于LLM输出中的代码块标记
        cleaned_string = re.sub(r'```xml\s*|\s*```', '', xml_string).strip()
        dom = minidom.parseString(cleaned_string)
        return dom.toprettyxml(indent="  ")
    except Exception as e:
        print(f"--- XML解析失败 ---")
        print(f"错误: {e}")
        print("将返回原始字符串:")
        return xml_string

def call_llm_with_prompt(prompt, system_prompt=None):
    messages = []
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})
    messages.append({"role": "user", "content": prompt})

    max_retries = 3
    delay = 5  # seconds
    for attempt in range(max_retries):
        try:
            print(f"正在调用LLM API (尝试次数 {attempt + 1}/{max_retries})...")
            response = llm_client.chat.completions.create(
                model=LLM_MODEL,
                messages=messages,
                stream=False,
                temperature=0.6,
                top_p=0.95
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"API 调用失败: {e}")
            if attempt < max_retries - 1:
                print(f"将在 {delay} 秒后重试...")
                time.sleep(delay)
            else:
                print("已达到最大重试次数。")
                return f"<error>API call failed after {max_retries} attempts: {e}</error>"

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

def format_toc_as_string(sections, indent_char='  '):
    """
    Format the extracted section list into a readable table of contents string.
    
    Args:
        sections (list): The list of sections returned by the parse_markdown_sections function.
        indent_char (str): Character used for indentation, default is two spaces.
        
    Returns:
        str: The formatted table of contents string.
    """
    if not sections:
        return "目录为空"
    
    toc_lines = []
    for section in sections:
        indent = indent_char * (section['level'] - 1)
        toc_lines.append(f"{indent}- {section['text']}")
    
    return '\n'.join(toc_lines)

def extract_xml(text: str, tag: str) -> str:
    """
    Extracts the content of the specified XML tag from the given text. Used for parsing structured responses 

    Args:
        text (str): The text containing the XML.
        tag (str): The XML tag to extract content from.

    Returns:
        str: The content of the specified XML tag, or an empty string if the tag is not found.
    """
    match = re.search(f'<{tag}>(.*?)</{tag}>', text, re.DOTALL)
    return match.group(1) if match else ""

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

# Chapter knowledge extraction
def knowledge_extraction(chapter_text, reference_text):
    prompt_template = """
<ROLE>
You are a rigorous knowledge engineer. Your task is to precisely extract and structure specific chapter content from academic papers into XML format. You must strictly follow the Schema I define, without omitting information or adding irrelevant content.
</ROLE>

<TASK>
Please carefully read the complete chapter text I provide in `<CHAPTER>` and references in this chapter`<REFERENCES>`, and extract all core entities and their relationships according to the defined XML Schema. Pay special attention to:
- **Entity identification:** Accurately identify all technologies, concepts, advantages, disadvantages, and key references.
- **Relationship establishment:** Associate advantages, disadvantages, and references with corresponding technologies/concepts.
- **Citation tracing:** The `<citation>` tag must contain the corresponding citation number from the paper, e.g., `[117]`.
</TASK>

<CHAPTER>
{CHAPTER}
</CHAPTER>

<REFERENCES>
{REFERENCES}
</REFERENCES>

<OUTPUT_SCHEMA>
Please strictly output results according to the following XML structure:
```xml
<knowledge_extraction>
  <scope>
    <chapter>Chapter title</chapter>
    <section>If applicable, fill in section title</section>
  </scope>
  <entities>
    <technologies_and_concepts>
      <concept>
        <name>Entity name (e.g., Poisson Process)</name>
        <description>A brief description of this technology or concept (1-3 sentences).</description>
        <attributes>
          <advantages>
            <advantage>Advantage 1</advantage>
          </advantages>
          <limitations>
            <limitation>Limitation 1</limitation>
          </limitations>
          <key_findings>
            <finding>Key finding 1</finding>
          </key_findings>
        </attributes>
        <citations>
          <citation>[Related reference number 1]</citation>
        </citations>
      </concept>
    </technologies_and_concepts>
  </entities>
  <key_references_in_chapter>
    <reference>
      <citation_id>[Citation number]</citation_id>
      <description>What is the main contribution of this literature.</description>
    </reference>
  </key_references_in_chapter>
</knowledge_extraction>
```
</OUTPUT_SCHEMA>

<INSTRUCTION>
Please begin processing the chapter text I provide and generate XML output that conforms to the above Schema.
</INSTRUCTION>
"""
    prompt = prompt_template.format(CHAPTER=chapter_text, REFERENCES=reference_text)
    knowledge_xml = call_llm_with_prompt(prompt)
    return knowledge_xml

def qa_extraction(knowledge_text, chapter_text, reference_text):
    prompt_template = """
<ROLE>
You are a professional educational assessment expert. Your task is to design a series of query-answer pairs that can accurately assess the capabilities of AI research assistants based on a structured knowledge summary (XML format).
</ROLE>

<TASK>
Please analyze the XML format knowledge summary `KNOWLEDGE`, the full chapter text `<CHAPTER>` and the reference of this chapter `<REFERENCES>`, and create 3-5 high-quality query-answer pairs. These queries should cover different types of cognitive abilities and strictly follow the output format I defined.
The query types must include at least three of the following:
1.  **Summary (summary):** Requires a comprehensive summary of a specific technology or concept.
2.  **Comparison (comparison):** Requires a comparison of the advantages and disadvantages of two or more technologies.
3.  **Specific Detail (specific_detail):** Asks about a specific advantage, disadvantage, or key finding.
4.  **Reference Tracing (reference_tracing):** Inquires about the reference literature corresponding to a key contribution.
</TASK>

<KNOWLEDGE>
{KNOWLEDGE}
</KNOWLEDGE>

<CHAPTER>
{CHAPTER}
</CHAPTER>

<REFERENCES>
{REFERENCES}
</REFERENCES>

<OUTPUT_FORMAT>
Please strictly follow the XML format below, wrapping all generated query-answer pairs in a root element `<qa_pairs>`:
```xml
<qa_pairs>
  <qa_pair id="Auto-generated unique ID (e.g., NTS_Survey_Chap4_Q1)">
    <chapter>Source chapter title</chapter>
    <section>Source section title</section>
    <query_type>Query type (summary, comparison, specific_detail, reference_tracing)</query_type>
    <query_text>Generated query question text.</query_text>
    <ground_truth>
      <key_points>
        <point>
          <text>Key point 1 that must be answered.</text>
          <citations>
            <citation>Reference number supporting this viewpoint</citation>
          </citations>
        </point>
      </key_points>
      <expected_keywords>
        <keyword>Keyword 1 for evaluation</keyword>
      </expected_keywords>
    </ground_truth>
  </qa_pair>
</qa_pairs>
```
</OUTPUT_FORMAT>

<INSTRUCTION>
Please begin generating query-answer pairs based on the knowledge summary XML I provide.
</INSTRUCTION>
"""
    prompt = prompt_template.format(KNOWLEDGE=knowledge_text, CHAPTER=chapter_text, REFERENCES=reference_text)
    response = call_llm_with_prompt(prompt)

    qa = []
    qa_pairs_xml = re.findall(r'<qa_pair id=".*?">.*?</qa_pair>', response, re.DOTALL)
    for qa_pair_xml in qa_pairs_xml:
        chapter = extract_xml(qa_pair_xml, "chapter")
        section = extract_xml(qa_pair_xml, "section")
        query_type = extract_xml(qa_pair_xml, "query_type")
        query_text = extract_xml(qa_pair_xml, "query_text")
        ground_truth_xml = extract_xml(qa_pair_xml, "ground_truth")
        key_points_xml = re.findall(r'<point>.*?</point>', ground_truth_xml, re.DOTALL)
        key_points = []
        for key_point_xml in key_points_xml:
            key_point = extract_xml(key_point_xml, "text")
            citations_xml = re.findall(r'<citation>.*?</citation>', key_point_xml, re.DOTALL)
            citations = []
            for citation_xml in citations_xml:
                citation = extract_xml(citation_xml, "citation")
                citations.append(citation.removeprefix("[").removesuffix("]"))
            key_points.append({
                "text": key_point,
                "citations": citations
            })
        keywords = []
        keywords_xml = re.findall(r'<keyword>.*?</keyword>', ground_truth_xml, re.DOTALL)
        for keyword_xml in keywords_xml:
            keyword = extract_xml(keyword_xml, "keyword")
            keywords.append(keyword)
        qa.append({
            "chapter": chapter,
            "section": section,
            "query_type": query_type,
            "query_text": query_text,
            "ground_truth": {
                "key_points": key_points,
                "expected_keywords": keywords
            }
        })

    return qa

if __name__ == "__main__":
    corpus_file = "data/corpus.json"
    if not os.path.exists(corpus_file):
        src_file = "data/AI4Research - A Survey of Artificial Intelligence for Scientific Research.md"
        print(f"正在处理文件: {src_file}")
        full_paper_text = load_paper(src_file)
        print(f"论文总字数: {len(full_paper_text)} 字")
        sections, references = parse_markdown_sections(full_paper_text)
        with open(corpus_file, "w", encoding="utf-8") as f:
            json.dump({"sections": sections, "references": references}, f, ensure_ascii=False, indent=2)
    else:
        with open(corpus_file, "r", encoding="utf-8") as f:
            data = json.load(f)
            sections, references = data["sections"], data["references"]
    print(f"{len(sections)}个章节被解析。")

    dst_file = "data/veritas.jsonl"
    start = 0
    if os.path.exists(dst_file):
        with open(dst_file, "r", encoding="utf-8") as f:
            for line in f:
                start += 1

    with open(dst_file, "a", encoding="utf-8") as f:
        for section in tqdm(sections[start:], desc="Processing sections"):
            if section["level"] == 1:
                continue
            section_content = section["content"]
            print(f"章节总字数: {len(section_content)} 字")
            reference_text = references_extraction(chapter_text=section_content, references=references)
            print(f"章节引用总字数: {len(reference_text)} 字")
            knowledge = knowledge_extraction(section_content, reference_text)
            print(f"知识抽取结果总字数: {len(knowledge)} 字")
            qa_pairs = qa_extraction(knowledge, section_content, reference_text)
            data = {
                "section_content": section_content,
                "qa_pairs": qa_pairs,
                "references": references
            }
            f.write(json.dumps(data, ensure_ascii=False))
            f.write("\n")
