# Efficient AI

Techniques to train and serve massive models on constrained resources.

## SOTA Roadmap

### 1. Quantization & Compression
*   **Weight-Only**: GPTQ, AWQ (Activation-aware Weight Quantization), ExLlamaV2.
*   **LoRA & Derivatives**: QLoRA (4-bit), DoRA (Weight-Decomposed), LongLoRA.
*   **Extreme Quantization**: 1.58-bit LLMs (BitNet b1.58), QuIP#.

### 2. Efficient Architectures (Beyond Transformer)
*   **State Space Models (SSM)**: Mamba, S4, H3.
*   **Linear Attention**: RWKV, RetNet (Retentive Networks).
*   **Hybrid Models**: Jamba (Mamba + Transformer + MoE).

### 3. Inference Optimization
*   **Memory Management**: PagedAttention (vLLM), RadixAttention (SGLang).
*   **Decoding Strategies**: Speculative Decoding (Medusa, Lookahead), KV Cache Compression.
*   **Frameworks**: TensorRT-LLM, MLX (Apple Silicon), TGI (HuggingFace).

### 4. Sparsity & Pruning
*   **Structured Sparsity**: 2:4 Sparsity (NVIDIA Ampere).
*   **One-Shot Pruning**: SparseGPT, Wanda (Pruning by Weight and Activation).
