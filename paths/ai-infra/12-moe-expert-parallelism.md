---
title: '12 · GShard、Switch Transformer 与 DeepSeek MoE'
---

# 12 · GShard、Switch Transformer 与 DeepSeek MoE

从 router 到专家计算，再到跨 GPU token 分发；总参数、激活参数与负载均衡分别讨论。

[完整地图](../ai-infra-map.md) · [课程与论文出处](../ai-infra-sources.md) · [GAPS](../../GAPS.md)

本页是学习导航。节点问题、先修与验证方案由本仓库编排；课程栏链接材料入口，补充节点另行标注。**本章验证均未运行；没有个人掌握度判断或性能实测。**

(ai-12-1)=
## 12.1 Dense FFN → MoE Experts：总参数和每 token 激活参数怎样不同，模型容量怎样连接实际工作量？

- **先修节点**：[01.7 RMSNorm、SwiGLU 与 Residual Connection](01-tokenizer-transformer.md#ai-01-7)、[01.8 GPT/LLaMA 模型配置](01-tokenizer-transformer.md#ai-01-8)
- **课程出处**：**课程拆分**；[S04 · L04 · Mixture of experts (Tatsu)](../ai-infra-sources.md#course-s04)、[M19 · Large models with Mixture-of-Expert](../ai-infra-sources.md#course-m19)。
- **论文与实现**：[Switch Transformers](../ai-infra-sources.md#source-switch)。
- **后续验证（未运行）**：CPU：对教学用 dense/MoE 配置分别计算总参数、激活参数和每 token FLOPs。

(ai-12-2)=
## 12.2 Router 与 Top-k Routing：token 怎样选择 experts，routing weights 怎样参与输出和训练？

- **先修节点**：[12.1 Dense FFN → MoE Experts](12-moe-expert-parallelism.md#ai-12-1)、[02.3 Autograd 与 Backward Graph](02-pytorch-training-step.md#ai-02-3)
- **课程出处**：**课程拆分**；[S04 · L04 · Mixture of experts (Tatsu)](../ai-infra-sources.md#course-s04)、[M19 · Large models with Mixture-of-Expert](../ai-infra-sources.md#course-m19)。
- **论文与实现**：[GShard](../ai-infra-sources.md#source-gshard)、[Switch Transformers](../ai-infra-sources.md#source-switch)。
- **后续验证（未运行）**：CPU：手算 token→expert 分配与合并结果；解释哪些环节有可训练参数。

(ai-12-3)=
## 12.3 Capacity、Token Dropping 与 Dropless MoE：某个 expert 收到过多 token 时，容量规则怎样影响计算与训练？

- **先修节点**：[12.2 Router 与 Top-k Routing](12-moe-expert-parallelism.md#ai-12-2)、[02.7 Gradient Accumulation](02-pytorch-training-step.md#ai-02-7)
- **课程出处**：**课程拆分与工程补充**；[S04 · L04 · Mixture of experts (Tatsu)](../ai-infra-sources.md#course-s04)、[M19 · Large models with Mixture-of-Expert](../ai-infra-sources.md#course-m19)。
- **论文与实现**：[Switch Transformers](../ai-infra-sources.md#source-switch)、[DeepSpeed-MoE](../ai-infra-sources.md#source-dsmoe)。
- **后续验证（未运行）**：CPU：给定不均匀分配，比较 dropping 与 dropless 的工作量和输出语义。

(ai-12-4)=
## 12.4 Load-balancing Loss 与 Router 稳定性：负载、路由偏好与学习目标怎样互相影响，哪些平衡机制属于不同设计？

- **先修节点**：[12.2 Router 与 Top-k Routing](12-moe-expert-parallelism.md#ai-12-2)、[12.3 Capacity、Token Dropping 与 Dropless MoE](12-moe-expert-parallelism.md#ai-12-3)
- **课程出处**：**课程拆分**；[S04 · L04 · Mixture of experts (Tatsu)](../ai-infra-sources.md#course-s04)、[M19 · Large models with Mixture-of-Expert](../ai-infra-sources.md#course-m19)。
- **论文与实现**：[Switch Transformers](../ai-infra-sources.md#source-switch)、[DeepSeek-V3 Technical Report](../ai-infra-sources.md#source-deepseek3)。
- **后续验证（未运行）**：CPU/单 GPU：统计教学 router 的负载，分别观察平衡目标与路由分布；区分辅助 loss 与其他机制。

(ai-12-5)=
## 12.5 GShard / Switch Transformer：两种稀疏设计在 routing、并行和训练稳定性上怎样取舍？

- **先修节点**：[12.2 Router 与 Top-k Routing](12-moe-expert-parallelism.md#ai-12-2)、[12.4 Load-balancing Loss 与 Router 稳定性](12-moe-expert-parallelism.md#ai-12-4)、[07.6 Megatron Tensor Parallelism](07-nccl-model-parallelism.md#ai-07-6)
- **课程出处**：**课程拆分**；[S04 · L04 · Mixture of experts (Tatsu)](../ai-infra-sources.md#course-s04)、[M19 · Large models with Mixture-of-Expert](../ai-infra-sources.md#course-m19)。
- **论文与实现**：[GShard](../ai-infra-sources.md#source-gshard)、[Switch Transformers](../ai-infra-sources.md#source-switch)。
- **后续验证（未运行）**：论文比较：列出 routing、容量、通信和训练条件，不把所有 MoE 当作同一套算法。

(ai-12-6)=
## 12.6 DeepSeek MoE：fine-grained experts 与 shared experts 怎样划分工作，怎样影响计算和路由？

- **先修节点**：[12.1 Dense FFN → MoE Experts](12-moe-expert-parallelism.md#ai-12-1)、[12.2 Router 与 Top-k Routing](12-moe-expert-parallelism.md#ai-12-2)
- **课程出处**：**课程拆分**；[S04 · L04 · Mixture of experts (Tatsu)](../ai-infra-sources.md#course-s04)、[M19 · Large models with Mixture-of-Expert](../ai-infra-sources.md#course-m19)。
- **论文与实现**：[DeepSeekMoE](../ai-infra-sources.md#source-deepseekmoe)。
- **后续验证（未运行）**：CPU/论文阅读：按教学配置画 shared/routed 路径，分别核对参数、激活计算与负载。

(ai-12-7)=
## 12.7 Expert Parallelism 与 AllToAll：dispatch/combine 如何把 token 发到 expert 所在设备，又怎样还原顺序？

- **先修节点**：[12.2 Router 与 Top-k Routing](12-moe-expert-parallelism.md#ai-12-2)、[07.1 Send/Recv 与 Collective Communication](07-nccl-model-parallelism.md#ai-07-1)、[07.2 AllReduce、ReduceScatter 与 AllGather](07-nccl-model-parallelism.md#ai-07-2)
- **课程出处**：**课程拆分与工程补充**；[M19 · Large models with Mixture-of-Expert](../ai-infra-sources.md#course-m19)、[S07 · L07 · Parallelism (Tatsu)](../ai-infra-sources.md#course-s07)。
- **论文与实现**：[DeepSpeed-MoE](../ai-infra-sources.md#source-dsmoe)、[Megatron Core](../ai-infra-sources.md#source-mcore)。
- **后续验证（未运行）**：CPU 示意/多 GPU：使用唯一 token ID 追踪分发与合并，检查逆置换与通信流量。

(ai-12-8)=
## 12.8 Grouped GEMM 与 MoE Kernel：不等长 expert batches 怎样组成矩阵计算，什么时候会有小 GEMM 与 padding 成本？

- **先修节点**：[12.3 Capacity、Token Dropping 与 Dropless MoE](12-moe-expert-parallelism.md#ai-12-3)、[12.7 Expert Parallelism 与 AllToAll](12-moe-expert-parallelism.md#ai-12-7)、[05.6 Tensor Core GEMM](05-cuda-triton-kernels.md#ai-05-6)
- **课程出处**：**工程补充**；[S04 · L04 · Mixture of experts (Tatsu)](../ai-infra-sources.md#course-s04)、[M19 · Large models with Mixture-of-Expert](../ai-infra-sources.md#course-m19)。
- **论文与实现**：[NVIDIA CUTLASS](../ai-infra-sources.md#source-cutlass)、[Megatron Core](../ai-infra-sources.md#source-mcore)。
- **后续验证（未运行）**：单 GPU：固定 routing 分布，比较 grouped 与逐 expert 计算的数值和时间。

(ai-12-9)=
## 12.9 DeepSpeed-MoE / DeepSeek-V3：一套完整 MoE 系统怎样组合专家结构、负载均衡、并行与通信？

- **先修节点**：[12.5 GShard / Switch Transformer](12-moe-expert-parallelism.md#ai-12-5)、[12.6 DeepSeek MoE](12-moe-expert-parallelism.md#ai-12-6)、[12.7 Expert Parallelism 与 AllToAll](12-moe-expert-parallelism.md#ai-12-7)、[07.11 DP×TP×PP 组合与 Rank Placement](07-nccl-model-parallelism.md#ai-07-11)
- **课程出处**：**课程拆分与论文补充**；[M19 · Large models with Mixture-of-Expert](../ai-infra-sources.md#course-m19)、[MDEEP · Deepseek V3 and R1](../ai-infra-sources.md#course-mdeep)。
- **论文与实现**：[DeepSpeed-MoE](../ai-infra-sources.md#source-dsmoe)、[DeepSeek-V3 Technical Report](../ai-infra-sources.md#source-deepseek3)、[DeepSpeed MoE](../ai-infra-sources.md#source-ds-moe-code)。
- **后续验证（未运行）**：代码/报告阅读：沿 token 路径画一张系统图，注明具体版本；大规模结果只作来源结论。

## 回到实际学习

选一个节点，先复述当前解释，再核查材料或代码并预测实验结果。实验前记录硬件、依赖版本、源码 commit、输入、同步与计时方法；重复测量保留原始记录。具体解释与证据逐步补到 topic 主笔记，未运行的方案保持标注。

[返回总地图](../ai-infra-map.md) · [上一章：11](11-vllm-serving.md) · [下一章：13](13-scaling-evaluation.md)
