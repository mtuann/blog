---
title: Distributed Training Playbook
date: 2026-04-24
updated: 2026-04-24
tags:
  - ai systems
  - distributed training
  - fsdp
  - megatron
status: evergreen
series: ai-systems
summary: A practical mental model for choosing between data parallelism, ZeRO or FSDP, tensor parallelism, and pipeline parallelism.
---

# Distributed Training Playbook

Most distributed-training confusion comes from treating every parallelism strategy as interchangeable. They are not. Each technique solves a different bottleneck, and the cleanest training stacks start by identifying what is actually breaking first: model-state memory, activation memory, layer size, or total training time.

This page is a practical map for that decision.

## The First Question

Before picking a framework, ask:

**Why does the model not fit or not scale well?**

That answer usually falls into one of four buckets:

- the whole model fits, but throughput is too low
- model states do not fit comfortably on each GPU
- individual layers are too large for a single device
- pipeline depth or end-to-end throughput needs larger-scale orchestration

Different strategies attack different buckets.

## The Main Strategies

| Strategy | What it replicates or shards | Best first use | Main tax |
| --- | --- | --- | --- |
| Data Parallel / DDP | Replicates full model on each rank | Model fits per GPU and you want simple scale-out | Replicated model state |
| ZeRO / FSDP | Shards optimizer state, gradients, and often parameters | Model-state memory is the main problem | More collective communication |
| Tensor Parallelism | Splits tensors inside layers | Layers are too wide for one device | Tight intra-layer communication |
| Pipeline Parallelism | Splits layers across stages | Model depth or memory needs stage-wise partitioning | Pipeline bubbles and scheduling complexity |

## Data Parallelism

Standard data parallelism is the cleanest place to start. Every worker keeps a full copy of the model, processes a different batch shard, and synchronizes gradients.

Use it when:

- the model fits on a single GPU
- you want the simplest debugging path
- communication overhead is still manageable

Its weakness is obvious: as model size grows, every rank still pays the full model-state cost.

## ZeRO And FSDP

When memory pressure comes mostly from model states rather than the size of one individual layer, sharding is the right tool.

[ZeRO](https://arxiv.org/abs/1910.02054) is the canonical reference for this idea. The core progression is:

- shard optimizer states
- shard gradients
- shard parameters

PyTorch [FSDP](https://docs.pytorch.org/docs/stable/fsdp.html) is the practical expression of the same philosophy in many training stacks.

Use ZeRO or FSDP when:

- the model mostly fits conceptually, but replicated states waste too much memory
- you want to keep a largely familiar programming model
- the interconnect is good enough to tolerate all-gather and reduce-scatter overhead

## Tensor Parallelism

Tensor parallelism splits individual layers across devices. This is the right move when a single layer is too large or too compute-heavy for one device, especially in large dense transformer blocks.

The practical reference here is [Efficient Large-Scale Language Model Training on GPU Clusters Using Megatron-LM](https://arxiv.org/abs/2104.04473).

Use tensor parallelism when:

- matrix multiplications are too large for one accelerator
- the devices have fast links such as NVLink or NVSwitch
- you can tolerate fine-grained communication inside the layer

Its biggest cost is communication frequency. Tensor parallelism is rarely the first tool you reach for across weak interconnects.

## Pipeline Parallelism

Pipeline parallelism divides the model across stages and runs microbatches through them. It is often the right move when the model is too deep or too large to place on one device group cleanly.

Use it when:

- layer groups naturally partition into stages
- you need more memory headroom than sharding alone gives you
- you can manage bubble overhead with scheduling and microbatch tuning

The failure mode is complexity. Pipeline schedules, microbatch counts, activation rematerialization, and checkpoint boundaries all start interacting.

## A Practical Decision Sequence

If I were choosing from scratch, I would use this order:

1. Start with DDP if the model fits.
2. Add ZeRO or FSDP when replicated model states become the dominant memory problem.
3. Add tensor parallelism when individual layers no longer fit well or intra-layer compute is too large.
4. Add pipeline parallelism when model partitioning across stages becomes the cleaner scaling path.
5. Compose strategies only when the bottlenecks clearly demand it.

This avoids the common mistake of introducing a full 3D-parallel stack before the team understands which constraint is actually binding.

## What Changes At Large Scale

At very large model sizes, the problem becomes a composition problem:

- data parallelism for throughput
- ZeRO or FSDP for model-state memory
- tensor parallelism for large layers
- pipeline parallelism for stage-wise partitioning

That is why Megatron-style systems feel complicated. They are not a single trick; they are a negotiated compromise between memory, compute, and communication.

## Stable Lessons

- Simplicity is a performance feature because it reduces debugging time and operational risk.
- Sharding helps most when model-state memory dominates.
- Tensor parallelism is powerful but unforgiving on slow interconnects.
- Pipeline parallelism solves real problems, but only if the schedule is tuned carefully.

## Related Notes

- [AI Systems Overview](index.md)
- [GPU Systems & CUDA](../cuda/index.md)
- [Prefill, Decode, and Goodput](prefill-decode-goodput.md)
- [Reading Map: Efficient LLM Inference](../research-notes/reading-maps/efficient-llm-inference.md)
