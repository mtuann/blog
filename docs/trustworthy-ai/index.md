---
title: Trustworthy AI
summary: Live research directions in evaluation, interpretability, jailbreaks, backdoor attacks, hallucination, and agent oversight.
status: evergreen
updated: 2026-04-25
tags:
  - trustworthy ai
  - safety
  - evaluation
---

This page is a living map of trustworthy-AI research. It focuses on the moving frontier in evaluation, auditing, interpretability, hallucination, and agent oversight, rather than trying to summarize “AI safety” as one monolithic subject.

## Topic Map

- **Evaluation and auditing**
  This is where much of the field is re-centering: moving from static benchmark worship to audits, hidden-behavior discovery, deployment-shaped testbeds, and evaluation agents.
- **Jailbreaks and safety-utility tradeoffs**
  The live question is no longer just “can a model be jailbroken?” but which attacks transfer, which defenses stay useful, and what costs safety measures impose on legitimate use.
- **Backdoor attacks and trojaned post-training**
  This is increasingly a foundation-model problem rather than only a classical poisoned-classifier problem: triggers can be clean-sample, hidden in supply-chain artifacts, or activated through multimodal and agentic workflows.
- **Interpretability and mechanistic reliability**
  Sparse autoencoders, feature dictionaries, and automated interpretability pipelines are now central, but the real frontier question is whether they change engineering decisions or only produce attractive analyses.
- **Hallucination and calibration**
  This is shifting from anecdotal error collection to benchmark design, authentic-user evaluation, abstention behavior, and uncertainty-aware response strategies.
- **Agent oversight**
  As models become longer-horizon tool users, trustworthy-AI work is increasingly about monitoring, auditing, and constraining agentic behavior rather than only scoring single-shot outputs.

## Research Questions Right Now

- What evaluation setups still matter once frontier models saturate the old public benchmarks?
- Which jailbreak benchmarks measure real deployment risk rather than benchmark gaming?
- What realistic backdoor threat models matter once attackers no longer need explicit trigger strings in user prompts?
- When do interpretability tools produce operational leverage instead of post hoc storytelling?
- How should hallucination be measured when tasks are ambiguous, open-ended, or multi-turn?
- What does scalable oversight look like once agents browse, code, and plan over long horizons?

## Research Radar

Updated April 24, 2026.

This radar emphasizes 2025-2026 work. Older entries remain only when they are still the benchmark anchor or the cleanest canonical reference for a live subfield.

### Active Directions

- Safety evaluation is moving from static benchmarks toward audit realism, hidden-objective discovery, and deployment-shaped testbeds.
- Jailbreak research is shifting from one-shot attacks toward multi-turn, weak-to-strong, and workflow-specific attacks, with explicit safety-utility tradeoff measurement.
- Backdoor research is shifting from toy trigger poisoning toward clean-sample, multimodal, agentic, and distributed attack surfaces, alongside trigger-agnostic defenses.
- Interpretability is increasingly centered on sparse autoencoders, feature robustness, and whether mechanistic tools actually help engineering and auditing.
- Hallucination work is becoming more evaluation-aware: better taxonomies, authentic-user benchmarks, and incentives for calibrated abstention.
- Agent safety and scalable oversight are becoming central as models take longer-horizon actions with tools and memory.

### Keywords To Track

`AuditBench`, `alignment auditing`, `agentic misalignment`, `StrongREJECT`, `BackdoorLLM`, `triggerless backdoor`, `safety-utility tradeoff`, `sparse autoencoders`, `hallucination benchmarks`, `preparedness`, `system cards`, `agentic oversight`

### Recent Papers And Research Signals By Direction

#### Evaluation, Auditing, And Oversight

