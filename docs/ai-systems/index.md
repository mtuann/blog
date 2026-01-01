# AI Systems (SysML)

Bridging the gap between cutting-edge algorithms and massive-scale hardware.

## SOTA Roadmap

### 1. Scaling Infrastructure
*   **Cluster Orchestration**: Kubernetes for ML (KubeFlow, Ray on K8s), Slurm.
*   **Interconnects**: InfiniBand vs Ethernet (RoCEv2), NVLink/NVSwitch topology.
*   **Storage**: High-performance implementations (Lustre, GPUDirect Storage).

### 2. Distributed Training Frameworks
*   **3D Parallelism**: Creating the optimal recipe of Data, Tensor, and Pipeline parallelism (Megatron-LM).
*   **Optimization**: ZeRO Stages (DeepSpeed), FSDP (Fully Sharded Data Parallel).
*   **Fault Tolerance**: Checkpointing strategies, auto-recovery design.

### 3. Inference at Scale
*   **Serving Engines**: Deeper dive into TGI vs vLLM vs TRT-LLM architectures.
*   **Continuous Batching**: Orca scheduling.
*   **Prefill vs/and Decode separation**: Distaggregating prefill and decode compute (Splitwise).

### 4. Data Engineering for AI
*   **Dataloaders**: Ray Data, MosaicML Streaming.
*   **Formats**: Parquet, Arrow, LanceDB.

## Key Resources
*   **Course**: [CS329S: Machine Learning Systems Design](https://stanford-cs329s.github.io/) (Stanford/Chip Huyen).
*   **Blog**: [Chip Huyen's Blog](https://huyenchip.com/) (Real-world MLSys).
*   **Paper**: [Efficient Large-Scale Language Model Training on GPU Clusters](https://arxiv.org/abs/2104.04473) (Megatron-LM).
