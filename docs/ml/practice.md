# Machine Learning Practice

This section focuses on implementation details, best practices, and code snippets.

## SOTA Roadmap

### 1. Distributed Training
*   **Parallelism**: Data Parallel (DDP/FSDP), Tensor Parallel (TP), Pipeline Parallel (PP).
*   **Infrastructure**: DeepSpeed, Megatron-LM, DTensor (PyTorch).

### 2. High-Performance Kernels
*   **Triton**: Writing custom CUDA kernels in Python.
*   **FlashAttention**: IO-Aware exact attention.
*   **Kernel Fusion**: torch.compile (Inductor).

### 3. MLOps for LLMs (LLMOps)
*   **Evaluation**: Ragas, TruLens.
*   **serving**: vLLM, TGI, SGLang.

## Efficient Data Loading

When training large models, data loading can become a bottleneck. Here is a comparison of standard vs optimized loading patterns.

=== "Standard PyTorch"

    ```python
    import torch
    from torch.utils.data import DataLoader, Dataset

    class SimpleDataset(Dataset):
        def __init__(self, data):
            self.data = data

        def __getitem__(self, index):
            return self.data[index]

        def __len__(self):
            return len(self.data)

    # Standard loader
    loader = DataLoader(
        SimpleDataset(range(1000)), 
        batch_size=32, 
        shuffle=True
    )
    ```

=== "Optimized with Prefetch"

    ```python
    import torch
    from torch.utils.data import DataLoader

    # Optimized loader config
    loader = DataLoader(
        dataset, 
        batch_size=32, 
        shuffle=True,
        num_workers=4,           # Parallelize reading
        pin_memory=True,         # Fast transfer to CUDA
        prefetch_factor=2        # Pre-load batches
    )
    ```

## Fun with Python

Sometimes we need to remember the roots of our tools.

```python
--8<-- "docs/snippets/antigravity.py"
```

This snippet is loaded dynamically from `docs/snippets/antigravity.py`!
