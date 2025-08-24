import os
import re
import xml.etree.ElementTree as ET
from xml.dom import minidom
from openai import OpenAI
import time

# --- 配置 ---
LLM_MODEL = "qwen/qwen3-coder"
LLM_API_KEY = ""
LLM_BASE_URL = "https://ai-assistant.jianguoyun.net.cn/openid/openrouter"
llm_client = OpenAI(api_key=LLM_API_KEY, base_url=LLM_BASE_URL)

# --- 工具函数 ---

def pretty_print_xml(xml_string):
    """用于美化输出XML字符串，使其更具可读性"""
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

def call_llm_with_prompt(prompt):
    """封装调用LLM API的函数 (通过 LiteLLM)，包含重试机制"""
    messages = [{"role": "user", "content": prompt}]
    
    max_retries = 3
    delay = 5  # seconds
    for attempt in range(max_retries):
        try:
            print(f"正在LLM API (尝试次数 {attempt + 1}/{max_retries})...")
            # 使用 litellm.completion 调用模型
            response = llm_client.chat.completions.create(
                model=LLM_MODEL,
                messages=messages,
                stream=False,
                temperature=0.6,
                top_p=0.95
            )
            print("API 调用成功！")
            # 从响应中提取内容
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
    # --- 加载论文数据 ---
    try:
        with open(paper_path, 'r', encoding='utf-8') as f:
            full_paper_text = f.read()
        print(f"成功加载论文: {paper_path}")
        print(f"论文总字数: {len(full_paper_text)} 字")
        return full_paper_text
    except FileNotFoundError:
        print(f"错误: 未找到论文文件 '{paper_path}'。请确保它与此Notebook在同一目录下。")
        raise

def parse_markdown_sections(markdown_text):
    """
    提取markdown文档中的章节标题，并将原文分割成结构化的包含各个章节内容的数据
    重构后：每个章节的内容包含所有子章节的内容
    
    Args:
        markdown_text (str): markdown格式的文本内容
        
    Returns:
        list: 包含章节信息的字典列表，每个字典包含:
            - level (int): 标题级别 (1 for #, 2 for ##, etc.)
            - text (str): 标题文本内容
            - content (str): 从标题开始到下一个同级别标题之前的所有内容（包含所有子章节）
    """
    import re
    
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
    references = ""
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
            references = content
        else:
          sections.append({
              'level': header['level'],
              'text': header['text'],
              'content': content
          })
    
    return sections, references

def format_toc_as_string(sections, indent_char='  '):
    """
    将提取的章节列表格式化为可读的目录字符串
    
    Args:
        sections (list): parse_markdown_sections函数返回的章节列表
        indent_char (str): 用于缩进的字符，默认为两个空格
        
    Returns:
        str: 格式化后的目录字符串
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

# --- Pipeline 主流程 ---

# 章节内知识抽取
def knowledge_extraction(chapter_text, references):
    print("\n" + "="*20 + " 步骤 1: 章节内知识抽取 " + "="*20)
    
    prompt_template = """
<ROLE>
你是一位严谨的知识工程师，你的任务是将学术论文的特定章节内容，精确地抽取并结构化为XML格式。你必须严格遵循我定义的Schema，不得遗漏信息或添加无关内容。
</ROLE>

<TASK>
请仔细阅读我提供的章节全文`<CHAPTER>`和参考文献`<REFERENCES>`，并根据定义的XML Schema，抽取出所有的核心实体和它们之间的关系。特别注意：
- **实体识别:** 准确识别出所有的技术、概念、优点、缺点和关键参考文献。
- **关系建立:** 将优点、缺点和参考文献与对应的技术/概念关联起来。
- **引用溯源:** `<citation>` 标签内必须包含论文中对应的引用编号，例如 `[117]`。
</TASK>

<CHAPTER>
{CHAPTER}
</CHAPTER>

<REFERENCES>
{REFERENCES}
</REFERENCES>

<OUTPUT_SCHEMA>
请严格按照以下XML结构输出结果：
```xml
<knowledge_extraction>
  <scope>
    <chapter>章节标题</chapter>
    <section>如果适用，填写小节标题</section>
  </scope>
  <entities>
    <technologies_and_concepts>
      <concept>
        <name>实体名称 (例如: Poisson Process)</name>
        <description>对该技术或概念的简要描述 (1-3句话)。</description>
        <attributes>
          <advantages>
            <advantage>优点1</advantage>
          </advantages>
          <limitations>
            <limitation>局限性1</limitation>
          </limitations>
          <key_findings>
            <finding>关键发现1</finding>
          </key_findings>
        </attributes>
        <citations>
          <citation>[相关的参考文献编号1]</citation>
        </citations>
      </concept>
    </technologies_and_concepts>
  </entities>
  <key_references_in_chapter>
    <reference>
      <citation_id>[引用编号]</citation_id>
      <description>这篇文献的主要贡献是什么。</description>
    </reference>
  </key_references_in_chapter>
</knowledge_extraction>
```
</OUTPUT_SCHEMA>

