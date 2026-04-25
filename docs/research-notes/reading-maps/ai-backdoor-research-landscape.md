---
title: Reading Map - AI Backdoor Research Landscape
date: 2026-04-25
updated: 2026-04-25
tags:
  - reading map
  - trustworthy ai
  - backdoor attacks
  - research strategy
status: evergreen
series: reading-maps
summary: A field map of AI backdoor research across domains, model classes, threat surfaces, benchmarks, and the strongest paper opportunities as of April 2026.
---

# Reading Map: AI Backdoor Research Landscape

This note answers one practical question: **if you want to work on backdoor research in 2026, where is the field mature, where is it still opening up, and which directions are most likely to produce a strong paper rather than a small variant?**

The useful mental model is that `backdoor research` is no longer one field. It is now a family of subfields split by model class, deployment surface, output structure, and benchmark maturity. A paper that is interesting in CIFAR-style classification may be uninteresting in LLMs, and a clever attack in LLMs may still be weak if it ignores the real supply chain through adapters, merging, or agents.

## How To Read This Map

Use five axes to judge whether a backdoor direction is still worth entering:

- **Model class**: classifiers, language models, vision-language models, diffusion models, speech models, graph models, or RL agents.
- **Output structure**: single-label classification is much more saturated than structured outputs such as detection, segmentation, generation, planning, or tool-use.
- **Attack surface**: poisoned data, fine-tuning, PEFT adapters, model merging, decentralized training, architectural tampering, and simulator or workflow compromise are not equally mature.
- **Benchmark maturity**: fields with standardized suites are easier to compare but often more crowded.
- **Deployment realism**: the best recent papers usually explain why the threat survives actual user workflows, not just toy threat models.

In 2026, a strong backdoor paper usually does at least one of these:

- Opens a new and realistic attack surface.
- Standardizes a fragmented benchmark space.
- Shows a mechanistic or systems reason older defenses fail.
- Introduces a defense that survives adaptive evaluation on modern models.

Weak papers usually do the opposite:

- Slightly improve attack success rate on image classification.
- Assume unrealistic attacker power.
- Ignore structured outputs, generation, or workflow state.
- Evaluate only against weak or outdated defenses.

## Stage 0: Learn The Canonical Core

Before branching into frontier work, read the original threat model and the classic benchmark layer:

