---
title: GPU 执行与算子优化
---

# GPU 执行与算子优化

一个算子怎样映射到 GPU 的线程、存储和指令，执行如何被融合或编译？

[主题索引](../README.md) · [开始一次学习](../../paths/start-here.md)

## 分类边界

数学定义连接模型表示；正确计时、性能上界和观测工具连接性能模型。

## Topic 与材料入口

下表按机制归类已有材料节点。材料页保留具体问题、先修与来源；教学 Notebook 在实际学习后逐步展开。条目不表示个人掌握度。

| Topic | 要解释的问题 | 材料入口 |
| --- | --- | --- |
| Grid、Block、Thread 与 Warp | 一个 kernel 的逻辑线程怎样对应输入元素与硬件执行单元？ | [04.1](../../paths/ai-infra/04-gpu-profiling.md#ai-04-1) |
| SM、Warp Scheduler 与 SIMT | SM 怎样执行 warp，分支与依赖会怎样影响有效执行？ | [04.2](../../paths/ai-infra/04-gpu-profiling.md#ai-04-2) |
| Registers、Shared Memory、L2 与 HBM | kernel 的数据和状态分别占用哪些内存层级？ | [04.3](../../paths/ai-infra/04-gpu-profiling.md#ai-04-3) |
| Tensor Cores 与矩阵乘法指令 | dtype、矩阵布局与形状怎样限制矩阵指令的使用？ | [04.4](../../paths/ai-infra/04-gpu-profiling.md#ai-04-4) |
| Coalesced Access 与 Memory Layout | 相邻线程访问怎样形成内存事务，stride 会增加什么成本？ | [04.5](../../paths/ai-infra/04-gpu-profiling.md#ai-04-5) |
| Occupancy、寄存器压力与 Latency Hiding | 为什么更多线程或更高 occupancy 不必然得到更快的 kernel？ | [04.6](../../paths/ai-infra/04-gpu-profiling.md#ai-04-6) |
| CUDA Vector Add | 怎样写出覆盖输入、处理尾部边界且正确的 kernel？ | [05.1](../../paths/ai-infra/05-cuda-triton-kernels.md#ai-05-1) |
| Triton Vector Add | program ID、block 与 mask 怎样表达同一份向量工作？ | [05.2](../../paths/ai-infra/05-cuda-triton-kernels.md#ai-05-2) |
| Reduction Kernel | 怎样并行归约，同步与浮点加法次序会怎样影响结果？ | [05.3](../../paths/ai-infra/05-cuda-triton-kernels.md#ai-05-3) |
| Fused Softmax | 怎样在一次 kernel 内完成稳定 softmax，减少哪些中间数据？ | [05.4](../../paths/ai-infra/05-cuda-triton-kernels.md#ai-05-4) |
| Naive GEMM → Tiled GEMM | 分块怎样复用矩阵数据，边界 tile 怎样处理？ | [05.5](../../paths/ai-infra/05-cuda-triton-kernels.md#ai-05-5) |
| Tensor Core GEMM | shape、dtype 与 layout 怎样进入矩阵指令的实现？ | [05.6](../../paths/ai-infra/05-cuda-triton-kernels.md#ai-05-6) |
| RMSNorm/SwiGLU Fusion | 哪些算子能融合，减少访存或 launch 是否会引入其他限制？ | [05.7](../../paths/ai-infra/05-cuda-triton-kernels.md#ai-05-7) |
| 标准 Attention 的显存与 IO | QK、softmax、AV 产生和消费哪些中间矩阵，成本如何随序列变化？ | [06.1](../../paths/ai-infra/06-flashattention-compilation.md#ai-06-1) |
| Online Softmax | 看不到全部 logits 时，怎样合并分块的最大值、归一化项与输出？ | [06.2](../../paths/ai-infra/06-flashattention-compilation.md#ai-06-2) |
| FlashAttention-1 | tiling 与 online softmax 怎样避免保存完整 Attention 矩阵，backward 怎样重计算？ | [06.3](../../paths/ai-infra/06-flashattention-compilation.md#ai-06-3) |
| FlashAttention-2 | thread block 与 warp 的工作划分怎样减少不必要的操作并改善并行度？ | [06.4](../../paths/ai-infra/06-flashattention-compilation.md#ai-06-4) |
| FlashAttention-3 | 异步矩阵指令、数据移动和低精度计算怎样形成新的流水线？ | [06.5](../../paths/ai-infra/06-flashattention-compilation.md#ai-06-5) |
| FlashAttention 的 Causal、Varlen 与 Packed 接口 | causal 对齐、序列边界与 QKV 布局怎样对应各接口的语义？ | [06.6](../../paths/ai-infra/06-flashattention-compilation.md#ai-06-6) |
| LightSeq / LightSeq2 | Transformer 推理与训练有哪些可联合优化的算子、内存和执行步骤？ | [06.7](../../paths/ai-infra/06-flashattention-compilation.md#ai-06-7) |
| torch.compile、Fusion 与 Graph Break | 编译如何改变执行，哪些动态行为可能打断图或触发重编译？ | [06.8](../../paths/ai-infra/06-flashattention-compilation.md#ai-06-8) |
| CUDA Graph 与 JAX JIT | capture/replay 和编译缓存分别复用什么，输入与内存约束怎样不同？ | [06.9](../../paths/ai-infra/06-flashattention-compilation.md#ai-06-9) |
| Grouped GEMM 与 MoE Kernel | 不等长 expert batches 怎样组成矩阵计算，什么时候会有小 GEMM 与 padding 成本？ | [12.8](../../paths/ai-infra/12-moe-expert-parallelism.md#ai-12-8) |

关联分类：[模型表示与生成机制](../models/README.md) · [性能模型与观测](../performance/README.md)。
