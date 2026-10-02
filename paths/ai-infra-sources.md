---
title: '课程、论文与工程来源'
description: CS336、CMU 11-868 的逐课覆盖，以及多模态与 diffusion 的补充入口。
---

# 课程、论文与工程来源

[topic 分类](../topics/README.md) · [返回学习地图](ai-infra-map.md)

**核查日期：2026-10-02。** 使用 2025 课程归档作为主干；材料入口、课程大纲和论文书目信息已核查。尚未逐篇精读或完成课程作业。本页说明来源与覆盖，不把参考材料数量当作学习进度。

## 节点来源怎样区分

- **课程拆分**：从原课主题组织具体学习问题，标题与先修是本仓库编排，不能当作原讲义逐字标题。
- **论文补充 / 工程补充**：为主线补具体设计或当前实现；关联课程仅提供接入位置，不声称原课讲过全部补充内容。
- **补充课程**：只取 CMU Generative AI 中与已确定范围相关的课次。
- **验证**：所有 chapter 页的实验/复述方案均未运行；进入实际学习后再记录全文阅读、代码版本、观察与修正。

## 范围边界

学习范围是 LLM 训练/推理、MoE、多模态与 diffusion。按用户明确约定，传统 ML、CNN、推荐、GNN、检索/RAG、边缘与联邦学习不设学习节点。课程中的 RAG/HNSW 和 CacheBlend 因此移出；数学/OS/网络仅保留必要先修。

## 分布式运行时补充：Ray

(source-ray)=
### Ray Core

