import re


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

knowledge_xml = """
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
"""

knowledge = {}
knowledge_extraction_xml = extract_xml(knowledge_xml, "knowledge_extraction")
if knowledge_extraction_xml:
    scope_xml = extract_xml(knowledge_extraction_xml, "scope")
    if scope_xml:
        chapter = extract_xml(scope_xml, "chapter")
        section = extract_xml(scope_xml, "section")
        knowledge['scope'] = {'chapter': chapter, 'section': section}
print(knowledge)