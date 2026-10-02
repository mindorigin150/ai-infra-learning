---
title: '05 · 从 Vector Add 到 Triton Matmul'
---

# 05 · 从 Vector Add 到 Triton Matmul

从索引和正确性开始，逐步连接访存复用、矩阵指令与 kernel fusion。

[完整地图](../ai-infra-map.md) · [课程与论文出处](../ai-infra-sources.md) · [GAPS](../../GAPS.md)

本页是学习导航。节点问题、先修与验证方案由本仓库编排；课程栏链接材料入口，补充节点另行标注。**本章验证均未运行；没有个人掌握度判断或性能实测。**

(ai-05-1)=
## 05.1 CUDA Vector Add：怎样写出覆盖输入、处理尾部边界且正确的 kernel？

- **先修节点**：[04.1 Grid、Block、Thread 与 Warp](04-gpu-profiling.md#ai-04-1)、[04.3 Registers、Shared Memory、L2 与 HBM](04-gpu-profiling.md#ai-04-3)
- **课程出处**：**课程拆分**；[M02 · GPU Programming Basics 1](../ai-infra-sources.md#course-m02)、[M03 · GPU Programming Basics 2](../ai-infra-sources.md#course-m03)。
- **论文与实现**：[CUDA Programming Guide](../ai-infra-sources.md#source-cuda)。
- **后续验证（未运行）**：单 GPU：先预测索引覆盖，比较参考结果；用不整除 block 的输入检查边界。

(ai-05-2)=
## 05.2 Triton Vector Add：program ID、block 与 mask 怎样表达同一份向量工作？

- **先修节点**：[05.1 CUDA Vector Add](05-cuda-triton-kernels.md#ai-05-1)
- **课程出处**：**课程拆分**；[S06 · L06 · Kernels, Triton (Tatsu)](../ai-infra-sources.md#course-s06)。
- **论文与实现**：[Triton kernel tutorials](../ai-infra-sources.md#source-triton)。
- **后续验证（未运行）**：单 GPU：复现相同输入与边界检查，解释 Triton program 和 CUDA thread 的映射差别。

(ai-05-3)=
## 05.3 Reduction Kernel：怎样并行归约，同步与浮点加法次序会怎样影响结果？

- **先修节点**：[05.2 Triton Vector Add](05-cuda-triton-kernels.md#ai-05-2)、[04.3 Registers、Shared Memory、L2 与 HBM](04-gpu-profiling.md#ai-04-3)
- **课程出处**：**课程拆分**；[M03 · GPU Programming Basics 2](../ai-infra-sources.md#course-m03)、[M10 · GPU Acceleration](../ai-infra-sources.md#course-m10)。
- **论文与实现**：[Triton kernel tutorials](../ai-infra-sources.md#source-triton)、[CUDA Best Practices](../ai-infra-sources.md#source-cuda-best)。
- **后续验证（未运行）**：单 GPU：对不同长度和不同数值范围比较归约，记录误差与计时。

(ai-05-4)=
## 05.4 Fused Softmax：怎样在一次 kernel 内完成稳定 softmax，减少哪些中间数据？

- **先修节点**：[01.5 Causal Attention、Q/K/V 与 Multi-head Attention](01-tokenizer-transformer.md#ai-01-5)、[05.3 Reduction Kernel](05-cuda-triton-kernels.md#ai-05-3)
- **课程出处**：**课程拆分**；[S06 · L06 · Kernels, Triton (Tatsu)](../ai-infra-sources.md#course-s06)、[M11 · Accelerating Transformer on GPU Part 1](../ai-infra-sources.md#course-m11)。
- **论文与实现**：[Triton kernel tutorials](../ai-infra-sources.md#source-triton)。
- **后续验证（未运行）**：单 GPU：检查大 logits 的数值稳定性，再比较独立算子与 fused 实现的数据路径。

(ai-05-5)=
## 05.5 Naive GEMM → Tiled GEMM：分块怎样复用矩阵数据，边界 tile 怎样处理？

- **先修节点**：[02.2 Broadcasting、Matmul 与 Einsum](02-pytorch-training-step.md#ai-02-2)、[04.5 Coalesced Access 与 Memory Layout](04-gpu-profiling.md#ai-04-5)、[04.7 FLOPs、Bytes、Arithmetic Intensity 与 Roofline](04-gpu-profiling.md#ai-04-7)、[05.2 Triton Vector Add](05-cuda-triton-kernels.md#ai-05-2)
- **课程出处**：**课程拆分**；[M10 · GPU Acceleration](../ai-infra-sources.md#course-m10)、[S06 · L06 · Kernels, Triton (Tatsu)](../ai-infra-sources.md#course-s06)。
- **论文与实现**：[Triton kernel tutorials](../ai-infra-sources.md#source-triton)、[NVIDIA CUTLASS](../ai-infra-sources.md#source-cutlass)。
- **后续验证（未运行）**：单 GPU：先画数据复用，再比较多种矩阵 shape 与 tile，记录错误与性能条件。

(ai-05-6)=
## 05.6 Tensor Core GEMM：shape、dtype 与 layout 怎样进入矩阵指令的实现？

- **先修节点**：[05.5 Naive GEMM → Tiled GEMM](05-cuda-triton-kernels.md#ai-05-5)、[04.4 Tensor Cores 与矩阵乘法指令](04-gpu-profiling.md#ai-04-4)
- **课程出处**：**工程补充**；[S06 · L06 · Kernels, Triton (Tatsu)](../ai-infra-sources.md#course-s06)、[M10 · GPU Acceleration](../ai-infra-sources.md#course-m10)。
- **论文与实现**：[NVIDIA CUTLASS](../ai-infra-sources.md#source-cutlass)、[Triton kernel tutorials](../ai-infra-sources.md#source-triton)。
- **后续验证（未运行）**：单 GPU：固定输入和误差容忍条件，确认采用的指令，再比较相同精度下的基线。

(ai-05-7)=
## 05.7 RMSNorm/SwiGLU Fusion：哪些算子能融合，减少访存或 launch 是否会引入其他限制？

- **先修节点**：[01.7 RMSNorm、SwiGLU 与 Residual Connection](01-tokenizer-transformer.md#ai-01-7)、[05.4 Fused Softmax](05-cuda-triton-kernels.md#ai-05-4)、[05.5 Naive GEMM → Tiled GEMM](05-cuda-triton-kernels.md#ai-05-5)
- **课程出处**：**工程补充**；[M11 · Accelerating Transformer on GPU Part 1](../ai-infra-sources.md#course-m11)、[M12 · Accelerating Transformer on GPU Part 2](../ai-infra-sources.md#course-m12)、[S06 · L06 · Kernels, Triton (Tatsu)](../ai-infra-sources.md#course-s06)。
- **论文与实现**：[LightSeq2](../ai-infra-sources.md#source-lightseq2)、[Triton kernel tutorials](../ai-infra-sources.md#source-triton)。
- **后续验证（未运行）**：单 GPU：分别核对数值结果与端到端计时，检查融合后的资源占用。

(ai-05-8)=
## 05.8 Kernel Benchmark 与正确性比较：怎样避免用错误计时、单一 shape 或过宽误差阈值判断优化？

- **先修节点**：[04.8 CUDA Events、Warmup 与 Synchronization](04-gpu-profiling.md#ai-04-8)、[04.9 PyTorch Profiler、Nsight Systems 与 Nsight Compute](04-gpu-profiling.md#ai-04-9)、[05.5 Naive GEMM → Tiled GEMM](05-cuda-triton-kernels.md#ai-05-5)
- **课程出处**：**课程拆分**；[S06 · L06 · Kernels, Triton (Tatsu)](../ai-infra-sources.md#course-s06)。
- **论文与实现**：[CUDA Best Practices](../ai-infra-sources.md#source-cuda-best)、[Triton kernel tutorials](../ai-infra-sources.md#source-triton)。
- **后续验证（未运行）**：单 GPU：对不同规模保留预热、原始重复计时、误差和环境，解释测量开销。

## 回到实际学习

选一个节点，先复述当前解释，再核查材料或代码并预测实验结果。实验前记录硬件、依赖版本、源码 commit、输入、同步与计时方法；重复测量保留原始记录。具体解释与证据逐步补到 topic 主笔记，未运行的方案保持标注。

[返回总地图](../ai-infra-map.md) · [上一章：04](04-gpu-profiling.md) · [下一章：06](06-flashattention-compilation.md)
