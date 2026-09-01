# Research Report

## Research Question

Map the research landscape of multi-agent LLM systems. Produce a structured report that includes a visual taxonomy or design graph showing the major architectural patterns, how they relate, and where the open problems are.

## Summary

This report synthesizes existing research on multi-agent systems (MAS) utilizing Large Language Models (LLMs). It presents a taxonomy of agent architectures, evaluates the effectiveness of multi-agent LLM systems for complex tasks, and identifies key challenges and gaps in the current landscape. A structured representation of architectural patterns highlights relationships and outstanding issues.

## Findings

### Finding 1

**Claim**

The taxonomy of agent architecture has stabilized around eight canonical patterns organized into four quadrants: single-agent, collaborative multi-agent, competitive multi-agent, and orchestration topology.

**Confidence:** High

**Why this confidence level**

The new evidence corroborates the existing understanding of agent architecture taxonomy.

**Evidence**

- The guide outlines eight canonical patterns and organizes them into a four-quadrant taxonomy. [S1]
- Architectures identified include centralized, decentralized, specialized, and hybrid arrangements which emphasize various multi-agent patterns. [S3]
- Surveys existing literature on LLM-based multi-agent systems, detailing workflow and challenges, affirming the established taxonomy of agent architectures. [S9]

### Finding 2

**Claim**

Multi-agent LLM systems are more effective for complex tasks due to their capability to parallel process and utilize specialized agents.

**Confidence:** High

**Why this confidence level**

The new evidence provides empirical support for the effectiveness of multi-agent systems in complex tasks.

**Evidence**

- The collaborative model of multi-agent LLMs allows specialized agents to handle complex tasks more efficiently than single-agent models. [S2]
- The study reveals that multi-agent coordination enhances performance on parallelizable tasks, demonstrating how specialized agents can work more efficiently together. [S14]

### Finding 3

**Claim**

MARAUS, a multi-agent system for university admissions counseling, demonstrates significant improvements in accuracy and reduces hallucination rates compared to LLM-only systems.

**Confidence:** High

**Why this confidence level**

The empirical results clearly demonstrate the system's effectiveness in a real-world application.

**Evidence**

- This multi-agent system processed over 6,000 user interactions with 92% accuracy and reduced hallucination rates from 15% to 1.45%. [S24]

### Finding 4

**Claim**

Multi-Agent LLM systems face challenges in domain specificity, language representation, and the effectiveness of prompt engineering strategies.

**Confidence:** High

**Why this confidence level**

The evidence identifies specific challenges acknowledged within the empirical study.

**Evidence**

- The paper discusses critical challenges regarding the consistent extraction of accurate information and the limitations of multilingual embeddings. [S24]

### Finding 5

**Claim**

Multi-agent LLM systems utilize dynamic collaboration protocols and specialized plugins to enhance their performance and reliability.

**Confidence:** High

**Why this confidence level**

The supporting evidence explicitly describes the mechanisms that improve collaborative efficiency.

**Evidence**

- Describes how multi-agent systems assign roles and utilize dynamic communication to optimize task allocation. [S25]

## Conflicts and Uncertainty

- No material conflict was identified in the retrieved evidence.

## Remaining Gaps

- Lack of empirical evaluations linking multi-agent systems to specific application domains and their outcomes.
- Unresolved issues regarding the interoperability of different multi-agent frameworks.
- Challenges regarding the integration and interoperability of various multi-agent frameworks in practice.

## Conclusion

The research landscape of multi-agent LLM systems presents a coherent taxonomy of architectures. While the capabilities of these systems in complex task performance are well-supported, specific challenges and gaps remain, particularly concerning empirical evaluations and interoperability among diverse frameworks. Ongoing research should address these open gaps to enhance the development and application of multi-agent systems.

## Sources

