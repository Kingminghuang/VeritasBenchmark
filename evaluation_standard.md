## Ground Truth 构建方法

### 1. **数据来源与预处理**
- **原始数据**：从科学文献中提取的章节内容（`section_content`），包含完整的研究描述、方法论和参考文献
- **文献范围**：涵盖多个领域的综述性论文，如AI研究、多模态大语言模型、计算机视觉等
- **数据格式**：每个数据样本以JSON格式存储，包含section_content、references等字段

### 2. **三阶段自动化生成流程**
基于main.py中的实现，Ground Truth通过以下三个阶段自动生成：

#### 阶段一：结构化内容摘要生成（`generate_structured_content_summary`）
- **输入**：原始科学文献章节内容
- **处理方法**：使用LLM进行深度理解和结构化总结
- **输出要求**：
  - 准确识别核心主题和论点
  - 遵循原文逻辑结构，形成清晰的要点和子要点
  - 提取关键概念和术语
  - 保持客观视角，不添加原文未提及的个人观点

#### 阶段二：综合性问题生成（`generate_comprehensive_question`）
- **输入**：第一阶段生成的结构化摘要
- **处理方法**：基于摘要内容，制定一个涵盖全文核心思想的综合性问题
- **输出要求**：
  - 问题应触及文本的所有主要部分和关键论点
  - 需要整合、比较或分析不同信息片段，而非简单事实回忆
  - 引导深层次思考
  - 表述清晰、明确无歧义

#### 阶段三：结构化研究计划制定（`formulate_structured_research_plan`）
- **输入**：第一阶段生成的结构化摘要
- **处理方法**：将研究主题转化为具体可执行的研究计划
- **输出要求**：
  - 使用编号步骤格式，每步骤明确具体的研究目标
  - 遵循逻辑顺序：定义核心概念 → 调研现状 → 深入分析 → 比较评估 → 未来方向
  - 每个步骤描述具体的研究行动（如"调研和列举..."、"分析和比较..."）
  - 全面覆盖提供内容的所有核心方面

### 3. **质量控制机制**
- **模型配置**：使用temperature=0.6, top_p=0.95确保输出的一致性和创造性平衡
- **重试机制**：API调用失败时自动重试，最多3次，确保生成的稳定性
- **格式规范**：使用XML标签提取特定内容，确保输出结构的标准化

### 4. **Ground Truth的特点**
- **高质量标准答案**：经过三阶段精炼，形成从内容理解到研究规划的完整链条
- **领域专业性**：针对不同科学领域的特定术语和概念进行准确处理
- **结构化程度高**：research_plan采用明确的编号步骤，便于后续比较分析

## 评估方法

### 1. **比较分析法**
- 将Ground Truth计划作为"Plan A"（标准答案）
- 将AI Agent生成的计划作为"Plan B"（待评估对象）
- 进行逐点对比分析

### 2. **三层次评估结构**
- **整体结论层**：对覆盖情况给出总体判断
- **逐点分析层**：针对Plan A中每个要点进行详细分析
- **差异总结层**：归纳两个计划的核心差异

## 评估标准

### 1. **覆盖状态分类**
- **Fully Covered（完全覆盖）**：Plan B完整包含了Plan A的要点
- **Partially Covered（部分覆盖）**：Plan B部分涉及了Plan A的要点
- **Not Covered（未覆盖）**：Plan B完全没有涉及Plan A的要点

### 2. **评估维度**
- **内容完整性**：是否覆盖了所有研究要点
- **视角差异性**：是否从不同角度或更深层次覆盖
- **方法论差异**：研究方法和重点的差异
- **遗漏识别**：明确指出Plan B中的缺失部分

### 3. **定量分析**
通过正则表达式提取"Coverage Status"，统计各类覆盖状态的数量和比例，提供量化的评估结果。

这种评估方法强调**全面性**和**准确性**，既关注内容覆盖的广度，也考虑表达方式和研究视角的差异。

## Output Example
**I. Overall Conclusion**
[State your overall judgment here]

**II. Point-by-Point Comparative Analysis**
* **Regarding Point (1) of Plan A:**
    * **Coverage Status:** [e.g., Fully Covered / Partially Covered / Not Covered]
    * **Rationale and Analysis:** [Explain in detail which parts of Plan B correspond to this point and describe the manner and extent of the coverage.]
* **Regarding Point (2) of Plan A:**
    * **Coverage Status:** [...]
    * **Rationale and Analysis:** [...]
* (Continue for every point in Plan A)

**III. Summary of Core Differences**
[Summarize the fundamental differences between the two plans here]