- [BadNets: Identifying Vulnerabilities in the Machine Learning Model Supply Chain](https://arxiv.org/abs/1708.06733)
- [Detecting Backdoor Attacks on Deep Neural Networks by Activation Clustering](https://arxiv.org/abs/1811.03728)
- [Backdoor Learning: A Survey](https://arxiv.org/abs/2007.08745)
- [BackdoorBench: A Comprehensive Benchmark of Backdoor Learning](https://openreview.net/forum?id=31_U7n18gM7)
- [A Unified Evaluation of Textual Backdoor Learning: Frameworks and Benchmarks](https://openreview.net/forum?id=k3462dQtQhg)

What to focus on:

- Why the basic attack objective is `high ASR + high clean accuracy + stealth`.
- Why image classification and text classification dominated early evaluation.
- Why many old defenses assume reusable, explicit triggers and therefore break down on newer attacks.

## Stage 1: Know Which Branches Are Already Mature

Some backdoor branches already have enough surveys and benchmarks that a plain attack variant is likely to look incremental.

### LLMs And Code LLMs

- [A Survey of Recent Backdoor Attacks and Defenses in Large Language Models](https://openreview.net/forum?id=wZLWuFHxt5)
- [A Survey on Backdoor Threats in Large Language Models (LLMs): Attacks, Defenses, and Evaluations](https://arxiv.org/abs/2502.05224)
- [A review of backdoor attacks and defenses in code large language models](https://www.sciencedirect.com/science/article/pii/S0950584925000461)
- [BackdoorLLM: A Comprehensive Benchmark for Backdoor Attacks and Defenses on Large Language Models](https://openreview.net/forum?id=sYLiY87mNn)

What to focus on:

- The shift from text classification to open-ended generation.
- Why `harmless-input`, `triggerless`, and reasoning-level attacks matter more than simple token triggers.
- Why benchmark work is now as important as attack design.

### Federated Learning

- [Backdoor attacks and defense mechanisms in federated learning: A survey](https://www.sciencedirect.com/science/article/abs/pii/S1566253525003215)
- [Backdoor attacks and defenses in federated learning: Survey, challenges and future research directions](https://www.sciencedirect.com/science/article/pii/S0952197623013507)
- [Backdoor Attacks and Defenses in Federated Learning: State-of-the-Art, Taxonomy, and Future Directions](https://openreview.net/forum?id=HbhG88Bs5V)
- [BackFed: A Standardized and Efficient Benchmark Framework for Backdoor Attacks in Federated Learning](https://openreview.net/forum?id=0hHnZeXr9k)

What to focus on:

- Why malicious-client assumptions and training-time budgets matter.
- Why many older FL results look weaker once standardized evaluation is enforced.
- Why FL is now a benchmark-rich branch, which raises the bar for novelty.

### Face Recognition And Biometrics

- [A Comprehensive Survey on Backdoor Attacks and Their Defenses in Face Recognition Systems](https://openreview.net/pdf?id=UDG64Min1E)

What to focus on:

- How full biometric pipelines change the threat model.
- Why physical robustness and pre-processing stages matter.
- Why this line is more deployment-aware than many generic CV papers.

### Graph Neural Networks

- [Graph Neural Backdoor: Fundamentals, Methodologies, Applications, and Future Directions](https://arxiv.org/abs/2406.10573)

What to focus on:

- How graph triggers differ from patch-style triggers.
- Why graph-specific structure makes transfer from image intuition unreliable.

## Stage 2: Study The Foundation-Model Supply Chain

This is one of the most important shifts in the field. The compromised object is often no longer a dataset alone. It can be an adapter, a merged model, a pipeline stage, a pre-trained encoder, or even architecture-level logic.

- [Merge Hijacking: Backdoor Attacks to Model Merging of Large Language Models](https://arxiv.org/abs/2505.23561)
- [LoBAM: LoRA-Based Backdoor Attack on Model Merging](https://openreview.net/forum?id=NHOEz72fip)
- [Mitigating the Backdoor Effect for Multi-Task Model Merging via Safety-Aware Subspace](https://openreview.net/forum?id=dqMqAaw7Sq)
- [Backdoor Attacks on Decentralised Post-Training](https://openreview.net/forum?id=FveQNDaHnZ)
- [Architectural Backdoors in Deep Learning: A Survey of Vulnerabilities, Detection, and Defense](https://arxiv.org/abs/2507.12919)

What to focus on:

- The unit of compromise is changing from `sample` to `artifact`.
- Security questions are moving into `PEFT`, `merging`, `shared checkpoints`, and `training infrastructure`.
- Supply-chain realism is now a strong paper value signal.

## Stage 3: Move Into Multimodal, Generative, And Agentic Backdoors

This part of the field is newer, more fragmented, and often more publishable than classic branches.

### Vision-Language, Speech, And Multimodal Models

- [BackdoorVLM: A Benchmark for Backdoor Attacks on Vision-Language Models](https://arxiv.org/abs/2511.18921)
- [BackdoorMBTI: A Backdoor Learning Multimodal Benchmark Tool Kit for Backdoor Defense Evaluation](https://arxiv.org/abs/2411.11006)
- [Backdoor Attacks Against Speech Language Models](https://openreview.net/forum?id=HcytH0HSaG)

What to focus on:

- Which modality dominates trigger activation.
- Whether text overrides image or audio cues.
- Why multimodal benchmarks are still immature compared with LLM-only evaluation.

### Diffusion And Generative Data Pipelines

- [How to Backdoor Diffusion Models?](https://openreview.net/forum?id=iIg0_loMVm)
- [DisDet: Exploring Detectability of Backdoor Attack on Diffusion Models](https://openreview.net/forum?id=SfqCaAOF1S)
- [UFID: A Unified Framework for Black-box Input-level Backdoor Detection on Diffusion Models](https://openreview.net/forum?id=lZLvwHYSFA)
- [Data-Chain Backdoor: Do You Trust Diffusion Models as Generative Data Supplier?](https://arxiv.org/abs/2512.15769)
- [When One Modality Rules Them All: Backdoor Modality Collapse in Multimodal Diffusion Models](https://openreview.net/forum?id=he9MIuoaup)

What to focus on:

- Diffusion models are both models and data suppliers.
- Synthetic-data supply chains create a new propagation story that older backdoor literature barely touched.
- Detection and unlearning on diffusion systems still look under-standardized.

### Agentic Workflows

- [BackdoorAgent: A Unified Framework for Backdoor Attacks on LLM-based Agents](https://arxiv.org/abs/2601.04566)
- [Watch Out for Your Agents! Investigating Backdoor Threats to LLM-Based Agents](https://openreview.net/forum?id=Nf4MHF1pi5)

What to focus on:

- Triggers can live in planning, memory, or tool use rather than only user prompts.
- Persistence across intermediate states is the key new phenomenon.
- Agent benchmarks are still young, which means there is room for strong measurement papers.

## Stage 4: Explore Structured Outputs And Domain-Specific AI

This is where many of the best `less crowded but still important` opportunities live.

### Structured Computer Vision

- [BadDet: Backdoor Attacks on Object Detection](https://arxiv.org/abs/2205.14497)
- [TransCAB: Transferable Clean-Annotation Backdoor to Object Detection with Natural Trigger in Real-World](https://arxiv.org/abs/2209.02339)
- [BadDet+: Robust Backdoor Attacks for Object Detection](https://openreview.net/forum?id=6rz7VyAatm)
- [Influencer Backdoor Attack on Semantic Segmentation](https://openreview.net/forum?id=VmGRoNDQgJ)
- [ConSeg: Contextual Backdoor Attack Against Semantic Segmentation](https://arxiv.org/abs/2507.19905)
- [Poisoning the Pixels: Revisiting Backdoor Attacks on Semantic Segmentation](https://arxiv.org/abs/2603.16405)
- [Clean-Label Backdoor Attacks on Video Recognition Models](https://arxiv.org/abs/2003.03030)
- [Look, Listen, and Attack: Backdoor Attacks Against Video Action Recognition](https://openreview.net/forum?id=YBSONcjwCa)
- [Palette: Physically-Realizable Backdoor Attacks Against Video Recognition Models](https://openreview.net/forum?id=CcinTjYZno)

What to focus on:

- Structured outputs create attack semantics that do not exist in classification.
- `Object disappearance`, `ghost object generation`, and `contextual mis-segmentation` are not small variants of image backdoors.
- These branches still lack a unified benchmark layer comparable to BackdoorBench.

### Medical, Scientific, And Genomic Models

- [Machine Learning with Electronic Health Records is vulnerable to Backdoor Trigger Attacks](https://arxiv.org/abs/2106.07925)
- [Exploiting Missing Value Patterns for a Backdoor Attack on Machine Learning Models of Electronic Health Records: Development and Validation Study](https://medinform.jmir.org/2022/8/e38440/)
- [Backdoor Attack on Unpaired Medical Image-Text Foundation Models: A Pilot Study on MedCLIP](https://arxiv.org/abs/2401.01911)
- [Poisoning the Genome: Targeted Backdoor Attacks on DNA Foundation Models](https://arxiv.org/abs/2603.27465)

What to focus on:

- Scientific and medical settings are high-stakes but still benchmark-poor.
- Data provenance and weak supervision make the supply chain unusually fragile.
- This is one of the least saturated branches of modern backdoor research.

### AI for Science Coverage

This publisher sweep is important because `AI for science backdoors` still does **not** look like one consolidated subfield as of **April 25, 2026**. What exists is concentrated in a few biomedical pockets, while large parts of scientific foundation modeling remain almost untouched.

#### What The Publisher Sweep Clearly Finds

- **Nature family**
  The clearest direct hit is [Unveiling potential threats: backdoor attacks in single-cell pre-trained models](https://www.nature.com/articles/s41421-024-00753-1), published in **Cell Discovery on November 30, 2024**. This is the strongest `AI-for-science` backdoor paper in the sweep: it attacks `scGPT`, `GeneFormer`, and `scBERT`, and explicitly frames backdoors as a threat to downstream biomedical analysis, drug discovery, and clinical interpretation.
- **IEEE**
  The strongest direct hit is [Backdoor Attack on Unpaired Medical Image-Text Foundation Models: A Pilot Study on MedCLIP](https://ieeexplore.ieee.org/document/10516621), also available as [OpenReview](https://openreview.net/forum?id=YymNvIkmKR) and [arXiv](https://arxiv.org/abs/2401.01911). This is best viewed as a `medical multimodal foundation-model supply-chain` paper rather than a generic VLM paper.
- **Elsevier / ScienceDirect**
  The most relevant direct journal hit is [Backdoor attack and defense in federated generative adversarial network-based medical image synthesis](https://www.sciencedirect.com/science/article/pii/S1361841523002256), which appears in **Medical Image Analysis (2024)** and studies backdoors in `federated medical image synthesis`. Elsevier also has several graph-backdoor papers such as [Crucial rather than random: Attacking crucial substructure for backdoor attacks on graph neural networks](https://www.sciencedirect.com/science/article/pii/S0952197624011242) and [Backdoor attacks on unsupervised graph representation learning](https://www.sciencedirect.com/science/article/pii/S0893608024005926). These are scientifically relevant because they touch `molecule classification`, `drug discovery`, or `protein-network` style applications, but most of them are still really `graph-security papers with science-flavored tasks`, not papers centered on scientific foundation models.
- **Springer**
  Springer returns graph-backdoor work such as [Stealthy graph backdoor attack based on feature trigger](https://link.springer.com/article/10.1007/s40747-025-01934-5) and [A graph backdoor detection method for data collection scenarios](https://link.springer.com/article/10.1186/s42400-024-00305-w). Again, these are relevant to scientific data through graph tasks and molecule datasets, but the literature is still not specifically organized around `AI-for-science backdoors`.
- **Domain journals**
  The most direct domain-journal hit is [Exploiting Missing Value Patterns for a Backdoor Attack on Machine Learning Models of Electronic Health Records](https://medinform.jmir.org/2022/8/e38440/), published in **JMIR Medical Informatics on August 19, 2022**. This gives the clinical-tabular branch a real domain-specific anchor instead of only ML-security venue coverage.

#### What Looks Only Partially Covered

- `Drug discovery` and `molecular property prediction` currently appear mostly through `graph neural network` backdoor papers rather than through scientific foundation-model papers.
- `Medical multimodal foundation models` have at least one strong direct paper through `MedCLIP`, but the space is still far from saturated.
- `Scientific data synthesis` is beginning to appear through federated or generative medical imaging work, but benchmark standardization is still weak.

#### What Still Looks Largely Open

- `Protein language / protein structure foundation models`
- `RNA foundation models`
- `Drug-target interaction foundation models`
- `Protein-ligand or molecular generative foundation models`
- `Materials-science foundation models`
- `Physics, climate, or simulator-based scientific foundation models`

The practical meaning is that `AI for science backdoor research` is strongest today in:

- `single-cell foundation models`
- `medical image-text foundation models`
- `clinical / EHR models`
- `medical image synthesis under federated settings`

Everything beyond that still looks unusually open for new work.

#### Why This Matters For Paper Strategy

- If you want the safest path with direct prior art, work in `single-cell` or `medical multimodal foundation models`.
- If you want the highest novelty, move into `protein`, `RNA`, `DTI`, `molecular generation`, or broader `scientific foundation-model supply chains`.
- If you want the most balanced strategy, a strong paper would likely combine one real scientific domain with one underdeveloped evaluation layer such as provenance checks, benchmark construction, or artifact-level supply-chain attacks.

### Reinforcement Learning

- [BACKDOORL: Backdoor Attack against Competitive Reinforcement Learning](https://arxiv.org/abs/2105.00579)
- [Beware Untrusted Simulators -- Reward-Free Backdoor Attacks in Reinforcement Learning](https://openreview.net/forum?id=Z3SH1xlFs6)

What to focus on:

- The simulator itself can become the compromised artifact.
- Backdoor activation in RL changes policies and trajectories, not just labels or text outputs.
- RL backdoor research is still thin enough that new benchmark or threat-model papers can stand out quickly.

## Stage 5: Learn The Benchmark Layer Before Picking A Topic

The easiest way to waste time in this field is to choose a topic with no realistic evaluation plan. The benchmark layer is one of the best predictors of paper quality.

### Strong Benchmark Support

- [BackdoorBench](https://openreview.net/forum?id=31_U7n18gM7)
- [OpenBackdoor / Unified textual evaluation](https://openreview.net/forum?id=k3462dQtQhg)
- [BackdoorLLM](https://openreview.net/forum?id=sYLiY87mNn)
- [BackFed](https://openreview.net/forum?id=0hHnZeXr9k)

These areas are easier to evaluate well, but harder to impress reviewers with small attack improvements.

### Medium Benchmark Support

- [BackdoorVLM](https://arxiv.org/abs/2511.18921)
- [BackdoorMBTI](https://arxiv.org/abs/2411.11006)
- diffusion benchmarks and detection suites such as [DisDet](https://openreview.net/forum?id=SfqCaAOF1S)

These are good places to work if you can improve realism or standardization.

### Weak Benchmark Support

- agents
- scientific and medical foundation models
- genomics
- structured-output CV tasks
- architectural backdoors
- RL backdoors

These are high-upside areas, but the paper often has to build part of the evaluation stack itself.

## Best Paper Opportunities As Of April 25, 2026

If the goal is to write a paper efficiently, I would rank the landscape like this.

### Tier 1: Best Bets

- **Agent and workflow backdoors**
  The attack surface is genuinely new, benchmark maturity is low, and there is strong practical relevance. Good papers here can combine threat modeling, instrumentation, and long-horizon evaluation.
- **Supply-chain backdoors for PEFT, model merging, and decentralized post-training**
  This line fits how people actually use open models. It has strong systems relevance and clear artifact-level threat models.
- **Medical, scientific, and genomic foundation-model backdoors**
  High stakes plus low saturation is a strong combination. This is especially attractive if you can define provenance-aware or domain-aware evaluation.
- **Structured-output backdoors in detection, segmentation, and video**
  These tasks have real novelty because the attack semantics are task-specific, yet the field is still fragmented.
- **Diffusion and synthetic-data supply-chain backdoors**
  This line is timely because generative models are increasingly used to create training data for downstream systems.

### Tier 2: Good But More Crowded Or Harder To Differentiate

- **Generic LLM backdoor attacks**
  Still relevant, but a plain new trigger family is unlikely to be enough unless you bring a new benchmark, workflow, or mechanistic story.
- **Federated learning attack variants**
  Useful, but strong survey and benchmark coverage means novelty needs to be clearer than before.
- **Graph backdoors**
  Promising, but often needs a compelling application domain beyond another graph trigger construction.

### Tier 3: Low-Leverage Directions

- Another CIFAR or GTSRB patch-trigger paper with slightly higher ASR.
- A defense that only handles fixed explicit triggers.
- A paper that never tests adaptive attackers or realistic poisoning budgets.
- A threat model that assumes total attacker control without deployment justification.

## If I Had To Choose Three Concrete Paper Directions

### 1. A Unified Benchmark For Agent Backdoors

What to build:

- One benchmark spanning `planning`, `memory`, `tool-use`, and `retrieval/tool artifacts`.
- Persistence metrics, not just final-output ASR.
- Evaluation on coding, browsing, and research agents.

Why this is strong:

- The threat is new.
- The benchmark layer is weak.
- The contribution can be valuable even if the defense story is not solved yet.

### 2. A Supply-Chain Benchmark For PEFT And Model-Merging Backdoors

What to build:

- One benchmark that unifies `LoRA adapters`, `merged models`, `shared checkpoints`, and `decentralized post-training`.
- Realistic attacker-cost constraints and deployment scenarios.
- Strong baselines from [Merge Hijacking](https://arxiv.org/abs/2505.23561), [LoBAM](https://openreview.net/forum?id=NHOEz72fip), and [Backdoor Attacks on Decentralised Post-Training](https://openreview.net/forum?id=FveQNDaHnZ).

Why this is strong:

- This is how open-source model ecosystems actually work.
- Reviewers can immediately see the practical importance.
- The field still lacks a shared evaluation language.

### 3. A Domain-Aware Backdoor Benchmark For Scientific Foundation Models

What to build:

- One evaluation stack covering `medical image-text`, `genomics`, and optionally `molecular or graph scientific models`.
- Provenance-aware triggers and weak-label supply-chain attacks.
- Defenses tied to data integrity, not just generic pruning or filtering.

Why this is strong:

- The branch is high stakes and unsaturated.
- Domain-specific assumptions are not well encoded in current backdoor benchmarks.
- Even a careful measurement paper could be meaningful here.

## What I Would Avoid Unless There Is A Very Sharp Twist

- A new explicit trigger pattern for plain image classification.
- Another LLM attack paper that only changes the trigger string or prompt template.
- A defense paper that ignores merged models, adapters, agents, or structured outputs.
- Any result that cannot explain why current standardized benchmarks are insufficient.

## Open Questions

- Can we build trigger-agnostic defenses that still work for agents, multimodal systems, and structured outputs?
- Which artifact is now the dominant real-world risk: poisoned data, adapters, merged models, decentralized training pipelines, or architecture-level compromise?
- How should benchmark design capture persistence, propagation, and delayed activation rather than only single-step ASR?
- Can provenance, attestation, or model-signing ideas become practical defenses against supply-chain backdoors?

## Related Notes

- [Backdoor Attacks](../../trustworthy-ai/backdoor-attacks/index.md)
- [Trustworthy AI](../../trustworthy-ai/index.md)
- [Federated Learning](../../ai-systems/distributed-learning/federated-learning.md)