**主要教材**：[《Learning Ray》公开版第 2 章](https://maxpumperla.com/learning_ray/ch_02_ray_core/)，Max Pumperla、Edward Oakes、Richard Liaw。已阅读其中 A Ray Core Intro 的正文与代码，采用其连续的数据读取案例，完整改编入门范围；具体取舍、许可和对应关系见 [Ray 主题页](../topics/distributed-runtime/ray/README.md)。系统内部和 MapReduce 暂不展开。

**来源版本**：[公开 Notebook](https://github.com/maxpumperla/learning_ray/blob/321ebe5fdab451f75f2736683fd40921feffdf27/notebooks/ch_02_ray_core.ipynb)，提交 `321ebe5fdab451f75f2736683fd40921feffdf27`，MIT 许可；原示例基于 Ray 2.2.0，本地代码面向 Ray 2.59.0，查阅日期 2026-10-02。

**辅助对照**：[官方 Gentle Introduction](https://docs.ray.io/en/latest/ray-core/examples/gentle_walkthrough.html)。**技术核查**：[Tasks](https://docs.ray.io/en/latest/ray-core/tasks.html)、[Objects](https://docs.ray.io/en/latest/ray-core/objects.html)、[Actors](https://docs.ray.io/en/latest/ray-core/actors.html)、[Actor 执行顺序](https://docs.ray.io/en/latest/ray-core/actors/task-orders.html)、[资源模型](https://docs.ray.io/en/latest/ray-core/scheduling/resources.html)。本地补充解释、注释和练习，修正原文的 GIL 归因、超时语义及计数更新等待关系，不复制历史运行数字。

**主笔记**：[Ray CPU 中文入门与实验](../topics/distributed-runtime/ray/cpu.ipynb)。**关联材料**：[14.7 ReaLHF / verl](ai-infra/14-post-training-rlhf.md#ai-14-7)。这是独立工程补充；运行状态见主题入口。

用户提供的[视频](https://www.bilibili.com/video/BV1HuZcBEEyy/)标题与简介已核查，聚焦 Task、Actor、调度与并发。正文、字幕和简介里的私有代码未读取，不作为本次改编来源。

## CS336 Spring 2025：逐课对照

[官方归档](https://cs336.stanford.edu/spring2025/) · [官方讲义源码](https://github.com/stanford-cs336/spring2025-lectures)

(course-s01)=
### S01 · L01 · Overview, tokenization (Percy)

2025 归档；进度与讲义/代码入口已核查。

[课程页面](https://cs336.stanford.edu/spring2025/) · [lecture_01.py](https://cs336.stanford.edu/spring2025-lectures/?trace=var/traces/lecture_01.json)

**对应节点**：[01.1 Byte-level BPE](ai-infra/01-tokenizer-transformer.md#ai-01-1)、[01.3 Special Tokens、BOS/EOS 与 Chat Template](ai-infra/01-tokenizer-transformer.md#ai-01-3)。

(course-s02)=
### S02 · L02 · PyTorch, resource accounting (Percy)

2025 归档；进度与讲义/代码入口已核查。

[课程页面](https://cs336.stanford.edu/spring2025/) · [lecture_02.py](https://cs336.stanford.edu/spring2025-lectures/?trace=var/traces/lecture_02.json)

**对应节点**：[01.8 GPT/LLaMA 模型配置](ai-infra/01-tokenizer-transformer.md#ai-01-8)、[02.1 Tensor Storage、Stride、View 与 Contiguous](ai-infra/02-pytorch-training-step.md#ai-02-1)、[02.2 Broadcasting、Matmul 与 Einsum](ai-infra/02-pytorch-training-step.md#ai-02-2)、[02.8 FP32、FP16、BF16 与 AMP](ai-infra/02-pytorch-training-step.md#ai-02-8)、[03.4 Padding、Length Bucketing 与有效 Token 比例](ai-infra/03-data-sequence-packing.md#ai-03-4)、[04.7 FLOPs、Bytes、Arithmetic Intensity 与 Roofline](ai-infra/04-gpu-profiling.md#ai-04-7)、[08.1 训练显存账本](ai-infra/08-zero-fsdp-memory.md#ai-08-1)、[13.1 参数量、Token 数与训练 FLOPs](ai-infra/13-scaling-evaluation.md#ai-13-1)、[13.7 MFU 与 Time-to-quality](ai-infra/13-scaling-evaluation.md#ai-13-7)。

(course-s03)=
### S03 · L03 · Architectures, hyperparameters (Tatsu)

2025 归档；进度与讲义/代码入口已核查。

[课程页面](https://cs336.stanford.edu/spring2025/) · [lecture 3.pdf](https://github.com/stanford-cs336/spring2025-lectures/blob/e9cb2488fdb53ea37f0e38924ec3a1701925cef3/nonexecutable/2025%20Lecture%203%20-%20architecture.pdf)

**对应节点**：[01.4 Decoder-only Transformer](ai-infra/01-tokenizer-transformer.md#ai-01-4)、[01.5 Causal Attention、Q/K/V 与 Multi-head Attention](ai-infra/01-tokenizer-transformer.md#ai-01-5)、[01.6 RoPE 与位置编码](ai-infra/01-tokenizer-transformer.md#ai-01-6)、[01.7 RMSNorm、SwiGLU 与 Residual Connection](ai-infra/01-tokenizer-transformer.md#ai-01-7)、[01.8 GPT/LLaMA 模型配置](ai-infra/01-tokenizer-transformer.md#ai-01-8)、[02.5 Cross-entropy 与 Next-token Prediction](ai-infra/02-pytorch-training-step.md#ai-02-5)、[02.6 AdamW](ai-infra/02-pytorch-training-step.md#ai-02-6)、[10.5 MHA → MQA → GQA](ai-infra/10-kv-cache-decoding.md#ai-10-5)、[13.4 Learning Rate、Batch Size 与训练长度](ai-infra/13-scaling-evaluation.md#ai-13-4)。

(course-s04)=
### S04 · L04 · Mixture of experts (Tatsu)

2025 归档；进度与讲义/代码入口已核查。

[课程页面](https://cs336.stanford.edu/spring2025/) · [lecture 4.pdf](https://github.com/stanford-cs336/spring2025-lectures/blob/98455ec198c9a88ec1ab2b1c4058662431b54ce3/nonexecutable/2025%20Lecture%204%20-%20MoEs.pdf)

**对应节点**：[10.6 MLA](ai-infra/10-kv-cache-decoding.md#ai-10-6)、[12.1 Dense FFN → MoE Experts](ai-infra/12-moe-expert-parallelism.md#ai-12-1)、[12.2 Router 与 Top-k Routing](ai-infra/12-moe-expert-parallelism.md#ai-12-2)、[12.3 Capacity、Token Dropping 与 Dropless MoE](ai-infra/12-moe-expert-parallelism.md#ai-12-3)、[12.4 Load-balancing Loss 与 Router 稳定性](ai-infra/12-moe-expert-parallelism.md#ai-12-4)、[12.5 GShard / Switch Transformer](ai-infra/12-moe-expert-parallelism.md#ai-12-5)、[12.6 DeepSeek MoE](ai-infra/12-moe-expert-parallelism.md#ai-12-6)、[12.8 Grouped GEMM 与 MoE Kernel](ai-infra/12-moe-expert-parallelism.md#ai-12-8)。

(course-s05)=
### S05 · L05 · GPUs (Tatsu)

2025 归档；进度与讲义/代码入口已核查。

[课程页面](https://cs336.stanford.edu/spring2025/) · [lecture 5.pdf](https://github.com/stanford-cs336/spring2025-lectures/blob/main/nonexecutable/2025%20Lecture%205%20-%20GPUs.pdf)

**对应节点**：[04.1 Grid、Block、Thread 与 Warp](ai-infra/04-gpu-profiling.md#ai-04-1)、[04.2 SM、Warp Scheduler 与 SIMT](ai-infra/04-gpu-profiling.md#ai-04-2)、[04.3 Registers、Shared Memory、L2 与 HBM](ai-infra/04-gpu-profiling.md#ai-04-3)、[04.4 Tensor Cores 与矩阵乘法指令](ai-infra/04-gpu-profiling.md#ai-04-4)、[04.6 Occupancy、寄存器压力与 Latency Hiding](ai-infra/04-gpu-profiling.md#ai-04-6)、[04.7 FLOPs、Bytes、Arithmetic Intensity 与 Roofline](ai-infra/04-gpu-profiling.md#ai-04-7)。

(course-s06)=
### S06 · L06 · Kernels, Triton (Tatsu)

2025 归档；进度与讲义/代码入口已核查。

[课程页面](https://cs336.stanford.edu/spring2025/) · [lecture_06.py](https://cs336.stanford.edu/spring2025-lectures/?trace=var/traces/lecture_06.json)

**对应节点**：[03.8 数据读取、Prefetch 与 CPU→GPU Copy](ai-infra/03-data-sequence-packing.md#ai-03-8)、[04.8 CUDA Events、Warmup 与 Synchronization](ai-infra/04-gpu-profiling.md#ai-04-8)、[04.9 PyTorch Profiler、Nsight Systems 与 Nsight Compute](ai-infra/04-gpu-profiling.md#ai-04-9)、[05.2 Triton Vector Add](ai-infra/05-cuda-triton-kernels.md#ai-05-2)、[05.4 Fused Softmax](ai-infra/05-cuda-triton-kernels.md#ai-05-4)、[05.5 Naive GEMM → Tiled GEMM](ai-infra/05-cuda-triton-kernels.md#ai-05-5)、[05.6 Tensor Core GEMM](ai-infra/05-cuda-triton-kernels.md#ai-05-6)、[05.7 RMSNorm/SwiGLU Fusion](ai-infra/05-cuda-triton-kernels.md#ai-05-7)、[05.8 Kernel Benchmark 与正确性比较](ai-infra/05-cuda-triton-kernels.md#ai-05-8)、[06.1 标准 Attention 的显存与 IO](ai-infra/06-flashattention-compilation.md#ai-06-1)、[06.2 Online Softmax](ai-infra/06-flashattention-compilation.md#ai-06-2)、[06.3 FlashAttention-1](ai-infra/06-flashattention-compilation.md#ai-06-3)、[06.4 FlashAttention-2](ai-infra/06-flashattention-compilation.md#ai-06-4)、[06.6 FlashAttention 的 Causal、Varlen 与 Packed 接口](ai-infra/06-flashattention-compilation.md#ai-06-6)、[06.8 torch.compile、Fusion 与 Graph Break](ai-infra/06-flashattention-compilation.md#ai-06-8)。

(course-s07)=
### S07 · L07 · Parallelism (Tatsu)

2025 归档；进度与讲义/代码入口已核查。

[课程页面](https://cs336.stanford.edu/spring2025/) · [lecture 7.pdf](https://github.com/stanford-cs336/spring2025-lectures/blob/4eff81bee0a853217209e163936b264f03572b66/nonexecutable/2025%20Lecture%207%20-%20Parallelism%20basics.pdf)

**对应节点**：[07.1 Send/Recv 与 Collective Communication](ai-infra/07-nccl-model-parallelism.md#ai-07-1)、[07.2 AllReduce、ReduceScatter 与 AllGather](ai-infra/07-nccl-model-parallelism.md#ai-07-2)、[07.3 Ring/Tree 与通信成本](ai-infra/07-nccl-model-parallelism.md#ai-07-3)、[07.4 PCIe、NVLink、InfiniBand/RDMA](ai-infra/07-nccl-model-parallelism.md#ai-07-4)、[07.6 Megatron Tensor Parallelism](ai-infra/07-nccl-model-parallelism.md#ai-07-6)、[07.7 GPipe 与 Pipeline Parallelism](ai-infra/07-nccl-model-parallelism.md#ai-07-7)、[07.9 Sequence Parallelism 与 Context Parallelism](ai-infra/07-nccl-model-parallelism.md#ai-07-9)、[07.11 DP×TP×PP 组合与 Rank Placement](ai-infra/07-nccl-model-parallelism.md#ai-07-11)、[12.7 Expert Parallelism 与 AllToAll](ai-infra/12-moe-expert-parallelism.md#ai-12-7)。

(course-s08)=
### S08 · L08 · Parallelism (Percy)

2025 归档；进度与讲义/代码入口已核查。

[课程页面](https://cs336.stanford.edu/spring2025/) · [lecture_08.py](https://cs336.stanford.edu/spring2025-lectures/?trace=var/traces/lecture_08.json)

**对应节点**：[02.7 Gradient Accumulation](ai-infra/02-pytorch-training-step.md#ai-02-7)、[07.2 AllReduce、ReduceScatter 与 AllGather](ai-infra/07-nccl-model-parallelism.md#ai-07-2)、[07.5 DDP](ai-infra/07-nccl-model-parallelism.md#ai-07-5)、[07.6 Megatron Tensor Parallelism](ai-infra/07-nccl-model-parallelism.md#ai-07-6)、[07.11 DP×TP×PP 组合与 Rank Placement](ai-infra/07-nccl-model-parallelism.md#ai-07-11)、[08.1 训练显存账本](ai-infra/08-zero-fsdp-memory.md#ai-08-1)、[08.2 Activation Checkpointing](ai-infra/08-zero-fsdp-memory.md#ai-08-2)、[08.3 ZeRO-1](ai-infra/08-zero-fsdp-memory.md#ai-08-3)、[08.4 ZeRO-2](ai-infra/08-zero-fsdp-memory.md#ai-08-4)、[08.5 ZeRO-3](ai-infra/08-zero-fsdp-memory.md#ai-08-5)、[08.6 FSDP / FSDP2](ai-infra/08-zero-fsdp-memory.md#ai-08-6)、[08.8 Distributed Checkpoint](ai-infra/08-zero-fsdp-memory.md#ai-08-8)。

(course-s09)=
### S09 · L09 · Scaling laws (Tatsu)

2025 归档；进度与讲义/代码入口已核查。

[课程页面](https://cs336.stanford.edu/spring2025/) · [lecture 9.pdf](https://github.com/stanford-cs336/spring2025-lectures/blob/fb79eb018fa047bf99c4c785dcbbd62fff361e54/nonexecutable/2025%20Lecture%209%20-%20Scaling%20laws%20basics.pdf)

**对应节点**：[13.1 参数量、Token 数与训练 FLOPs](ai-infra/13-scaling-evaluation.md#ai-13-1)、[13.2 Kaplan Scaling Laws](ai-infra/13-scaling-evaluation.md#ai-13-2)、[13.4 Learning Rate、Batch Size 与训练长度](ai-infra/13-scaling-evaluation.md#ai-13-4)、[13.7 MFU 与 Time-to-quality](ai-infra/13-scaling-evaluation.md#ai-13-7)。

(course-s10)=
### S10 · L10 · Inference (Percy)

2025 归档；进度与讲义/代码入口已核查。

[课程页面](https://cs336.stanford.edu/spring2025/) · [lecture_10.py](https://cs336.stanford.edu/spring2025-lectures/?trace=var/traces/lecture_10.json)

**对应节点**：[10.1 Greedy、Temperature、Top-k、Top-p 与 Beam Search](ai-infra/10-kv-cache-decoding.md#ai-10-1)、[10.2 Prefill 与 Decode](ai-infra/10-kv-cache-decoding.md#ai-10-2)、[10.3 KV Cache](ai-infra/10-kv-cache-decoding.md#ai-10-3)、[10.4 KV Cache 显存估算](ai-infra/10-kv-cache-decoding.md#ai-10-4)、[10.5 MHA → MQA → GQA](ai-infra/10-kv-cache-decoding.md#ai-10-5)、[11.1 Static Batching → Continuous Batching](ai-infra/11-vllm-serving.md#ai-11-1)、[11.5 Chunked Prefill](ai-infra/11-vllm-serving.md#ai-11-5)、[11.8 Speculative Decoding](ai-infra/11-vllm-serving.md#ai-11-8)、[11.11 TTFT、TPOT、吞吐与尾延迟](ai-infra/11-vllm-serving.md#ai-11-11)。

(course-s11)=
### S11 · L11 · Scaling laws (Tatsu)

2025 归档；进度与讲义/代码入口已核查。

[课程页面](https://cs336.stanford.edu/spring2025/) · [lecture 11.pdf](https://github.com/stanford-cs336/spring2025-lectures/blob/00191bba00d6d64621dc46ccaed9122681413a24/nonexecutable/2025%20Lecture%2011%20-%20Scaling%20details.pdf)

**对应节点**：[13.3 Chinchilla](ai-infra/13-scaling-evaluation.md#ai-13-3)、[13.4 Learning Rate、Batch Size 与训练长度](ai-infra/13-scaling-evaluation.md#ai-13-4)、[13.7 MFU 与 Time-to-quality](ai-infra/13-scaling-evaluation.md#ai-13-7)。

(course-s12)=
### S12 · L12 · Evaluation (Percy)

2025 归档；进度与讲义/代码入口已核查。

[课程页面](https://cs336.stanford.edu/spring2025/) · [lecture_12.py](https://cs336.stanford.edu/spring2025-lectures/?trace=var/traces/lecture_12.json)

**对应节点**：[09.9 Quantized Kernel 与模型质量验证](ai-infra/09-quantization-peft.md#ai-09-9)、[13.5 Loss、Perplexity 与 Downstream Evaluation](ai-infra/13-scaling-evaluation.md#ai-13-5)、[13.6 Benchmark Contamination 与数据泄漏](ai-infra/13-scaling-evaluation.md#ai-13-6)。

(course-s13)=
### S13 · L13 · Data (Percy)

2025 归档；进度与讲义/代码入口已核查。

[课程页面](https://cs336.stanford.edu/spring2025/) · [lecture_13.py](https://cs336.stanford.edu/spring2025-lectures/?trace=var/traces/lecture_13.json)

**对应节点**：[03.1 文本清洗、质量过滤与去重](ai-infra/03-data-sequence-packing.md#ai-03-1)、[03.2 数据混合与 Sampling](ai-infra/03-data-sequence-packing.md#ai-03-2)、[03.3 Tokenization、Dataset Sharding 与 DataLoader](ai-infra/03-data-sequence-packing.md#ai-03-3)。

(course-s14)=
### S14 · L14 · Data (Percy)

2025 归档；进度与讲义/代码入口已核查。

[课程页面](https://cs336.stanford.edu/spring2025/) · [lecture_14.py](https://cs336.stanford.edu/spring2025-lectures/?trace=var/traces/lecture_14.json)

**对应节点**：[03.1 文本清洗、质量过滤与去重](ai-infra/03-data-sequence-packing.md#ai-03-1)、[03.2 数据混合与 Sampling](ai-infra/03-data-sequence-packing.md#ai-03-2)、[03.3 Tokenization、Dataset Sharding 与 DataLoader](ai-infra/03-data-sequence-packing.md#ai-03-3)、[03.4 Padding、Length Bucketing 与有效 Token 比例](ai-infra/03-data-sequence-packing.md#ai-03-4)、[03.5 Sequence Packing](ai-infra/03-data-sequence-packing.md#ai-03-5)、[13.6 Benchmark Contamination 与数据泄漏](ai-infra/13-scaling-evaluation.md#ai-13-6)。

(course-s15)=
### S15 · L15 · Alignment - SFT/RLHF (Tatsu)

2025 归档；进度与讲义/代码入口已核查。

[课程页面](https://cs336.stanford.edu/spring2025/) · [lecture 15.pdf](https://github.com/stanford-cs336/spring2025-lectures/blob/61eddac004df975466cff0329b615f2d24230069/nonexecutable/2025%20Lecture%2015%20-%20RLHF%20Alignment.pdf)

**对应节点**：[14.1 SFT](ai-infra/14-post-training-rlhf.md#ai-14-1)、[14.2 Preference Data 与 Reward Model](ai-infra/14-post-training-rlhf.md#ai-14-2)、[14.3 DPO](ai-infra/14-post-training-rlhf.md#ai-14-3)、[14.4 PPO / InstructGPT](ai-infra/14-post-training-rlhf.md#ai-14-4)。

(course-s16)=
### S16 · L16 · Alignment - RL (Tatsu)

2025 归档；进度与讲义/代码入口已核查。

[课程页面](https://cs336.stanford.edu/spring2025/) · [lecture 16.pdf](https://github.com/stanford-cs336/spring2025-lectures/blob/e94e33f433985e57036b25215dff2a4292e67a4f/nonexecutable/2025%20Lecture%2016%20-%20RLVR.pdf)

**对应节点**：[14.4 PPO / InstructGPT](ai-infra/14-post-training-rlhf.md#ai-14-4)、[14.5 GRPO / RLVR](ai-infra/14-post-training-rlhf.md#ai-14-5)。

(course-s17)=
### S17 · L17 · Alignment - RL (Percy)

2025 归档；进度与讲义/代码入口已核查。

[课程页面](https://cs336.stanford.edu/spring2025/) · [lecture_17.py](https://cs336.stanford.edu/spring2025-lectures/?trace=var/traces/lecture_17.json)

**对应节点**：[14.5 GRPO / RLVR](ai-infra/14-post-training-rlhf.md#ai-14-5)、[14.8 同步/异步 Rollout 与策略版本](ai-infra/14-post-training-rlhf.md#ai-14-8)。

(course-s18)=
### S18 · L18 · Guest Lecture by Junyang Lin

2025 归档；进度与讲义/代码入口已核查。

[课程页面](https://cs336.stanford.edu/spring2025/)

**覆盖记录**：公开大纲只列嘉宾课标题，未提供独立材料；不根据嘉宾身份推断内容或新建节点。

(course-s19)=
### S19 · L19 · Guest lecture by Mike Lewis

2025 归档；进度与讲义/代码入口已核查。

[课程页面](https://cs336.stanford.edu/spring2025/)

**覆盖记录**：公开大纲只列嘉宾课标题，未提供独立材料；不根据嘉宾身份推断内容或新建节点。

## CMU 11-868 Spring 2025：逐题对照

[官方 Syllabus](https://llmsystem.github.io/llmsystem2025spring/docs/Syllabus/)

大纲中的 Part 1/2 当前指向同一份 Transformer acceleration slides，保留原链接并另列 LightSeq/LightSeq2 论文。VOLT 和 CIAT 属于分词/adapter 课的相关 reading，分别归到 01.1–01.2 与 09.7 的主题范围，现阶段不增加独立 section。

(course-m01)=
### M01 · Introduction to LLM

2025 官方大纲；原课标题与材料入口已核查。

[课程页面](https://llmsystem.github.io/llmsystem2025spring/docs/Syllabus/) · [[slides]](https://llmsystem.github.io/llmsystem2025spring/assets/files/llmsys-01-intro-cd7350c64ac8b720a51aa45a52e9fa50.pdf)

**覆盖记录**：总地图承接课程介绍和框架定位，不单列重复学习节点。

(course-m02)=
### M02 · GPU Programming Basics 1

2025 官方大纲；原课标题与材料入口已核查。

[课程页面](https://llmsystem.github.io/llmsystem2025spring/docs/Syllabus/) · [[slides]](https://llmsystem.github.io/llmsystem2025spring/assets/files/llmsys-02-gpu-programming-b6078a9a5fc33d8ae03dff5b3e5fd8bb.pdf)

**对应节点**：[04.1 Grid、Block、Thread 与 Warp](ai-infra/04-gpu-profiling.md#ai-04-1)、[04.2 SM、Warp Scheduler 与 SIMT](ai-infra/04-gpu-profiling.md#ai-04-2)、[05.1 CUDA Vector Add](ai-infra/05-cuda-triton-kernels.md#ai-05-1)。

(course-m03)=
### M03 · GPU Programming Basics 2

2025 官方大纲；原课标题与材料入口已核查。

[课程页面](https://llmsystem.github.io/llmsystem2025spring/docs/Syllabus/) · [[slides]](https://llmsystem.github.io/llmsystem2025spring/assets/files/llmsys-03-gpu-programming2-4075ed5f62b3601db6bbe1991e5980c0.pdf)

**对应节点**：[04.1 Grid、Block、Thread 与 Warp](ai-infra/04-gpu-profiling.md#ai-04-1)、[04.2 SM、Warp Scheduler 与 SIMT](ai-infra/04-gpu-profiling.md#ai-04-2)、[04.3 Registers、Shared Memory、L2 与 HBM](ai-infra/04-gpu-profiling.md#ai-04-3)、[04.5 Coalesced Access 与 Memory Layout](ai-infra/04-gpu-profiling.md#ai-04-5)、[05.1 CUDA Vector Add](ai-infra/05-cuda-triton-kernels.md#ai-05-1)、[05.3 Reduction Kernel](ai-infra/05-cuda-triton-kernels.md#ai-05-3)。

(course-m04)=
### M04 · Learning algorithm and Auto Differentiation

2025 官方大纲；原课标题与材料入口已核查。

[课程页面](https://llmsystem.github.io/llmsystem2025spring/docs/Syllabus/) · [[slides]](https://llmsystem.github.io/llmsystem2025spring/assets/files/llmsys-04-autodiff-2ff210695355c7f9089b6209c515731c.pdf)

**对应节点**：[02.3 Autograd 与 Backward Graph](ai-infra/02-pytorch-training-step.md#ai-02-3)、[02.4 Saved Tensors 与显存生命周期](ai-infra/02-pytorch-training-step.md#ai-02-4)。

(course-m05)=
### M05 · Deep Learning Frameworks Design

2025 官方大纲；原课标题与材料入口已核查。

[课程页面](https://llmsystem.github.io/llmsystem2025spring/docs/Syllabus/) · [[slides]](https://llmsystem.github.io/llmsystem2025spring/assets/files/llmsys-05-dl-framework-3786a6ca3a677b14b94300fa6734893b.pdf)

**对应节点**：[02.1 Tensor Storage、Stride、View 与 Contiguous](ai-infra/02-pytorch-training-step.md#ai-02-1)、[02.3 Autograd 与 Backward Graph](ai-infra/02-pytorch-training-step.md#ai-02-3)、[02.4 Saved Tensors 与显存生命周期](ai-infra/02-pytorch-training-step.md#ai-02-4)、[06.8 torch.compile、Fusion 与 Graph Break](ai-infra/06-flashattention-compilation.md#ai-06-8)。

(course-m06)=
### M06 · Transformer

2025 官方大纲；原课标题与材料入口已核查。

[课程页面](https://llmsystem.github.io/llmsystem2025spring/docs/Syllabus/) · [[slides]](https://llmsystem.github.io/llmsystem2025spring/assets/files/llmsys-06-transformer-8cbfe810b0027cd5aed9f0c649499352.pdf)

**对应节点**：[01.4 Decoder-only Transformer](ai-infra/01-tokenizer-transformer.md#ai-01-4)、[01.5 Causal Attention、Q/K/V 与 Multi-head Attention](ai-infra/01-tokenizer-transformer.md#ai-01-5)、[01.6 RoPE 与位置编码](ai-infra/01-tokenizer-transformer.md#ai-01-6)、[02.2 Broadcasting、Matmul 与 Einsum](ai-infra/02-pytorch-training-step.md#ai-02-2)、[03.6 Packed Attention Mask、Position IDs 与 Loss Mask](ai-infra/03-data-sequence-packing.md#ai-03-6)。

(course-m07)=
### M07 · Pre-trained LLMs

2025 官方大纲；原课标题与材料入口已核查。

[课程页面](https://llmsystem.github.io/llmsystem2025spring/docs/Syllabus/) · [[slides]](https://llmsystem.github.io/llmsystem2025spring/assets/files/llmsys-07-llms-2054572db24531f7bea2feb74baaf987.pdf)

**对应节点**：[01.4 Decoder-only Transformer](ai-infra/01-tokenizer-transformer.md#ai-01-4)、[01.7 RMSNorm、SwiGLU 与 Residual Connection](ai-infra/01-tokenizer-transformer.md#ai-01-7)、[01.8 GPT/LLaMA 模型配置](ai-infra/01-tokenizer-transformer.md#ai-01-8)、[02.5 Cross-entropy 与 Next-token Prediction](ai-infra/02-pytorch-training-step.md#ai-02-5)。

(course-m08)=
### M08 · Tokenization

2025 官方大纲；原课标题与材料入口已核查。

[课程页面](https://llmsystem.github.io/llmsystem2025spring/docs/Syllabus/) · [[slides]](https://llmsystem.github.io/llmsystem2025spring/assets/files/llmsys-08-tokenization-46bef31fb38ec1f6a0ab0c593c5959b3.pdf)

**对应节点**：[01.1 Byte-level BPE](ai-infra/01-tokenizer-transformer.md#ai-01-1)、[01.2 SentencePiece](ai-infra/01-tokenizer-transformer.md#ai-01-2)、[01.3 Special Tokens、BOS/EOS 与 Chat Template](ai-infra/01-tokenizer-transformer.md#ai-01-3)。

(course-m09)=
### M09 · LLM Decoding

2025 官方大纲；原课标题与材料入口已核查。

[课程页面](https://llmsystem.github.io/llmsystem2025spring/docs/Syllabus/) · [[slides]](https://llmsystem.github.io/llmsystem2025spring/assets/files/llmsys-09-decoding-7735f8be9186c8840ed83128173a0c8f.pdf)

**对应节点**：[10.1 Greedy、Temperature、Top-k、Top-p 与 Beam Search](ai-infra/10-kv-cache-decoding.md#ai-10-1)。

(course-m10)=
### M10 · GPU Acceleration

2025 官方大纲；原课标题与材料入口已核查。

[课程页面](https://llmsystem.github.io/llmsystem2025spring/docs/Syllabus/) · [[slides]](https://llmsystem.github.io/llmsystem2025spring/assets/files/llmsys-10-gpu-acceleration-e14f3a7de2dae98b3cb01ce8034e8e7e.pdf)

**对应节点**：[04.3 Registers、Shared Memory、L2 与 HBM](ai-infra/04-gpu-profiling.md#ai-04-3)、[04.4 Tensor Cores 与矩阵乘法指令](ai-infra/04-gpu-profiling.md#ai-04-4)、[04.5 Coalesced Access 与 Memory Layout](ai-infra/04-gpu-profiling.md#ai-04-5)、[04.6 Occupancy、寄存器压力与 Latency Hiding](ai-infra/04-gpu-profiling.md#ai-04-6)、[05.3 Reduction Kernel](ai-infra/05-cuda-triton-kernels.md#ai-05-3)、[05.5 Naive GEMM → Tiled GEMM](ai-infra/05-cuda-triton-kernels.md#ai-05-5)、[05.6 Tensor Core GEMM](ai-infra/05-cuda-triton-kernels.md#ai-05-6)。

(course-m11)=
### M11 · Accelerating Transformer on GPU Part 1

2025 官方大纲；原课标题与材料入口已核查。

[课程页面](https://llmsystem.github.io/llmsystem2025spring/docs/Syllabus/) · [[slides]](https://llmsystem.github.io/llmsystem2025spring/assets/files/llmsys-11-transformer-acc-118c60f3304ec2de30bd6a80cb670613.pdf)

**对应节点**：[05.4 Fused Softmax](ai-infra/05-cuda-triton-kernels.md#ai-05-4)、[05.7 RMSNorm/SwiGLU Fusion](ai-infra/05-cuda-triton-kernels.md#ai-05-7)、[06.7 LightSeq / LightSeq2](ai-infra/06-flashattention-compilation.md#ai-06-7)。

(course-m12)=
### M12 · Accelerating Transformer on GPU Part 2

2025 官方大纲；原课标题与材料入口已核查。

[课程页面](https://llmsystem.github.io/llmsystem2025spring/docs/Syllabus/) · [[slides]](https://llmsystem.github.io/llmsystem2025spring/assets/files/llmsys-11-transformer-acc-118c60f3304ec2de30bd6a80cb670613.pdf)

**对应节点**：[05.7 RMSNorm/SwiGLU Fusion](ai-infra/05-cuda-triton-kernels.md#ai-05-7)、[06.7 LightSeq / LightSeq2](ai-infra/06-flashattention-compilation.md#ai-06-7)。

(course-m13)=
### M13 · Distributed Model Training

2025 官方大纲；原课标题与材料入口已核查。

[课程页面](https://llmsystem.github.io/llmsystem2025spring/docs/Syllabus/) · [[slides]](https://llmsystem.github.io/llmsystem2025spring/assets/files/llmsys-13-distributed-training-4012db2fbea5c325dea36cc9f6ccbae5.pdf)

**对应节点**：[07.1 Send/Recv 与 Collective Communication](ai-infra/07-nccl-model-parallelism.md#ai-07-1)、[07.2 AllReduce、ReduceScatter 与 AllGather](ai-infra/07-nccl-model-parallelism.md#ai-07-2)、[07.3 Ring/Tree 与通信成本](ai-infra/07-nccl-model-parallelism.md#ai-07-3)、[07.4 PCIe、NVLink、InfiniBand/RDMA](ai-infra/07-nccl-model-parallelism.md#ai-07-4)。

(course-m14)=
### M14 · Distributed Model Training II

2025 官方大纲；原课标题与材料入口已核查。

[课程页面](https://llmsystem.github.io/llmsystem2025spring/docs/Syllabus/) · [[slides]](https://llmsystem.github.io/llmsystem2025spring/assets/files/llmsys-14-ddp-4c41acd0996bb77e65703f85b1340b3f.pdf)

**对应节点**：[02.7 Gradient Accumulation](ai-infra/02-pytorch-training-step.md#ai-02-7)、[07.5 DDP](ai-infra/07-nccl-model-parallelism.md#ai-07-5)。

(course-m15)=
### M15 · Distributed Model Training III

2025 官方大纲；原课标题与材料入口已核查。

[课程页面](https://llmsystem.github.io/llmsystem2025spring/docs/Syllabus/) · [[slides]](https://llmsystem.github.io/llmsystem2025spring/assets/files/llmsys-15-model-parallel-1278ecd34702c1538bf26894762ec90f.pdf)

**对应节点**：[07.6 Megatron Tensor Parallelism](ai-infra/07-nccl-model-parallelism.md#ai-07-6)、[07.7 GPipe 与 Pipeline Parallelism](ai-infra/07-nccl-model-parallelism.md#ai-07-7)、[07.8 PipeDream / 1F1B Schedule](ai-infra/07-nccl-model-parallelism.md#ai-07-8)、[07.9 Sequence Parallelism 与 Context Parallelism](ai-infra/07-nccl-model-parallelism.md#ai-07-9)、[07.10 Ring Attention / Ulysses](ai-infra/07-nccl-model-parallelism.md#ai-07-10)、[07.11 DP×TP×PP 组合与 Rank Placement](ai-infra/07-nccl-model-parallelism.md#ai-07-11)。

(course-m16)=
### M16 · Model Quantization

2025 官方大纲；原课标题与材料入口已核查。

[课程页面](https://llmsystem.github.io/llmsystem2025spring/docs/Syllabus/) · [[slides]](https://llmsystem.github.io/llmsystem2025spring/assets/files/llmsys-16-quantization-80e192f2e967b00c68b29faa9d9e71de.pdf)

**对应节点**：[02.8 FP32、FP16、BF16 与 AMP](ai-infra/02-pytorch-training-step.md#ai-02-8)、[09.1 Quantization 的 Scale、Zero Point 与 Granularity](ai-infra/09-quantization-peft.md#ai-09-1)、[09.2 PTQ 与 QAT](ai-infra/09-quantization-peft.md#ai-09-2)、[09.6 FP8、Weight/Activation/KV Quantization](ai-infra/09-quantization-peft.md#ai-09-6)。

(course-m17)=
### M17 · Model Quantization II

2025 官方大纲；原课标题与材料入口已核查。

[课程页面](https://llmsystem.github.io/llmsystem2025spring/docs/Syllabus/) · [[slides]](https://llmsystem.github.io/llmsystem2025spring/assets/files/llmsys-17-quantization2-bec91c67e6870c9c398fcc4a22f0b446.pdf)

**对应节点**：[09.2 PTQ 与 QAT](ai-infra/09-quantization-peft.md#ai-09-2)、[09.3 GPTQ](ai-infra/09-quantization-peft.md#ai-09-3)、[09.4 SmoothQuant](ai-infra/09-quantization-peft.md#ai-09-4)、[09.5 AWQ](ai-infra/09-quantization-peft.md#ai-09-5)、[09.6 FP8、Weight/Activation/KV Quantization](ai-infra/09-quantization-peft.md#ai-09-6)、[09.9 Quantized Kernel 与模型质量验证](ai-infra/09-quantization-peft.md#ai-09-9)。

(course-m18)=
### M18 · Efficient fine-tuning for Large Models

2025 官方大纲；原课标题与材料入口已核查。

[课程页面](https://llmsystem.github.io/llmsystem2025spring/docs/Syllabus/) · [[slides]](https://llmsystem.github.io/llmsystem2025spring/assets/files/llmsys-18-peft-1555d9a7770e87fb10e2e95bf46ef12d.pdf)

**对应节点**：[09.7 Adapters 与 LoRA](ai-infra/09-quantization-peft.md#ai-09-7)、[09.8 QLoRA](ai-infra/09-quantization-peft.md#ai-09-8)。

(course-m19)=
### M19 · Large models with Mixture-of-Expert

2025 官方大纲；原课标题与材料入口已核查。

[课程页面](https://llmsystem.github.io/llmsystem2025spring/docs/Syllabus/) · [[slides]](https://llmsystem.github.io/llmsystem2025spring/assets/files/llmsys-19-MoE-1fd3b9f72ba69c8d3d71e01186674c5e.pdf)

**对应节点**：[12.1 Dense FFN → MoE Experts](ai-infra/12-moe-expert-parallelism.md#ai-12-1)、[12.2 Router 与 Top-k Routing](ai-infra/12-moe-expert-parallelism.md#ai-12-2)、[12.3 Capacity、Token Dropping 与 Dropless MoE](ai-infra/12-moe-expert-parallelism.md#ai-12-3)、[12.4 Load-balancing Loss 与 Router 稳定性](ai-infra/12-moe-expert-parallelism.md#ai-12-4)、[12.5 GShard / Switch Transformer](ai-infra/12-moe-expert-parallelism.md#ai-12-5)、[12.6 DeepSeek MoE](ai-infra/12-moe-expert-parallelism.md#ai-12-6)、[12.7 Expert Parallelism 与 AllToAll](ai-infra/12-moe-expert-parallelism.md#ai-12-7)、[12.8 Grouped GEMM 与 MoE Kernel](ai-infra/12-moe-expert-parallelism.md#ai-12-8)、[12.9 DeepSpeed-MoE / DeepSeek-V3](ai-infra/12-moe-expert-parallelism.md#ai-12-9)。

(course-m20)=
### M20 · Optimizing Attention for Modern Hardware (Tri Dao)

2025 官方大纲；原课标题与材料入口已核查。

[课程页面](https://llmsystem.github.io/llmsystem2025spring/docs/Syllabus/) · [[slides]](https://llmsystem.github.io/llmsystem2025spring/assets/files/llmsys-20-FlashAttention_tridao-cac5b634b4ad77cb027451422b07ae75.pdf)

**对应节点**：[03.7 Variable-length Attention 与 cu_seqlens](ai-infra/03-data-sequence-packing.md#ai-03-7)、[06.1 标准 Attention 的显存与 IO](ai-infra/06-flashattention-compilation.md#ai-06-1)、[06.2 Online Softmax](ai-infra/06-flashattention-compilation.md#ai-06-2)、[06.3 FlashAttention-1](ai-infra/06-flashattention-compilation.md#ai-06-3)、[06.4 FlashAttention-2](ai-infra/06-flashattention-compilation.md#ai-06-4)、[06.5 FlashAttention-3](ai-infra/06-flashattention-compilation.md#ai-06-5)、[06.6 FlashAttention 的 Causal、Varlen 与 Packed 接口](ai-infra/06-flashattention-compilation.md#ai-06-6)。

(course-m21)=
### M21 · Communication Efficient Distributed Training

2025 官方大纲；原课标题与材料入口已核查。

[课程页面](https://llmsystem.github.io/llmsystem2025spring/docs/Syllabus/) · [[slides]](https://llmsystem.github.io/llmsystem2025spring/assets/files/llmsys-21-zero-20eb6c8d8c1e7092e1b922abf03d8cdd.pdf)

**对应节点**：[08.1 训练显存账本](ai-infra/08-zero-fsdp-memory.md#ai-08-1)、[08.2 Activation Checkpointing](ai-infra/08-zero-fsdp-memory.md#ai-08-2)、[08.3 ZeRO-1](ai-infra/08-zero-fsdp-memory.md#ai-08-3)、[08.4 ZeRO-2](ai-infra/08-zero-fsdp-memory.md#ai-08-4)、[08.5 ZeRO-3](ai-infra/08-zero-fsdp-memory.md#ai-08-5)、[08.6 FSDP / FSDP2](ai-infra/08-zero-fsdp-memory.md#ai-08-6)、[08.7 CPU/NVMe Offload](ai-infra/08-zero-fsdp-memory.md#ai-08-7)、[08.8 Distributed Checkpoint](ai-infra/08-zero-fsdp-memory.md#ai-08-8)。

(course-m22)=
### M22 · LLM Serving with PageAttention (Woosuk Kwon)

2025 官方大纲；原课标题与材料入口已核查。

[课程页面](https://llmsystem.github.io/llmsystem2025spring/docs/Syllabus/) · [[slides]](https://llmsystem.github.io/llmsystem2025spring/assets/files/llmsys-22-vLLM_woosuk_kwon-1f34697dbb1a1fb5b798daf6eff14b67.pdf)

**对应节点**：[10.2 Prefill 与 Decode](ai-infra/10-kv-cache-decoding.md#ai-10-2)、[10.3 KV Cache](ai-infra/10-kv-cache-decoding.md#ai-10-3)、[10.4 KV Cache 显存估算](ai-infra/10-kv-cache-decoding.md#ai-10-4)、[11.1 Static Batching → Continuous Batching](ai-infra/11-vllm-serving.md#ai-11-1)、[11.3 PagedAttention](ai-infra/11-vllm-serving.md#ai-11-3)、[11.4 vLLM Scheduler → KV Manager → Model Runner](ai-infra/11-vllm-serving.md#ai-11-4)、[11.5 Chunked Prefill](ai-infra/11-vllm-serving.md#ai-11-5)、[11.7 抢占、Recompute 与 KV 回收](ai-infra/11-vllm-serving.md#ai-11-7)、[11.11 TTFT、TPOT、吞吐与尾延迟](ai-infra/11-vllm-serving.md#ai-11-11)。

(course-m23)=
### M23 · Better KV Cache for LLM Serving (Yuhan Liu)

2025 官方大纲；原课标题与材料入口已核查。

[课程页面](https://llmsystem.github.io/llmsystem2025spring/docs/Syllabus/) · [[slides]](https://llmsystem.github.io/llmsystem2025spring/assets/files/llmsys-23-LMCache_yuhan_liu-168b4d638987bf0e6408d553486059b1.pdf)

**对应节点**：[10.3 KV Cache](ai-infra/10-kv-cache-decoding.md#ai-10-3)、[11.9 CacheGen 与分层 KV Cache](ai-infra/11-vllm-serving.md#ai-11-9)。

(course-m24)=
### M24 · DistServe: Disaggregated Prefill-Decoding (Hao Zhang)

2025 官方大纲；原课标题与材料入口已核查。

[课程页面](https://llmsystem.github.io/llmsystem2025spring/docs/Syllabus/) · [[slides]](https://llmsystem.github.io/llmsystem2025spring/assets/files/llmsys-24-disaggregating_prefill_decode_hao_zhang-c0e55139d20512a2348783423397cc7f.pdf)

**对应节点**：[11.10 DistServe / Prefill–Decode Disaggregation](ai-infra/11-vllm-serving.md#ai-11-10)、[11.11 TTFT、TPOT、吞吐与尾延迟](ai-infra/11-vllm-serving.md#ai-11-11)。

(course-m25)=
### M25 · LLM serving with SGL (Ying Sheng)

2025 官方大纲；原课标题与材料入口已核查。

[课程页面](https://llmsystem.github.io/llmsystem2025spring/docs/Syllabus/) · [[slides]](https://llmsystem.github.io/llmsystem2025spring/assets/files/llmsys-25-sglang-72edc5043338f59db34d47e5b96ac870.pdf)

**对应节点**：[11.6 Prefix Caching / SGLang RadixAttention](ai-infra/11-vllm-serving.md#ai-11-6)。

(course-mreal)=
### MREAL · Efficient Reinforcement Learning System for LLMs

2025 官方大纲；原课标题与材料入口已核查；无独立 slides 链接，使用大纲及指定论文。

[课程页面](https://llmsystem.github.io/llmsystem2025spring/docs/Syllabus/)

**对应节点**：[14.6 Rollout Engine 与权重同步](ai-infra/14-post-training-rlhf.md#ai-14-6)、[14.7 ReaLHF / verl](ai-infra/14-post-training-rlhf.md#ai-14-7)、[14.8 同步/异步 Rollout 与策略版本](ai-infra/14-post-training-rlhf.md#ai-14-8)。

(course-mapp)=
### MAPP · App Stack and Model Serving

2025 官方大纲；原课标题与材料入口已核查；该专题未排日期，不据此断言已实际授课。

[课程页面](https://llmsystem.github.io/llmsystem2025spring/docs/Syllabus/) · [[slides]](https://llmsystem.github.io/llmsystem2025spring/assets/files/llmsys-15-serving-c4a70ab21cde01fb60068a256c6e163a.pdf)

**对应节点**：[11.12 Triton Inference Server、LightLLM 与 Dynamo](ai-infra/11-vllm-serving.md#ai-11-12)。

(course-mjit)=
### MJIT · GPU just-in-time compilation

2025 官方大纲；原课标题与材料入口已核查；该专题未排日期，不据此断言已实际授课；无独立 slides 链接，使用大纲及指定论文。

[课程页面](https://llmsystem.github.io/llmsystem2025spring/docs/Syllabus/)

**对应节点**：[06.9 CUDA Graph 与 JAX JIT](ai-infra/06-flashattention-compilation.md#ai-06-9)。

(course-mspec)=
### MSPEC · Speculative Decoding

2025 官方大纲；原课标题与材料入口已核查；该专题未排日期，不据此断言已实际授课；无独立 slides 链接，使用大纲及指定论文。

[课程页面](https://llmsystem.github.io/llmsystem2025spring/docs/Syllabus/)

**对应节点**：[11.8 Speculative Decoding](ai-infra/11-vllm-serving.md#ai-11-8)。

(course-mmulti)=
### MMULTI · Multimodal LLMs

2025 官方大纲；原课标题与材料入口已核查；该专题未排日期，不据此断言已实际授课；无独立 slides 链接，使用大纲及指定论文。

[课程页面](https://llmsystem.github.io/llmsystem2025spring/docs/Syllabus/)

**对应节点**：[15.2 Projector 与 Cross-attention](ai-infra/15-multimodal-bagel.md#ai-15-2)、[15.3 Flamingo / LLaVA](ai-infra/15-multimodal-bagel.md#ai-15-3)、[15.7 多模态 Prefill、Encoder Cache 与请求 Batch](ai-infra/15-multimodal-bagel.md#ai-15-7)。

(course-mdeep)=
### MDEEP · Deepseek V3 and R1

2025 官方大纲；原课标题与材料入口已核查；该专题未排日期，不据此断言已实际授课；无独立 slides 链接，使用大纲及指定论文。

[课程页面](https://llmsystem.github.io/llmsystem2025spring/docs/Syllabus/)

**对应节点**：[10.6 MLA](ai-infra/10-kv-cache-decoding.md#ai-10-6)、[12.9 DeepSpeed-MoE / DeepSeek-V3](ai-infra/12-moe-expert-parallelism.md#ai-12-9)。

(course-msink)=
### MSINK · Efficient Streaming Language Models with Attention Sinks

2025 官方大纲；原课标题与材料入口已核查；该专题未排日期，不据此断言已实际授课；无独立 slides 链接，使用大纲及指定论文。

[课程页面](https://llmsystem.github.io/llmsystem2025spring/docs/Syllabus/)

**对应节点**：[10.7 Sliding-window Attention 与 Attention Sinks](ai-infra/10-kv-cache-decoding.md#ai-10-7)。

(course-morca)=
### MORCA · Advanced Large Model Serving

2025 官方大纲；原课标题与材料入口已核查；该专题未排日期，不据此断言已实际授课；无独立 slides 链接，使用大纲及指定论文。

[课程页面](https://llmsystem.github.io/llmsystem2025spring/docs/Syllabus/)

**对应节点**：[11.2 Orca](ai-infra/11-vllm-serving.md#ai-11-2)。

(course-mdynamo)=
### MDYNAMO · Dynamo

2025 官方大纲；原课标题与材料入口已核查；该专题未排日期，不据此断言已实际授课；无独立 slides 链接，使用大纲及指定论文。

[课程页面](https://llmsystem.github.io/llmsystem2025spring/docs/Syllabus/)

**对应节点**：[11.12 Triton Inference Server、LightLLM 与 Dynamo](ai-infra/11-vllm-serving.md#ai-11-12)。

## CMU Generative AI：补充课次

[Spring 2025 官方进度](https://www.cs.cmu.edu/~mgormley/courses/10423-s25/schedule.html)

05 只取 ViT，08 的 VAE 只作为 latent 路径需要的前提；不据此增加 CNN 等独立章节。DiT、Flow Matching、并行推理和缓存的具体设计来自下面论文/实现，不能由课次名称推断全部已授内容。

(course-g05)=
### G05 · L05 · Vision Transformers 部分

Spring 2025；补充课程进度已核查，只取本地图所需部分。

[课程页面](https://www.cs.cmu.edu/~mgormley/courses/10423-s25/schedule.html)

**对应节点**：[15.1 ViT 与 Patch Tokens](ai-infra/15-multimodal-bagel.md#ai-15-1)。

(course-g07)=
### G07 · L07 · Diffusion models (Part I)

Spring 2025；补充课程进度已核查，只取本地图所需部分。

[课程页面](https://www.cs.cmu.edu/~mgormley/courses/10423-s25/schedule.html)

**对应节点**：[16.1 DDPM](ai-infra/16-diffusion-dit.md#ai-16-1)、[16.2 DDIM / DPM-Solver](ai-infra/16-diffusion-dit.md#ai-16-2)、[16.6 Flow Matching / Rectified Flow](ai-infra/16-diffusion-dit.md#ai-16-6)、[16.9 Diffusion 的训练 Batch、混合精度与 Checkpointing](ai-infra/16-diffusion-dit.md#ai-16-9)。

(course-g08)=
### G08 · L08 · Diffusion models (Part II) / VAE 前提

Spring 2025；补充课程进度已核查，只取本地图所需部分。

[课程页面](https://www.cs.cmu.edu/~mgormley/courses/10423-s25/schedule.html)

**对应节点**：[16.1 DDPM](ai-infra/16-diffusion-dit.md#ai-16-1)、[16.2 DDIM / DPM-Solver](ai-infra/16-diffusion-dit.md#ai-16-2)、[16.6 Flow Matching / Rectified Flow](ai-infra/16-diffusion-dit.md#ai-16-6)、[16.9 Diffusion 的训练 Batch、混合精度与 Checkpointing](ai-infra/16-diffusion-dit.md#ai-16-9)。

(course-g12)=
### G12 · L12 · Text-to-image / Latent diffusion 部分

Spring 2025；补充课程进度已核查，只取本地图所需部分。

[课程页面](https://www.cs.cmu.edu/~mgormley/courses/10423-s25/schedule.html)

**对应节点**：[16.3 Latent Diffusion 与 VAE](ai-infra/16-diffusion-dit.md#ai-16-3)、[16.5 Classifier-free Guidance](ai-infra/16-diffusion-dit.md#ai-16-5)、[16.7 MMDiT](ai-infra/16-diffusion-dit.md#ai-16-7)。

(course-g14)=
### G14 · L14 · Vision-language models

Spring 2025；补充课程进度已核查，只取本地图所需部分。

[课程页面](https://www.cs.cmu.edu/~mgormley/courses/10423-s25/schedule.html)

**对应节点**：[15.2 Projector 与 Cross-attention](ai-infra/15-multimodal-bagel.md#ai-15-2)、[15.3 Flamingo / LLaVA](ai-infra/15-multimodal-bagel.md#ai-15-3)、[15.4 Qwen-VL 风格动态分辨率与多模态位置编码](ai-infra/15-multimodal-bagel.md#ai-15-4)、[15.5 多模态 Sequence Packing](ai-infra/15-multimodal-bagel.md#ai-15-5)、[15.6 视觉 Token 数量与显存/Attention 成本](ai-infra/15-multimodal-bagel.md#ai-15-6)、[15.8 BAGEL 的理解与生成路径](ai-infra/15-multimodal-bagel.md#ai-15-8)、[16.7 MMDiT](ai-infra/16-diffusion-dit.md#ai-16-7)。

(course-g19)=
### G19 · L19 · Long Context in LLM

Spring 2025；补充课程进度已核查，只取本地图所需部分。

[课程页面](https://www.cs.cmu.edu/~mgormley/courses/10423-s25/schedule.html)

**对应节点**：[10.8 RoPE Scaling 与长上下文](ai-infra/10-kv-cache-decoding.md#ai-10-8)。

(course-g25)=
### G25 · L25 · Generative Models for Videos

Spring 2025；补充课程进度已核查，只取本地图所需部分。

[课程页面](https://www.cs.cmu.edu/~mgormley/courses/10423-s25/schedule.html)

**对应节点**：[15.9 Video Tokens 与时空 Attention](ai-infra/15-multimodal-bagel.md#ai-15-9)、[16.4 DiT](ai-infra/16-diffusion-dit.md#ai-16-4)、[16.8 Image/Video Diffusion 的计算与显存账本](ai-infra/16-diffusion-dit.md#ai-16-8)、[16.10 DistriFusion / PipeFusion](ai-infra/16-diffusion-dit.md#ai-16-10)、[16.11 TeaCache](ai-infra/16-diffusion-dit.md#ai-16-11)、[16.12 Diffusers / xDiT 的执行优化](ai-infra/16-diffusion-dit.md#ai-16-12)。

## 代表论文与工程入口

年份记录首次公开或明确发表年份；两者不同时并列。下面按首次使用的章分组，每个材料只登记一次；其他章节通过相同标签引用。论文定位以大纲、摘要和一手书目信息为依据，全文论证留到主题学习。工程文档按查阅日期定位；实际实验记录安装版本与源码 commit。

### 01 · BPE、Tokenizer 与 LLaMA 风格 Transformer

(source-bpe)=
#### BPE / Neural Machine Translation of Rare Words

**类型**：论文 · **年份/版本定位**：2015；ACL 2016 · [一手入口](https://arxiv.org/abs/1508.07909)

**关联节点**：[01.1 Byte-level BPE](ai-infra/01-tokenizer-transformer.md#ai-01-1)。

(source-hf-tokenizer)=
#### Transformers tokenizers

**类型**：工程文档 · **年份/版本定位**：查阅 2026-10-02 · [一手入口](https://huggingface.co/docs/transformers/main_classes/tokenizer)

**关联节点**：[01.1 Byte-level BPE](ai-infra/01-tokenizer-transformer.md#ai-01-1)、[01.3 Special Tokens、BOS/EOS 与 Chat Template](ai-infra/01-tokenizer-transformer.md#ai-01-3)、[03.1 文本清洗、质量过滤与去重](ai-infra/03-data-sequence-packing.md#ai-03-1)、[03.2 数据混合与 Sampling](ai-infra/03-data-sequence-packing.md#ai-03-2)。

(source-sentencepiece)=
#### SentencePiece

**类型**：论文 · **年份/版本定位**：2018 · [一手入口](https://aclanthology.org/D18-2012/)

**关联节点**：[01.2 SentencePiece](ai-infra/01-tokenizer-transformer.md#ai-01-2)。

(source-chat)=
#### Transformers chat templates

**类型**：工程文档 · **年份/版本定位**：查阅 2026-10-02 · [一手入口](https://huggingface.co/docs/transformers/chat_templating)

**关联节点**：[01.3 Special Tokens、BOS/EOS 与 Chat Template](ai-infra/01-tokenizer-transformer.md#ai-01-3)、[14.1 SFT](ai-infra/14-post-training-rlhf.md#ai-14-1)。

(source-transformer)=
#### Attention Is All You Need

**类型**：论文 · **年份/版本定位**：2017 · [一手入口](https://arxiv.org/abs/1706.03762)

**关联节点**：[01.4 Decoder-only Transformer](ai-infra/01-tokenizer-transformer.md#ai-01-4)、[01.5 Causal Attention、Q/K/V 与 Multi-head Attention](ai-infra/01-tokenizer-transformer.md#ai-01-5)、[10.1 Greedy、Temperature、Top-k、Top-p 与 Beam Search](ai-infra/10-kv-cache-decoding.md#ai-10-1)。

(source-llama)=
#### LLaMA

**类型**：论文 · **年份/版本定位**：2023 · [一手入口](https://arxiv.org/abs/2302.13971)

**关联节点**：[01.4 Decoder-only Transformer](ai-infra/01-tokenizer-transformer.md#ai-01-4)、[01.7 RMSNorm、SwiGLU 与 Residual Connection](ai-infra/01-tokenizer-transformer.md#ai-01-7)、[01.8 GPT/LLaMA 模型配置](ai-infra/01-tokenizer-transformer.md#ai-01-8)、[02.5 Cross-entropy 与 Next-token Prediction](ai-infra/02-pytorch-training-step.md#ai-02-5)、[10.1 Greedy、Temperature、Top-k、Top-p 与 Beam Search](ai-infra/10-kv-cache-decoding.md#ai-10-1)、[10.8 RoPE Scaling 与长上下文](ai-infra/10-kv-cache-decoding.md#ai-10-8)、[13.5 Loss、Perplexity 与 Downstream Evaluation](ai-infra/13-scaling-evaluation.md#ai-13-5)、[13.6 Benchmark Contamination 与数据泄漏](ai-infra/13-scaling-evaluation.md#ai-13-6)。

(source-rope)=
#### RoFormer / RoPE

**类型**：论文 · **年份/版本定位**：2021 · [一手入口](https://arxiv.org/abs/2104.09864)

**关联节点**：[01.6 RoPE 与位置编码](ai-infra/01-tokenizer-transformer.md#ai-01-6)、[10.8 RoPE Scaling 与长上下文](ai-infra/10-kv-cache-decoding.md#ai-10-8)。

(source-rmsnorm)=
#### RMSNorm

**类型**：论文 · **年份/版本定位**：2019 · [一手入口](https://arxiv.org/abs/1910.07467)

**关联节点**：[01.7 RMSNorm、SwiGLU 与 Residual Connection](ai-infra/01-tokenizer-transformer.md#ai-01-7)。

(source-swiglu)=
#### GLU Variants Improve Transformer

**类型**：论文 · **年份/版本定位**：2020 · [一手入口](https://arxiv.org/abs/2002.05202)

**关联节点**：[01.7 RMSNorm、SwiGLU 与 Residual Connection](ai-infra/01-tokenizer-transformer.md#ai-01-7)。

### 02 · PyTorch Tensor、Autograd 与一次训练更新

(source-tensor)=
#### PyTorch tensor views

**类型**：工程文档 · **年份/版本定位**：查阅 2026-10-02 · [一手入口](https://docs.pytorch.org/docs/stable/tensor_view)

**关联节点**：[02.1 Tensor Storage、Stride、View 与 Contiguous](ai-infra/02-pytorch-training-step.md#ai-02-1)。

(source-pytorch)=
#### PyTorch: An Imperative Style, High-Performance Deep Learning Library

**类型**：论文 · **年份/版本定位**：2019 · [一手入口](https://arxiv.org/abs/1912.01703)

**关联节点**：[02.1 Tensor Storage、Stride、View 与 Contiguous](ai-infra/02-pytorch-training-step.md#ai-02-1)、[02.2 Broadcasting、Matmul 与 Einsum](ai-infra/02-pytorch-training-step.md#ai-02-2)、[02.3 Autograd 与 Backward Graph](ai-infra/02-pytorch-training-step.md#ai-02-3)。

(source-autograd)=
#### PyTorch autograd

**类型**：工程文档 · **年份/版本定位**：查阅 2026-10-02 · [一手入口](https://docs.pytorch.org/tutorials/beginner/blitz/autograd_tutorial.html)

**关联节点**：[02.3 Autograd 与 Backward Graph](ai-infra/02-pytorch-training-step.md#ai-02-3)、[02.4 Saved Tensors 与显存生命周期](ai-infra/02-pytorch-training-step.md#ai-02-4)。

(source-tuning)=
#### PyTorch performance tuning

**类型**：工程文档 · **年份/版本定位**：查阅 2026-10-02 · [一手入口](https://docs.pytorch.org/tutorials/recipes/recipes/tuning_guide.html)

**关联节点**：[02.4 Saved Tensors 与显存生命周期](ai-infra/02-pytorch-training-step.md#ai-02-4)、[02.7 Gradient Accumulation](ai-infra/02-pytorch-training-step.md#ai-02-7)、[03.3 Tokenization、Dataset Sharding 与 DataLoader](ai-infra/03-data-sequence-packing.md#ai-03-3)、[03.4 Padding、Length Bucketing 与有效 Token 比例](ai-infra/03-data-sequence-packing.md#ai-03-4)、[03.8 数据读取、Prefetch 与 CPU→GPU Copy](ai-infra/03-data-sequence-packing.md#ai-03-8)、[04.8 CUDA Events、Warmup 与 Synchronization](ai-infra/04-gpu-profiling.md#ai-04-8)、[04.9 PyTorch Profiler、Nsight Systems 与 Nsight Compute](ai-infra/04-gpu-profiling.md#ai-04-9)、[08.1 训练显存账本](ai-infra/08-zero-fsdp-memory.md#ai-08-1)。

(source-adamw)=
#### Decoupled Weight Decay Regularization / AdamW

**类型**：论文 · **年份/版本定位**：2017；ICLR 2019 · [一手入口](https://arxiv.org/abs/1711.05101)

**关联节点**：[02.6 AdamW](ai-infra/02-pytorch-training-step.md#ai-02-6)。

(source-ddp)=
#### PyTorch DDP tutorial

**类型**：工程文档 · **年份/版本定位**：查阅 2026-10-02 · [一手入口](https://docs.pytorch.org/tutorials/intermediate/ddp_tutorial.html)

**关联节点**：[02.7 Gradient Accumulation](ai-infra/02-pytorch-training-step.md#ai-02-7)、[07.5 DDP](ai-infra/07-nccl-model-parallelism.md#ai-07-5)。

(source-mixed)=
#### Mixed Precision Training

**类型**：论文 · **年份/版本定位**：2017；ICLR 2018 · [一手入口](https://arxiv.org/abs/1710.03740)

**关联节点**：[02.8 FP32、FP16、BF16 与 AMP](ai-infra/02-pytorch-training-step.md#ai-02-8)。

(source-amp)=
#### PyTorch AMP

**类型**：工程文档 · **年份/版本定位**：查阅 2026-10-02 · [一手入口](https://docs.pytorch.org/tutorials/recipes/recipes/amp_recipe.html)

**关联节点**：[02.8 FP32、FP16、BF16 与 AMP](ai-infra/02-pytorch-training-step.md#ai-02-8)、[16.9 Diffusion 的训练 Batch、混合精度与 Checkpointing](ai-infra/16-diffusion-dit.md#ai-16-9)。

### 03 · 预训练数据、Padding 与 Sequence Packing

(source-fa-code)=
#### FlashAttention implementation

**类型**：工程文档 · **年份/版本定位**：查阅 2026-10-02 · [一手入口](https://github.com/Dao-AILab/flash-attention)

**关联节点**：[03.5 Sequence Packing](ai-infra/03-data-sequence-packing.md#ai-03-5)、[03.6 Packed Attention Mask、Position IDs 与 Loss Mask](ai-infra/03-data-sequence-packing.md#ai-03-6)、[03.7 Variable-length Attention 与 cu_seqlens](ai-infra/03-data-sequence-packing.md#ai-03-7)、[06.3 FlashAttention-1](ai-infra/06-flashattention-compilation.md#ai-06-3)、[06.4 FlashAttention-2](ai-infra/06-flashattention-compilation.md#ai-06-4)、[06.5 FlashAttention-3](ai-infra/06-flashattention-compilation.md#ai-06-5)、[06.6 FlashAttention 的 Causal、Varlen 与 Packed 接口](ai-infra/06-flashattention-compilation.md#ai-06-6)。

(source-bagel)=
#### BAGEL implementation

**类型**：工程文档 · **年份/版本定位**：查阅 2026-10-02 · [一手入口](https://github.com/bytedance-seed/BAGEL)

**关联节点**：[03.5 Sequence Packing](ai-infra/03-data-sequence-packing.md#ai-03-5)、[03.6 Packed Attention Mask、Position IDs 与 Loss Mask](ai-infra/03-data-sequence-packing.md#ai-03-6)、[15.5 多模态 Sequence Packing](ai-infra/15-multimodal-bagel.md#ai-15-5)、[15.8 BAGEL 的理解与生成路径](ai-infra/15-multimodal-bagel.md#ai-15-8)。

(source-nsys)=
#### Nsight Systems

**类型**：工程文档 · **年份/版本定位**：查阅 2026-10-02 · [一手入口](https://docs.nvidia.com/nsight-systems/UserGuide/index.html)

**关联节点**：[03.8 数据读取、Prefetch 与 CPU→GPU Copy](ai-infra/03-data-sequence-packing.md#ai-03-8)、[04.9 PyTorch Profiler、Nsight Systems 与 Nsight Compute](ai-infra/04-gpu-profiling.md#ai-04-9)、[07.4 PCIe、NVLink、InfiniBand/RDMA](ai-infra/07-nccl-model-parallelism.md#ai-07-4)。

### 04 · GPU SM、Warp、显存与性能测量

(source-cuda)=
#### CUDA Programming Guide

**类型**：工程文档 · **年份/版本定位**：查阅 2026-10-02 · [一手入口](https://docs.nvidia.com/cuda/cuda-programming-guide/)

**关联节点**：[04.1 Grid、Block、Thread 与 Warp](ai-infra/04-gpu-profiling.md#ai-04-1)、[04.2 SM、Warp Scheduler 与 SIMT](ai-infra/04-gpu-profiling.md#ai-04-2)、[04.3 Registers、Shared Memory、L2 与 HBM](ai-infra/04-gpu-profiling.md#ai-04-3)、[04.4 Tensor Cores 与矩阵乘法指令](ai-infra/04-gpu-profiling.md#ai-04-4)、[05.1 CUDA Vector Add](ai-infra/05-cuda-triton-kernels.md#ai-05-1)。

(source-cuda-best)=
#### CUDA Best Practices

**类型**：工程文档 · **年份/版本定位**：查阅 2026-10-02 · [一手入口](https://docs.nvidia.com/cuda/cuda-c-best-practices-guide/)

**关联节点**：[04.2 SM、Warp Scheduler 与 SIMT](ai-infra/04-gpu-profiling.md#ai-04-2)、[04.3 Registers、Shared Memory、L2 与 HBM](ai-infra/04-gpu-profiling.md#ai-04-3)、[04.5 Coalesced Access 与 Memory Layout](ai-infra/04-gpu-profiling.md#ai-04-5)、[04.6 Occupancy、寄存器压力与 Latency Hiding](ai-infra/04-gpu-profiling.md#ai-04-6)、[04.8 CUDA Events、Warmup 与 Synchronization](ai-infra/04-gpu-profiling.md#ai-04-8)、[05.3 Reduction Kernel](ai-infra/05-cuda-triton-kernels.md#ai-05-3)、[05.8 Kernel Benchmark 与正确性比较](ai-infra/05-cuda-triton-kernels.md#ai-05-8)。

(source-cutlass)=
#### NVIDIA CUTLASS

**类型**：工程文档 · **年份/版本定位**：查阅 2026-10-02 · [一手入口](https://github.com/NVIDIA/cutlass)

**关联节点**：[04.4 Tensor Cores 与矩阵乘法指令](ai-infra/04-gpu-profiling.md#ai-04-4)、[05.5 Naive GEMM → Tiled GEMM](ai-infra/05-cuda-triton-kernels.md#ai-05-5)、[05.6 Tensor Core GEMM](ai-infra/05-cuda-triton-kernels.md#ai-05-6)、[12.8 Grouped GEMM 与 MoE Kernel](ai-infra/12-moe-expert-parallelism.md#ai-12-8)。

(source-ncu)=
#### Nsight Compute Profiling Guide

**类型**：工程文档 · **年份/版本定位**：查阅 2026-10-02 · [一手入口](https://docs.nvidia.com/nsight-compute/ProfilingGuide/index.html)

**关联节点**：[04.6 Occupancy、寄存器压力与 Latency Hiding](ai-infra/04-gpu-profiling.md#ai-04-6)、[04.9 PyTorch Profiler、Nsight Systems 与 Nsight Compute](ai-infra/04-gpu-profiling.md#ai-04-9)。

(source-roofline)=
#### Roofline performance model

**类型**：来源说明 · **年份/版本定位**：2009 模型；查阅 2026-10-02 · [一手入口](https://amcr.lbl.gov/departments/computer-science-department/ppan/roofline-performance-model/)

**关联节点**：[04.7 FLOPs、Bytes、Arithmetic Intensity 与 Roofline](ai-infra/04-gpu-profiling.md#ai-04-7)。

### 05 · 从 Vector Add 到 Triton Matmul

(source-triton)=
#### Triton kernel tutorials

**类型**：工程文档 · **年份/版本定位**：查阅 2026-10-02 · [一手入口](https://triton-lang.org/main/getting-started/tutorials/index.html)

**关联节点**：[05.2 Triton Vector Add](ai-infra/05-cuda-triton-kernels.md#ai-05-2)、[05.3 Reduction Kernel](ai-infra/05-cuda-triton-kernels.md#ai-05-3)、[05.4 Fused Softmax](ai-infra/05-cuda-triton-kernels.md#ai-05-4)、[05.5 Naive GEMM → Tiled GEMM](ai-infra/05-cuda-triton-kernels.md#ai-05-5)、[05.6 Tensor Core GEMM](ai-infra/05-cuda-triton-kernels.md#ai-05-6)、[05.7 RMSNorm/SwiGLU Fusion](ai-infra/05-cuda-triton-kernels.md#ai-05-7)、[05.8 Kernel Benchmark 与正确性比较](ai-infra/05-cuda-triton-kernels.md#ai-05-8)。

(source-lightseq2)=
#### LightSeq2

**类型**：论文 · **年份/版本定位**：2021 · [一手入口](https://arxiv.org/abs/2110.05722)

**关联节点**：[05.7 RMSNorm/SwiGLU Fusion](ai-infra/05-cuda-triton-kernels.md#ai-05-7)、[06.7 LightSeq / LightSeq2](ai-infra/06-flashattention-compilation.md#ai-06-7)。

### 06 · FlashAttention、LightSeq 与编译执行

(source-fa1)=
#### FlashAttention-1

**类型**：论文 · **年份/版本定位**：2022 · [一手入口](https://arxiv.org/abs/2205.14135)

**关联节点**：[06.1 标准 Attention 的显存与 IO](ai-infra/06-flashattention-compilation.md#ai-06-1)、[06.2 Online Softmax](ai-infra/06-flashattention-compilation.md#ai-06-2)、[06.3 FlashAttention-1](ai-infra/06-flashattention-compilation.md#ai-06-3)。

(source-fa2)=
#### FlashAttention-2

**类型**：论文 · **年份/版本定位**：2023 · [一手入口](https://arxiv.org/abs/2307.08691)

**关联节点**：[06.4 FlashAttention-2](ai-infra/06-flashattention-compilation.md#ai-06-4)。

(source-fa3)=
#### FlashAttention-3

**类型**：论文 · **年份/版本定位**：2024 · [一手入口](https://arxiv.org/abs/2407.08608)

**关联节点**：[06.5 FlashAttention-3](ai-infra/06-flashattention-compilation.md#ai-06-5)。

(source-lightseq)=
#### LightSeq

**类型**：论文 · **年份/版本定位**：2020 · [一手入口](https://arxiv.org/abs/2010.13887)

**关联节点**：[06.7 LightSeq / LightSeq2](ai-infra/06-flashattention-compilation.md#ai-06-7)。

(source-compile)=
#### torch.compile tutorial

**类型**：工程文档 · **年份/版本定位**：查阅 2026-10-02 · [一手入口](https://docs.pytorch.org/tutorials/intermediate/torch_compile_tutorial.html)

**关联节点**：[06.8 torch.compile、Fusion 与 Graph Break](ai-infra/06-flashattention-compilation.md#ai-06-8)。

(source-graphs)=
#### PyTorch CUDA Graphs

**类型**：工程文档 · **年份/版本定位**：查阅 2026-10-02 · [一手入口](https://docs.pytorch.org/docs/stable/notes/cuda#cuda-graphs)

**关联节点**：[06.9 CUDA Graph 与 JAX JIT](ai-infra/06-flashattention-compilation.md#ai-06-9)。

(source-jax)=
#### JAX JIT

**类型**：工程文档 · **年份/版本定位**：查阅 2026-10-02 · [一手入口](https://docs.jax.dev/en/latest/jit-compilation.html)

**关联节点**：[06.9 CUDA Graph 与 JAX JIT](ai-infra/06-flashattention-compilation.md#ai-06-9)。

### 07 · NCCL、DDP、Megatron 与 GPipe

(source-nccl)=
#### NCCL user guide

**类型**：工程文档 · **年份/版本定位**：查阅 2026-10-02 · [一手入口](https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/overview.html)

**关联节点**：[07.1 Send/Recv 与 Collective Communication](ai-infra/07-nccl-model-parallelism.md#ai-07-1)、[07.2 AllReduce、ReduceScatter 与 AllGather](ai-infra/07-nccl-model-parallelism.md#ai-07-2)、[07.3 Ring/Tree 与通信成本](ai-infra/07-nccl-model-parallelism.md#ai-07-3)、[07.4 PCIe、NVLink、InfiniBand/RDMA](ai-infra/07-nccl-model-parallelism.md#ai-07-4)、[07.11 DP×TP×PP 组合与 Rank Placement](ai-infra/07-nccl-model-parallelism.md#ai-07-11)。

(source-ddp-paper)=
#### PyTorch Distributed Data Parallel

**类型**：论文 · **年份/版本定位**：2020 · [一手入口](https://www.vldb.org/pvldb/vol13/p3005-li.pdf)

**关联节点**：[07.5 DDP](ai-infra/07-nccl-model-parallelism.md#ai-07-5)。

(source-megatron)=
#### Megatron-LM: Training Multi-Billion Parameter Language Models

**类型**：论文 · **年份/版本定位**：2019 · [一手入口](https://arxiv.org/abs/1909.08053)

**关联节点**：[07.6 Megatron Tensor Parallelism](ai-infra/07-nccl-model-parallelism.md#ai-07-6)。

(source-megatron-scale)=
#### Efficient Large-Scale Language Model Training Using Megatron-LM

**类型**：论文 · **年份/版本定位**：2021 · [一手入口](https://arxiv.org/abs/2104.04473)

**关联节点**：[07.6 Megatron Tensor Parallelism](ai-infra/07-nccl-model-parallelism.md#ai-07-6)、[07.8 PipeDream / 1F1B Schedule](ai-infra/07-nccl-model-parallelism.md#ai-07-8)、[07.9 Sequence Parallelism 与 Context Parallelism](ai-infra/07-nccl-model-parallelism.md#ai-07-9)、[13.7 MFU 与 Time-to-quality](ai-infra/13-scaling-evaluation.md#ai-13-7)。

(source-mcore)=
#### Megatron Core

**类型**：工程文档 · **年份/版本定位**：查阅 2026-10-02 · [一手入口](https://docs.nvidia.com/megatron-core/developer-guide/latest/index.html)

**关联节点**：[07.6 Megatron Tensor Parallelism](ai-infra/07-nccl-model-parallelism.md#ai-07-6)、[07.9 Sequence Parallelism 与 Context Parallelism](ai-infra/07-nccl-model-parallelism.md#ai-07-9)、[07.11 DP×TP×PP 组合与 Rank Placement](ai-infra/07-nccl-model-parallelism.md#ai-07-11)、[12.7 Expert Parallelism 与 AllToAll](ai-infra/12-moe-expert-parallelism.md#ai-12-7)、[12.8 Grouped GEMM 与 MoE Kernel](ai-infra/12-moe-expert-parallelism.md#ai-12-8)。

(source-gpipe)=
#### GPipe

**类型**：论文 · **年份/版本定位**：2018；NeurIPS 2019 · [一手入口](https://arxiv.org/abs/1811.06965)

**关联节点**：[07.7 GPipe 与 Pipeline Parallelism](ai-infra/07-nccl-model-parallelism.md#ai-07-7)。

(source-pipedream)=
#### PipeDream

**类型**：论文 · **年份/版本定位**：2018；SOSP 2019 · [一手入口](https://arxiv.org/abs/1806.03377)

**关联节点**：[07.8 PipeDream / 1F1B Schedule](ai-infra/07-nccl-model-parallelism.md#ai-07-8)。

(source-ring)=
#### Ring Attention with Blockwise Transformers

**类型**：论文 · **年份/版本定位**：2023 · [一手入口](https://arxiv.org/abs/2310.01889)

**关联节点**：[07.10 Ring Attention / Ulysses](ai-infra/07-nccl-model-parallelism.md#ai-07-10)。

(source-ulysses)=
#### DeepSpeed Ulysses

**类型**：论文 · **年份/版本定位**：2023 · [一手入口](https://arxiv.org/abs/2309.14509)

**关联节点**：[07.10 Ring Attention / Ulysses](ai-infra/07-nccl-model-parallelism.md#ai-07-10)。

### 08 · Activation Checkpointing、DeepSpeed ZeRO 与 FSDP

(source-zero)=
#### ZeRO

**类型**：论文 · **年份/版本定位**：2019；SC 2020 · [一手入口](https://arxiv.org/abs/1910.02054)

**关联节点**：[08.1 训练显存账本](ai-infra/08-zero-fsdp-memory.md#ai-08-1)、[08.3 ZeRO-1](ai-infra/08-zero-fsdp-memory.md#ai-08-3)、[08.4 ZeRO-2](ai-infra/08-zero-fsdp-memory.md#ai-08-4)、[08.5 ZeRO-3](ai-infra/08-zero-fsdp-memory.md#ai-08-5)。

(source-checkpoint-paper)=
#### Training Deep Nets with Sublinear Memory Cost

**类型**：论文 · **年份/版本定位**：2016 · [一手入口](https://arxiv.org/abs/1604.06174)

**关联节点**：[08.2 Activation Checkpointing](ai-infra/08-zero-fsdp-memory.md#ai-08-2)。

(source-checkpoint)=
#### PyTorch activation checkpoint

**类型**：工程文档 · **年份/版本定位**：查阅 2026-10-02 · [一手入口](https://docs.pytorch.org/docs/stable/checkpoint)

**关联节点**：[08.2 Activation Checkpointing](ai-infra/08-zero-fsdp-memory.md#ai-08-2)、[16.9 Diffusion 的训练 Batch、混合精度与 Checkpointing](ai-infra/16-diffusion-dit.md#ai-16-9)。

(source-deepspeed)=
#### DeepSpeed ZeRO

**类型**：工程文档 · **年份/版本定位**：查阅 2026-10-02 · [一手入口](https://deepspeed.readthedocs.io/en/latest/zero3.html)

**关联节点**：[08.3 ZeRO-1](ai-infra/08-zero-fsdp-memory.md#ai-08-3)、[08.4 ZeRO-2](ai-infra/08-zero-fsdp-memory.md#ai-08-4)、[08.5 ZeRO-3](ai-infra/08-zero-fsdp-memory.md#ai-08-5)、[08.7 CPU/NVMe Offload](ai-infra/08-zero-fsdp-memory.md#ai-08-7)。

(source-fsdp)=
#### PyTorch FSDP2 tutorial

**类型**：工程文档 · **年份/版本定位**：查阅 2026-10-02 · [一手入口](https://docs.pytorch.org/tutorials/intermediate/FSDP_tutorial.html)

**关联节点**：[08.6 FSDP / FSDP2](ai-infra/08-zero-fsdp-memory.md#ai-08-6)。

(source-zero-offload)=
#### ZeRO-Offload

**类型**：论文 · **年份/版本定位**：2021 · [一手入口](https://arxiv.org/abs/2101.06840)

**关联节点**：[08.7 CPU/NVMe Offload](ai-infra/08-zero-fsdp-memory.md#ai-08-7)。

(source-zero-infinity)=
#### ZeRO-Infinity

**类型**：论文 · **年份/版本定位**：2021 · [一手入口](https://arxiv.org/abs/2104.07857)

**关联节点**：[08.7 CPU/NVMe Offload](ai-infra/08-zero-fsdp-memory.md#ai-08-7)。

(source-dcp)=
#### PyTorch Distributed Checkpoint

**类型**：工程文档 · **年份/版本定位**：查阅 2026-10-02 · [一手入口](https://docs.pytorch.org/tutorials/recipes/distributed_checkpoint_recipe.html)

**关联节点**：[08.8 Distributed Checkpoint](ai-infra/08-zero-fsdp-memory.md#ai-08-8)。

### 09 · GPTQ、AWQ、FP8、LoRA 与 QLoRA

(source-gptq)=
#### GPTQ

**类型**：论文 · **年份/版本定位**：2022；ICLR 2023 · [一手入口](https://arxiv.org/abs/2210.17323)

**关联节点**：[09.1 Quantization 的 Scale、Zero Point 与 Granularity](ai-infra/09-quantization-peft.md#ai-09-1)、[09.2 PTQ 与 QAT](ai-infra/09-quantization-peft.md#ai-09-2)、[09.3 GPTQ](ai-infra/09-quantization-peft.md#ai-09-3)。

(source-smoothquant)=
#### SmoothQuant

**类型**：论文 · **年份/版本定位**：2022；ICML 2023 · [一手入口](https://arxiv.org/abs/2211.10438)

**关联节点**：[09.2 PTQ 与 QAT](ai-infra/09-quantization-peft.md#ai-09-2)、[09.4 SmoothQuant](ai-infra/09-quantization-peft.md#ai-09-4)。

(source-awq)=
#### AWQ

**类型**：论文 · **年份/版本定位**：2023；MLSys 2024 · [一手入口](https://arxiv.org/abs/2306.00978)

**关联节点**：[09.5 AWQ](ai-infra/09-quantization-peft.md#ai-09-5)、[09.9 Quantized Kernel 与模型质量验证](ai-infra/09-quantization-peft.md#ai-09-9)。

(source-transformer-engine)=
#### NVIDIA Transformer Engine

**类型**：工程文档 · **年份/版本定位**：查阅 2026-10-02 · [一手入口](https://docs.nvidia.com/deeplearning/transformer-engine/getting_started/index.html)

**关联节点**：[09.6 FP8、Weight/Activation/KV Quantization](ai-infra/09-quantization-peft.md#ai-09-6)。

(source-vllm)=
#### vLLM architecture

**类型**：工程文档 · **年份/版本定位**：查阅 2026-10-02 · [一手入口](https://docs.vllm.ai/en/latest/design/arch_overview/)

**关联节点**：[09.6 FP8、Weight/Activation/KV Quantization](ai-infra/09-quantization-peft.md#ai-09-6)、[09.9 Quantized Kernel 与模型质量验证](ai-infra/09-quantization-peft.md#ai-09-9)、[10.2 Prefill 与 Decode](ai-infra/10-kv-cache-decoding.md#ai-10-2)、[10.3 KV Cache](ai-infra/10-kv-cache-decoding.md#ai-10-3)、[11.1 Static Batching → Continuous Batching](ai-infra/11-vllm-serving.md#ai-11-1)、[11.3 PagedAttention](ai-infra/11-vllm-serving.md#ai-11-3)、[11.4 vLLM Scheduler → KV Manager → Model Runner](ai-infra/11-vllm-serving.md#ai-11-4)、[11.5 Chunked Prefill](ai-infra/11-vllm-serving.md#ai-11-5)、[11.6 Prefix Caching / SGLang RadixAttention](ai-infra/11-vllm-serving.md#ai-11-6)、[11.7 抢占、Recompute 与 KV 回收](ai-infra/11-vllm-serving.md#ai-11-7)、[11.8 Speculative Decoding](ai-infra/11-vllm-serving.md#ai-11-8)、[15.7 多模态 Prefill、Encoder Cache 与请求 Batch](ai-infra/15-multimodal-bagel.md#ai-15-7)。

(source-lora)=
#### LoRA

**类型**：论文 · **年份/版本定位**：2021；ICLR 2022 · [一手入口](https://arxiv.org/abs/2106.09685)

**关联节点**：[09.7 Adapters 与 LoRA](ai-infra/09-quantization-peft.md#ai-09-7)。

(source-peft)=
#### Hugging Face PEFT

**类型**：工程文档 · **年份/版本定位**：查阅 2026-10-02 · [一手入口](https://huggingface.co/docs/peft/index)

**关联节点**：[09.7 Adapters 与 LoRA](ai-infra/09-quantization-peft.md#ai-09-7)、[09.8 QLoRA](ai-infra/09-quantization-peft.md#ai-09-8)。

(source-qlora)=
#### QLoRA

**类型**：论文 · **年份/版本定位**：2023 · [一手入口](https://arxiv.org/abs/2305.14314)

**关联节点**：[09.8 QLoRA](ai-infra/09-quantization-peft.md#ai-09-8)。

### 10 · Prefill、Decode、KV Cache 与长上下文

(source-paged)=
#### PagedAttention / vLLM

**类型**：论文 · **年份/版本定位**：2023 · [一手入口](https://arxiv.org/abs/2309.06180)

**关联节点**：[10.2 Prefill 与 Decode](ai-infra/10-kv-cache-decoding.md#ai-10-2)、[10.3 KV Cache](ai-infra/10-kv-cache-decoding.md#ai-10-3)、[10.4 KV Cache 显存估算](ai-infra/10-kv-cache-decoding.md#ai-10-4)、[11.3 PagedAttention](ai-infra/11-vllm-serving.md#ai-11-3)。

(source-mqa)=
#### Fast Transformer Decoding: One Write-Head is All You Need / MQA

**类型**：论文 · **年份/版本定位**：2019 · [一手入口](https://arxiv.org/abs/1911.02150)

**关联节点**：[10.5 MHA → MQA → GQA](ai-infra/10-kv-cache-decoding.md#ai-10-5)。

(source-gqa)=
#### GQA

**类型**：论文 · **年份/版本定位**：2023 · [一手入口](https://arxiv.org/abs/2305.13245)

**关联节点**：[10.5 MHA → MQA → GQA](ai-infra/10-kv-cache-decoding.md#ai-10-5)。

(source-deepseek2)=
#### DeepSeek-V2 / MLA

**类型**：论文 · **年份/版本定位**：2024 · [一手入口](https://arxiv.org/abs/2405.04434)

**关联节点**：[10.6 MLA](ai-infra/10-kv-cache-decoding.md#ai-10-6)。

(source-sinks)=
#### StreamingLLM / Attention Sinks

**类型**：论文 · **年份/版本定位**：2023 · [一手入口](https://arxiv.org/abs/2309.17453)

**关联节点**：[10.7 Sliding-window Attention 与 Attention Sinks](ai-infra/10-kv-cache-decoding.md#ai-10-7)。

### 11 · PagedAttention、vLLM、SGLang 与 DistServe

(source-orca)=
#### Orca

**类型**：论文 · **年份/版本定位**：2022 · [一手入口](https://www.usenix.org/conference/osdi22/presentation/yu)

**关联节点**：[11.1 Static Batching → Continuous Batching](ai-infra/11-vllm-serving.md#ai-11-1)、[11.2 Orca](ai-infra/11-vllm-serving.md#ai-11-2)。

(source-sglang-paper)=
#### SGLang / RadixAttention

**类型**：论文 · **年份/版本定位**：2023；NeurIPS 2024 · [一手入口](https://arxiv.org/abs/2312.07104)

**关联节点**：[11.6 Prefix Caching / SGLang RadixAttention](ai-infra/11-vllm-serving.md#ai-11-6)。

(source-sglang)=
#### SGLang documentation

**类型**：工程文档 · **年份/版本定位**：查阅 2026-10-02 · [一手入口](https://docs.sglang.io/)

**关联节点**：[11.6 Prefix Caching / SGLang RadixAttention](ai-infra/11-vllm-serving.md#ai-11-6)。

(source-speculative)=
#### Fast Inference from Transformers via Speculative Decoding

**类型**：论文 · **年份/版本定位**：2022；ICML 2023 · [一手入口](https://arxiv.org/abs/2211.17192)

**关联节点**：[11.8 Speculative Decoding](ai-infra/11-vllm-serving.md#ai-11-8)。

(source-cachegen)=
#### CacheGen

**类型**：论文 · **年份/版本定位**：2023；SIGCOMM 2024 · [一手入口](https://arxiv.org/abs/2310.07240)

**关联节点**：[11.9 CacheGen 与分层 KV Cache](ai-infra/11-vllm-serving.md#ai-11-9)。

(source-lmcache)=
#### LMCache documentation

**类型**：工程文档 · **年份/版本定位**：查阅 2026-10-02 · [一手入口](https://docs.lmcache.ai/)

**关联节点**：[11.9 CacheGen 与分层 KV Cache](ai-infra/11-vllm-serving.md#ai-11-9)。

(source-distserve)=
#### DistServe

**类型**：论文 · **年份/版本定位**：2024 · [一手入口](https://arxiv.org/abs/2401.09670)

**关联节点**：[11.10 DistServe / Prefill–Decode Disaggregation](ai-infra/11-vllm-serving.md#ai-11-10)。

(source-dynamo)=
#### NVIDIA Dynamo architecture

**类型**：工程文档 · **年份/版本定位**：查阅 2026-10-02 · [一手入口](https://docs.nvidia.com/dynamo/dev/knowledge-base/concepts/architecture)

**关联节点**：[11.10 DistServe / Prefill–Decode Disaggregation](ai-infra/11-vllm-serving.md#ai-11-10)、[11.12 Triton Inference Server、LightLLM 与 Dynamo](ai-infra/11-vllm-serving.md#ai-11-12)。

(source-vllm-metrics)=
#### vLLM metrics

**类型**：工程文档 · **年份/版本定位**：查阅 2026-10-02 · [一手入口](https://docs.vllm.ai/en/latest/usage/metrics/)

**关联节点**：[11.11 TTFT、TPOT、吞吐与尾延迟](ai-infra/11-vllm-serving.md#ai-11-11)。

(source-server)=
#### Triton Inference Server

**类型**：工程文档 · **年份/版本定位**：查阅 2026-10-02 · [一手入口](https://github.com/triton-inference-server/server)

**关联节点**：[11.12 Triton Inference Server、LightLLM 与 Dynamo](ai-infra/11-vllm-serving.md#ai-11-12)。

(source-lightllm)=
#### LightLLM implementation

**类型**：工程文档 · **年份/版本定位**：查阅 2026-10-02 · [一手入口](https://github.com/ModelTC/lightllm)

**关联节点**：[11.12 Triton Inference Server、LightLLM 与 Dynamo](ai-infra/11-vllm-serving.md#ai-11-12)。

### 12 · GShard、Switch Transformer 与 DeepSeek MoE

(source-switch)=
#### Switch Transformers

**类型**：论文 · **年份/版本定位**：2021 · [一手入口](https://arxiv.org/abs/2101.03961)

**关联节点**：[12.1 Dense FFN → MoE Experts](ai-infra/12-moe-expert-parallelism.md#ai-12-1)、[12.2 Router 与 Top-k Routing](ai-infra/12-moe-expert-parallelism.md#ai-12-2)、[12.3 Capacity、Token Dropping 与 Dropless MoE](ai-infra/12-moe-expert-parallelism.md#ai-12-3)、[12.4 Load-balancing Loss 与 Router 稳定性](ai-infra/12-moe-expert-parallelism.md#ai-12-4)、[12.5 GShard / Switch Transformer](ai-infra/12-moe-expert-parallelism.md#ai-12-5)。

(source-gshard)=
#### GShard

**类型**：论文 · **年份/版本定位**：2020；ICLR 2021 · [一手入口](https://arxiv.org/abs/2006.16668)

**关联节点**：[12.2 Router 与 Top-k Routing](ai-infra/12-moe-expert-parallelism.md#ai-12-2)、[12.5 GShard / Switch Transformer](ai-infra/12-moe-expert-parallelism.md#ai-12-5)。

(source-dsmoe)=
#### DeepSpeed-MoE

**类型**：论文 · **年份/版本定位**：2022 · [一手入口](https://arxiv.org/abs/2201.05596)

**关联节点**：[12.3 Capacity、Token Dropping 与 Dropless MoE](ai-infra/12-moe-expert-parallelism.md#ai-12-3)、[12.7 Expert Parallelism 与 AllToAll](ai-infra/12-moe-expert-parallelism.md#ai-12-7)、[12.9 DeepSpeed-MoE / DeepSeek-V3](ai-infra/12-moe-expert-parallelism.md#ai-12-9)。

(source-deepseek3)=
#### DeepSeek-V3 Technical Report

**类型**：论文 · **年份/版本定位**：2024 · [一手入口](https://arxiv.org/abs/2412.19437)

**关联节点**：[12.4 Load-balancing Loss 与 Router 稳定性](ai-infra/12-moe-expert-parallelism.md#ai-12-4)、[12.9 DeepSpeed-MoE / DeepSeek-V3](ai-infra/12-moe-expert-parallelism.md#ai-12-9)。

(source-deepseekmoe)=
#### DeepSeekMoE

**类型**：论文 · **年份/版本定位**：2024 · [一手入口](https://arxiv.org/abs/2401.06066)

**关联节点**：[12.6 DeepSeek MoE](ai-infra/12-moe-expert-parallelism.md#ai-12-6)。

(source-ds-moe-code)=
#### DeepSpeed MoE

**类型**：工程文档 · **年份/版本定位**：查阅 2026-10-02 · [一手入口](https://www.deepspeed.ai/tutorials/mixture-of-experts/)

**关联节点**：[12.9 DeepSpeed-MoE / DeepSeek-V3](ai-infra/12-moe-expert-parallelism.md#ai-12-9)。

### 13 · Scaling Laws、Chinchilla 与模型评估

(source-kaplan)=
#### Scaling Laws for Neural Language Models

**类型**：论文 · **年份/版本定位**：2020 · [一手入口](https://arxiv.org/abs/2001.08361)

**关联节点**：[13.1 参数量、Token 数与训练 FLOPs](ai-infra/13-scaling-evaluation.md#ai-13-1)、[13.2 Kaplan Scaling Laws](ai-infra/13-scaling-evaluation.md#ai-13-2)、[13.4 Learning Rate、Batch Size 与训练长度](ai-infra/13-scaling-evaluation.md#ai-13-4)。

(source-chinchilla)=
#### Training Compute-Optimal Large Language Models / Chinchilla

**类型**：论文 · **年份/版本定位**：2022 · [一手入口](https://arxiv.org/abs/2203.15556)

**关联节点**：[13.3 Chinchilla](ai-infra/13-scaling-evaluation.md#ai-13-3)、[13.4 Learning Rate、Batch Size 与训练长度](ai-infra/13-scaling-evaluation.md#ai-13-4)。

### 14 · SFT、DPO、PPO、GRPO 与 RLHF 系统

(source-instructgpt)=
#### InstructGPT

**类型**：论文 · **年份/版本定位**：2022 · [一手入口](https://arxiv.org/abs/2203.02155)

**关联节点**：[14.1 SFT](ai-infra/14-post-training-rlhf.md#ai-14-1)、[14.2 Preference Data 与 Reward Model](ai-infra/14-post-training-rlhf.md#ai-14-2)、[14.4 PPO / InstructGPT](ai-infra/14-post-training-rlhf.md#ai-14-4)。

(source-dpo)=
#### Direct Preference Optimization

**类型**：论文 · **年份/版本定位**：2023 · [一手入口](https://arxiv.org/abs/2305.18290)

**关联节点**：[14.3 DPO](ai-infra/14-post-training-rlhf.md#ai-14-3)。

(source-ppo)=
#### Proximal Policy Optimization Algorithms

**类型**：论文 · **年份/版本定位**：2017 · [一手入口](https://arxiv.org/abs/1707.06347)

**关联节点**：[14.4 PPO / InstructGPT](ai-infra/14-post-training-rlhf.md#ai-14-4)。

(source-grpo)=
#### DeepSeekMath / GRPO

**类型**：论文 · **年份/版本定位**：2024 · [一手入口](https://arxiv.org/abs/2402.03300)

**关联节点**：[14.5 GRPO / RLVR](ai-infra/14-post-training-rlhf.md#ai-14-5)。

(source-realhf)=
#### ReaL / ReaLHF

**类型**：论文 · **年份/版本定位**：2024 · [一手入口](https://arxiv.org/abs/2406.14088)

**关联节点**：[14.6 Rollout Engine 与权重同步](ai-infra/14-post-training-rlhf.md#ai-14-6)、[14.7 ReaLHF / verl](ai-infra/14-post-training-rlhf.md#ai-14-7)。

(source-verl)=
#### verl documentation

**类型**：工程文档 · **年份/版本定位**：查阅 2026-10-02 · [一手入口](https://verl.readthedocs.io/en/latest/)

**关联节点**：[14.6 Rollout Engine 与权重同步](ai-infra/14-post-training-rlhf.md#ai-14-6)、[14.7 ReaLHF / verl](ai-infra/14-post-training-rlhf.md#ai-14-7)、[14.8 同步/异步 Rollout 与策略版本](ai-infra/14-post-training-rlhf.md#ai-14-8)。

(source-hybridflow)=
#### HybridFlow / verl

**类型**：论文 · **年份/版本定位**：2024 · [一手入口](https://arxiv.org/abs/2409.19256)

**关联节点**：[14.7 ReaLHF / verl](ai-infra/14-post-training-rlhf.md#ai-14-7)、[14.8 同步/异步 Rollout 与策略版本](ai-infra/14-post-training-rlhf.md#ai-14-8)。

### 15 · ViT、Flamingo、LLaVA、Qwen-VL 与 BAGEL

(source-vit)=
#### An Image is Worth 16x16 Words / ViT

**类型**：论文 · **年份/版本定位**：2020；ICLR 2021 · [一手入口](https://arxiv.org/abs/2010.11929)

**关联节点**：[15.1 ViT 与 Patch Tokens](ai-infra/15-multimodal-bagel.md#ai-15-1)、[15.6 视觉 Token 数量与显存/Attention 成本](ai-infra/15-multimodal-bagel.md#ai-15-6)。

(source-flamingo)=
#### Flamingo

**类型**：论文 · **年份/版本定位**：2022 · [一手入口](https://arxiv.org/abs/2204.14198)

**关联节点**：[15.2 Projector 与 Cross-attention](ai-infra/15-multimodal-bagel.md#ai-15-2)、[15.3 Flamingo / LLaVA](ai-infra/15-multimodal-bagel.md#ai-15-3)。

(source-llava)=
#### Visual Instruction Tuning / LLaVA

**类型**：论文 · **年份/版本定位**：2023 · [一手入口](https://arxiv.org/abs/2304.08485)

**关联节点**：[15.2 Projector 与 Cross-attention](ai-infra/15-multimodal-bagel.md#ai-15-2)、[15.3 Flamingo / LLaVA](ai-infra/15-multimodal-bagel.md#ai-15-3)。

(source-qwen2vl)=
#### Qwen2-VL

**类型**：论文 · **年份/版本定位**：2024 · [一手入口](https://arxiv.org/abs/2409.12191)

**关联节点**：[15.4 Qwen-VL 风格动态分辨率与多模态位置编码](ai-infra/15-multimodal-bagel.md#ai-15-4)、[15.6 视觉 Token 数量与显存/Attention 成本](ai-infra/15-multimodal-bagel.md#ai-15-6)、[15.9 Video Tokens 与时空 Attention](ai-infra/15-multimodal-bagel.md#ai-15-9)。

### 16 · DDPM、Latent Diffusion、DiT 与扩散推理加速

(source-ddpm)=
#### Denoising Diffusion Probabilistic Models / DDPM

**类型**：论文 · **年份/版本定位**：2020 · [一手入口](https://arxiv.org/abs/2006.11239)

**关联节点**：[16.1 DDPM](ai-infra/16-diffusion-dit.md#ai-16-1)。

(source-ddim)=
#### Denoising Diffusion Implicit Models / DDIM

**类型**：论文 · **年份/版本定位**：2020；ICLR 2021 · [一手入口](https://arxiv.org/abs/2010.02502)

**关联节点**：[16.2 DDIM / DPM-Solver](ai-infra/16-diffusion-dit.md#ai-16-2)。

(source-dpmsolver)=
#### DPM-Solver

**类型**：论文 · **年份/版本定位**：2022 · [一手入口](https://arxiv.org/abs/2206.00927)

**关联节点**：[16.2 DDIM / DPM-Solver](ai-infra/16-diffusion-dit.md#ai-16-2)。

(source-ldm)=
#### Latent Diffusion Models

**类型**：论文 · **年份/版本定位**：2021；CVPR 2022 · [一手入口](https://arxiv.org/abs/2112.10752)

**关联节点**：[16.3 Latent Diffusion 与 VAE](ai-infra/16-diffusion-dit.md#ai-16-3)。

(source-dit)=
#### Scalable Diffusion Models with Transformers / DiT

**类型**：论文 · **年份/版本定位**：2022；ICCV 2023 · [一手入口](https://arxiv.org/abs/2212.09748)

**关联节点**：[16.4 DiT](ai-infra/16-diffusion-dit.md#ai-16-4)、[16.8 Image/Video Diffusion 的计算与显存账本](ai-infra/16-diffusion-dit.md#ai-16-8)、[16.9 Diffusion 的训练 Batch、混合精度与 Checkpointing](ai-infra/16-diffusion-dit.md#ai-16-9)。

(source-cfg)=
#### Classifier-Free Diffusion Guidance

**类型**：论文 · **年份/版本定位**：2022 · [一手入口](https://arxiv.org/abs/2207.12598)

**关联节点**：[16.5 Classifier-free Guidance](ai-infra/16-diffusion-dit.md#ai-16-5)。

(source-flow)=
#### Flow Matching for Generative Modeling

**类型**：论文 · **年份/版本定位**：2022 · [一手入口](https://arxiv.org/abs/2210.02747)

**关联节点**：[16.6 Flow Matching / Rectified Flow](ai-infra/16-diffusion-dit.md#ai-16-6)。

(source-rectified)=
#### Flow Straight and Fast / Rectified Flow

**类型**：论文 · **年份/版本定位**：2022 · [一手入口](https://arxiv.org/abs/2209.03003)

**关联节点**：[16.6 Flow Matching / Rectified Flow](ai-infra/16-diffusion-dit.md#ai-16-6)。

(source-mmdit)=
#### Scaling Rectified Flow Transformers / MMDiT

**类型**：论文 · **年份/版本定位**：2024 · [一手入口](https://arxiv.org/abs/2403.03206)

**关联节点**：[16.7 MMDiT](ai-infra/16-diffusion-dit.md#ai-16-7)。

(source-xdit)=
#### xDiT implementation

**类型**：工程文档 · **年份/版本定位**：查阅 2026-10-02 · [一手入口](https://github.com/xdit-project/xDiT)

**关联节点**：[16.8 Image/Video Diffusion 的计算与显存账本](ai-infra/16-diffusion-dit.md#ai-16-8)、[16.10 DistriFusion / PipeFusion](ai-infra/16-diffusion-dit.md#ai-16-10)、[16.12 Diffusers / xDiT 的执行优化](ai-infra/16-diffusion-dit.md#ai-16-12)。

(source-distrifusion)=
#### DistriFusion

**类型**：论文 · **年份/版本定位**：2024 · [一手入口](https://arxiv.org/abs/2402.19481)

**关联节点**：[16.10 DistriFusion / PipeFusion](ai-infra/16-diffusion-dit.md#ai-16-10)。

(source-pipefusion)=
#### PipeFusion

**类型**：论文 · **年份/版本定位**：2024 · [一手入口](https://arxiv.org/abs/2405.14430)

**关联节点**：[16.10 DistriFusion / PipeFusion](ai-infra/16-diffusion-dit.md#ai-16-10)。

(source-teacache)=
#### Timestep Embedding Tells / TeaCache

**类型**：论文 · **年份/版本定位**：2024；CVPR 2025 · [一手入口](https://arxiv.org/abs/2411.19108)

**关联节点**：[16.11 TeaCache](ai-infra/16-diffusion-dit.md#ai-16-11)。

(source-tea-code)=
#### TeaCache implementation

**类型**：工程文档 · **年份/版本定位**：查阅 2026-10-02 · [一手入口](https://github.com/ali-vilab/TeaCache)

**关联节点**：[16.11 TeaCache](ai-infra/16-diffusion-dit.md#ai-16-11)。

(source-diffusers)=
#### Diffusers memory optimization

**类型**：工程文档 · **年份/版本定位**：查阅 2026-10-02 · [一手入口](https://huggingface.co/docs/diffusers/main/optimization/memory)

**关联节点**：[16.12 Diffusers / xDiT 的执行优化](ai-infra/16-diffusion-dit.md#ai-16-12)。

## 核查的实际边界

本轮核对公开大纲、链接、题名和主题定位，未把未公开的嘉宾讲义补成已读材料，也未进行学习实验。CS336/CMU 课次覆盖与具体节点逐项关联；新版本 API 的运行行为须由未来实验确认。论文中的机器、速度和质量数值没有转写成本仓库实测。

个人 Notion 旧笔记仅作为回顾线索；本页使用公开一手入口，没有复制私人笔记正文或把模型生成解释标作学习者自己的复述。