<INSTRUCTION>
请开始处理我提供的章节文本，并生成符合上述Schema的XML输出。
</INSTRUCTION>
"""
    prompt = prompt_template.format(CHAPTER=chapter_text, REFERENCES=references)
    knowledge_xml = call_llm_with_prompt(prompt)

    print("\n--- LLM 返回的结构化知识 (XML格式) ---")
    print(pretty_print_xml(knowledge_xml))

    knowledge = {}
    knowledge_extraction_xml = extract_xml(knowledge_xml, "knowledge_extraction")
    if knowledge_extraction_xml:
        scope_xml = extract_xml(knowledge_extraction_xml, "scope")
        if scope_xml:
            chapter = extract_xml(scope_xml, "chapter")
            section = extract_xml(scope_xml, "section")
            knowledge["scope"] = {"chapter": chapter, "section": section}

            # entities_xml = extract_xml(knowledge_extraction_xml, "entities")
            # for entity_xml in entities_xml:
            #     name = extract_xml(entity_xml, "name")
            #     description = extract_xml(entity_xml, "description")
            #     advantages = extract_xml(entity_xml, "advantages")
            #     limitations = extract_xml(entity_xml, "limitations")
            #     key_findings = extract_xml(entity_xml, "key_findings")
            #     citations = extract_xml(entity_xml, "citations")
            #     knowledge["entities"].append({
            #         "name": name,
            #         "description": description,
            #         "advantages": advantages,
            #         "limitations": limitations,
            #         "key_findings": key_findings,
            #         "citations": citations
            #     })

    return knowledge

# 4. 构建聚焦型查询-答案对 (Prompt 4)
def step_4_qa_formulation(knowledge_xml):
    """
    执行流程的第四步：根据结构化知识构建QA对。
    """
    print("\n" + "="*20 + " 步骤 4: 构建聚焦型查询-答案对 " + "="*20)
    
    prompt_template = """
# ROLE
你是一位专业的教育评估专家，你的任务是基于一份结构化的知识摘要（XML格式），设计一系列能够精确评估AI研究助理能力的查询-答案对。

# TASK
请分析我提供的XML格式的知识摘要，并创建3-5个高质量的查询-答案对。这些查询应覆盖不同类型的认知能力，并严格遵循我定义的输出格式。
查询类型应至少包含以下几种中的三种：
1.  **总结型 (summary):** 要求对某个技术或概念进行全面总结。
2.  **比较型 (comparison):** 要求比较两个或多个技术的优缺点。
3.  **细节型 (specific_detail):** 针对某个具体的优点、缺点或关键发现提问。
4.  **追溯型 (reference_tracing):** 询问某项关键贡献对应的参考文献。

# INPUT CONTEXT
[INPUT_CONTEXT]

# OUTPUT FORMAT
请严格按照以下XML格式，将所有生成的查询-答案对包裹在一个根元素`<qa_pairs>`中：
```xml
<qa_pairs>
  <qa_pair id="自动生成的唯一ID (例如: NTS_Survey_Chap4_Q1)">
    <scope>
      <chapter>源章节标题</chapter>
      <section>源小节标题</section>
    </scope>
    <query_type>查询类型 (summary, comparison, specific_detail, reference_tracing)</query_type>
    <query_text>生成的查询问题文本。</query_text>
    <ground_truth>
      <key_points>
        <point>
          <text>必须回答的关键点1。</text>
          <citations>
            <citation>支持该观点的参考文献编号</citation>
          </citations>
        </point>
      </key_points>
      <expected_keywords>
        <keyword>用于评估的关键词1</keyword>
      </expected_keywords>
    </ground_truth>
  </qa_pair>
</qa_pairs>
```

# INSTRUCTION
请根据我提供的知识摘要XML，开始生成查询-答案对。
"""
    qa_pairs_xml = call_llm_with_prompt(prompt_template, knowledge_xml)
    
    print("\n--- LLM 生成的最终基准数据集模块 (XML格式) ---")
    print(pretty_print_xml(qa_pairs_xml))
    
    return qa_pairs_xml

# --- 运行完整的 Pipeline ---
if __name__ == "__main__":
    dir = "src/evaluation/data/raw"
    for file in os.listdir(dir):
        print(f"\n正在处理文件: {file}")
        full_paper_text = load_paper(os.path.join(dir, file))
        sections, references = parse_markdown_sections(full_paper_text)
        print(len(sections), "个章节被解析。")

        for section in sections:
            knowledge = knowledge_extraction(section["content"], references)
            print(knowledge.to_dict())
            break

    #     final_dataset_module = step_4_qa_formulation(extracted_knowledge)

    #     print("\n" + "="*20 + " Pipeline 执行完毕 " + "="*20)
    #     print("您已成功生成一个Veritas Benchmark的数据集模块。")
    #     print("您可以将最后一个XML输出保存为文件，作为基准测试的一部分。")
        break
