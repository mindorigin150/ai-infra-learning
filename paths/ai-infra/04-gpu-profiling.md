---
title: '04 · GPU SM、Warp、显存与性能测量'
---

# 04 · GPU SM、Warp、显存与性能测量

建立能解释 kernel 的 GPU 执行视图，并明确测量的硬件、输入与同步前提。

[完整地图](../ai-infra-map.md) · [课程与论文出处](../ai-infra-sources.md) · [GAPS](../../GAPS.md)

本页是学习导航。节点问题、先修与验证方案由本仓库编排；课程栏链接材料入口，补充节点另行标注。**本章验证均未运行；没有个人掌握度判断或性能实测。**

(ai-04-1)=
## 04.1 Grid、Block、Thread 与 Warp：一个 kernel 的逻辑线程怎样对应输入元素与硬件执行单元？

- **先修节点**：本图入口；学习时按问题诊断必要的基础。
- **课程出处**：**课程拆分**；[S05 · L05 · GPUs (Tatsu)](../ai-infra-sources.md#course-s05)、[M02 · GPU Programming Basics 1](../ai-infra-sources.md#course-m02)、[M03 · GPU Programming Basics 2](../ai-infra-sources.md#course-m03)。
- **论文与实现**：[CUDA Programming Guide](../ai-infra-sources.md#source-cuda)。
- **后续验证（未运行）**：复述/CPU：画出教学用 grid 与线程索引，检查尾部元素覆盖；运行留到单 GPU 环境。

(ai-04-2)=
## 04.2 SM、Warp Scheduler 与 SIMT：SM 怎样执行 warp，分支与依赖会怎样影响有效执行？

- **先修节点**：[04.1 Grid、Block、Thread 与 Warp](04-gpu-profiling.md#ai-04-1)
- **课程出处**：**课程拆分**；[S05 · L05 · GPUs (Tatsu)](../ai-infra-sources.md#course-s05)、[M02 · GPU Programming Basics 1](../ai-infra-sources.md#course-m02)、[M03 · GPU Programming Basics 2](../ai-infra-sources.md#course-m03)。
- **论文与实现**：[CUDA Programming Guide](../ai-infra-sources.md#source-cuda)、[CUDA Best Practices](../ai-infra-sources.md#source-cuda-best)。
- **后续验证（未运行）**：复述/单 GPU：预测不同分支布局的有效工作，再结合 profiler 解释观察。

(ai-04-3)=
## 04.3 Registers、Shared Memory、L2 与 HBM：kernel 的数据和状态分别占用哪些内存层级？

- **先修节点**：[04.2 SM、Warp Scheduler 与 SIMT](04-gpu-profiling.md#ai-04-2)
- **课程出处**：**课程拆分**；[S05 · L05 · GPUs (Tatsu)](../ai-infra-sources.md#course-s05)、[M03 · GPU Programming Basics 2](../ai-infra-sources.md#course-m03)、[M10 · GPU Acceleration](../ai-infra-sources.md#course-m10)。
- **论文与实现**：[CUDA Programming Guide](../ai-infra-sources.md#source-cuda)、[CUDA Best Practices](../ai-infra-sources.md#source-cuda-best)。
- **后续验证（未运行）**：复述：标注 GEMM/向量操作的数据路径；区分模型估算流量与实际硬件流量。

(ai-04-4)=
## 04.4 Tensor Cores 与矩阵乘法指令：dtype、矩阵布局与形状怎样限制矩阵指令的使用？

- **先修节点**：[04.2 SM、Warp Scheduler 与 SIMT](04-gpu-profiling.md#ai-04-2)、[02.8 FP32、FP16、BF16 与 AMP](02-pytorch-training-step.md#ai-02-8)
- **课程出处**：**课程拆分**；[S05 · L05 · GPUs (Tatsu)](../ai-infra-sources.md#course-s05)、[M10 · GPU Acceleration](../ai-infra-sources.md#course-m10)。
- **论文与实现**：[NVIDIA CUTLASS](../ai-infra-sources.md#source-cutlass)、[CUDA Programming Guide](../ai-infra-sources.md#source-cuda)。
- **后续验证（未运行）**：单 GPU：记录型号与支持格式，比较适配与不适配 shapes 的执行证据。

(ai-04-5)=
## 04.5 Coalesced Access 与 Memory Layout：相邻线程访问怎样形成内存事务，stride 会增加什么成本？

- **先修节点**：[04.1 Grid、Block、Thread 与 Warp](04-gpu-profiling.md#ai-04-1)、[04.3 Registers、Shared Memory、L2 与 HBM](04-gpu-profiling.md#ai-04-3)、[02.1 Tensor Storage、Stride、View 与 Contiguous](02-pytorch-training-step.md#ai-02-1)
- **课程出处**：**课程拆分**；[M03 · GPU Programming Basics 2](../ai-infra-sources.md#course-m03)、[M10 · GPU Acceleration](../ai-infra-sources.md#course-m10)。
- **论文与实现**：[CUDA Best Practices](../ai-infra-sources.md#source-cuda-best)。
- **后续验证（未运行）**：单 GPU：比较连续与跨步访问，记录 useful bytes、时间与计数器，控制缓存影响。

(ai-04-6)=
## 04.6 Occupancy、寄存器压力与 Latency Hiding：为什么更多线程或更高 occupancy 不必然得到更快的 kernel？

- **先修节点**：[04.2 SM、Warp Scheduler 与 SIMT](04-gpu-profiling.md#ai-04-2)、[04.3 Registers、Shared Memory、L2 与 HBM](04-gpu-profiling.md#ai-04-3)
- **课程出处**：**课程拆分**；[S05 · L05 · GPUs (Tatsu)](../ai-infra-sources.md#course-s05)、[M10 · GPU Acceleration](../ai-infra-sources.md#course-m10)。
- **论文与实现**：[CUDA Best Practices](../ai-infra-sources.md#source-cuda-best)、[Nsight Compute Profiling Guide](../ai-infra-sources.md#source-ncu)。
- **后续验证（未运行）**：单 GPU：改变 block 大小，记录寄存器、occupancy 和耗时，解释资源限制。

(ai-04-7)=
## 04.7 FLOPs、Bytes、Arithmetic Intensity 与 Roofline：一个操作的上界怎样估算，哪些实际成本被模型省略？

- **先修节点**：[01.5 Causal Attention、Q/K/V 与 Multi-head Attention](01-tokenizer-transformer.md#ai-01-5)、[04.3 Registers、Shared Memory、L2 与 HBM](04-gpu-profiling.md#ai-04-3)
- **课程出处**：**课程拆分**；[S02 · L02 · PyTorch, resource accounting (Percy)](../ai-infra-sources.md#course-s02)、[S05 · L05 · GPUs (Tatsu)](../ai-infra-sources.md#course-s05)。
- **论文与实现**：[Roofline performance model](../ai-infra-sources.md#source-roofline)。
- **后续验证（未运行）**：CPU/复述：连接仓库性能模型示例，为向量与 GEMM 估算强度，列出简化假设。

(ai-04-8)=
## 04.8 CUDA Events、Warmup 与 Synchronization：怎样区分提交开销、GPU 执行时间和端到端时间？

- **先修节点**：[04.1 Grid、Block、Thread 与 Warp](04-gpu-profiling.md#ai-04-1)
- **课程出处**：**课程拆分**；[S06 · L06 · Kernels, Triton (Tatsu)](../ai-infra-sources.md#course-s06)。
- **论文与实现**：[CUDA Best Practices](../ai-infra-sources.md#source-cuda-best)、[PyTorch performance tuning](../ai-infra-sources.md#source-tuning)。
- **后续验证（未运行）**：单 GPU：比较主机计时与 event 计时，先预测未同步的偏差，再预热与重复测量。

(ai-04-9)=
## 04.9 PyTorch Profiler、Nsight Systems 与 Nsight Compute：算子时间、系统 timeline 与 kernel 指标分别帮助排查什么？

- **先修节点**：[04.7 FLOPs、Bytes、Arithmetic Intensity 与 Roofline](04-gpu-profiling.md#ai-04-7)、[04.8 CUDA Events、Warmup 与 Synchronization](04-gpu-profiling.md#ai-04-8)
- **课程出处**：**工程补充**；[S06 · L06 · Kernels, Triton (Tatsu)](../ai-infra-sources.md#course-s06)。
- **论文与实现**：[Nsight Systems](../ai-infra-sources.md#source-nsys)、[Nsight Compute Profiling Guide](../ai-infra-sources.md#source-ncu)、[PyTorch performance tuning](../ai-infra-sources.md#source-tuning)。
- **后续验证（未运行）**：单 GPU：对同一短训练步骤生成三种观察，说明各工具能证实或无法证实的判断。

## 回到实际学习

选一个节点，先复述当前解释，再核查材料或代码并预测实验结果。实验前记录硬件、依赖版本、源码 commit、输入、同步与计时方法；重复测量保留原始记录。具体解释与证据逐步补到 topic 主笔记，未运行的方案保持标注。

[返回总地图](../ai-infra-map.md) · [上一章：03](03-data-sequence-packing.md) · [下一章：05](05-cuda-triton-kernels.md)
