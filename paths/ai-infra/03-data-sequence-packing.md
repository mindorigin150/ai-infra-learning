---
title: '03 · 预训练数据、Padding 与 Sequence Packing'
---

# 03 · 预训练数据、Padding 与 Sequence Packing

把数据质量、batch 组织和 Attention/loss 语义接起来；packing 的语义由任务定义。

[完整地图](../ai-infra-map.md) · [课程与论文出处](../ai-infra-sources.md) · [GAPS](../../GAPS.md)

本页是学习导航。节点问题、先修与验证方案由本仓库编排；课程栏链接材料入口，补充节点另行标注。**本章验证均未运行；没有个人掌握度判断或性能实测。**

(ai-03-1)=
## 03.1 文本清洗、质量过滤与去重：哪些预处理改变训练分布，哪些重复可能影响数据划分与评估？

- **先修节点**：[01.1 Byte-level BPE](01-tokenizer-transformer.md#ai-01-1)
- **课程出处**：**课程拆分**；[S13 · L13 · Data (Percy)](../ai-infra-sources.md#course-s13)、[S14 · L14 · Data (Percy)](../ai-infra-sources.md#course-s14)。
- **论文与实现**：[Transformers tokenizers](../ai-infra-sources.md#source-hf-tokenizer)。
- **后续验证（未运行）**：CPU：对小样本文本做过滤与去重，保存每一步留下和删除的样本及理由。

(ai-03-2)=
## 03.2 数据混合与 Sampling：不同数据来源如何进入训练，抽样比例与实际 token 比例为何可能不同？

- **先修节点**：[03.1 文本清洗、质量过滤与去重](03-data-sequence-packing.md#ai-03-1)
- **课程出处**：**课程拆分**；[S13 · L13 · Data (Percy)](../ai-infra-sources.md#course-s13)、[S14 · L14 · Data (Percy)](../ai-infra-sources.md#course-s14)。
- **论文与实现**：[Transformers tokenizers](../ai-infra-sources.md#source-hf-tokenizer)。
- **后续验证（未运行）**：CPU：在长度不同的教学样本上比较按样本和按 token 混合，核对随机种子与统计。

(ai-03-3)=
## 03.3 Tokenization、Dataset Sharding 与 DataLoader：原始文本怎样成为各 worker 消费的 token batch，哪里可能重读或漏读？

- **先修节点**：[01.1 Byte-level BPE](01-tokenizer-transformer.md#ai-01-1)、[03.2 数据混合与 Sampling](03-data-sequence-packing.md#ai-03-2)
- **课程出处**：**工程补充**；[S13 · L13 · Data (Percy)](../ai-infra-sources.md#course-s13)、[S14 · L14 · Data (Percy)](../ai-infra-sources.md#course-s14)。
- **论文与实现**：[PyTorch performance tuning](../ai-infra-sources.md#source-tuning)。
- **后续验证（未运行）**：CPU：用带唯一 ID 的小数据集追踪 sharding 与 worker 输出，检查覆盖和顺序。

(ai-03-4)=
## 03.4 Padding、Length Bucketing 与有效 Token 比例：按长度组织 batch 能减少哪些浪费，又可能改变什么采样行为？

- **先修节点**：[03.3 Tokenization、Dataset Sharding 与 DataLoader](03-data-sequence-packing.md#ai-03-3)、[02.5 Cross-entropy 与 Next-token Prediction](02-pytorch-training-step.md#ai-02-5)
- **课程出处**：**工程补充**；[S02 · L02 · PyTorch, resource accounting (Percy)](../ai-infra-sources.md#course-s02)、[S14 · L14 · Data (Percy)](../ai-infra-sources.md#course-s14)。
- **论文与实现**：[PyTorch performance tuning](../ai-infra-sources.md#source-tuning)。
- **后续验证（未运行）**：CPU：对同一长度列表比较 batching 方案，计算有效 token 比例，不推断 GPU 加速倍数。

(ai-03-5)=
## 03.5 Sequence Packing：拼接样本以后，哪些 attention、位置与 loss 规则必须由任务明确？

- **先修节点**：[03.4 Padding、Length Bucketing 与有效 Token 比例](03-data-sequence-packing.md#ai-03-4)、[01.5 Causal Attention、Q/K/V 与 Multi-head Attention](01-tokenizer-transformer.md#ai-01-5)、[02.5 Cross-entropy 与 Next-token Prediction](02-pytorch-training-step.md#ai-02-5)
- **课程出处**：**工程补充**；[S14 · L14 · Data (Percy)](../ai-infra-sources.md#course-s14)。
- **论文与实现**：[FlashAttention implementation](../ai-infra-sources.md#source-fa-code)、[BAGEL implementation](../ai-infra-sources.md#source-bagel)。
- **后续验证（未运行）**：CPU：画出两个样本拼接后的 token 布局，分别声明允许跨样本访问或需要隔离的任务语义。

(ai-03-6)=
## 03.6 Packed Attention Mask、Position IDs 与 Loss Mask：独立样本的边界怎样同时体现在 attention、位置和监督目标中？

- **先修节点**：[03.5 Sequence Packing](03-data-sequence-packing.md#ai-03-5)、[01.6 RoPE 与位置编码](01-tokenizer-transformer.md#ai-01-6)
- **课程出处**：**工程补充**；[M06 · Transformer](../ai-infra-sources.md#course-m06)。
- **论文与实现**：[FlashAttention implementation](../ai-infra-sources.md#source-fa-code)、[BAGEL implementation](../ai-infra-sources.md#source-bagel)。
- **后续验证（未运行）**：CPU：按独立样本语义比较单独计算与 packed 计算；检查边界标签、位置与 loss 权重。

(ai-03-7)=
## 03.7 Variable-length Attention 与 cu_seqlens：每条序列的边界怎样传给 varlen kernel，和固定长度的 packed QKV 接口有何区别？

- **先修节点**：[03.6 Packed Attention Mask、Position IDs 与 Loss Mask](03-data-sequence-packing.md#ai-03-6)、[04.1 Grid、Block、Thread 与 Warp](04-gpu-profiling.md#ai-04-1)
- **课程出处**：**工程补充**；[M20 · Optimizing Attention for Modern Hardware (Tri Dao)](../ai-infra-sources.md#course-m20)。
- **论文与实现**：[FlashAttention implementation](../ai-infra-sources.md#source-fa-code)。
- **后续验证（未运行）**：CPU/单 GPU：先手算 cu_seqlens；GPU 上再比较 varlen 与逐条 attention 的数值结果。

(ai-03-8)=
## 03.8 数据读取、Prefetch 与 CPU→GPU Copy：GPU 等待数据时，瓶颈在读取、处理、拷贝还是同步？

- **先修节点**：[03.3 Tokenization、Dataset Sharding 与 DataLoader](03-data-sequence-packing.md#ai-03-3)、[04.8 CUDA Events、Warmup 与 Synchronization](04-gpu-profiling.md#ai-04-8)
- **课程出处**：**工程补充**；[S06 · L06 · Kernels, Triton (Tatsu)](../ai-infra-sources.md#course-s06)。
- **论文与实现**：[PyTorch performance tuning](../ai-infra-sources.md#source-tuning)、[Nsight Systems](../ai-infra-sources.md#source-nsys)。
- **后续验证（未运行）**：单 GPU：用 timeline 区分读取与拷贝阶段；一次只改 worker/prefetch/拷贝设置并记录环境。

## 回到实际学习

选一个节点，先复述当前解释，再核查材料或代码并预测实验结果。实验前记录硬件、依赖版本、源码 commit、输入、同步与计时方法；重复测量保留原始记录。具体解释与证据逐步补到 topic 主笔记，未运行的方案保持标注。

[返回总地图](../ai-infra-map.md) · [上一章：02](02-pytorch-training-step.md) · [下一章：04](04-gpu-profiling.md)
