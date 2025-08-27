import json
import os
import re
import time
from openai import OpenAI
from dotenv import load_dotenv


load_dotenv(override=True)
LLM_MODEL = os.getenv("llm_model")
LLM_API_KEY = os.getenv("llm_api_key")
LLM_BASE_URL = os.getenv("llm_base_url")
llm_client = OpenAI(api_key=LLM_API_KEY, base_url=LLM_BASE_URL)

def call_llm_with_prompt(prompt, system_prompt=None):
    messages = []
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})
    messages.append({"role": "user", "content": prompt})

    max_retries = 3
    delay = 5
    for attempt in range(max_retries):
        try:
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
            
def extract_xml(text: str, tag: str) -> str:
    match = re.search(f'<{tag}>(.*?)</{tag}>', text, re.DOTALL)
    return match.group(1) if match else ""

def generate_structured_content_summary(section_content):
    prompt_template = """
<role>
You are a professional academic research assistant, skilled at quickly reading, understanding, and summarizing complex scientific literature.
</role>

<task>
Your task is to read and summarize the scientific text provided in `<section_content>`. The summary should accurately capture the core thesis, main arguments, and the logical relationships between them.
</task>

<requirements>
1. **Core Thesis:** Accurately identify and articulate the central theme of the text.
2. **Structured Outline:** Follow the logical structure of the original text, organizing the summary with clear points and sub-points.
3. **Key Concepts:** Extract the key terminology and core concepts presented in the text.
4. **Objective Tone:** Maintain an objective perspective. Do not add personal opinions or interpretations not mentioned in the original text.
</requirements>

<output_format_example>
Please follow this structure:
```XML
<summary>
### **Example Summary: The Process of Photosynthesis**
* **Core Concept and Significance of Photosynthesis**
    * **Primary Function:** The process used by plants, algae, and some bacteria to convert light energy into chemical energy in the form of glucose (sugar).
    * **Key Components:**
        * **Chloroplasts:** The organelles within plant cells where photosynthesis occurs.
        * **Chlorophyll:** The green pigment inside chloroplasts that absorbs sunlight.
    * **Global Importance:**
        * Produces the majority of Earth's oxygen.
        * Forms the foundational energy source for most of the planet's ecosystems.
* **The Two Major Stages of Photosynthesis**
    * **Stage 1: Light-Dependent Reactions**
        * **Location:** Occurs in the thylakoid membranes within the chloroplasts.
        * **Primary Input:** Requires direct sunlight and water ($H_2O$).
        * **Core Process:** Light energy is captured to split water molecules.
        * **Key Outputs:**
            * Oxygen ($O_2$) is released as a byproduct.
            * Energy is stored in temporary carrier molecules (ATP and NADPH).
    * **Stage 2: Light-Independent Reactions (Calvin Cycle)**
        * **Location:** Occurs in the stroma (the fluid-filled space) of the chloroplasts.
        * **Primary Input:** Uses the ATP and NADPH from the first stage, along with carbon dioxide ($CO_2$) from the atmosphere.
        * **Core Process:** Carbon dioxide is "fixed" and converted into sugar.
</summary>
```
</output_format_example>

---
<section_content>
{section_content}
</section_content>
"""
    prompt = prompt_template.format(section_content=section_content)
    response = call_llm_with_prompt(prompt)
    return extract_xml(response, "summary")

def generate_comprehensive_question(summary):
    prompt_template = """
<role>
You are an insightful academic researcher, skilled at distilling core questions from complex materials.
</role>

<task>
Based on the summary provided in `<summary>`, your task is to formulate **ONE (1)** comprehensive and thought-provoking question that covers the core ideas of the entire text.
</task>

<requirements>
1. **Comprehensive:** The question should touch upon all major sections and key arguments of the text.
2. **Synthesizing:** The question should require the respondent to integrate, compare, or analyze different pieces of information from the text, rather than simply recalling a single fact.
3. **In-depth:** The question should guide a deeper level of thinking on the subject.
4. **Clear and Unambiguous:** The question must be clearly and precisely phrased.
</requirements>

<output_format>
Please provide a well-structured question in XML element <question>.
</output_format>

---
<summary>
{summary}
</summary>
"""
    prompt = prompt_template.format(summary=summary)
    response = call_llm_with_prompt(prompt)
    return extract_xml(response, "question")

def formulate_structured_research_plan(summary):
    prompt_template = """
<role>
You are an experienced research advisor, proficient in converting a research topic or a literature review into a concrete, actionable research plan.
</role>

<task>
Based on the provided overview or summary of a research area in `<summary>`, your task is to distill it into a structured and actionable research plan.
</task>

<requirements>
1. **Structured:** Use a step-by-step format, with each step clearly numbered and stating a specific research objective.
2. **Logical Flow:** The steps should follow a logical sequence, such as: defining core concepts, surveying the current landscape, conducting an in-depth analysis, performing a comparative evaluation, and finally, looking toward future directions.
3. **Actionable Steps:** Each step should describe a concrete research action (e.g., "Investigate and define...", "Survey and list...", "Analyze and compare...").
4. **Comprehensive Coverage:** The plan should cover all core aspects of the provided content.
</requirements>

<output_format_example>
Please follow this structure:
```XML
<research_plan>
(1) Investigate the core concepts of..., defining...
(2) Survey and list the current mainstream techniques, models, or frameworks for...
(3) For each identified framework, deeply analyze its implementation mechanisms for...
(4) Compare the strengths and limitations of different frameworks regarding...
(5) Evaluate the capability of these frameworks in addressing the challenge of...
(6) Summarize the frontier research directions and future challenges in the field of...
</research_plan>
```
</output_format_example>

---
<summary>
{summary}
</summary>
"""
    prompt = prompt_template.format(summary=summary)
    response = call_llm_with_prompt(prompt)
    return extract_xml(response, "research_plan")

if __name__ == "__main__":
    corpus_dir = "data/veritas"
    for file in os.listdir(corpus_dir):
        if not file.endswith(".json"):
            continue

        file_path = os.path.join(corpus_dir, file)
        print(f"Processing {file}...")

        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        section_content = data["section_content"]
        summary = generate_structured_content_summary(section_content)
        data["summary"] = summary
        question = generate_comprehensive_question(summary)
        data["question"] = question
        research_plan = formulate_structured_research_plan(summary)
        data["research_plan"] = research_plan

        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"Finished processing {file}. Summary, question, and research plan added.")