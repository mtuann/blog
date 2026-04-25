---
title: Backdoor Attacks
summary: Live research directions in backdoor attacks and defenses for LLMs, VLMs, agents, model merging, and decentralized post-training.
status: evergreen
updated: 2026-04-25
tags:
  - trustworthy ai
  - backdoor attacks
  - trojan attacks
  - llm security
---

This page is a living map of backdoor-attack research for foundation models. It focuses on LLMs, VLMs, agents, model merging, federated or decentralized post-training, and trigger-agnostic defenses; it does not try to cover every poisoning or adversarial-example result outside the backdoor setting.

## Topic Map

- **Canonical backdoor threat model**
  The original framing is still useful: an attacker implants hidden behavior during training or model preparation, the model stays mostly normal on benign inputs, and a trigger or latent condition activates malicious behavior later.
- **Stealthier trigger design**
  The frontier is moving beyond visible token triggers toward clean-sample, harmless-input, endogenous-feature, and reasoning-level triggers that better match real deployments.
- **Foundation-model supply-chain attacks**
  Open checkpoints, PEFT adapters, model merging, and decentralized post-training create new supply-chain surfaces that did not exist in the classic image-classification setting.
- **Multimodal and agentic backdoors**
  Backdoor threats now propagate through image-text systems, tool-use workflows, planning traces, memory, and other long-horizon execution states.
- **Defense, attribution, and purification**
  The main research shift is away from simple trigger inversion assumptions toward generative-model purification, mechanistic attribution, and workflow-aware defenses.
- **Evaluation and benchmark design**
  Benchmark quality matters a lot here because attack success rate on a toy trigger is much less useful than realistic trigger coverage, open-ended generation behavior, and deployment-shaped tasks.

## Research Questions Right Now

- What is the right threat model for foundation-model backdoors when attackers do not control user prompts directly?
- Which supply-chain surface is now the most dangerous in practice: poisoned data, public checkpoints, LoRA adapters, model merges, federated updates, or pipeline stages?
- Which defenses still work when the trigger is unknown, clean-sample, or endogenous to the system prompt or workflow state?
- How should backdoors be evaluated for open-ended generation, multimodal systems, and agentic workflows rather than only classification accuracy?
- Which backdoor behaviors matter most in modern deployments: harmful completions, deceptive reasoning, hidden refusals, cost inflation, jailbreak-style overrides, or tool-use corruption?

## Research Radar

Updated April 25, 2026.

This radar emphasizes 2025-2026 work. Older references stay only when they still define the core threat model, canonical attack pattern, or benchmark foundation.

### Active Directions

- Threat models are shifting from explicit attacker-inserted trigger strings toward clean-sample, harmless-input, and endogenous-feature triggers that ordinary users might naturally produce.
- Backdoor research is expanding beyond fine-tuning data poisoning into model merging, federated or decentralized post-training, agents, and multimodal systems.
- The objective of a backdoor is broadening from simple target completions to deceptive reasoning, refusal overrides, cost inflation, and workflow corruption.
- Benchmarks are finally becoming more standardized for language and multimodal settings, making attack and defense claims easier to compare.
- Defenses are moving from generic pruning or filtering toward trigger-agnostic purification, mechanistic attribution, and deployment-shaped anomaly detection.

### Keywords To Track

`BadNets`, `clean-sample backdoor`, `harmless-input poisoning`, `triggerless backdoor`, `model merging backdoor`, `BackdoorLLM`, `BackdoorVLM`, `agent backdoor`, `backdoor attribution`, `backdoor purification`

### Recent Papers And Research Signals By Direction

#### Threat Models And Trigger Design

