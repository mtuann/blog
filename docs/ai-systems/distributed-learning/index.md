---
title: Distributed Learning
summary: Live research directions in distributed optimization, hybrid parallelism, communication efficiency, and resilient training.
status: evergreen
updated: 2026-04-24
tags:
  - distributed learning
  - distributed training
  - parallelism
---

This page is a living map of distributed-learning research for foundation models. It focuses on hybrid parallelism, communication efficiency, decentralized training, expert parallelism, and resilience; serving-specific runtime work stays under AI Systems, and kernel-level performance work stays under GPU Systems & CUDA.

## Topic Map

- **Hybrid parallelism**
  The modern question is not “data or model parallelism?” but how to compose FSDP, tensor parallelism, pipeline parallelism, context parallelism, and optimizer sharding under real workload imbalance.
- **Communication efficiency**
  This is the heart of the field whenever bandwidth, overlap, resharding, or topology starts dominating training throughput.
- **Decentralized and low-bandwidth training**
  The newer frontier is making large-model training survive imperfect networks, heterogeneous hardware, and node churn, not only pristine datacenter assumptions.
- **MoE and expert parallelism**
  Mixture-of-experts training is turning routing, token movement, and expert load balancing into central distributed-learning questions.
- **Checkpointing and resilience**
  As runs become larger and longer, the system’s ability to save, resume, and survive failure becomes part of the training algorithm’s practical envelope.

## Research Questions Right Now

- Which hybrid-parallel recipes remain robust when workload shape, sequence length, and document packing vary in the wild?
- How much communication can be hidden before numerical behavior or implementation complexity becomes the real bottleneck?
- What kinds of decentralized training are actually viable for foundation models, beyond proof-of-concept deployments?
- Which expert-parallel abstractions scale cleanly enough to become standard, rather than one-off system hacks?
- What is the right unit of comparison for distributed checkpointing: throughput, pause time, recovery time, or lost learning progress?

## Research Radar

Updated April 24, 2026.

This radar prefers 2025-2026 work. Older items stay only when they remain the clearest systems reference for a still-active distributed-training pattern.

### Active Directions

- Hybrid parallelism is shifting from fixed recipes toward workload-aware composition across FSDP, tensor parallelism, pipeline parallelism, and context parallelism.
- Communication-efficient training on imperfect or low-bandwidth networks is moving from toy decentralization to realistic large-model training.
- MoE scaling is making expert parallelism, communication overlap, and routing-aware load balancing central research problems.
- Distributed checkpointing and recovery are becoming first-class design problems as runs stretch across more accelerators and longer wall-clock windows.
- Native distributed APIs such as PyTorch DTensor/FSDP2 and Megatron-Core are increasingly acting as the substrate on which new research ideas are deployed.

### Keywords To Track

`FSDP2`, `DTensor`, `context parallelism`, `expert parallelism`, `resharding`, `distributed optimizer`, `decentralized training`, `low-bandwidth training`, `overlapped checkpointing`, `elastic training`

### Recent Papers And Research Signals By Direction

#### Hybrid Parallelism And Load Balancing

- [WLB-LLM: Workload-Balanced 4D Parallelism for Large Language Model Training](https://arxiv.org/abs/2503.17924) (2025)
- [ByteScale: Efficient Scaling of LLM Training with a 2048K Context Length on More Than 12,000 GPUs](https://arxiv.org/abs/2502.21231) (2025)
- [Data-Centric Elastic Pipeline Parallelism for Efficient Long-Context LLM Training](https://arxiv.org/abs/2509.21275) (2025)
- [Speeding Up Variable-Length Training with Dynamic Context Parallelism and NVIDIA Megatron Core](https://developer.nvidia.com/blog/speeding-up-variable-length-training-with-dynamic-context-parallelism-and-nvidia-megatron-core/) (NVIDIA, February 27, 2026)

#### Communication-Efficient And Decentralized Training

- [DiLoCoX: A Low-Communication Large-Scale Training Framework for Decentralized Cluster](https://arxiv.org/abs/2506.21263) (2025)
- [Go With The Flow: Churn-Tolerant Decentralized Training of Large Language Models](https://arxiv.org/abs/2509.21221) (2025)
- [On Optimizing the Communication of Model Parallelism](https://arxiv.org/abs/2211.05322) (2024, kept as a strong reference for cross-mesh resharding)

#### MoE Expert Parallelism

- [UniEP: Unified Expert-Parallel MoE MegaKernel for LLM Training](https://arxiv.org/abs/2604.19241) (2026)
- [Dynamic Expert Sharing: Decoupling Memory from Parallelism in Mixture-of-Experts Diffusion LLMs](https://arxiv.org/abs/2602.00879) (2026)

#### Checkpointing, Recovery, And Resilience

- [DataStates-LLM: Scalable Checkpointing for Transformer Models Using Composable State Providers](https://arxiv.org/abs/2601.16956) (2026)
- [GoCkpt: Gradient-Assisted Multi-Step overlapped Checkpointing for Efficient LLM Training](https://arxiv.org/abs/2511.07035) (2025)

### Related Notes

- [Distributed Training Playbook](../distributed-training-playbook.md)
- [AI Systems](../index.md)

## Site Coverage

- [Distributed Training Playbook](../distributed-training-playbook.md)
  The current internal anchor for the main families of parallelism and how they are used in practice.
- [AI Systems](../index.md)
  The parent overview for serving/runtime questions that sit next to distributed-learning concerns but should not be merged with them.

## Sources To Follow

- [PyTorch Distributed Overview](https://docs.pytorch.org/tutorials/beginner/dist_overview.html)
- [PyTorch FSDP2 Tutorial](https://docs.pytorch.org/tutorials/intermediate/FSDP_tutorial.html)
- [PyTorch Tensor Parallel Docs](https://docs.pytorch.org/docs/stable/distributed.tensor.parallel)
- [Megatron Core Developer Guide](https://docs.nvidia.com/megatron-core/index.html)
- [NCCL Getting Started](https://developer.nvidia.com/nccl/getting_started)
- [DeepSpeed ZeRO Docs](https://deepspeed.readthedocs.io/en/stable/zero3.html)

## Open Backlog

- A deeper note on hybrid parallelism design patterns after 2025: FSDP2, TP, PP, CP, and optimizer sharding in one mental model.
- A dedicated page on communication bottlenecks: overlap, resharding, topology, and when low-bandwidth training is realistic.
- A focused note on expert parallelism and MoE communication as a distributed-learning problem in its own right.
- A research note on distributed checkpointing, failure recovery, and what “resilient training” should actually measure.
- A future comparison page mapping PyTorch native distributed APIs, Megatron Core, and DeepSpeed to the research questions they make easiest to study.
