---
title: Prefill, Decode, and Goodput
date: 2026-04-24
updated: 2026-04-24
tags:
  - ai systems
  - inference
  - serving
  - kv cache
status: evergreen
series: ai-systems
summary: A systems note on why LLM serving behaves like two workloads glued together, and why goodput matters more than raw throughput.
---

# Prefill, Decode, and Goodput

LLM serving is awkward because it is not one workload. It is two different workloads stitched together:

- **prefill**: process the prompt and build the initial KV cache
- **decode**: generate tokens autoregressively, one step at a time

If you optimize serving as if these two phases have the same bottleneck, you usually end up disappointed.

## The Two Phases

### Prefill

Prefill ingests the prompt. It has plenty of parallel work across prompt tokens, especially for long inputs. In practice, prefill often behaves more like a throughput-heavy bulk computation phase.

### Decode

Decode is sequential. Each new token depends on the previous one, so the system repeatedly touches model weights and KV cache for very small amounts of fresh computation. This is where memory movement and cache management become painful.

That is why a single request often feels like:

$$
\text{Total latency} \approx \text{prefill latency} + T \cdot \text{decode step latency},
$$

where $T$ is the number of generated tokens.

## Metrics That Actually Matter

Two metrics are especially useful:

- **Time to first token (TTFT)**, which is heavily influenced by prefill
- **Time per output token (TPOT)**, which is heavily influenced by decode

The product question is not just "How many tokens per second can I print?" It is:

**How many user requests can I serve while still meeting acceptable TTFT and TPOT?**

That is where **goodput** becomes a better framing than raw throughput.

## Why KV Cache Changes Everything

The KV cache turns serving into a memory-management problem. It grows with sequence length, stays resident during generation, and competes with batching for scarce accelerator memory.

This is why [PagedAttention](https://arxiv.org/abs/2309.06180) mattered so much. It reframed KV-cache handling with a memory-management abstraction that reduced fragmentation and improved batch utilization.

Once you internalize that idea, a lot of later serving work makes more sense.

## Why Prefill And Decode Want Different Systems

The next key insight is that colocating prefill and decode can create interference. Long prompts and ongoing decoding compete for resources in ways that are bad for user-facing latency.

That is the motivation behind systems such as:

- [DistServe](https://arxiv.org/abs/2401.09670), which separates prefill and decode for better goodput
- [Mooncake](https://arxiv.org/abs/2407.00079), which treats KV cache as a first-class architectural concern

The important lesson is not that disaggregation is always best. It is that phase-aware serving is now a serious design axis.

## Continuous Batching

Continuous batching is one of the most important serving ideas because decode requests arrive and finish at different times. Static batches waste too much opportunity.

Continuous batching helps because it:

- keeps decode hardware busier
- reduces idle gaps between requests
- turns irregular arrival patterns into something schedulable

But it only works well if memory management and cache layout cooperate with the scheduler.

## A Useful Mental Model

If I had to compress modern LLM serving into one sentence, it would be:

**You are scheduling memory-bound sequential work on top of compute-heavy prompt processing while trying not to break latency SLOs.**

That is why serving systems now spend so much energy on:

- cache placement
- request scheduling
- batching policy
- prefill and decode separation
- compression and quantization that actually help end-to-end goodput

## Stable Lessons

- TTFT and TPOT should be measured separately.
- Raw throughput is not enough; SLO-aware goodput is a better systems target.
- KV cache is not just a model artifact, it is an architectural resource.
- Prefill and decode often deserve different resource strategies.

## Related Notes

- [AI Systems Overview](index.md)
- [Distributed Training Playbook](distributed-training-playbook.md)
- [April 2026 Roundup: KV Cache Optimization Becomes A Systems Problem](../research-notes/roundups/2026-04-kv-cache-optimization.md)
- [Reading Map: Efficient LLM Inference](../research-notes/reading-maps/efficient-llm-inference.md)
