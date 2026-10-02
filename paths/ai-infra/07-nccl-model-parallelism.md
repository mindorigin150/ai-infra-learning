---
title: '07 · NCCL、DDP、Megatron 与 GPipe'
---

# 07 · NCCL、DDP、Megatron 与 GPipe

先画通信的输入输出，再连接梯度、矩阵与层的划分；保持不同流水线的训练语义区别。

[完整地图](../ai-infra-map.md) · [课程与论文出处](../ai-infra-sources.md) · [GAPS](../../GAPS.md)

本页是学习导航。节点问题、先修与验证方案由本仓库编排；课程栏链接材料入口，补充节点另行标注。**本章验证均未运行；没有个人掌握度判断或性能实测。**

(ai-07-1)=
## 07.1 Send/Recv 与 Collective Communication：点对点和 AllReduce/AllGather/AllToAll 等 collectives 分别表达什么数据交换？

- **先修节点**：[02.2 Broadcasting、Matmul 与 Einsum](02-pytorch-training-step.md#ai-02-2)、[04.8 CUDA Events、Warmup 与 Synchronization](04-gpu-profiling.md#ai-04-8)
- **课程出处**：**课程拆分**；[M13 · Distributed Model Training](../ai-infra-sources.md#course-m13)、[S07 · L07 · Parallelism (Tatsu)](../ai-infra-sources.md#course-s07)。
- **论文与实现**：[NCCL user guide](../ai-infra-sources.md#source-nccl)。
- **后续验证（未运行）**：CPU 示意/多 GPU：先画每个 rank 的输入输出，再用少量可识别数据核对通信。

(ai-07-2)=
## 07.2 AllReduce、ReduceScatter 与 AllGather：各 rank 最后持有什么结果，归约和分发怎样组合？

- **先修节点**：[07.1 Send/Recv 与 Collective Communication](07-nccl-model-parallelism.md#ai-07-1)、[05.3 Reduction Kernel](05-cuda-triton-kernels.md#ai-05-3)
- **课程出处**：**课程拆分**；[M13 · Distributed Model Training](../ai-infra-sources.md#course-m13)、[S07 · L07 · Parallelism (Tatsu)](../ai-infra-sources.md#course-s07)、[S08 · L08 · Parallelism (Percy)](../ai-infra-sources.md#course-s08)。
- **论文与实现**：[NCCL user guide](../ai-infra-sources.md#source-nccl)。
- **后续验证（未运行）**：CPU 示意/多 GPU：手算教学数组；检查 collective 结果及求和/平均的区别。

(ai-07-3)=
## 07.3 Ring/Tree 与通信成本：不同消息大小、rank 数和拓扑下，延迟与带宽怎样影响算法选择？

- **先修节点**：[07.2 AllReduce、ReduceScatter 与 AllGather](07-nccl-model-parallelism.md#ai-07-2)、[04.7 FLOPs、Bytes、Arithmetic Intensity 与 Roofline](04-gpu-profiling.md#ai-04-7)
- **课程出处**：**课程拆分**；[M13 · Distributed Model Training](../ai-infra-sources.md#course-m13)、[S07 · L07 · Parallelism (Tatsu)](../ai-infra-sources.md#course-s07)。
- **论文与实现**：[NCCL user guide](../ai-infra-sources.md#source-nccl)。
- **后续验证（未运行）**：多 GPU：改变消息大小并重复测量，记录拓扑与实际通信证据，不固定性能排序。

(ai-07-4)=
## 07.4 PCIe、NVLink、InfiniBand/RDMA：卡内、卡间与跨节点的数据经过什么路径，带宽瓶颈如何出现？

- **先修节点**：[04.3 Registers、Shared Memory、L2 与 HBM](04-gpu-profiling.md#ai-04-3)、[07.1 Send/Recv 与 Collective Communication](07-nccl-model-parallelism.md#ai-07-1)
- **课程出处**：**课程拆分**；[M13 · Distributed Model Training](../ai-infra-sources.md#course-m13)、[S07 · L07 · Parallelism (Tatsu)](../ai-infra-sources.md#course-s07)。
- **论文与实现**：[NCCL user guide](../ai-infra-sources.md#source-nccl)、[Nsight Systems](../ai-infra-sources.md#source-nsys)。
- **后续验证（未运行）**：环境检查/多 GPU：记录设备拓扑并画路径；跨节点实验需真实多节点环境。

(ai-07-5)=
## 07.5 DDP：梯度 bucket 与同步怎样和 backward 重叠，哪些更新仍是本地进行？

- **先修节点**：[07.2 AllReduce、ReduceScatter 与 AllGather](07-nccl-model-parallelism.md#ai-07-2)、[02.7 Gradient Accumulation](02-pytorch-training-step.md#ai-02-7)
- **课程出处**：**课程拆分**；[M14 · Distributed Model Training II](../ai-infra-sources.md#course-m14)、[S08 · L08 · Parallelism (Percy)](../ai-infra-sources.md#course-s08)。
- **论文与实现**：[PyTorch Distributed Data Parallel](../ai-infra-sources.md#source-ddp-paper)、[PyTorch DDP tutorial](../ai-infra-sources.md#source-ddp)。
- **后续验证（未运行）**：两 GPU：比较一步 DDP 与等效整 batch 的更新，再查看 bucket 与 backward timeline。

(ai-07-6)=
## 07.6 Megatron Tensor Parallelism：Column/Row Parallel Linear 切哪些维度，在哪些位置需要通信？

- **先修节点**：[07.2 AllReduce、ReduceScatter 与 AllGather](07-nccl-model-parallelism.md#ai-07-2)、[05.5 Naive GEMM → Tiled GEMM](05-cuda-triton-kernels.md#ai-05-5)、[01.7 RMSNorm、SwiGLU 与 Residual Connection](01-tokenizer-transformer.md#ai-01-7)
- **课程出处**：**课程拆分**；[M15 · Distributed Model Training III](../ai-infra-sources.md#course-m15)、[S07 · L07 · Parallelism (Tatsu)](../ai-infra-sources.md#course-s07)、[S08 · L08 · Parallelism (Percy)](../ai-infra-sources.md#course-s08)。
- **论文与实现**：[Megatron-LM: Training Multi-Billion Parameter Language Models](../ai-infra-sources.md#source-megatron)、[Efficient Large-Scale Language Model Training Using Megatron-LM](../ai-infra-sources.md#source-megatron-scale)、[Megatron Core](../ai-infra-sources.md#source-mcore)。
- **后续验证（未运行）**：CPU 示意/两 GPU：对小线性层手算分片，核对合并输出与梯度。

(ai-07-7)=
## 07.7 GPipe 与 Pipeline Parallelism：按层切分之后，microbatch 如何通过前向和反向，bubble 从哪里出现？

- **先修节点**：[02.7 Gradient Accumulation](02-pytorch-training-step.md#ai-02-7)、[07.1 Send/Recv 与 Collective Communication](07-nccl-model-parallelism.md#ai-07-1)
- **课程出处**：**课程拆分**；[M15 · Distributed Model Training III](../ai-infra-sources.md#course-m15)、[S07 · L07 · Parallelism (Tatsu)](../ai-infra-sources.md#course-s07)。
- **论文与实现**：[GPipe](../ai-infra-sources.md#source-gpipe)。
- **后续验证（未运行）**：CPU 时间线/多 GPU：画两个 stage 的 microbatch 时序；说明填充、排空与激活保存。

(ai-07-8)=
## 07.8 PipeDream / 1F1B Schedule：不同 pipeline schedules 在权重版本、更新时机和激活存储上怎样不同？

- **先修节点**：[07.7 GPipe 与 Pipeline Parallelism](07-nccl-model-parallelism.md#ai-07-7)、[02.6 AdamW](02-pytorch-training-step.md#ai-02-6)
- **课程出处**：**论文补充**；[M15 · Distributed Model Training III](../ai-infra-sources.md#course-m15)。
- **论文与实现**：[PipeDream](../ai-infra-sources.md#source-pipedream)、[Efficient Large-Scale Language Model Training Using Megatron-LM](../ai-infra-sources.md#source-megatron-scale)。
- **后续验证（未运行）**：复述/时间线：区分原始 PipeDream 的版本语义与同步 1F1B；比较更新点和激活峰值。

(ai-07-9)=
## 07.9 Sequence Parallelism 与 Context Parallelism：同样沿序列切分时，各方案在什么算子、状态和通信边界上不同？

- **先修节点**：[07.6 Megatron Tensor Parallelism](07-nccl-model-parallelism.md#ai-07-6)、[01.5 Causal Attention、Q/K/V 与 Multi-head Attention](01-tokenizer-transformer.md#ai-01-5)
- **课程出处**：**工程补充**；[S07 · L07 · Parallelism (Tatsu)](../ai-infra-sources.md#course-s07)、[M15 · Distributed Model Training III](../ai-infra-sources.md#course-m15)。
- **论文与实现**：[Megatron Core](../ai-infra-sources.md#source-mcore)、[Efficient Large-Scale Language Model Training Using Megatron-LM](../ai-infra-sources.md#source-megatron-scale)。
- **后续验证（未运行）**：代码阅读/多 GPU：沿一个 block 标注 sharded/replicated tensors，明确采用的实现命名。

(ai-07-10)=
## 07.10 Ring Attention / Ulysses：长序列 attention 如何在多卡计算，KV 轮转与 AllToAll 重排分别付出什么？

- **先修节点**：[07.9 Sequence Parallelism 与 Context Parallelism](07-nccl-model-parallelism.md#ai-07-9)、[06.3 FlashAttention-1](06-flashattention-compilation.md#ai-06-3)、[07.2 AllReduce、ReduceScatter 与 AllGather](07-nccl-model-parallelism.md#ai-07-2)
- **课程出处**：**论文补充**；[M15 · Distributed Model Training III](../ai-infra-sources.md#course-m15)。
- **论文与实现**：[Ring Attention with Blockwise Transformers](../ai-infra-sources.md#source-ring)、[DeepSpeed Ulysses](../ai-infra-sources.md#source-ulysses)。
- **后续验证（未运行）**：CPU 示意/多 GPU：画分块交换与计算；比较完整 attention 的数值与通信流量模型。

(ai-07-11)=
## 07.11 DP×TP×PP 组合与 Rank Placement：并行 groups 怎样对应 rank 和硬件拓扑，不同阶段的通信走哪里？

- **先修节点**：[07.4 PCIe、NVLink、InfiniBand/RDMA](07-nccl-model-parallelism.md#ai-07-4)、[07.5 DDP](07-nccl-model-parallelism.md#ai-07-5)、[07.6 Megatron Tensor Parallelism](07-nccl-model-parallelism.md#ai-07-6)、[07.7 GPipe 与 Pipeline Parallelism](07-nccl-model-parallelism.md#ai-07-7)
- **课程出处**：**工程补充**；[S07 · L07 · Parallelism (Tatsu)](../ai-infra-sources.md#course-s07)、[S08 · L08 · Parallelism (Percy)](../ai-infra-sources.md#course-s08)、[M15 · Distributed Model Training III](../ai-infra-sources.md#course-m15)。
- **论文与实现**：[Megatron Core](../ai-infra-sources.md#source-mcore)、[NCCL user guide](../ai-infra-sources.md#source-nccl)。
- **后续验证（未运行）**：复述/多 GPU：为教学用拓扑列出 groups；硬件数量足够时再检验通信路径。

## 回到实际学习

选一个节点，先复述当前解释，再核查材料或代码并预测实验结果。实验前记录硬件、依赖版本、源码 commit、输入、同步与计时方法；重复测量保留原始记录。具体解释与证据逐步补到 topic 主笔记，未运行的方案保持标注。

[返回总地图](../ai-infra-map.md) · [上一章：06](06-flashattention-compilation.md) · [下一章：08](08-zero-fsdp-memory.md)
