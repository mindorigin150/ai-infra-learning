---
title: '10 · Prefill、Decode、KV Cache 与长上下文'
---

# 10 · Prefill、Decode、KV Cache 与长上下文

从 token 选择和两阶段执行理解 KV 生命周期，再连接 head 结构与长上下文。

[完整地图](../ai-infra-map.md) · [课程与论文出处](../ai-infra-sources.md) · [GAPS](../../GAPS.md)

本页是学习导航。节点问题、先修与验证方案由本仓库编排；课程栏链接材料入口，补充节点另行标注。**本章验证均未运行；没有个人掌握度判断或性能实测。**

(ai-10-1)=
## 10.1 Greedy、Temperature、Top-k、Top-p 与 Beam Search：不同策略怎样选择 token，怎样影响生成状态与结果？

- **先修节点**：[01.3 Special Tokens、BOS/EOS 与 Chat Template](01-tokenizer-transformer.md#ai-01-3)、[02.5 Cross-entropy 与 Next-token Prediction](02-pytorch-training-step.md#ai-02-5)
- **课程出处**：**课程拆分**；[M09 · LLM Decoding](../ai-infra-sources.md#course-m09)、[S10 · L10 · Inference (Percy)](../ai-infra-sources.md#course-s10)。
- **论文与实现**：[Attention Is All You Need](../ai-infra-sources.md#source-transformer)、[LLaMA](../ai-infra-sources.md#source-llama)。
- **后续验证（未运行）**：CPU：给定教学 logits 和随机种子手算采样；比较策略并追踪 beam 状态。

(ai-10-2)=
## 10.2 Prefill 与 Decode：两阶段的输入、可并行工作和瓶颈怎样随 batch、长度和硬件改变？

- **先修节点**：[01.5 Causal Attention、Q/K/V 与 Multi-head Attention](01-tokenizer-transformer.md#ai-01-5)、[10.1 Greedy、Temperature、Top-k、Top-p 与 Beam Search](10-kv-cache-decoding.md#ai-10-1)、[04.7 FLOPs、Bytes、Arithmetic Intensity 与 Roofline](04-gpu-profiling.md#ai-04-7)
- **课程出处**：**课程拆分**；[S10 · L10 · Inference (Percy)](../ai-infra-sources.md#course-s10)、[M22 · LLM Serving with PageAttention (Woosuk Kwon)](../ai-infra-sources.md#course-m22)。
- **论文与实现**：[PagedAttention / vLLM](../ai-infra-sources.md#source-paged)、[vLLM architecture](../ai-infra-sources.md#source-vllm)。
- **后续验证（未运行）**：CPU 估算/单 GPU：分别计时两阶段并改变输入条件，不把 compute/memory-bound 当成无条件结论。

(ai-10-3)=
## 10.3 KV Cache：缓存哪些历史表示，追加 token 时哪些内容复用、哪些重新计算？

- **先修节点**：[10.2 Prefill 与 Decode](10-kv-cache-decoding.md#ai-10-2)
- **课程出处**：**课程拆分**；[S10 · L10 · Inference (Percy)](../ai-infra-sources.md#course-s10)、[M22 · LLM Serving with PageAttention (Woosuk Kwon)](../ai-infra-sources.md#course-m22)、[M23 · Better KV Cache for LLM Serving (Yuhan Liu)](../ai-infra-sources.md#course-m23)。
- **论文与实现**：[PagedAttention / vLLM](../ai-infra-sources.md#source-paged)、[vLLM architecture](../ai-infra-sources.md#source-vllm)。
- **后续验证（未运行）**：CPU/单 GPU：比较带 cache 与全序列重算的输出，画每层 KV 的追加过程。

(ai-10-4)=
## 10.4 KV Cache 显存估算：层数、KV heads、head dimension、长度、batch 与 dtype 怎样决定缓存容量？

- **先修节点**：[10.3 KV Cache](10-kv-cache-decoding.md#ai-10-3)、[02.8 FP32、FP16、BF16 与 AMP](02-pytorch-training-step.md#ai-02-8)
- **课程出处**：**课程拆分**；[S10 · L10 · Inference (Percy)](../ai-infra-sources.md#course-s10)、[M22 · LLM Serving with PageAttention (Woosuk Kwon)](../ai-infra-sources.md#course-m22)。
- **论文与实现**：[PagedAttention / vLLM](../ai-infra-sources.md#source-paged)。
- **后续验证（未运行）**：CPU：用教学配置手算有效 KV bytes；再区分 allocator/block/临时缓冲区开销。

(ai-10-5)=
## 10.5 MHA → MQA → GQA：减少 KV head 数怎样影响共享关系、缓存容量与 Attention 计算？

- **先修节点**：[10.4 KV Cache 显存估算](10-kv-cache-decoding.md#ai-10-4)、[01.5 Causal Attention、Q/K/V 与 Multi-head Attention](01-tokenizer-transformer.md#ai-01-5)
- **课程出处**：**论文补充**；[S03 · L03 · Architectures, hyperparameters (Tatsu)](../ai-infra-sources.md#course-s03)、[S10 · L10 · Inference (Percy)](../ai-infra-sources.md#course-s10)。
- **论文与实现**：[Fast Transformer Decoding: One Write-Head is All You Need / MQA](../ai-infra-sources.md#source-mqa)、[GQA](../ai-infra-sources.md#source-gqa)。
- **后续验证（未运行）**：CPU：画 Q heads 与 KV heads 的映射，核对缓存计数和 attention shape。

(ai-10-6)=
## 10.6 MLA：低秩 latent KV 怎样保存，内容与位置相关计算怎样连接？

- **先修节点**：[10.5 MHA → MQA → GQA](10-kv-cache-decoding.md#ai-10-5)、[01.6 RoPE 与位置编码](01-tokenizer-transformer.md#ai-01-6)
- **课程出处**：**论文补充**；[S04 · L04 · Mixture of experts (Tatsu)](../ai-infra-sources.md#course-s04)、[MDEEP · Deepseek V3 and R1](../ai-infra-sources.md#course-mdeep)。
- **论文与实现**：[DeepSeek-V2 / MLA](../ai-infra-sources.md#source-deepseek2)。
- **后续验证（未运行）**：CPU/代码阅读：对照 DeepSeek-V2 画压缩与重构/吸收路径，注明比较的实现与配置。

(ai-10-7)=
## 10.7 Sliding-window Attention 与 Attention Sinks：哪些历史 token 状态保留，窗口/缓存策略怎样影响 attention 语义？

- **先修节点**：[10.3 KV Cache](10-kv-cache-decoding.md#ai-10-3)、[01.5 Causal Attention、Q/K/V 与 Multi-head Attention](01-tokenizer-transformer.md#ai-01-5)
- **课程出处**：**课程拆分与论文补充**；[MSINK · Efficient Streaming Language Models with Attention Sinks](../ai-infra-sources.md#course-msink)。
- **论文与实现**：[StreamingLLM / Attention Sinks](../ai-infra-sources.md#source-sinks)。
- **后续验证（未运行）**：CPU/单 GPU：画可见区域；比较短窗口、sink 保留与完整上下文，不默认输出等价。

(ai-10-8)=
## 10.8 RoPE Scaling 与长上下文：位置扩展怎样连接模型质量、KV 容量与计算成本？

- **先修节点**：[01.6 RoPE 与位置编码](01-tokenizer-transformer.md#ai-01-6)、[10.4 KV Cache 显存估算](10-kv-cache-decoding.md#ai-10-4)
- **课程出处**：**补充课程拆分**；[G19 · L19 · Long Context in LLM](../ai-infra-sources.md#course-g19)。
- **论文与实现**：[RoFormer / RoPE](../ai-infra-sources.md#source-rope)、[LLaMA](../ai-infra-sources.md#source-llama)。
- **后续验证（未运行）**：CPU/单 GPU：先画位置变换；选定模型后比较不同长度的质量与成本，记录 scaling 配置。

## 回到实际学习

选一个节点，先复述当前解释，再核查材料或代码并预测实验结果。实验前记录硬件、依赖版本、源码 commit、输入、同步与计时方法；重复测量保留原始记录。具体解释与证据逐步补到 topic 主笔记，未运行的方案保持标注。

[返回总地图](../ai-infra-map.md) · [上一章：09](09-quantization-peft.md) · [下一章：11](11-vllm-serving.md)
