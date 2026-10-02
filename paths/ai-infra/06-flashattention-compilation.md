---
title: '06 · FlashAttention、LightSeq 与编译执行'
---

# 06 · FlashAttention、LightSeq 与编译执行

沿 Attention 的 IO、工作划分和硬件执行看三代 FlashAttention；区分算子优化、编译与 graph capture。

[完整地图](../ai-infra-map.md) · [课程与论文出处](../ai-infra-sources.md) · [GAPS](../../GAPS.md)

本页是学习导航。节点问题、先修与验证方案由本仓库编排；课程栏链接材料入口，补充节点另行标注。**本章验证均未运行；没有个人掌握度判断或性能实测。**

(ai-06-1)=
## 06.1 标准 Attention 的显存与 IO：QK、softmax、AV 产生和消费哪些中间矩阵，成本如何随序列变化？

- **先修节点**：[01.5 Causal Attention、Q/K/V 与 Multi-head Attention](01-tokenizer-transformer.md#ai-01-5)、[04.7 FLOPs、Bytes、Arithmetic Intensity 与 Roofline](04-gpu-profiling.md#ai-04-7)
- **课程出处**：**课程拆分**；[M20 · Optimizing Attention for Modern Hardware (Tri Dao)](../ai-infra-sources.md#course-m20)、[S06 · L06 · Kernels, Triton (Tatsu)](../ai-infra-sources.md#course-s06)。
- **论文与实现**：[FlashAttention-1](../ai-infra-sources.md#source-fa1)。
- **后续验证（未运行）**：CPU/复述：画完整数据路径；分别估算计算、存储容量和指定内存层级的流量。

(ai-06-2)=
## 06.2 Online Softmax：看不到全部 logits 时，怎样合并分块的最大值、归一化项与输出？

- **先修节点**：[01.5 Causal Attention、Q/K/V 与 Multi-head Attention](01-tokenizer-transformer.md#ai-01-5)、[05.4 Fused Softmax](05-cuda-triton-kernels.md#ai-05-4)
- **课程出处**：**课程拆分**；[M20 · Optimizing Attention for Modern Hardware (Tri Dao)](../ai-infra-sources.md#course-m20)、[S06 · L06 · Kernels, Triton (Tatsu)](../ai-infra-sources.md#course-s06)。
- **论文与实现**：[FlashAttention-1](../ai-infra-sources.md#source-fa1)。
- **后续验证（未运行）**：CPU：分块处理教学用 logits，比较全量 softmax，并测试数值跨度很大的输入。

(ai-06-3)=
## 06.3 FlashAttention-1：tiling 与 online softmax 怎样避免保存完整 Attention 矩阵，backward 怎样重计算？

- **先修节点**：[06.1 标准 Attention 的显存与 IO](06-flashattention-compilation.md#ai-06-1)、[06.2 Online Softmax](06-flashattention-compilation.md#ai-06-2)、[05.5 Naive GEMM → Tiled GEMM](05-cuda-triton-kernels.md#ai-05-5)、[04.3 Registers、Shared Memory、L2 与 HBM](04-gpu-profiling.md#ai-04-3)
- **课程出处**：**课程拆分**；[M20 · Optimizing Attention for Modern Hardware (Tri Dao)](../ai-infra-sources.md#course-m20)、[S06 · L06 · Kernels, Triton (Tatsu)](../ai-infra-sources.md#course-s06)。
- **论文与实现**：[FlashAttention-1](../ai-infra-sources.md#source-fa1)、[FlashAttention implementation](../ai-infra-sources.md#source-fa-code)。
- **后续验证（未运行）**：CPU/单 GPU：先追踪一对 Q/KV tiles；再核对输出和梯度，记录显存与计时方法。

(ai-06-4)=
## 06.4 FlashAttention-2：thread block 与 warp 的工作划分怎样减少不必要的操作并改善并行度？

- **先修节点**：[06.3 FlashAttention-1](06-flashattention-compilation.md#ai-06-3)、[04.6 Occupancy、寄存器压力与 Latency Hiding](04-gpu-profiling.md#ai-04-6)
- **课程出处**：**论文补充**；[M20 · Optimizing Attention for Modern Hardware (Tri Dao)](../ai-infra-sources.md#course-m20)、[S06 · L06 · Kernels, Triton (Tatsu)](../ai-infra-sources.md#course-s06)。
- **论文与实现**：[FlashAttention-2](../ai-infra-sources.md#source-fa2)、[FlashAttention implementation](../ai-infra-sources.md#source-fa-code)。
- **后续验证（未运行）**：复述/单 GPU：对照论文图解释分工；仅在支持的环境比较相同输入，注明 backend。

(ai-06-5)=
## 06.5 FlashAttention-3：异步矩阵指令、数据移动和低精度计算怎样形成新的流水线？

- **先修节点**：[06.4 FlashAttention-2](06-flashattention-compilation.md#ai-06-4)、[04.4 Tensor Cores 与矩阵乘法指令](04-gpu-profiling.md#ai-04-4)、[02.8 FP32、FP16、BF16 与 AMP](02-pytorch-training-step.md#ai-02-8)
- **课程出处**：**论文补充**；[M20 · Optimizing Attention for Modern Hardware (Tri Dao)](../ai-infra-sources.md#course-m20)。
- **论文与实现**：[FlashAttention-3](../ai-infra-sources.md#source-fa3)、[FlashAttention implementation](../ai-infra-sources.md#source-fa-code)。
- **后续验证（未运行）**：复述；需要支持相应实现的 GPU：画访存/GEMM/softmax 重叠，不把 FA3 的特点归给 FA2。

(ai-06-6)=
## 06.6 FlashAttention 的 Causal、Varlen 与 Packed 接口：causal 对齐、序列边界与 QKV 布局怎样对应各接口的语义？

- **先修节点**：[06.3 FlashAttention-1](06-flashattention-compilation.md#ai-06-3)、[03.7 Variable-length Attention 与 cu_seqlens](03-data-sequence-packing.md#ai-03-7)
- **课程出处**：**工程补充**；[M20 · Optimizing Attention for Modern Hardware (Tri Dao)](../ai-infra-sources.md#course-m20)、[S06 · L06 · Kernels, Triton (Tatsu)](../ai-infra-sources.md#course-s06)。
- **论文与实现**：[FlashAttention implementation](../ai-infra-sources.md#source-fa-code)。
- **后续验证（未运行）**：单 GPU：比较逐条与 varlen；另检查 packed QKV 的布局，记录版本与 causal 对齐规则。

(ai-06-7)=
## 06.7 LightSeq / LightSeq2：Transformer 推理与训练有哪些可联合优化的算子、内存和执行步骤？

- **先修节点**：[05.7 RMSNorm/SwiGLU Fusion](05-cuda-triton-kernels.md#ai-05-7)、[02.4 Saved Tensors 与显存生命周期](02-pytorch-training-step.md#ai-02-4)、[04.9 PyTorch Profiler、Nsight Systems 与 Nsight Compute](04-gpu-profiling.md#ai-04-9)
- **课程出处**：**课程拆分**；[M11 · Accelerating Transformer on GPU Part 1](../ai-infra-sources.md#course-m11)、[M12 · Accelerating Transformer on GPU Part 2](../ai-infra-sources.md#course-m12)。
- **论文与实现**：[LightSeq](../ai-infra-sources.md#source-lightseq)、[LightSeq2](../ai-infra-sources.md#source-lightseq2)。
- **后续验证（未运行）**：代码阅读/单 GPU：选一条执行路径，对照论文标出融合与内存复用，不搬用原论文加速数值。

(ai-06-8)=
## 06.8 torch.compile、Fusion 与 Graph Break：编译如何改变执行，哪些动态行为可能打断图或触发重编译？

- **先修节点**：[02.3 Autograd 与 Backward Graph](02-pytorch-training-step.md#ai-02-3)、[05.7 RMSNorm/SwiGLU Fusion](05-cuda-triton-kernels.md#ai-05-7)、[04.8 CUDA Events、Warmup 与 Synchronization](04-gpu-profiling.md#ai-04-8)
- **课程出处**：**工程补充**；[S06 · L06 · Kernels, Triton (Tatsu)](../ai-infra-sources.md#course-s06)、[M05 · Deep Learning Frameworks Design](../ai-infra-sources.md#course-m05)。
- **论文与实现**：[torch.compile tutorial](../ai-infra-sources.md#source-compile)。
- **后续验证（未运行）**：单 GPU/CPU：对小函数观察首次编译与稳态运行，改变 shape 并查看 graph break 的证据。

(ai-06-9)=
## 06.9 CUDA Graph 与 JAX JIT：capture/replay 和编译缓存分别复用什么，输入与内存约束怎样不同？

- **先修节点**：[06.8 torch.compile、Fusion 与 Graph Break](06-flashattention-compilation.md#ai-06-8)、[04.8 CUDA Events、Warmup 与 Synchronization](04-gpu-profiling.md#ai-04-8)
- **课程出处**：**课程拆分与工程补充**；[MJIT · GPU just-in-time compilation](../ai-infra-sources.md#course-mjit)。
- **论文与实现**：[PyTorch CUDA Graphs](../ai-infra-sources.md#source-graphs)、[JAX JIT](../ai-infra-sources.md#source-jax)。
- **后续验证（未运行）**：CPU/单 GPU：分别追踪 JIT 的首次/重复调用与 CUDA Graph replay，比较稳态和端到端成本。

## 回到实际学习

选一个节点，先复述当前解释，再核查材料或代码并预测实验结果。实验前记录硬件、依赖版本、源码 commit、输入、同步与计时方法；重复测量保留原始记录。具体解释与证据逐步补到 topic 主笔记，未运行的方案保持标注。

[返回总地图](../ai-infra-map.md) · [上一章：05](05-cuda-triton-kernels.md) · [下一章：07](07-nccl-model-parallelism.md)
