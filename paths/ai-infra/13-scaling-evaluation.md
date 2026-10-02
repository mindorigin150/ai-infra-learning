---
title: '13 · Scaling Laws、Chinchilla 与模型评估'
---

# 13 · Scaling Laws、Chinchilla 与模型评估

把训练预算、模型质量和测量目标连接起来；历史 scaling 关系是带条件的经验规律。

[完整地图](../ai-infra-map.md) · [课程与论文出处](../ai-infra-sources.md) · [GAPS](../../GAPS.md)

本页是学习导航。节点问题、先修与验证方案由本仓库编排；课程栏链接材料入口，补充节点另行标注。**本章验证均未运行；没有个人掌握度判断或性能实测。**

(ai-13-1)=
## 13.1 参数量、Token 数与训练 FLOPs：训练预算怎样随架构、输入长度和有效 token 数变化？

- **先修节点**：[01.8 GPT/LLaMA 模型配置](01-tokenizer-transformer.md#ai-01-8)、[04.7 FLOPs、Bytes、Arithmetic Intensity 与 Roofline](04-gpu-profiling.md#ai-04-7)、[03.4 Padding、Length Bucketing 与有效 Token 比例](03-data-sequence-packing.md#ai-03-4)
- **课程出处**：**课程拆分**；[S02 · L02 · PyTorch, resource accounting (Percy)](../ai-infra-sources.md#course-s02)、[S09 · L09 · Scaling laws (Tatsu)](../ai-infra-sources.md#course-s09)。
- **论文与实现**：[Scaling Laws for Neural Language Models](../ai-infra-sources.md#source-kaplan)。
- **后续验证（未运行）**：CPU：对教学用配置核算参数与计算，列出 Attention、padding 和 backward 的假设。

(ai-13-2)=
## 13.2 Kaplan Scaling Laws：怎样从不同规模训练的 loss 观察趋势，拟合与外推依赖什么前提？

- **先修节点**：[13.1 参数量、Token 数与训练 FLOPs](13-scaling-evaluation.md#ai-13-1)、[02.5 Cross-entropy 与 Next-token Prediction](02-pytorch-training-step.md#ai-02-5)
- **课程出处**：**课程拆分**；[S09 · L09 · Scaling laws (Tatsu)](../ai-infra-sources.md#course-s09)。
- **论文与实现**：[Scaling Laws for Neural Language Models](../ai-infra-sources.md#source-kaplan)。
- **后续验证（未运行）**：CPU/已有公开数据：比较拟合范围与外推，不把教学参数或来源结果当作本机实测。

(ai-13-3)=
## 13.3 Chinchilla：固定计算预算时，模型大小与训练 token 数怎样共同选择？

- **先修节点**：[13.2 Kaplan Scaling Laws](13-scaling-evaluation.md#ai-13-2)
- **课程出处**：**课程拆分**；[S11 · L11 · Scaling laws (Tatsu)](../ai-infra-sources.md#course-s11)。
- **论文与实现**：[Training Compute-Optimal Large Language Models / Chinchilla](../ai-infra-sources.md#source-chinchilla)。
- **后续验证（未运行）**：CPU 模型：改变教学用预算和假设，说明与 Kaplan 配方差异，不直接套固定比例。

(ai-13-4)=
## 13.4 Learning Rate、Batch Size 与训练长度：硬件吞吐、更新次数和收敛怎样共同影响训练配置？

- **先修节点**：[02.6 AdamW](02-pytorch-training-step.md#ai-02-6)、[02.7 Gradient Accumulation](02-pytorch-training-step.md#ai-02-7)、[13.1 参数量、Token 数与训练 FLOPs](13-scaling-evaluation.md#ai-13-1)
- **课程出处**：**课程拆分**；[S03 · L03 · Architectures, hyperparameters (Tatsu)](../ai-infra-sources.md#course-s03)、[S09 · L09 · Scaling laws (Tatsu)](../ai-infra-sources.md#course-s09)、[S11 · L11 · Scaling laws (Tatsu)](../ai-infra-sources.md#course-s11)。
- **论文与实现**：[Scaling Laws for Neural Language Models](../ai-infra-sources.md#source-kaplan)、[Training Compute-Optimal Large Language Models / Chinchilla](../ai-infra-sources.md#source-chinchilla)。
- **后续验证（未运行）**：CPU/单 GPU 小模型：一次改变一个条件，记录 loss、有效 token 与 time-to-quality。

(ai-13-5)=
## 13.5 Loss、Perplexity 与 Downstream Evaluation：语言建模 loss 与下游任务指标分别评价什么，评估过程怎样复现？

- **先修节点**：[02.5 Cross-entropy 与 Next-token Prediction](02-pytorch-training-step.md#ai-02-5)、[10.1 Greedy、Temperature、Top-k、Top-p 与 Beam Search](10-kv-cache-decoding.md#ai-10-1)
- **课程出处**：**课程拆分**；[S12 · L12 · Evaluation (Percy)](../ai-infra-sources.md#course-s12)。
- **论文与实现**：[LLaMA](../ai-infra-sources.md#source-llama)。
- **后续验证（未运行）**：CPU/已有模型：明确 tokenizer、prompt、样本与评分规则，再比较两个评价指标。

(ai-13-6)=
## 13.6 Benchmark Contamination 与数据泄漏：训练、验证与评估数据中的重复或信息泄漏怎样影响结论？

- **先修节点**：[03.1 文本清洗、质量过滤与去重](03-data-sequence-packing.md#ai-03-1)、[13.5 Loss、Perplexity 与 Downstream Evaluation](13-scaling-evaluation.md#ai-13-5)
- **课程出处**：**课程拆分**；[S12 · L12 · Evaluation (Percy)](../ai-infra-sources.md#course-s12)、[S14 · L14 · Data (Percy)](../ai-infra-sources.md#course-s14)。
- **论文与实现**：[LLaMA](../ai-infra-sources.md#source-llama)。
- **后续验证（未运行）**：CPU：用教学用重叠数据检查污染路径；记录可发现的重复与无法确定的污染。

(ai-13-7)=
## 13.7 MFU 与 Time-to-quality：模型 FLOPs 利用率和达到目标质量的时间为什么是不同指标？

- **先修节点**：[13.1 参数量、Token 数与训练 FLOPs](13-scaling-evaluation.md#ai-13-1)、[13.4 Learning Rate、Batch Size 与训练长度](13-scaling-evaluation.md#ai-13-4)、[04.8 CUDA Events、Warmup 与 Synchronization](04-gpu-profiling.md#ai-04-8)
- **课程出处**：**工程补充**；[S02 · L02 · PyTorch, resource accounting (Percy)](../ai-infra-sources.md#course-s02)、[S09 · L09 · Scaling laws (Tatsu)](../ai-infra-sources.md#course-s09)、[S11 · L11 · Scaling laws (Tatsu)](../ai-infra-sources.md#course-s11)。
- **论文与实现**：[Efficient Large-Scale Language Model Training Using Megatron-LM](../ai-infra-sources.md#source-megatron-scale)。
- **后续验证（未运行）**：单 GPU/多 GPU：声明 FLOPs 分子、硬件峰值与计时口径，同时记录质量阈值和训练时间。

## 回到实际学习

选一个节点，先复述当前解释，再核查材料或代码并预测实验结果。实验前记录硬件、依赖版本、源码 commit、输入、同步与计时方法；重复测量保留原始记录。具体解释与证据逐步补到 topic 主笔记，未运行的方案保持标注。

[返回总地图](../ai-infra-map.md) · [上一章：12](12-moe-expert-parallelism.md) · [下一章：14](14-post-training-rlhf.md)
