---
title: '11 · PagedAttention、vLLM、SGLang 与 DistServe'
---

# 11 · PagedAttention、vLLM、SGLang 与 DistServe

沿请求、缓存与调度的生命周期理解 serving 系统。Triton Inference Server 与 Triton kernel language 分别定位。

[完整地图](../ai-infra-map.md) · [课程与论文出处](../ai-infra-sources.md) · [GAPS](../../GAPS.md)

本页是学习导航。节点问题、先修与验证方案由本仓库编排；课程栏链接材料入口，补充节点另行标注。**本章验证均未运行；没有个人掌握度判断或性能实测。**

(ai-11-1)=
## 11.1 Static Batching → Continuous Batching：请求怎样加入和离开 batch，未完成请求怎样继续执行？

- **先修节点**：[10.2 Prefill 与 Decode](10-kv-cache-decoding.md#ai-10-2)、[10.3 KV Cache](10-kv-cache-decoding.md#ai-10-3)
- **课程出处**：**课程拆分**；[S10 · L10 · Inference (Percy)](../ai-infra-sources.md#course-s10)、[M22 · LLM Serving with PageAttention (Woosuk Kwon)](../ai-infra-sources.md#course-m22)。
- **论文与实现**：[Orca](../ai-infra-sources.md#source-orca)、[vLLM architecture](../ai-infra-sources.md#source-vllm)。
- **后续验证（未运行）**：CPU 时间线/单 GPU：用不同请求长度画静态和连续 batch，分别讨论排队、吞吐与延迟。

(ai-11-2)=
## 11.2 Orca：iteration-level scheduling 与 selective batching 怎样组织生成模型执行？

- **先修节点**：[11.1 Static Batching → Continuous Batching](11-vllm-serving.md#ai-11-1)
- **课程出处**：**课程拆分**；[MORCA · Advanced Large Model Serving](../ai-infra-sources.md#course-morca)。
- **论文与实现**：[Orca](../ai-infra-sources.md#source-orca)。
- **后续验证（未运行）**：论文阅读/时间线：追踪两条请求的加入与完成，标出选择性 batching 的算子边界。

(ai-11-3)=
## 11.3 PagedAttention：逻辑 token 怎样经 block table 找到物理 KV block，块怎样分配与回收？

- **先修节点**：[10.3 KV Cache](10-kv-cache-decoding.md#ai-10-3)、[10.4 KV Cache 显存估算](10-kv-cache-decoding.md#ai-10-4)
- **课程出处**：**课程拆分**；[M22 · LLM Serving with PageAttention (Woosuk Kwon)](../ai-infra-sources.md#course-m22)。
- **论文与实现**：[PagedAttention / vLLM](../ai-infra-sources.md#source-paged)、[vLLM architecture](../ai-infra-sources.md#source-vllm)。
- **后续验证（未运行）**：CPU 模拟/单 GPU：手算跨 block 的 token 地址，追踪增长、共享和释放。

(ai-11-4)=
## 11.4 vLLM Scheduler → KV Manager → Model Runner：一个请求从提交到每轮 GPU 执行，调度信息与缓存元数据怎样流动？

- **先修节点**：[11.1 Static Batching → Continuous Batching](11-vllm-serving.md#ai-11-1)、[11.3 PagedAttention](11-vllm-serving.md#ai-11-3)、[06.6 FlashAttention 的 Causal、Varlen 与 Packed 接口](06-flashattention-compilation.md#ai-06-6)
- **课程出处**：**工程补充**；[M22 · LLM Serving with PageAttention (Woosuk Kwon)](../ai-infra-sources.md#course-m22)。
- **论文与实现**：[vLLM architecture](../ai-infra-sources.md#source-vllm)。
- **后续验证（未运行）**：代码阅读/单 GPU：固定源码版本，追踪一个短请求的 scheduler、cache manager、runner 与 backend。

(ai-11-5)=
## 11.5 Chunked Prefill：prompt 怎样分块，怎样与 decode 共用 token budget？

- **先修节点**：[11.1 Static Batching → Continuous Batching](11-vllm-serving.md#ai-11-1)、[10.2 Prefill 与 Decode](10-kv-cache-decoding.md#ai-10-2)
- **课程出处**：**工程补充**；[S10 · L10 · Inference (Percy)](../ai-infra-sources.md#course-s10)、[M22 · LLM Serving with PageAttention (Woosuk Kwon)](../ai-infra-sources.md#course-m22)。
- **论文与实现**：[vLLM architecture](../ai-infra-sources.md#source-vllm)。
- **后续验证（未运行）**：单 GPU：比较不同 prompt/输出长度下的调度 timeline、TTFT 和 TPOT，记录 budget。

(ai-11-6)=
## 11.6 Prefix Caching / SGLang RadixAttention：共享前缀怎样识别、引用和回收，缓存命中怎样改变 prefill？

- **先修节点**：[11.3 PagedAttention](11-vllm-serving.md#ai-11-3)、[10.3 KV Cache](10-kv-cache-decoding.md#ai-10-3)
- **课程出处**：**课程拆分与工程补充**；[M25 · LLM serving with SGL (Ying Sheng)](../ai-infra-sources.md#course-m25)。
- **论文与实现**：[SGLang / RadixAttention](../ai-infra-sources.md#source-sglang-paper)、[SGLang documentation](../ai-infra-sources.md#source-sglang)、[vLLM architecture](../ai-infra-sources.md#source-vllm)。
- **后续验证（未运行）**：CPU 示意/单 GPU：画共享前缀树或 block；分别观察 cold/hit 请求并记录缓存条件。

(ai-11-7)=
## 11.7 抢占、Recompute 与 KV 回收：缓存不足时怎样暂停和恢复请求，生命周期中哪些状态需要保留？

- **先修节点**：[11.3 PagedAttention](11-vllm-serving.md#ai-11-3)、[11.4 vLLM Scheduler → KV Manager → Model Runner](11-vllm-serving.md#ai-11-4)
- **课程出处**：**工程补充**；[M22 · LLM Serving with PageAttention (Woosuk Kwon)](../ai-infra-sources.md#course-m22)。
- **论文与实现**：[vLLM architecture](../ai-infra-sources.md#source-vllm)。
- **后续验证（未运行）**：单 GPU：在受控缓存预算下追踪请求状态，核对完成结果与 latency；行为按版本记录。

(ai-11-8)=
## 11.8 Speculative Decoding：draft、verification 与接受/拒绝怎样减少串行步骤并保持目标采样分布？

- **先修节点**：[10.1 Greedy、Temperature、Top-k、Top-p 与 Beam Search](10-kv-cache-decoding.md#ai-10-1)、[10.2 Prefill 与 Decode](10-kv-cache-decoding.md#ai-10-2)
- **课程出处**：**课程拆分**；[MSPEC · Speculative Decoding](../ai-infra-sources.md#course-mspec)、[S10 · L10 · Inference (Percy)](../ai-infra-sources.md#course-s10)。
- **论文与实现**：[Fast Inference from Transformers via Speculative Decoding](../ai-infra-sources.md#source-speculative)、[vLLM architecture](../ai-infra-sources.md#source-vllm)。
- **后续验证（未运行）**：CPU/单 GPU：先手算接受与修正分布，再记录 draft 成本、接受率与端到端速度。

(ai-11-9)=
## 11.9 CacheGen 与分层 KV Cache：缓存压缩、加载、传输与重算之间怎样取舍，压缩是否改变结果？

- **先修节点**：[10.4 KV Cache 显存估算](10-kv-cache-decoding.md#ai-10-4)、[07.4 PCIe、NVLink、InfiniBand/RDMA](07-nccl-model-parallelism.md#ai-07-4)、[09.1 Quantization 的 Scale、Zero Point 与 Granularity](09-quantization-peft.md#ai-09-1)
- **课程出处**：**课程拆分与工程补充**；[M23 · Better KV Cache for LLM Serving (Yuhan Liu)](../ai-infra-sources.md#course-m23)。
- **论文与实现**：[CacheGen](../ai-infra-sources.md#source-cachegen)、[LMCache documentation](../ai-infra-sources.md#source-lmcache)。
- **后续验证（未运行）**：单 GPU加主存/存储：分别记录构建、压缩、传输、恢复与质量；数据路径必须明确。

(ai-11-10)=
## 11.10 DistServe / Prefill–Decode Disaggregation：两阶段分开部署后，KV 传输、并行计划与资源分配怎样组织？

- **先修节点**：[10.2 Prefill 与 Decode](10-kv-cache-decoding.md#ai-10-2)、[11.5 Chunked Prefill](11-vllm-serving.md#ai-11-5)、[07.4 PCIe、NVLink、InfiniBand/RDMA](07-nccl-model-parallelism.md#ai-07-4)
- **课程出处**：**课程拆分**；[M24 · DistServe: Disaggregated Prefill-Decoding (Hao Zhang)](../ai-infra-sources.md#course-m24)。
- **论文与实现**：[DistServe](../ai-infra-sources.md#source-distserve)、[NVIDIA Dynamo architecture](../ai-infra-sources.md#source-dynamo)。
- **后续验证（未运行）**：复述/多 GPU：画请求与 KV 传输路径；真实实验需足够资源和网络，按 SLO 比较 goodput。

(ai-11-11)=
## 11.11 TTFT、TPOT、吞吐与尾延迟：各指标包含哪些时间，服务负载和缓存条件怎样影响比较？

- **先修节点**：[04.8 CUDA Events、Warmup 与 Synchronization](04-gpu-profiling.md#ai-04-8)、[11.1 Static Batching → Continuous Batching](11-vllm-serving.md#ai-11-1)
- **课程出处**：**工程补充**；[S10 · L10 · Inference (Percy)](../ai-infra-sources.md#course-s10)、[M22 · LLM Serving with PageAttention (Woosuk Kwon)](../ai-infra-sources.md#course-m22)、[M24 · DistServe: Disaggregated Prefill-Decoding (Hao Zhang)](../ai-infra-sources.md#course-m24)。
- **论文与实现**：[vLLM metrics](../ai-infra-sources.md#source-vllm-metrics)。
- **后续验证（未运行）**：单 GPU 服务：记录请求到达方式、输入/输出长度、并发、分位数与 cold/warm 条件。

(ai-11-12)=
## 11.12 Triton Inference Server、LightLLM 与 Dynamo：各系统承担哪些请求、执行或路由职责，怎样和模型 backend 连接？

- **先修节点**：[11.4 vLLM Scheduler → KV Manager → Model Runner](11-vllm-serving.md#ai-11-4)、[11.10 DistServe / Prefill–Decode Disaggregation](11-vllm-serving.md#ai-11-10)、[11.11 TTFT、TPOT、吞吐与尾延迟](11-vllm-serving.md#ai-11-11)
- **课程出处**：**课程拆分与工程补充**；[MAPP · App Stack and Model Serving](../ai-infra-sources.md#course-mapp)、[MDYNAMO · Dynamo](../ai-infra-sources.md#course-mdynamo)。
- **论文与实现**：[Triton Inference Server](../ai-infra-sources.md#source-server)、[LightLLM implementation](../ai-infra-sources.md#source-lightllm)、[NVIDIA Dynamo architecture](../ai-infra-sources.md#source-dynamo)。
- **后续验证（未运行）**：代码阅读/复述：分别画职责与请求路径；与 05.2 的 Triton language 做概念对照。

## 回到实际学习

选一个节点，先复述当前解释，再核查材料或代码并预测实验结果。实验前记录硬件、依赖版本、源码 commit、输入、同步与计时方法；重复测量保留原始记录。具体解释与证据逐步补到 topic 主笔记，未运行的方案保持标注。

[返回总地图](../ai-infra-map.md) · [上一章：10](10-kv-cache-decoding.md) · [下一章：12](12-moe-expert-parallelism.md)