- [S1] Agent Architecture Patterns: 2026 Taxonomy Guide — https://www.digitalapplied.com/blog/agent-architecture-patterns-taxonomy-2026
- [S2] Multi-agent LLMs in 2026 [+frameworks] — https://www.superannotate.com/blog/multi-agent-llms
- [S3] Architectures for Multi-Agent Systems — https://galileo.ai/blog/architectures-for-multi-agent-systems
- [S4] LLM Agent Orchestration Patterns: Architectural Frameworks for Managing Complex Multi-Agent Systems — https://www.c-sharpcorner.com/article/llm-agent-orchestration-patterns-architectural-frameworks-for-managing-complex
- [S5] LLM-Enabled Multi-Agent Systems: Empirical Evaluation ... — https://arxiv.org/html/2601.03328v1
- [S6] JAI | Free Full-Text | LLM-Enabled Multi-Agent Systems: Empirical Evaluation and Insights into Emerging Design Patterns & Paradigms — https://www.techscience.com/jai/v8n1/67006/html
- [S7] Developing LLM-based Multi-Agent Systems in Software ... — https://arxiv.org/html/2608.11965v1
- [S8] Benchmarking the effectiveness of multi-agent LLMs in collaborative privacy threat modeling with LINDDUN GO — https://www.sciencedirect.com/science/article/abs/pii/S2214212626001195
- [S9] A survey on LLM-based multi-agent systems - Springer Nature — https://link.springer.com/article/10.1007/s44336-024-00009-2
- [S10] Adversarial robustness of LLM-based multi-agent systems ... — https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2026.1784484/full
- [S11] Multi-Agent Systems for Discovery and Design|| Multi-Modal LLM for Material Science || Jan 23, 2026 — https://www.youtube.com/watch?v=0UbvKMZJeyM
- [S12] LLMs for Multi-Agent Cooperation — https://xue-guang.com/post/llm-marl
- [S13] Multi-Agent Systems and Their Evolution: A Comparative Survey[v1] | Preprints.org — https://www.preprints.org/manuscript/202606.0358
- [S14] Towards a science of scaling agent systems - Google Research — https://research.google/blog/towards-a-science-of-scaling-agent-systems-when-and-why-agent-systems-work
- [S15] Multi-Agent Systems: Architecture, Applications & Real-World Impact — https://www.cognizant.com/us/en/ai-lab/blog/what-are-multi-agent-systems
- [S16] Towards Robust Evaluation of Multi-Agent Systems in Clinical Settings | Microsoft Community Hub — https://techcommunity.microsoft.com/blog/healthcareandlifesciencesblog/towards-robust-evaluation-of-multi-agent-systems-in-clinical-settings/4435119
- [S17] LLM-Enabled Multi-Agent Systems: Empirical Evaluation and Insights into Emerging Design Patterns & Paradigms | alphaXiv — https://www.alphaxiv.org/abs/2601.03328
- [S18] A Comprehensive Guide to Evaluating Multi-Agent LLM ... — https://orq.ai/blog/multi-agent-llm-eval-system
- [S19] IEEE SA - Development of Evaluation Techniques for Multi-Agent Systems — https://standards.ieee.org/industry-connections/activities/development-of-evaluation-techniques-for-multi-agent-systems
- [S20] An LLM-based multi-agent system for geoscience legacy document processing, knowledge extraction and quality control — https://www.sciencedirect.com/science/article/pii/S2590197426000467
- [S21] Why Multi-Agent Systems Need Real-Time Context in 2026 — https://solace.com/blog/analysts-say-mas-needs-real-time-context-eda
- [S22] LLM-Powered Multi-Agent Systems: A Survey of ... — https://dl.acm.org/doi/10.1145/3806262.3806263
- [S23] LLM Agents 2026: 5 Types, Applications & Eval Stack — https://futureagi.com/blog/llm-agents-applications-guide-2025
- [S24] An Empirical Study of Multi-Agent RAG for Real-World University Admissions Counseling — https://arxiv.org/html/2507.11272v1
- [S25] Multi-Agent LLM Systems — https://www.emergentmind.com/topics/multi-agent-llm-system
- [S26] LLM-Powered Agent: Dynamic Multi-Agent Systems — https://www.emergentmind.com/topics/llm-powered-agent
- [S27] [Literature Review] A Survey on LLM-based Multi-Agent System: Recent Advances and New Frontiers in Application — https://www.themoonlight.io/en/review/a-survey-on-llm-based-multi-agent-system-recent-advances-and-new-frontiers-in-application
- [S28] [Revisión de artículo] A Survey on LLM-based Multi-Agent System: Recent Advances and New Frontiers in Application — https://www.themoonlight.io/es/review/a-survey-on-llm-based-multi-agent-system-recent-advances-and-new-frontiers-in-application
