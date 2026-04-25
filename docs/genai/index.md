---
title: Generative AI
summary: Notes on transformers, LLMs, multimodal models, post-training, and agentic systems.
status: evergreen
updated: 2026-04-24
tags:
  - generative ai
  - llms
  - multimodal
---

<div class="hero-shell section-hero genai-hero">
<p class="hero-eyebrow">Model Families</p>

<h1>Generative AI</h1>

<p class="hero-lead">This section follows the modern generative stack from transformer foundations to LLM behavior, post-training, multimodal generation, and tool-using systems. The goal is to connect equations, implementation choices, and deployed behavior without getting lost in hype cycles.</p>

<div class="chip-row">
<span class="chip">Transformers</span>
<span class="chip">Post-training</span>
<span class="chip">Multimodal</span>
<span class="chip">Agents</span>
</div>

<div class="hero-actions">
<a class="md-button md-button--primary" href="transformer-attention/">Read Transformer Foundations</a>
<a class="md-button" href="../paper-reviews/direct-preference-optimization/">Read DPO Review</a>
</div>
</div>

<div class="hub-grid">
<div class="hub-panel">
<h3>Start Here</h3>
<ul class="link-stack">
  <li><a href="transformer-attention/">Transformer &amp; Attention Foundations</a><p>Then use this hub to branch into LLMs, post-training, multimodal work, or agents.</p></li>
</ul>
</div>

<div class="hub-panel">
<h3>Core Tracks</h3>
<ul>
  <li>Large language models and architecture choices</li>
  <li>Post-training and preference optimization</li>
  <li>Multimodal generation and representation learning</li>
  <li>Agents, tool use, and systems-aware evaluation</li>
</ul>
</div>

<div class="hub-panel">
<h3>Latest Notes</h3>
<ul class="link-stack">
  <li><a href="../paper-reviews/direct-preference-optimization/">Paper Review: Direct Preference Optimization</a></li>
  <li><p>More model and post-training deep dives will accumulate here.</p></li>
</ul>
</div>
</div>

## Research Radar

Updated April 24, 2026.

This radar now prioritizes 2025-2026 material. A 2024 paper stays only if it still functions as an impact paper, a benchmark anchor, or the cleanest public reference for a direction.

### Active Directions

- Reasoning-centric post-training is shifting from plain SFT plus preference tuning toward reinforcement learning, verifiers, controllable thinking budgets, and stronger evaluation.
- Long-context work is increasingly about memory systems and retrieval-aware inference, not just bigger context windows on paper.
- Native multimodal systems are moving from image-text add-ons toward audio, video, and world-model-like reasoning stacks.
- Agent research is moving from single tool calls toward long-horizon orchestration, browsing, coding, and scientific-workflow evaluation.
- Frontier capability is fragmenting into general-purpose models plus domain-specialized reasoning systems for science, coding, and research assistance.

### Keywords To Track

`reasoning models`, `thinking budget`, `verifier`, `RL post-training`, `long-context memory`, `retrieval-augmented inference`, `multimodal world models`, `video generation`, `tool orchestration`, `agent evals`

### Recent Papers And Benchmarks By Direction

#### Reasoning And Post-Training

- [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](https://arxiv.org/abs/2501.12948) (2025)
- [Qwen3 Technical Report](https://arxiv.org/abs/2505.09388) (2025)
- [Our First Proof submissions](https://openai.com/research/index/conclusion/) (OpenAI, February 20, 2026; kept here as a frontier reasoning milestone rather than a classic paper)

#### Long-Context, Memory, And Retrieval-Aware Inference

- [Long Context Modeling with Ranked Memory-Augmented Retrieval](https://arxiv.org/abs/2503.14800) (2025)
- [Long-Context Inference with Retrieval-Augmented Speculative Decoding](https://arxiv.org/abs/2502.20330) (2025)
- [In-Context Learning with Long-Context Models: An In-Depth Exploration](https://arxiv.org/abs/2405.00200) (2024, kept because it remains a useful impact reference on many-shot long-context behavior)

#### Native Multimodal Models

- [AudioGen-Omni: A Unified Multimodal Diffusion Transformer for Video-Synchronized Audio, Speech, and Song Generation](https://arxiv.org/abs/2508.00733) (2025)
- [Bridging the Gap Between Multimodal Foundation Models and World Models](https://arxiv.org/abs/2510.03727) (2025)
- [Visual Reasoning Benchmark: Evaluating Multimodal LLMs on Classroom-Authentic Visual Problems from Primary Education](https://arxiv.org/abs/2602.12196) (2026)
- [CogVideoX: Text-to-Video Diffusion Models with An Expert Transformer](https://arxiv.org/abs/2408.06072) (2024, kept as an impact open video-generation reference)

#### Agents, Tool Use, And Evaluation

- [The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration](https://arxiv.org/abs/2603.22862) (2026 survey)
- [Survey on Evaluation of LLM-based Agents](https://arxiv.org/abs/2503.16416) (2025)
- [PaperBench: Evaluating AI's Ability to Replicate AI Research](https://openai.com/research/paperbench/) (OpenAI, April 2, 2025)
- [BrowseComp: a benchmark for browsing agents](https://openai.com/index/browsecomp/) (OpenAI, April 10, 2025)
- [MIRAI: Evaluating LLM Agents for Event Forecasting](https://arxiv.org/abs/2407.01231) (2024, kept as an impact benchmark)

### Sources To Follow

- [OpenAI Research Index](https://openai.com/research/index/)
- [Anthropic Research](https://www.anthropic.com/research)
- [Google DeepMind Research](https://deepmind.google/en/research/)
- [OpenReview](https://openreview.net/) for fast-moving ICLR-style agent and reasoning papers
- [Hugging Face Blog](https://huggingface.co/blog) for open-model, dataset, and post-training ecosystem updates

### Canonical References Worth Keeping

- [Attention Is All You Need](https://arxiv.org/abs/1706.03762)
- [Direct Preference Optimization](https://arxiv.org/abs/2305.18290)
- [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629)

## Key Resources

- **Blog**: [Lilian Weng's blog](https://lilianweng.github.io/) for technical summaries.
- **Visuals**: [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/).
- **Course**: [Neural Networks: Zero to Hero](https://karpathy.ai/zero-to-hero.html) by Andrej Karpathy.
