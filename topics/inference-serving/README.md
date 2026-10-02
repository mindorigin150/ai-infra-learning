---
title: 生成执行与推理服务
---

# 生成执行与推理服务

请求怎样进入生成循环，缓存、批处理与调度怎样组织模型执行？

[主题索引](../README.md) · [开始一次学习](../../paths/start-here.md)

## 分类边界

性能指标的定义在性能观测；模型的数学结构、低精度表示和执行 kernel 分别链接相应分类。

## Topic 与材料入口

下表按机制归类已有材料节点。材料页保留具体问题、先修与来源；教学 Notebook 在实际学习后逐步展开。条目不表示个人掌握度。

| Topic | 要解释的问题 | 材料入口 |
| --- | --- | --- |
| Greedy、Temperature、Top-k、Top-p 与 Beam Search | 不同策略怎样选择 token，怎样影响生成状态与结果？ | [10.1](../../paths/ai-infra/10-kv-cache-decoding.md#ai-10-1) |
| Prefill 与 Decode | 两阶段的输入、可并行工作和瓶颈怎样随 batch、长度和硬件改变？ | [10.2](../../paths/ai-infra/10-kv-cache-decoding.md#ai-10-2) |
| KV Cache | 缓存哪些历史表示，追加 token 时哪些内容复用、哪些重新计算？ | [10.3](../../paths/ai-infra/10-kv-cache-decoding.md#ai-10-3) |
| KV Cache 显存估算 | 层数、KV heads、head dimension、长度、batch 与 dtype 怎样决定缓存容量？ | [10.4](../../paths/ai-infra/10-kv-cache-decoding.md#ai-10-4) |
| MHA → MQA → GQA | 减少 KV head 数怎样影响共享关系、缓存容量与 Attention 计算？ | [10.5](../../paths/ai-infra/10-kv-cache-decoding.md#ai-10-5) |
| MLA | 低秩 latent KV 怎样保存，内容与位置相关计算怎样连接？ | [10.6](../../paths/ai-infra/10-kv-cache-decoding.md#ai-10-6) |
| Sliding-window Attention 与 Attention Sinks | 哪些历史 token 状态保留，窗口/缓存策略怎样影响 attention 语义？ | [10.7](../../paths/ai-infra/10-kv-cache-decoding.md#ai-10-7) |
| RoPE Scaling 与长上下文 | 位置扩展怎样连接模型质量、KV 容量与计算成本？ | [10.8](../../paths/ai-infra/10-kv-cache-decoding.md#ai-10-8) |
| Static Batching → Continuous Batching | 请求怎样加入和离开 batch，未完成请求怎样继续执行？ | [11.1](../../paths/ai-infra/11-vllm-serving.md#ai-11-1) |
| Orca | iteration-level scheduling 与 selective batching 怎样组织生成模型执行？ | [11.2](../../paths/ai-infra/11-vllm-serving.md#ai-11-2) |
| PagedAttention | 逻辑 token 怎样经 block table 找到物理 KV block，块怎样分配与回收？ | [11.3](../../paths/ai-infra/11-vllm-serving.md#ai-11-3) |
| vLLM Scheduler → KV Manager → Model Runner | 一个请求从提交到每轮 GPU 执行，调度信息与缓存元数据怎样流动？ | [11.4](../../paths/ai-infra/11-vllm-serving.md#ai-11-4) |
| Chunked Prefill | prompt 怎样分块，怎样与 decode 共用 token budget？ | [11.5](../../paths/ai-infra/11-vllm-serving.md#ai-11-5) |
| Prefix Caching / SGLang RadixAttention | 共享前缀怎样识别、引用和回收，缓存命中怎样改变 prefill？ | [11.6](../../paths/ai-infra/11-vllm-serving.md#ai-11-6) |
| 抢占、Recompute 与 KV 回收 | 缓存不足时怎样暂停和恢复请求，生命周期中哪些状态需要保留？ | [11.7](../../paths/ai-infra/11-vllm-serving.md#ai-11-7) |
| Speculative Decoding | draft、verification 与接受/拒绝怎样减少串行步骤并保持目标采样分布？ | [11.8](../../paths/ai-infra/11-vllm-serving.md#ai-11-8) |
| CacheGen 与分层 KV Cache | 缓存压缩、加载、传输与重算之间怎样取舍，压缩是否改变结果？ | [11.9](../../paths/ai-infra/11-vllm-serving.md#ai-11-9) |
| DistServe / Prefill–Decode Disaggregation | 两阶段分开部署后，KV 传输、并行计划与资源分配怎样组织？ | [11.10](../../paths/ai-infra/11-vllm-serving.md#ai-11-10) |
| Triton Inference Server、LightLLM 与 Dynamo | 各系统承担哪些请求、执行或路由职责，怎样和模型 backend 连接？ | [11.12](../../paths/ai-infra/11-vllm-serving.md#ai-11-12) |
| 多模态 Prefill、Encoder Cache 与请求 Batch | 视觉处理如何接入 prefill，encoder 结果怎样缓存、共享或重新计算？ | [15.7](../../paths/ai-infra/15-multimodal-bagel.md#ai-15-7) |
| DistriFusion / PipeFusion | patch 分配、流水线与跨 timestep 复用怎样组织多 GPU diffusion inference？ | [16.10](../../paths/ai-infra/16-diffusion-dit.md#ai-16-10) |
| TeaCache | 跨 timestep 的计算复用怎样决定跳过哪些计算，怎样衡量累积误差与质量代价？ | [16.11](../../paths/ai-infra/16-diffusion-dit.md#ai-16-11) |
| Diffusers / xDiT 的执行优化 | attention backend、compile、offload、VAE tiling 与并行组合分别改变哪个阶段？ | [16.12](../../paths/ai-infra/16-diffusion-dit.md#ai-16-12) |

关联分类：[模型表示与生成机制](../models/README.md) · [数值表示与模型适配](../model-efficiency/README.md) · [性能模型与观测](../performance/README.md)。