- [AuditBench: Evaluating Alignment Auditing Techniques on Models with Hidden Behaviors](https://alignment.anthropic.com/2026/auditbench/) (Anthropic, March 10, 2026)
- [Building and evaluating alignment auditing agents](https://alignment.anthropic.com/2025/automated-auditing/) (Anthropic, July 24, 2025)
- [Automated Alignment Researchers: Using large language models to scale scalable oversight](https://www.anthropic.com/research/automated-alignment-researchers?curius=1184) (Anthropic, April 14, 2026)
- [A3: An Automated Alignment Agent for Safety Finetuning](https://alignment.anthropic.com/2026/automated-alignment-agent/) (Anthropic, March 11, 2026)
- [MMLU-Pro: A More Robust and Challenging Multi-Task Language Understanding Benchmark](https://arxiv.org/abs/2406.01574) (2024, kept as a benchmark anchor)

#### Jailbreaks, Defenses, And Safety-Utility Tradeoffs

- [HarDBench: A Benchmark for Draft-Based Co-Authoring Jailbreak Attacks for Safe Human-LLM Collaborative Writing](https://arxiv.org/abs/2604.19274) (2026)
- [Boundary Point Jailbreaking of Black-Box LLMs](https://arxiv.org/abs/2602.15001) (2026)
- [AutoRAN: Weak-to-Strong Jailbreaking of Large Reasoning Models](https://arxiv.org/abs/2505.10846) (2025)
- [A StrongREJECT for Empty Jailbreaks](https://arxiv.org/abs/2402.10260) (2024, kept as a benchmark anchor)

#### Interpretability And Mechanistic Reliability

- [AdaptiveK Sparse Autoencoders: Dynamic Sparsity Allocation for Interpretable LLM Representations](https://arxiv.org/abs/2508.17320) (2025)
- [Temporal Sparse Autoencoders: Leveraging the Sequential Nature of Language for Interpretability](https://arxiv.org/abs/2511.05541) (2025)
- [Interpretability Illusions with Sparse Autoencoders: Evaluating Robustness of Concept Representations](https://arxiv.org/abs/2505.16004) (2025)
- [A Survey on Sparse Autoencoders: Interpreting the Internal Mechanisms of Large Language Models](https://arxiv.org/abs/2503.05613) (2025 survey)

#### Hallucination, Calibration, And Reliability

- [Why language models hallucinate](https://openai.com/index/why-language-models-hallucinate) (OpenAI, September 5, 2025)
- [Detecting Hallucinations in Authentic LLM-Human Interactions](https://arxiv.org/abs/2510.10539) (2025)
- [HalluLens: LLM Hallucination Benchmark](https://arxiv.org/abs/2504.17550) (2025)
- [HalluVerse25: Fine-grained Multilingual Benchmark Dataset for LLM Hallucinations](https://arxiv.org/abs/2503.07833) (2025)

## Site Coverage

- [Backdoor Attacks](backdoor-attacks/index.md)
  The dedicated subtopic page for backdoor threats in LLMs, VLMs, agents, model merging, and distributed post-training.
- [Research Notes](../research-notes/index.md)
  The home for future paper reviews, reading maps, and roundups that will deepen this topic without bloating the overview.
- [Paper Review: Direct Preference Optimization](../paper-reviews/direct-preference-optimization.md)
  A relevant current note for preference learning and post-training, which still touches evaluation and safety tradeoffs even if it is not a full trustworthy-AI page.

## Sources To Follow

- [Anthropic Research](https://www.anthropic.com/research)
- [Anthropic Alignment Research](https://www.anthropic.com/research/team/alignment)
- [OpenAI Safety](https://openai.com/safety/)
- [OpenAI Safety Evaluations Hub](https://openai.com/safety/evaluations-hub/)
- [Transformer Circuits](https://transformer-circuits.pub/)

## Open Backlog

- A deeper note on evaluation after benchmark saturation: auditing, grader design, hidden-behavior discovery, and deployment realism.
- A focused reading map on jailbreak research and safety-utility tradeoffs across 2025-2026.
- A dedicated note on sparse autoencoders, feature robustness, and what counts as real interpretability progress.
- A research note on hallucination taxonomies, abstention, and authentic-user evaluation.
- A future overview of agent oversight and scalable monitoring once agentic behavior becomes the default deployment mode.
