---
title: 数据组织与流水线
---

# 数据组织与流水线

样本怎样经过处理、采样、组合与搬运，成为模型消费的输入？

[主题索引](../README.md) · [开始一次学习](../../paths/start-here.md)

## 分类边界

Tokenizer 算法的主位置在模型表示；这里关注数据中的使用方式、样本边界和输入吞吐。

## Topic 与材料入口

下表按机制归类已有材料节点。材料页保留具体问题、先修与来源；主笔记在实际学习后逐步展开。条目不表示个人掌握度。

| Topic | 要解释的问题 | 材料入口 |
| --- | --- | --- |
| 文本清洗、质量过滤与去重 | 哪些预处理改变训练分布，哪些重复可能影响数据划分与评估？ | [03.1](../../paths/ai-infra/03-data-sequence-packing.md#ai-03-1) |
| 数据混合与 Sampling | 不同数据来源如何进入训练，抽样比例与实际 token 比例为何可能不同？ | [03.2](../../paths/ai-infra/03-data-sequence-packing.md#ai-03-2) |
| Tokenization、Dataset Sharding 与 DataLoader | 原始文本怎样成为各 worker 消费的 token batch，哪里可能重读或漏读？ | [03.3](../../paths/ai-infra/03-data-sequence-packing.md#ai-03-3) |
| Padding、Length Bucketing 与有效 Token 比例 | 按长度组织 batch 能减少哪些浪费，又可能改变什么采样行为？ | [03.4](../../paths/ai-infra/03-data-sequence-packing.md#ai-03-4) |
| Sequence Packing | 拼接样本以后，哪些 attention、位置与 loss 规则必须由任务明确？ | [03.5](../../paths/ai-infra/03-data-sequence-packing.md#ai-03-5) |
| Packed Attention Mask、Position IDs 与 Loss Mask | 独立样本的边界怎样同时体现在 attention、位置和监督目标中？ | [03.6](../../paths/ai-infra/03-data-sequence-packing.md#ai-03-6) |
| Variable-length Attention 与 cu_seqlens | 每条序列的边界怎样传给 varlen kernel，和固定长度的 packed QKV 接口有何区别？ | [03.7](../../paths/ai-infra/03-data-sequence-packing.md#ai-03-7) |
| 数据读取、Prefetch 与 CPU→GPU Copy | GPU 等待数据时，瓶颈在读取、处理、拷贝还是同步？ | [03.8](../../paths/ai-infra/03-data-sequence-packing.md#ai-03-8) |
| 多模态 Sequence Packing | text/image/video 的边界、attention mask、position 与不同 loss 怎样放进一个 batch？ | [15.5](../../paths/ai-infra/15-multimodal-bagel.md#ai-15-5) |

关联分类：[模型表示与生成机制](../models/README.md) · [张量计算与自动微分](../tensor-autograd/README.md) · [性能模型与观测](../performance/README.md)。
