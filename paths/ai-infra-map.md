---
title: '学习地图：CS336 × CMU 11-868'
description: 16 章、143 个具体技术节点，连接课程、论文、实现与先修关系。
---

# 学习地图：CS336 × CMU 11-868

主要导航现为 [topic 分类](../topics/README.md)；本页保留课程材料节点与先修链。[Ray Core](../topics/distributed-runtime/ray/cpu.ipynb)作为独立运行时主题接入，先修从 Task、ObjectRef 与 Actor 展开。

**章用于分组，section 是实际学习节点。** 本地图按已确定的范围整理为 **16 章、143 个 section**：LLM 训练与推理，以及 MoE、多模态、diffusion。每个 section 用技术名与具体问题命名，点开后可以看到先修、课程出处、论文/实现和后续验证。

主干来自 [CS336 Spring 2025](https://cs336.stanford.edu/spring2025/) 与 [CMU 11-868 Spring 2025 官方大纲](https://llmsystem.github.io/llmsystem2025spring/docs/Syllabus/)；多模态和 diffusion 用 [CMU Generative AI](https://www.cs.cmu.edu/~mgormley/courses/10423-s25/schedule.html)、原始论文和官方实现补充。

[课程、论文与工程来源](ai-infra-sources.md) · [开始一次学习](start-here.md) · [问题与认知边界](../GAPS.md)

## 如何读这张地图

当前先建立概念位置与联系。目录和验证方案不表示已经掌握、精读或运行。课程拆分保留原课材料入口；论文、工程和补充课程节点分别标注。数学、OS、网络前提在相关节点按需回顾。

| 回顾路径 | 入口与顺序 |
| --- | --- |
| 共同底座 | 01–06：文本/模型 → Tensor/训练 → 数据组织 → GPU/测量 → kernel → Attention/编译 |
| 训练主线 | 07–09：通信/并行 → 状态与显存 → 量化/适配；再连接 12–14 |
| 推理主线 | 10–11：生成/KV → 缓存/调度/服务；连接量化与 MoE |
| 多模态与 diffusion | 15–16：复用 token、mask、Attention、并行与训练节点 |

编号是定位工具。先修链接比章号更准确：例如 Attention 需要回顾 Tensor 运算，BAGEL 的生成路径要连接后面的 DiT/Flow Matching。两条主线的先后可随实际问题调整。

## 两条具体的先修链

- **FlashAttention-1**：[01.5 Causal Attention、Q/K/V 与 Multi-head Attention](ai-infra/01-tokenizer-transformer.md#ai-01-5)、[04.3 Registers、Shared Memory、L2 与 HBM](ai-infra/04-gpu-profiling.md#ai-04-3)、[05.5 Naive GEMM → Tiled GEMM](ai-infra/05-cuda-triton-kernels.md#ai-05-5)、[06.2 Online Softmax](ai-infra/06-flashattention-compilation.md#ai-06-2) → [06.3 FlashAttention-1](ai-infra/06-flashattention-compilation.md#ai-06-3)。
- **PagedAttention**：[10.2 Prefill 与 Decode](ai-infra/10-kv-cache-decoding.md#ai-10-2) → [10.3 KV Cache](ai-infra/10-kv-cache-decoding.md#ai-10-3) / [10.4 KV Cache 显存估算](ai-infra/10-kv-cache-decoding.md#ai-10-4) → [11.3 PagedAttention](ai-infra/11-vllm-serving.md#ai-11-3) → [11.4 vLLM Scheduler → KV Manager → Model Runner](ai-infra/11-vllm-serving.md#ai-11-4)。

下面的每一项都是可以独立进入的具体节点。

## 01 · BPE、Tokenizer 与 LLaMA 风格 Transformer

[进入本章](ai-infra/01-tokenizer-transformer.md) · 8 个 section

- **[01.1 Byte-level BPE](ai-infra/01-tokenizer-transformer.md#ai-01-1)**：词表与 merge 规则怎样把字节序列变成 token，又怎样还原？
- **[01.2 SentencePiece](ai-infra/01-tokenizer-transformer.md#ai-01-2)**：SentencePiece 的文本处理与分词算法是什么关系，为什么不能把它直接等同于 BPE？
- **[01.3 Special Tokens、BOS/EOS 与 Chat Template](ai-infra/01-tokenizer-transformer.md#ai-01-3)**：同一段对话怎样因模板和特殊 token 变成不同的模型输入？
- **[01.4 Decoder-only Transformer](ai-infra/01-tokenizer-transformer.md#ai-01-4)**：一个 decoder block 的输入、输出与每层 tensor shape 怎样对应？
- **[01.5 Causal Attention、Q/K/V 与 Multi-head Attention](ai-infra/01-tokenizer-transformer.md#ai-01-5)**：mask 和 head 怎样参与 QK、softmax 与 AV，哪些 token 能看到哪些 token？
- **[01.6 RoPE 与位置编码](ai-infra/01-tokenizer-transformer.md#ai-01-6)**：位置怎样进入 Q/K，哪些变换取决于 token 的位置？
- **[01.7 RMSNorm、SwiGLU 与 Residual Connection](ai-infra/01-tokenizer-transformer.md#ai-01-7)**：Norm、FFN 与 residual 分别放在哪里，怎样改变 shape 和计算？
- **[01.8 GPT/LLaMA 模型配置](ai-infra/01-tokenizer-transformer.md#ai-01-8)**：层数、宽度、head 与词表怎样决定参数量和主要计算？

## 02 · PyTorch Tensor、Autograd 与一次训练更新

[进入本章](ai-infra/02-pytorch-training-step.md) · 8 个 section

- **[02.1 Tensor Storage、Stride、View 与 Contiguous](ai-infra/02-pytorch-training-step.md#ai-02-1)**：reshape、transpose 与 view 何时共享存储，何时产生拷贝？
- **[02.2 Broadcasting、Matmul 与 Einsum](ai-infra/02-pytorch-training-step.md#ai-02-2)**：怎样从表达式追踪 shape，避免把广播与矩阵乘法混淆？
- **[02.3 Autograd 与 Backward Graph](ai-infra/02-pytorch-training-step.md#ai-02-3)**：一个输入通过多条路径影响 loss 时，梯度怎样累加？
- **[02.4 Saved Tensors 与显存生命周期](ai-infra/02-pytorch-training-step.md#ai-02-4)**：backward 为什么需要某些前向结果，它们什么时候能够释放？
- **[02.5 Cross-entropy 与 Next-token Prediction](ai-infra/02-pytorch-training-step.md#ai-02-5)**：输入、标签移位、padding 与 loss mask 怎样定义训练目标？
- **[02.6 AdamW](ai-infra/02-pytorch-training-step.md#ai-02-6)**：参数、梯度、动量与二阶状态怎样完成一次更新？
- **[02.7 Gradient Accumulation](ai-infra/02-pytorch-training-step.md#ai-02-7)**：多个 microbatch 怎样组成一次 optimizer step，loss 的权重怎样对齐？
- **[02.8 FP32、FP16、BF16 与 AMP](ai-infra/02-pytorch-training-step.md#ai-02-8)**：存储、计算与累加采用不同 dtype 时，何处可能溢出或损失精度？

## 03 · 预训练数据、Padding 与 Sequence Packing

[进入本章](ai-infra/03-data-sequence-packing.md) · 8 个 section

- **[03.1 文本清洗、质量过滤与去重](ai-infra/03-data-sequence-packing.md#ai-03-1)**：哪些预处理改变训练分布，哪些重复可能影响数据划分与评估？
- **[03.2 数据混合与 Sampling](ai-infra/03-data-sequence-packing.md#ai-03-2)**：不同数据来源如何进入训练，抽样比例与实际 token 比例为何可能不同？
- **[03.3 Tokenization、Dataset Sharding 与 DataLoader](ai-infra/03-data-sequence-packing.md#ai-03-3)**：原始文本怎样成为各 worker 消费的 token batch，哪里可能重读或漏读？
- **[03.4 Padding、Length Bucketing 与有效 Token 比例](ai-infra/03-data-sequence-packing.md#ai-03-4)**：按长度组织 batch 能减少哪些浪费，又可能改变什么采样行为？
- **[03.5 Sequence Packing](ai-infra/03-data-sequence-packing.md#ai-03-5)**：拼接样本以后，哪些 attention、位置与 loss 规则必须由任务明确？
- **[03.6 Packed Attention Mask、Position IDs 与 Loss Mask](ai-infra/03-data-sequence-packing.md#ai-03-6)**：独立样本的边界怎样同时体现在 attention、位置和监督目标中？
- **[03.7 Variable-length Attention 与 cu_seqlens](ai-infra/03-data-sequence-packing.md#ai-03-7)**：每条序列的边界怎样传给 varlen kernel，和固定长度的 packed QKV 接口有何区别？
- **[03.8 数据读取、Prefetch 与 CPU→GPU Copy](ai-infra/03-data-sequence-packing.md#ai-03-8)**：GPU 等待数据时，瓶颈在读取、处理、拷贝还是同步？

## 04 · GPU SM、Warp、显存与性能测量

[进入本章](ai-infra/04-gpu-profiling.md) · 9 个 section

- **[04.1 Grid、Block、Thread 与 Warp](ai-infra/04-gpu-profiling.md#ai-04-1)**：一个 kernel 的逻辑线程怎样对应输入元素与硬件执行单元？
- **[04.2 SM、Warp Scheduler 与 SIMT](ai-infra/04-gpu-profiling.md#ai-04-2)**：SM 怎样执行 warp，分支与依赖会怎样影响有效执行？
- **[04.3 Registers、Shared Memory、L2 与 HBM](ai-infra/04-gpu-profiling.md#ai-04-3)**：kernel 的数据和状态分别占用哪些内存层级？
- **[04.4 Tensor Cores 与矩阵乘法指令](ai-infra/04-gpu-profiling.md#ai-04-4)**：dtype、矩阵布局与形状怎样限制矩阵指令的使用？
- **[04.5 Coalesced Access 与 Memory Layout](ai-infra/04-gpu-profiling.md#ai-04-5)**：相邻线程访问怎样形成内存事务，stride 会增加什么成本？
- **[04.6 Occupancy、寄存器压力与 Latency Hiding](ai-infra/04-gpu-profiling.md#ai-04-6)**：为什么更多线程或更高 occupancy 不必然得到更快的 kernel？
- **[04.7 FLOPs、Bytes、Arithmetic Intensity 与 Roofline](ai-infra/04-gpu-profiling.md#ai-04-7)**：一个操作的上界怎样估算，哪些实际成本被模型省略？
- **[04.8 CUDA Events、Warmup 与 Synchronization](ai-infra/04-gpu-profiling.md#ai-04-8)**：怎样区分提交开销、GPU 执行时间和端到端时间？
- **[04.9 PyTorch Profiler、Nsight Systems 与 Nsight Compute](ai-infra/04-gpu-profiling.md#ai-04-9)**：算子时间、系统 timeline 与 kernel 指标分别帮助排查什么？

## 05 · 从 Vector Add 到 Triton Matmul

[进入本章](ai-infra/05-cuda-triton-kernels.md) · 8 个 section

- **[05.1 CUDA Vector Add](ai-infra/05-cuda-triton-kernels.md#ai-05-1)**：怎样写出覆盖输入、处理尾部边界且正确的 kernel？
- **[05.2 Triton Vector Add](ai-infra/05-cuda-triton-kernels.md#ai-05-2)**：program ID、block 与 mask 怎样表达同一份向量工作？
- **[05.3 Reduction Kernel](ai-infra/05-cuda-triton-kernels.md#ai-05-3)**：怎样并行归约，同步与浮点加法次序会怎样影响结果？
- **[05.4 Fused Softmax](ai-infra/05-cuda-triton-kernels.md#ai-05-4)**：怎样在一次 kernel 内完成稳定 softmax，减少哪些中间数据？
- **[05.5 Naive GEMM → Tiled GEMM](ai-infra/05-cuda-triton-kernels.md#ai-05-5)**：分块怎样复用矩阵数据，边界 tile 怎样处理？
- **[05.6 Tensor Core GEMM](ai-infra/05-cuda-triton-kernels.md#ai-05-6)**：shape、dtype 与 layout 怎样进入矩阵指令的实现？
- **[05.7 RMSNorm/SwiGLU Fusion](ai-infra/05-cuda-triton-kernels.md#ai-05-7)**：哪些算子能融合，减少访存或 launch 是否会引入其他限制？
- **[05.8 Kernel Benchmark 与正确性比较](ai-infra/05-cuda-triton-kernels.md#ai-05-8)**：怎样避免用错误计时、单一 shape 或过宽误差阈值判断优化？

## 06 · FlashAttention、LightSeq 与编译执行

[进入本章](ai-infra/06-flashattention-compilation.md) · 9 个 section

- **[06.1 标准 Attention 的显存与 IO](ai-infra/06-flashattention-compilation.md#ai-06-1)**：QK、softmax、AV 产生和消费哪些中间矩阵，成本如何随序列变化？
- **[06.2 Online Softmax](ai-infra/06-flashattention-compilation.md#ai-06-2)**：看不到全部 logits 时，怎样合并分块的最大值、归一化项与输出？
- **[06.3 FlashAttention-1](ai-infra/06-flashattention-compilation.md#ai-06-3)**：tiling 与 online softmax 怎样避免保存完整 Attention 矩阵，backward 怎样重计算？
- **[06.4 FlashAttention-2](ai-infra/06-flashattention-compilation.md#ai-06-4)**：thread block 与 warp 的工作划分怎样减少不必要的操作并改善并行度？
- **[06.5 FlashAttention-3](ai-infra/06-flashattention-compilation.md#ai-06-5)**：异步矩阵指令、数据移动和低精度计算怎样形成新的流水线？
- **[06.6 FlashAttention 的 Causal、Varlen 与 Packed 接口](ai-infra/06-flashattention-compilation.md#ai-06-6)**：causal 对齐、序列边界与 QKV 布局怎样对应各接口的语义？
- **[06.7 LightSeq / LightSeq2](ai-infra/06-flashattention-compilation.md#ai-06-7)**：Transformer 推理与训练有哪些可联合优化的算子、内存和执行步骤？
- **[06.8 torch.compile、Fusion 与 Graph Break](ai-infra/06-flashattention-compilation.md#ai-06-8)**：编译如何改变执行，哪些动态行为可能打断图或触发重编译？
- **[06.9 CUDA Graph 与 JAX JIT](ai-infra/06-flashattention-compilation.md#ai-06-9)**：capture/replay 和编译缓存分别复用什么，输入与内存约束怎样不同？

## 07 · NCCL、DDP、Megatron 与 GPipe

[进入本章](ai-infra/07-nccl-model-parallelism.md) · 11 个 section

- **[07.1 Send/Recv 与 Collective Communication](ai-infra/07-nccl-model-parallelism.md#ai-07-1)**：点对点和 AllReduce/AllGather/AllToAll 等 collectives 分别表达什么数据交换？
- **[07.2 AllReduce、ReduceScatter 与 AllGather](ai-infra/07-nccl-model-parallelism.md#ai-07-2)**：各 rank 最后持有什么结果，归约和分发怎样组合？
- **[07.3 Ring/Tree 与通信成本](ai-infra/07-nccl-model-parallelism.md#ai-07-3)**：不同消息大小、rank 数和拓扑下，延迟与带宽怎样影响算法选择？
- **[07.4 PCIe、NVLink、InfiniBand/RDMA](ai-infra/07-nccl-model-parallelism.md#ai-07-4)**：卡内、卡间与跨节点的数据经过什么路径，带宽瓶颈如何出现？
- **[07.5 DDP](ai-infra/07-nccl-model-parallelism.md#ai-07-5)**：梯度 bucket 与同步怎样和 backward 重叠，哪些更新仍是本地进行？
- **[07.6 Megatron Tensor Parallelism](ai-infra/07-nccl-model-parallelism.md#ai-07-6)**：Column/Row Parallel Linear 切哪些维度，在哪些位置需要通信？
- **[07.7 GPipe 与 Pipeline Parallelism](ai-infra/07-nccl-model-parallelism.md#ai-07-7)**：按层切分之后，microbatch 如何通过前向和反向，bubble 从哪里出现？
- **[07.8 PipeDream / 1F1B Schedule](ai-infra/07-nccl-model-parallelism.md#ai-07-8)**：不同 pipeline schedules 在权重版本、更新时机和激活存储上怎样不同？
- **[07.9 Sequence Parallelism 与 Context Parallelism](ai-infra/07-nccl-model-parallelism.md#ai-07-9)**：同样沿序列切分时，各方案在什么算子、状态和通信边界上不同？
- **[07.10 Ring Attention / Ulysses](ai-infra/07-nccl-model-parallelism.md#ai-07-10)**：长序列 attention 如何在多卡计算，KV 轮转与 AllToAll 重排分别付出什么？
- **[07.11 DP×TP×PP 组合与 Rank Placement](ai-infra/07-nccl-model-parallelism.md#ai-07-11)**：并行 groups 怎样对应 rank 和硬件拓扑，不同阶段的通信走哪里？

## 08 · Activation Checkpointing、DeepSpeed ZeRO 与 FSDP

[进入本章](ai-infra/08-zero-fsdp-memory.md) · 8 个 section

- **[08.1 训练显存账本](ai-infra/08-zero-fsdp-memory.md#ai-08-1)**：参数、梯度、optimizer、activation 与临时 buffer 怎样形成峰值？
- **[08.2 Activation Checkpointing](ai-infra/08-zero-fsdp-memory.md#ai-08-2)**：哪些中间结果可以不保存，backward 的重计算与随机状态怎样保持一致？
- **[08.3 ZeRO-1](ai-infra/08-zero-fsdp-memory.md#ai-08-3)**：优化器状态怎样分片，每个 rank 更新哪一部分参数？
- **[08.4 ZeRO-2](ai-infra/08-zero-fsdp-memory.md#ai-08-4)**：梯度分片怎样连接 ReduceScatter 与本地更新？
- **[08.5 ZeRO-3](ai-infra/08-zero-fsdp-memory.md#ai-08-5)**：参数分片以后，完整层所需参数什么时候取回、使用和释放？
- **[08.6 FSDP / FSDP2](ai-infra/08-zero-fsdp-memory.md#ai-08-6)**：wrap/shard、AllGather 与 Reshard 怎样组织，版本间接口与调度有什么区别？
- **[08.7 CPU/NVMe Offload](ai-infra/08-zero-fsdp-memory.md#ai-08-7)**：把状态移出显存以后，拷贝、传输与更新成本在哪里发生？
- **[08.8 Distributed Checkpoint](ai-infra/08-zero-fsdp-memory.md#ai-08-8)**：模型、optimizer、RNG 与数据进度怎样保存，恢复后如何核对训练语义？

## 09 · GPTQ、AWQ、FP8、LoRA 与 QLoRA

[进入本章](ai-infra/09-quantization-peft.md) · 9 个 section

- **[09.1 Quantization 的 Scale、Zero Point 与 Granularity](ai-infra/09-quantization-peft.md#ai-09-1)**：连续数值怎样映射整数或低精度表示，误差怎样随分组改变？
- **[09.2 PTQ 与 QAT](ai-infra/09-quantization-peft.md#ai-09-2)**：校准和训练分别承担什么，校准数据怎样影响量化结果？
- **[09.3 GPTQ](ai-infra/09-quantization-peft.md#ai-09-3)**：逐块权重量化怎样处理误差，使用哪些校准信息？
- **[09.4 SmoothQuant](ai-infra/09-quantization-peft.md#ai-09-4)**：activation outlier 的困难怎样转移到权重侧，哪些变换需要校准？
- **[09.5 AWQ](ai-infra/09-quantization-peft.md#ai-09-5)**：activation 信息怎样识别权重的重要性，校准如何进入量化？
- **[09.6 FP8、Weight/Activation/KV Quantization](ai-infra/09-quantization-peft.md#ai-09-6)**：量化权重、激活或 KV 分别改变哪些容量、带宽与算术成本？
- **[09.7 Adapters 与 LoRA](ai-infra/09-quantization-peft.md#ai-09-7)**：附加模块或低秩更新训练哪些参数，与基座怎样连接？
- **[09.8 QLoRA](ai-infra/09-quantization-peft.md#ai-09-8)**：量化基座与可训练 adapter 怎样共同完成 forward/backward？
- **[09.9 Quantized Kernel 与模型质量验证](ai-infra/09-quantization-peft.md#ai-09-9)**：容量减少怎样转成实际收益，怎样同时验证误差、任务质量和服务成本？

## 10 · Prefill、Decode、KV Cache 与长上下文

[进入本章](ai-infra/10-kv-cache-decoding.md) · 8 个 section

- **[10.1 Greedy、Temperature、Top-k、Top-p 与 Beam Search](ai-infra/10-kv-cache-decoding.md#ai-10-1)**：不同策略怎样选择 token，怎样影响生成状态与结果？
- **[10.2 Prefill 与 Decode](ai-infra/10-kv-cache-decoding.md#ai-10-2)**：两阶段的输入、可并行工作和瓶颈怎样随 batch、长度和硬件改变？
- **[10.3 KV Cache](ai-infra/10-kv-cache-decoding.md#ai-10-3)**：缓存哪些历史表示，追加 token 时哪些内容复用、哪些重新计算？
- **[10.4 KV Cache 显存估算](ai-infra/10-kv-cache-decoding.md#ai-10-4)**：层数、KV heads、head dimension、长度、batch 与 dtype 怎样决定缓存容量？
- **[10.5 MHA → MQA → GQA](ai-infra/10-kv-cache-decoding.md#ai-10-5)**：减少 KV head 数怎样影响共享关系、缓存容量与 Attention 计算？
- **[10.6 MLA](ai-infra/10-kv-cache-decoding.md#ai-10-6)**：低秩 latent KV 怎样保存，内容与位置相关计算怎样连接？
- **[10.7 Sliding-window Attention 与 Attention Sinks](ai-infra/10-kv-cache-decoding.md#ai-10-7)**：哪些历史 token 状态保留，窗口/缓存策略怎样影响 attention 语义？
- **[10.8 RoPE Scaling 与长上下文](ai-infra/10-kv-cache-decoding.md#ai-10-8)**：位置扩展怎样连接模型质量、KV 容量与计算成本？

## 11 · PagedAttention、vLLM、SGLang 与 DistServe

[进入本章](ai-infra/11-vllm-serving.md) · 12 个 section

- **[11.1 Static Batching → Continuous Batching](ai-infra/11-vllm-serving.md#ai-11-1)**：请求怎样加入和离开 batch，未完成请求怎样继续执行？
- **[11.2 Orca](ai-infra/11-vllm-serving.md#ai-11-2)**：iteration-level scheduling 与 selective batching 怎样组织生成模型执行？
- **[11.3 PagedAttention](ai-infra/11-vllm-serving.md#ai-11-3)**：逻辑 token 怎样经 block table 找到物理 KV block，块怎样分配与回收？
- **[11.4 vLLM Scheduler → KV Manager → Model Runner](ai-infra/11-vllm-serving.md#ai-11-4)**：一个请求从提交到每轮 GPU 执行，调度信息与缓存元数据怎样流动？
- **[11.5 Chunked Prefill](ai-infra/11-vllm-serving.md#ai-11-5)**：prompt 怎样分块，怎样与 decode 共用 token budget？
- **[11.6 Prefix Caching / SGLang RadixAttention](ai-infra/11-vllm-serving.md#ai-11-6)**：共享前缀怎样识别、引用和回收，缓存命中怎样改变 prefill？
- **[11.7 抢占、Recompute 与 KV 回收](ai-infra/11-vllm-serving.md#ai-11-7)**：缓存不足时怎样暂停和恢复请求，生命周期中哪些状态需要保留？
- **[11.8 Speculative Decoding](ai-infra/11-vllm-serving.md#ai-11-8)**：draft、verification 与接受/拒绝怎样减少串行步骤并保持目标采样分布？
- **[11.9 CacheGen 与分层 KV Cache](ai-infra/11-vllm-serving.md#ai-11-9)**：缓存压缩、加载、传输与重算之间怎样取舍，压缩是否改变结果？
- **[11.10 DistServe / Prefill–Decode Disaggregation](ai-infra/11-vllm-serving.md#ai-11-10)**：两阶段分开部署后，KV 传输、并行计划与资源分配怎样组织？
- **[11.11 TTFT、TPOT、吞吐与尾延迟](ai-infra/11-vllm-serving.md#ai-11-11)**：各指标包含哪些时间，服务负载和缓存条件怎样影响比较？
- **[11.12 Triton Inference Server、LightLLM 与 Dynamo](ai-infra/11-vllm-serving.md#ai-11-12)**：各系统承担哪些请求、执行或路由职责，怎样和模型 backend 连接？

## 12 · GShard、Switch Transformer 与 DeepSeek MoE

[进入本章](ai-infra/12-moe-expert-parallelism.md) · 9 个 section

- **[12.1 Dense FFN → MoE Experts](ai-infra/12-moe-expert-parallelism.md#ai-12-1)**：总参数和每 token 激活参数怎样不同，模型容量怎样连接实际工作量？
- **[12.2 Router 与 Top-k Routing](ai-infra/12-moe-expert-parallelism.md#ai-12-2)**：token 怎样选择 experts，routing weights 怎样参与输出和训练？
- **[12.3 Capacity、Token Dropping 与 Dropless MoE](ai-infra/12-moe-expert-parallelism.md#ai-12-3)**：某个 expert 收到过多 token 时，容量规则怎样影响计算与训练？
- **[12.4 Load-balancing Loss 与 Router 稳定性](ai-infra/12-moe-expert-parallelism.md#ai-12-4)**：负载、路由偏好与学习目标怎样互相影响，哪些平衡机制属于不同设计？
- **[12.5 GShard / Switch Transformer](ai-infra/12-moe-expert-parallelism.md#ai-12-5)**：两种稀疏设计在 routing、并行和训练稳定性上怎样取舍？
- **[12.6 DeepSeek MoE](ai-infra/12-moe-expert-parallelism.md#ai-12-6)**：fine-grained experts 与 shared experts 怎样划分工作，怎样影响计算和路由？
- **[12.7 Expert Parallelism 与 AllToAll](ai-infra/12-moe-expert-parallelism.md#ai-12-7)**：dispatch/combine 如何把 token 发到 expert 所在设备，又怎样还原顺序？
- **[12.8 Grouped GEMM 与 MoE Kernel](ai-infra/12-moe-expert-parallelism.md#ai-12-8)**：不等长 expert batches 怎样组成矩阵计算，什么时候会有小 GEMM 与 padding 成本？
- **[12.9 DeepSpeed-MoE / DeepSeek-V3](ai-infra/12-moe-expert-parallelism.md#ai-12-9)**：一套完整 MoE 系统怎样组合专家结构、负载均衡、并行与通信？

## 13 · Scaling Laws、Chinchilla 与模型评估

[进入本章](ai-infra/13-scaling-evaluation.md) · 7 个 section

- **[13.1 参数量、Token 数与训练 FLOPs](ai-infra/13-scaling-evaluation.md#ai-13-1)**：训练预算怎样随架构、输入长度和有效 token 数变化？
- **[13.2 Kaplan Scaling Laws](ai-infra/13-scaling-evaluation.md#ai-13-2)**：怎样从不同规模训练的 loss 观察趋势，拟合与外推依赖什么前提？
- **[13.3 Chinchilla](ai-infra/13-scaling-evaluation.md#ai-13-3)**：固定计算预算时，模型大小与训练 token 数怎样共同选择？
- **[13.4 Learning Rate、Batch Size 与训练长度](ai-infra/13-scaling-evaluation.md#ai-13-4)**：硬件吞吐、更新次数和收敛怎样共同影响训练配置？
- **[13.5 Loss、Perplexity 与 Downstream Evaluation](ai-infra/13-scaling-evaluation.md#ai-13-5)**：语言建模 loss 与下游任务指标分别评价什么，评估过程怎样复现？
- **[13.6 Benchmark Contamination 与数据泄漏](ai-infra/13-scaling-evaluation.md#ai-13-6)**：训练、验证与评估数据中的重复或信息泄漏怎样影响结论？
- **[13.7 MFU 与 Time-to-quality](ai-infra/13-scaling-evaluation.md#ai-13-7)**：模型 FLOPs 利用率和达到目标质量的时间为什么是不同指标？

## 14 · SFT、DPO、PPO、GRPO 与 RLHF 系统

[进入本章](ai-infra/14-post-training-rlhf.md) · 8 个 section

- **[14.1 SFT](ai-infra/14-post-training-rlhf.md#ai-14-1)**：instruction、chat template 与 loss mask 怎样定义一次监督微调？
- **[14.2 Preference Data 与 Reward Model](ai-infra/14-post-training-rlhf.md#ai-14-2)**：偏好对、评分与 reward 的含义是什么，数据怎样进入训练？
- **[14.3 DPO](ai-infra/14-post-training-rlhf.md#ai-14-3)**：policy/reference 怎样参与偏好目标，与 reward-model-based 流程有何不同？
- **[14.4 PPO / InstructGPT](ai-infra/14-post-training-rlhf.md#ai-14-4)**：rollout、reward、value 与 policy update 怎样组成一轮优化？
- **[14.5 GRPO / RLVR](ai-infra/14-post-training-rlhf.md#ai-14-5)**：group sampling、优势估计与可验证奖励怎样连接，GRPO 与 RLVR 为何不是同义词？
- **[14.6 Rollout Engine 与权重同步](ai-infra/14-post-training-rlhf.md#ai-14-6)**：训练更新后的 policy 怎样传到生成侧，每条轨迹怎样对应策略版本？
- **[14.7 ReaLHF / verl](ai-infra/14-post-training-rlhf.md#ai-14-7)**：角色部署、资源重分配与执行流水线怎样组合训练和生成？
- **[14.8 同步/异步 Rollout 与策略版本](ai-infra/14-post-training-rlhf.md#ai-14-8)**：增加并发或异步程度怎样改变数据新鲜度、资源竞争和学习结果？

## 15 · ViT、Flamingo、LLaVA、Qwen-VL 与 BAGEL

[进入本章](ai-infra/15-multimodal-bagel.md) · 9 个 section

- **[15.1 ViT 与 Patch Tokens](ai-infra/15-multimodal-bagel.md#ai-15-1)**：图像怎样分成 patches 并进入 Transformer，分辨率怎样影响序列长度？
- **[15.2 Projector 与 Cross-attention](ai-infra/15-multimodal-bagel.md#ai-15-2)**：视觉表示怎样连接语言 hidden space，拼接和 cross-attention 的计算路径怎样不同？
- **[15.3 Flamingo / LLaVA](ai-infra/15-multimodal-bagel.md#ai-15-3)**：两类视觉语言连接方式分别怎样组织输入、适配与训练？
- **[15.4 Qwen-VL 风格动态分辨率与多模态位置编码](ai-infra/15-multimodal-bagel.md#ai-15-4)**：动态图像/video token 怎样组织，M-RoPE 怎样表达文本与时空位置？
- **[15.5 多模态 Sequence Packing](ai-infra/15-multimodal-bagel.md#ai-15-5)**：text/image/video 的边界、attention mask、position 与不同 loss 怎样放进一个 batch？
- **[15.6 视觉 Token 数量与显存/Attention 成本](ai-infra/15-multimodal-bagel.md#ai-15-6)**：分辨率改变哪些序列与计算，encoder 成本和语言侧成本怎样区分？
- **[15.7 多模态 Prefill、Encoder Cache 与请求 Batch](ai-infra/15-multimodal-bagel.md#ai-15-7)**：视觉处理如何接入 prefill，encoder 结果怎样缓存、共享或重新计算？
- **[15.8 BAGEL 的理解与生成路径](ai-infra/15-multimodal-bagel.md#ai-15-8)**：自回归理解与连续生成如何共用模型，哪些 token、mask 与目标不同？
- **[15.9 Video Tokens 与时空 Attention](ai-infra/15-multimodal-bagel.md#ai-15-9)**：帧数、分辨率和时空布局怎样改变 token 数与 attention 执行？

## 16 · DDPM、Latent Diffusion、DiT 与扩散推理加速

[进入本章](ai-infra/16-diffusion-dit.md) · 12 个 section

- **[16.1 DDPM](ai-infra/16-diffusion-dit.md#ai-16-1)**：怎样加噪、训练去噪器并逐步采样，训练 timestep 与推理 step 怎样不同？
- **[16.2 DDIM / DPM-Solver](ai-infra/16-diffusion-dit.md#ai-16-2)**：怎样改变采样轨迹和步数，求解器的速度与质量怎样比较？
- **[16.3 Latent Diffusion 与 VAE](ai-infra/16-diffusion-dit.md#ai-16-3)**：像素与 latent 之间怎样流动，encoder/decoder 与去噪器分别承担什么？
- **[16.4 DiT](ai-infra/16-diffusion-dit.md#ai-16-4)**：patch、timestep conditioning 与 adaLN 等模块怎样组织去噪 Transformer？
- **[16.5 Classifier-free Guidance](ai-infra/16-diffusion-dit.md#ai-16-5)**：条件与无条件分支怎样组合，batch 组织与 guidance 值怎样影响成本和质量？
- **[16.6 Flow Matching / Rectified Flow](ai-infra/16-diffusion-dit.md#ai-16-6)**：路径、速度目标与采样积分怎样连接，两者各自采用什么假设？
- **[16.7 MMDiT](ai-infra/16-diffusion-dit.md#ai-16-7)**：text/image token 怎样进行联合 attention，不同流的参数与交互怎样组织？
- **[16.8 Image/Video Diffusion 的计算与显存账本](ai-infra/16-diffusion-dit.md#ai-16-8)**：分辨率、帧数、latent shape 与采样步数分别增加哪些成本？
- **[16.9 Diffusion 的训练 Batch、混合精度与 Checkpointing](ai-infra/16-diffusion-dit.md#ai-16-9)**：随机 timestep、训练目标和显存策略怎样接回共同训练底座？
- **[16.10 DistriFusion / PipeFusion](ai-infra/16-diffusion-dit.md#ai-16-10)**：patch 分配、流水线与跨 timestep 复用怎样组织多 GPU diffusion inference？
- **[16.11 TeaCache](ai-infra/16-diffusion-dit.md#ai-16-11)**：跨 timestep 的计算复用怎样决定跳过哪些计算，怎样衡量累积误差与质量代价？
- **[16.12 Diffusers / xDiT 的执行优化](ai-infra/16-diffusion-dit.md#ai-16-12)**：attention backend、compile、offload、VAE tiling 与并行组合分别改变哪个阶段？

## 从个人经历接回地图

以下只记录用户在 2026-10-02 的自述：有过相关学习和使用经历；具体理解随后由复述与实验验证。

- GPU 视图与简单 kernel 需要回顾：[04.1 Grid、Block、Thread 与 Warp](ai-infra/04-gpu-profiling.md#ai-04-1)、[05.1 CUDA Vector Add](ai-infra/05-cuda-triton-kernels.md#ai-05-1)。
- 接触过 FlashAttention：从 [06.3 FlashAttention-1](ai-infra/06-flashattention-compilation.md#ai-06-3) 连接三代设计。
- 接触过 DeepSpeed、communication：[07.2 AllReduce、ReduceScatter 与 AllGather](ai-infra/07-nccl-model-parallelism.md#ai-07-2)、[08.3 ZeRO-1](ai-infra/08-zero-fsdp-memory.md#ai-08-3) 至 [08.5 ZeRO-3](ai-infra/08-zero-fsdp-memory.md#ai-08-5)。
- 刚在 BAGEL 场景学过 packing：[03.5 Sequence Packing](ai-infra/03-data-sequence-packing.md#ai-03-5)、[15.5 多模态 Sequence Packing](ai-infra/15-multimodal-bagel.md#ai-15-5)。
- 使用过 vLLM，但实现不清楚：[11.4 vLLM Scheduler → KV Manager → Model Runner](ai-infra/11-vllm-serving.md#ai-11-4)；KV/page 从 [10.3 KV Cache](ai-infra/10-kv-cache-decoding.md#ai-10-3) 与 [11.3 PagedAttention](ai-infra/11-vllm-serving.md#ai-11-3) 接入。

CMU 旧笔记作为回顾线索；模型生成的解释在进入具体主题时与一手资料核对。保留学习者原有解释，修正时记录新证据。

## 学习后怎样维护

定位与顺序继续维护在 paths；实际解释补回 topic 的 README；代码、Notebook 与精选结果随需要创建。图中之外的新技术先查其与已有节点的关系。候选缺口进入 GAPS 并标待诊断。

**本轮学习实验未运行。** 未来实验默认在远程算力服务器进行：CPU 先核查可验证的语义，GPU/多卡按节点需要准备。网站只展示已保存输出，不执行这些方案。