- [Wei et al. (2026), When Clean Queries Become Triggers: Backdoor Attacks on Large Language Models](https://openreview.net/forum?id=51n0n1Lpdt) (ICLR 2026 submission)
- [Kong et al. (2026), Revisiting Backdoor Attacks on LLMs: A Stealthy and Practical Poisoning Framework via Harmless Inputs](https://openreview.net/forum?id=EG6K7ZWOwQ) (ICLR 2026 submission)
- [Hu et al. (2026), The Blind Spot of LLM Security: Time-Sensitive Backdoors Activated by Inherent Features](https://openreview.net/forum?id=e8w3aO02sq) (ICLR 2026 submission)
- [Shen et al. (2026), DecepChain: Inducing Deceptive Reasoning in Large Language Models](https://openreview.net/forum?id=q7UNF65j5m) (ICLR 2026 submission)
- [Reitano et al. (2026), Inflation-Troj: Inflating LLM Operating Costs through Stealthy Backdoor Injection](https://openreview.net/forum?id=aFukqpdsVJ) (ICLR 2026 submission)

#### Supply-Chain, Distributed, And Workflow Attack Surfaces

- [Yuan et al. (2025), Merge Hijacking: Backdoor Attacks to Model Merging of Large Language Models](https://arxiv.org/abs/2505.23561) (accepted to ACL 2025)
- [Ersoy et al. (2026), Backdoor Attacks on Decentralised Post-Training](https://openreview.net/forum?id=FveQNDaHnZ) (ICLR 2026 Trustworthy AI)
- [Feng et al. (2026), BackdoorAgent: A Unified Framework for Backdoor Attacks on LLM-based Agents](https://arxiv.org/abs/2601.04566)
- [Li et al. (2026), AutoBackdoor: Automating Backdoor Attacks via LLM Agents](https://openreview.net/forum?id=J2UFyF9YeD) (ICLR 2026 submission)

#### Benchmarks And Evaluation Infrastructure

- [Li et al. (2025), BackdoorLLM: A Comprehensive Benchmark for Backdoor Attacks and Defenses on Large Language Models](https://openreview.net/forum?id=sYLiY87mNn) (NeurIPS 2025 Datasets and Benchmarks poster)
- [Li et al. (2025), BackdoorVLM: A Benchmark for Backdoor Attacks on Vision-Language Models](https://arxiv.org/abs/2511.18921)
- [Chen et al. (2022), BackdoorBench: A Comprehensive Benchmark of Backdoor Learning](https://openreview.net/forum?id=31_U7n18gM7) (NeurIPS 2022 Datasets and Benchmarks, still the canonical benchmark anchor)

#### Defenses, Attribution, And Purification

- [Li et al. (2026), Purifying Generative LLMs from Backdoors without Prior Knowledge or Clean Reference](https://openreview.net/forum?id=M7eWB695jp) (ICLR 2026 poster)
- [Yu et al. (2026), Backdoor Attribution: Elucidating and Controlling Backdoor in Language Models](https://openreview.net/forum?id=RPflMrUF3O) (ICLR 2026 withdrawn submission, still a useful mechanistic signal)
- [Shen et al. (2026), From Poisoned to Aware: Fostering Backdoor Self-Awareness in LLMs](https://openreview.net/forum?id=kBzyIo7Ze6) (ICLR 2026 submission)
- [Chen et al. (2026), FedGraph: Defending Federated Large Language Model Fine-Tuning Against Backdoor Attacks via Graph-Based Aggregation](https://openreview.net/forum?id=DwwO0mfN0S) (ICLR 2026 Trustworthy AI)

### Canonical References Worth Keeping

- [Gu et al. (2017), BadNets: Identifying Vulnerabilities in the Machine Learning Model Supply Chain](https://arxiv.org/abs/1708.06733)
- [Chen et al. (2018), Detecting Backdoor Attacks on Deep Neural Networks by Activation Clustering](https://arxiv.org/abs/1811.03728)
- [Qi et al. (2021), Hidden Killer: Invisible Textual Backdoor Attacks with Syntactic Trigger](https://arxiv.org/abs/2105.12400) (ACL-IJCNLP 2021)
- [Zhao et al. (2025), A Survey of Recent Backdoor Attacks and Defenses in Large Language Models](https://openreview.net/forum?id=wZLWuFHxt5) (TMLR, January 12, 2025)
- [Zhou et al. (2025), A Survey on Backdoor Threats in Large Language Models (LLMs): Attacks, Defenses, and Evaluations](https://arxiv.org/abs/2502.05224)

## Domain Coverage

As of April 25, 2026, backdoor research is no longer confined to image classification, but the evidence base is uneven. Some domains now have strong `survey / journal / benchmark` support, while others are still best understood through a smaller number of recent primary papers.

### Survey-Backed And Better-Mapped Domains

- **Large language models and code LLMs**
  This is now one of the best-mapped parts of the field. The strongest overview anchors are [Zhao et al. (2025), A Survey of Recent Backdoor Attacks and Defenses in Large Language Models](https://openreview.net/forum?id=wZLWuFHxt5) (TMLR, January 12, 2025), [Zhou et al. (2025), A Survey on Backdoor Threats in Large Language Models (LLMs): Attacks, Defenses, and Evaluations](https://arxiv.org/abs/2502.05224), and the code-focused journal review [Qu et al. (2025), A review of backdoor attacks and defenses in code large language models](https://www.sciencedirect.com/science/article/pii/S0950584925000461) (Information and Software Technology, 2025). For benchmarking, [Li et al. (2025), BackdoorLLM](https://openreview.net/forum?id=sYLiY87mNn) is the most useful modern reference point.
- **Federated learning**
  This is the clearest non-LLM domain with mature survey coverage. The best anchors are [Li et al. (2025), Backdoor attacks and defense mechanisms in federated learning: A survey](https://www.sciencedirect.com/science/article/abs/pii/S1566253525003215) (Information Fusion, November 2025), [Nguyen et al. (2024), Backdoor attacks and defenses in federated learning: Survey, challenges and future research directions](https://www.sciencedirect.com/science/article/pii/S0952197623013507), and [Gong et al. (2023), Backdoor Attacks and Defenses in Federated Learning: State-of-the-Art, Taxonomy, and Future Directions](https://openreview.net/forum?id=HbhG88Bs5V). This is a strong sign that FL backdoors should be treated as a mature subfield rather than an edge case.
- **Face recognition**
  Backdoor work on biometric pipelines is also well enough developed to support a dedicated map. The best survey anchor here is [Roux et al. (2024), A Comprehensive Survey on Backdoor Attacks and Their Defenses in Face Recognition Systems](https://openreview.net/pdf?id=UDG64Min1E) (IEEE Access, April 4, 2024). This literature matters because it already reasons about full pipelines, physical robustness, and deployment constraints rather than only toy patch triggers.

### Emerging But Still Paper-Driven Domains

- **Object detection**
  This direction is clearly real and increasingly practical, but it is still more `paper-driven` than `survey-settled`. The cleanest backbone is [Chan et al. (2022), BadDet: Backdoor Attacks on Object Detection](https://arxiv.org/abs/2205.14497), [Ma et al. (2022), TransCAB: Transferable Clean-Annotation Backdoor to Object Detection with Natural Trigger in Real-World](https://arxiv.org/abs/2209.02339), [Zhang et al. (2025), Test-Time Backdoor Detection for Object Detection Models](https://arxiv.org/abs/2503.15293), and [Dunnett et al. (2026), BadDet+: Robust Backdoor Attacks for Object Detection](https://openreview.net/forum?id=6rz7VyAatm). This domain already has its own attack semantics, such as object disappearance, ghost objects, and regional misclassification.
- **Semantic segmentation**
  Segmentation is no longer a niche corner case. The clearest representatives are [Lan et al. (2024), Influencer Backdoor Attack on Semantic Segmentation](https://openreview.net/forum?id=VmGRoNDQgJ), [Abbasi et al. (2025), ConSeg: Contextual Backdoor Attack Against Semantic Segmentation](https://arxiv.org/abs/2507.19905), and [Zhang et al. (2026), Poisoning the Pixels: Revisiting Backdoor Attacks on Semantic Segmentation](https://arxiv.org/abs/2603.16405). A notable research shift here is that segmentation-specific attack vectors and defenses do not reduce cleanly to image-classification intuition.
- **Video and action recognition**
  Video backdoors are established, but the literature is still thinner than image or text. Good anchors are [Zhao et al. (2020), Clean-Label Backdoor Attacks on Video Recognition Models](https://arxiv.org/abs/2003.03030), [Hammoud et al. (2024), Look, Listen, and Attack: Backdoor Attacks Against Video Action Recognition](https://openreview.net/forum?id=YBSONcjwCa), and [Gong et al. (2024), Palette: Physically-Realizable Backdoor Attacks Against Video Recognition Models](https://openreview.net/forum?id=CcinTjYZno). This line matters because temporal structure and multi-modal cues create trigger pathways that static-image benchmarks miss.
- **Time series**
  Time-series backdoors are clearly present, but there is still no comparably strong survey layer. The best starting points are [Jiang et al. (2023), Backdoor Attacks on Time Series: A Generative Approach](https://openreview.net/forum?id=fuCQFswk0Y), [Huang et al. (2025), Revisiting Backdoor Attacks on Time Series Classification in the Frequency Domain](https://openreview.net/forum?id=SbEFbBhNRd), and [Wang et al. (2026), TrojanScope: Interpretable Backdoor Detection for Time Series Forecasting](https://openreview.net/forum?id=yj9cg8rBcL). This domain is important because forecasting and classification introduce trigger persistence and delayed activation issues that standard image benchmarks do not capture.
- **Health and medical AI**
  There is enough evidence to say backdoors matter in healthcare, but the field is still fragmented across subdomains. For clinical tabular and EHR settings, useful anchors are [Joe et al. (2021), Machine Learning with Electronic Health Records is vulnerable to Backdoor Trigger Attacks](https://arxiv.org/abs/2106.07925) and the journal version [Joe et al. (2022), Exploiting Missing Value Patterns for a Backdoor Attack on Machine Learning Models of Electronic Health Records: Development and Validation Study](https://medinform.jmir.org/2022/8/e38440/) (JMIR Medical Informatics, August 19, 2022). For medical foundation models, a representative signal is [Jin et al. (2024), Backdoor Attack on Unpaired Medical Image-Text Foundation Models: A Pilot Study on MedCLIP](https://arxiv.org/abs/2401.01911). The overview here is improving, but it is not yet unified the way LLM or FL backdoor research is.
- **Genomics and AI for science**
  This is the newest and least-settled part of the map. The clearest sign that the threat is no longer hypothetical is [Koilakos et al. (2026), Poisoning the Genome: Targeted Backdoor Attacks on DNA Foundation Models](https://arxiv.org/abs/2603.27465), which shows targeted poisoning risks for genomic foundation models. I would currently treat `AI for science` as an umbrella affected through concrete subdomains such as genomics and medical foundation models, rather than as a fully consolidated backdoor subfield with its own stable survey literature.

### What This Means For Reading The Field

- If you want the strongest high-level overview, start with the `LLM`, `federated learning`, and `face recognition` survey anchors above.
- If you want to understand frontier expansion, read the paper-driven domains next: `object detection`, `segmentation`, `video`, `time series`, `medical AI`, and `genomics`.
- The most important meta-pattern is that backdoor research is moving from toy classification to `structured outputs`, `distributed training`, `multimodal systems`, and `scientific or clinical pipelines`.

## Site Coverage

- [Trustworthy AI](../index.md)
  The parent topic page for safety evaluation, interpretability, hallucination, jailbreaks, oversight, and now backdoor-related work.
- [Reading Map: AI Backdoor Research Landscape](../../research-notes/reading-maps/ai-backdoor-research-landscape.md)
  A deeper field map for deciding which backdoor branches are mature, which are underexplored, and which are strongest for future paper ideas.
- [Research Notes](../../research-notes/index.md)
  The right home for future paper reviews, reading maps, and comparison notes that branch off this subtopic.

## Sources To Follow

- [BackdoorBench](https://backdoorbench.github.io/)
- [Li et al. (2025), BackdoorLLM](https://openreview.net/forum?id=sYLiY87mNn)
- [Wang et al. (2025), BackdoorVLM](https://arxiv.org/abs/2511.18921)
- [NIST TrojAI](https://www.nist.gov/itl/ssd/trojai)
- [IARPA TrojAI program](https://www.iarpa.gov/research-programs/trojai)

## Open Backlog

- A dedicated note on realistic trigger design after 2025: clean-sample triggers, harmless-input poisoning, endogenous features, and time-sensitive triggers.
- A benchmark note comparing `BackdoorBench`, `BackdoorLLM`, and `BackdoorVLM`, with an emphasis on what each does and does not measure.
- A focused note on backdoor defenses for generative LLMs: purification, attribution, self-awareness, and workflow-aware detection.
- A supply-chain note on checkpoint reuse, model merging, LoRA adapters, federated fine-tuning, and decentralized post-training.
- A note on agentic and multimodal backdoors, especially trigger propagation through planning, memory, and tool-use stages.
