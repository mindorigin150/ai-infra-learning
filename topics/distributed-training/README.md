---
title: 通信与分布式训练
---

# 通信与分布式训练

多个设备怎样交换张量、划分模型与训练状态，并保持一次更新的语义？

[主题索引](../README.md) · [开始一次学习](../../paths/start-here.md)

## 分类边界

Ray 的进程与角色编排在分布式运行时；推理侧的请求组织和分布式生成方案在推理服务。

## Topic 与材料入口

下表按机制归类已有材料节点。材料页保留具体问题、先修与来源；教学 Notebook 在实际学习后逐步展开。条目不表示个人掌握度。

| Topic | 要解释的问题 | 材料入口 |
| --- | --- | --- |
| Send/Recv 与 Collective Communication | 点对点和 AllReduce/AllGather/AllToAll 等 collectives 分别表达什么数据交换？ | [07.1](../../paths/ai-infra/07-nccl-model-parallelism.md#ai-07-1) |
| AllReduce、ReduceScatter 与 AllGather | 各 rank 最后持有什么结果，归约和分发怎样组合？ | [07.2](../../paths/ai-infra/07-nccl-model-parallelism.md#ai-07-2) |
| Ring/Tree 与通信成本 | 不同消息大小、rank 数和拓扑下，延迟与带宽怎样影响算法选择？ | [07.3](../../paths/ai-infra/07-nccl-model-parallelism.md#ai-07-3) |
| PCIe、NVLink、InfiniBand/RDMA | 卡内、卡间与跨节点的数据经过什么路径，带宽瓶颈如何出现？ | [07.4](../../paths/ai-infra/07-nccl-model-parallelism.md#ai-07-4) |
| DDP | 梯度 bucket 与同步怎样和 backward 重叠，哪些更新仍是本地进行？ | [07.5](../../paths/ai-infra/07-nccl-model-parallelism.md#ai-07-5) |
| Megatron Tensor Parallelism | Column/Row Parallel Linear 切哪些维度，在哪些位置需要通信？ | [07.6](../../paths/ai-infra/07-nccl-model-parallelism.md#ai-07-6) |
| GPipe 与 Pipeline Parallelism | 按层切分之后，microbatch 如何通过前向和反向，bubble 从哪里出现？ | [07.7](../../paths/ai-infra/07-nccl-model-parallelism.md#ai-07-7) |
| PipeDream / 1F1B Schedule | 不同 pipeline schedules 在权重版本、更新时机和激活存储上怎样不同？ | [07.8](../../paths/ai-infra/07-nccl-model-parallelism.md#ai-07-8) |
| Sequence Parallelism 与 Context Parallelism | 同样沿序列切分时，各方案在什么算子、状态和通信边界上不同？ | [07.9](../../paths/ai-infra/07-nccl-model-parallelism.md#ai-07-9) |
| Ring Attention / Ulysses | 长序列 attention 如何在多卡计算，KV 轮转与 AllToAll 重排分别付出什么？ | [07.10](../../paths/ai-infra/07-nccl-model-parallelism.md#ai-07-10) |
| DP×TP×PP 组合与 Rank Placement | 并行 groups 怎样对应 rank 和硬件拓扑，不同阶段的通信走哪里？ | [07.11](../../paths/ai-infra/07-nccl-model-parallelism.md#ai-07-11) |
| 训练显存账本 | 参数、梯度、optimizer、activation 与临时 buffer 怎样形成峰值？ | [08.1](../../paths/ai-infra/08-zero-fsdp-memory.md#ai-08-1) |
| Activation Checkpointing | 哪些中间结果可以不保存，backward 的重计算与随机状态怎样保持一致？ | [08.2](../../paths/ai-infra/08-zero-fsdp-memory.md#ai-08-2) |
| ZeRO-1 | 优化器状态怎样分片，每个 rank 更新哪一部分参数？ | [08.3](../../paths/ai-infra/08-zero-fsdp-memory.md#ai-08-3) |
| ZeRO-2 | 梯度分片怎样连接 ReduceScatter 与本地更新？ | [08.4](../../paths/ai-infra/08-zero-fsdp-memory.md#ai-08-4) |
| ZeRO-3 | 参数分片以后，完整层所需参数什么时候取回、使用和释放？ | [08.5](../../paths/ai-infra/08-zero-fsdp-memory.md#ai-08-5) |
| FSDP / FSDP2 | wrap/shard、AllGather 与 Reshard 怎样组织，版本间接口与调度有什么区别？ | [08.6](../../paths/ai-infra/08-zero-fsdp-memory.md#ai-08-6) |
| CPU/NVMe Offload | 把状态移出显存以后，拷贝、传输与更新成本在哪里发生？ | [08.7](../../paths/ai-infra/08-zero-fsdp-memory.md#ai-08-7) |
| Distributed Checkpoint | 模型、optimizer、RNG 与数据进度怎样保存，恢复后如何核对训练语义？ | [08.8](../../paths/ai-infra/08-zero-fsdp-memory.md#ai-08-8) |
| Expert Parallelism 与 AllToAll | dispatch/combine 如何把 token 发到 expert 所在设备，又怎样还原顺序？ | [12.7](../../paths/ai-infra/12-moe-expert-parallelism.md#ai-12-7) |
| DeepSpeed-MoE / DeepSeek-V3 | 一套完整 MoE 系统怎样组合专家结构、负载均衡、并行与通信？ | [12.9](../../paths/ai-infra/12-moe-expert-parallelism.md#ai-12-9) |

关联分类：[分布式运行时与资源编排](../distributed-runtime/README.md) · [张量计算与自动微分](../tensor-autograd/README.md) · [生成执行与推理服务](../inference-serving/README.md)。
