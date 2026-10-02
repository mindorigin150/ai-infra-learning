---
title: 训练目标与评估
---

# 训练目标与评估

优化的目标是什么，预算与数据怎样影响学习，怎样验证模型质量？

[主题索引](../README.md) · [开始一次学习](../../paths/start-here.md)

## 分类边界

算法目标与指标在这里；后训练中角色部署、流水线和策略版本连接分布式运行时。

## Topic 与材料入口

下表按机制归类已有材料节点。材料页保留具体问题、先修与来源；主笔记在实际学习后逐步展开。条目不表示个人掌握度。

| Topic | 要解释的问题 | 材料入口 |
| --- | --- | --- |
| Cross-entropy 与 Next-token Prediction | 输入、标签移位、padding 与 loss mask 怎样定义训练目标？ | [02.5](../../paths/ai-infra/02-pytorch-training-step.md#ai-02-5) |
| Kaplan Scaling Laws | 怎样从不同规模训练的 loss 观察趋势，拟合与外推依赖什么前提？ | [13.2](../../paths/ai-infra/13-scaling-evaluation.md#ai-13-2) |
| Chinchilla | 固定计算预算时，模型大小与训练 token 数怎样共同选择？ | [13.3](../../paths/ai-infra/13-scaling-evaluation.md#ai-13-3) |
| Learning Rate、Batch Size 与训练长度 | 硬件吞吐、更新次数和收敛怎样共同影响训练配置？ | [13.4](../../paths/ai-infra/13-scaling-evaluation.md#ai-13-4) |
| Loss、Perplexity 与 Downstream Evaluation | 语言建模 loss 与下游任务指标分别评价什么，评估过程怎样复现？ | [13.5](../../paths/ai-infra/13-scaling-evaluation.md#ai-13-5) |
| Benchmark Contamination 与数据泄漏 | 训练、验证与评估数据中的重复或信息泄漏怎样影响结论？ | [13.6](../../paths/ai-infra/13-scaling-evaluation.md#ai-13-6) |
| SFT | instruction、chat template 与 loss mask 怎样定义一次监督微调？ | [14.1](../../paths/ai-infra/14-post-training-rlhf.md#ai-14-1) |
| Preference Data 与 Reward Model | 偏好对、评分与 reward 的含义是什么，数据怎样进入训练？ | [14.2](../../paths/ai-infra/14-post-training-rlhf.md#ai-14-2) |
| DPO | policy/reference 怎样参与偏好目标，与 reward-model-based 流程有何不同？ | [14.3](../../paths/ai-infra/14-post-training-rlhf.md#ai-14-3) |
| PPO / InstructGPT | rollout、reward、value 与 policy update 怎样组成一轮优化？ | [14.4](../../paths/ai-infra/14-post-training-rlhf.md#ai-14-4) |
| GRPO / RLVR | group sampling、优势估计与可验证奖励怎样连接，GRPO 与 RLVR 为何不是同义词？ | [14.5](../../paths/ai-infra/14-post-training-rlhf.md#ai-14-5) |

关联分类：[数据组织与流水线](../data-pipelines/README.md) · [分布式运行时与资源编排](../distributed-runtime/README.md) · [性能模型与观测](../performance/README.md)。
