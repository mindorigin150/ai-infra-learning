---
title: '08 · Activation Checkpointing、DeepSpeed ZeRO 与 FSDP'
---

# 08 · Activation Checkpointing、DeepSpeed ZeRO 与 FSDP

沿一次训练的状态生命周期理解显存节省：重计算、状态分片与 offload 各有不同成本。

[完整地图](../ai-infra-map.md) · [课程与论文出处](../ai-infra-sources.md) · [GAPS](../../GAPS.md)

本页是学习导航。节点问题、先修与验证方案由本仓库编排；课程栏链接材料入口，补充节点另行标注。**本章验证均未运行；没有个人掌握度判断或性能实测。**

(ai-08-1)=
## 08.1 训练显存账本：参数、梯度、optimizer、activation 与临时 buffer 怎样形成峰值？

- **先修节点**：[02.4 Saved Tensors 与显存生命周期](02-pytorch-training-step.md#ai-02-4)、[02.6 AdamW](02-pytorch-training-step.md#ai-02-6)、[02.8 FP32、FP16、BF16 与 AMP](02-pytorch-training-step.md#ai-02-8)
- **课程出处**：**课程拆分**；[S02 · L02 · PyTorch, resource accounting (Percy)](../ai-infra-sources.md#course-s02)、[S08 · L08 · Parallelism (Percy)](../ai-infra-sources.md#course-s08)、[M21 · Communication Efficient Distributed Training](../ai-infra-sources.md#course-m21)。
- **论文与实现**：[ZeRO](../ai-infra-sources.md#source-zero)、[PyTorch performance tuning](../ai-infra-sources.md#source-tuning)。
- **后续验证（未运行）**：CPU 估算/单 GPU：逐项估算教学模型并标注 dtype；再将峰值与 allocator 观察比较。

(ai-08-2)=
## 08.2 Activation Checkpointing：哪些中间结果可以不保存，backward 的重计算与随机状态怎样保持一致？

- **先修节点**：[08.1 训练显存账本](08-zero-fsdp-memory.md#ai-08-1)、[02.3 Autograd 与 Backward Graph](02-pytorch-training-step.md#ai-02-3)
- **课程出处**：**论文补充**；[S08 · L08 · Parallelism (Percy)](../ai-infra-sources.md#course-s08)、[M21 · Communication Efficient Distributed Training](../ai-infra-sources.md#course-m21)。
- **论文与实现**：[Training Deep Nets with Sublinear Memory Cost](../ai-infra-sources.md#source-checkpoint-paper)、[PyTorch activation checkpoint](../ai-infra-sources.md#source-checkpoint)。
- **后续验证（未运行）**：单 GPU：比较保存策略下的输出、梯度、峰值显存与时间，并控制随机性。

(ai-08-3)=
## 08.3 ZeRO-1：优化器状态怎样分片，每个 rank 更新哪一部分参数？

- **先修节点**：[08.1 训练显存账本](08-zero-fsdp-memory.md#ai-08-1)、[07.5 DDP](07-nccl-model-parallelism.md#ai-07-5)
- **课程出处**：**课程拆分**；[M21 · Communication Efficient Distributed Training](../ai-infra-sources.md#course-m21)、[S08 · L08 · Parallelism (Percy)](../ai-infra-sources.md#course-s08)。
- **论文与实现**：[ZeRO](../ai-infra-sources.md#source-zero)、[DeepSpeed ZeRO](../ai-infra-sources.md#source-deepspeed)。
- **后续验证（未运行）**：复述/多 GPU：画更新前后每张卡持有的状态，区分容量模型与实际峰值。

(ai-08-4)=
## 08.4 ZeRO-2：梯度分片怎样连接 ReduceScatter 与本地更新？

- **先修节点**：[08.3 ZeRO-1](08-zero-fsdp-memory.md#ai-08-3)、[07.2 AllReduce、ReduceScatter 与 AllGather](07-nccl-model-parallelism.md#ai-07-2)
- **课程出处**：**课程拆分**；[M21 · Communication Efficient Distributed Training](../ai-infra-sources.md#course-m21)、[S08 · L08 · Parallelism (Percy)](../ai-infra-sources.md#course-s08)。
- **论文与实现**：[ZeRO](../ai-infra-sources.md#source-zero)、[DeepSpeed ZeRO](../ai-infra-sources.md#source-deepspeed)。
- **后续验证（未运行）**：复述/多 GPU：追踪一块梯度到参数更新，核对通信和状态持有范围。

(ai-08-5)=
## 08.5 ZeRO-3：参数分片以后，完整层所需参数什么时候取回、使用和释放？

- **先修节点**：[08.4 ZeRO-2](08-zero-fsdp-memory.md#ai-08-4)、[07.2 AllReduce、ReduceScatter 与 AllGather](07-nccl-model-parallelism.md#ai-07-2)
- **课程出处**：**课程拆分**；[M21 · Communication Efficient Distributed Training](../ai-infra-sources.md#course-m21)、[S08 · L08 · Parallelism (Percy)](../ai-infra-sources.md#course-s08)。
- **论文与实现**：[ZeRO](../ai-infra-sources.md#source-zero)、[DeepSpeed ZeRO](../ai-infra-sources.md#source-deepspeed)。
- **后续验证（未运行）**：复述/多 GPU：画 forward/backward 的 AllGather 与释放，检查峰值中的临时完整参数。

(ai-08-6)=
## 08.6 FSDP / FSDP2：wrap/shard、AllGather 与 Reshard 怎样组织，版本间接口与调度有什么区别？

- **先修节点**：[08.5 ZeRO-3](08-zero-fsdp-memory.md#ai-08-5)、[02.4 Saved Tensors 与显存生命周期](02-pytorch-training-step.md#ai-02-4)
- **课程出处**：**工程补充**；[S08 · L08 · Parallelism (Percy)](../ai-infra-sources.md#course-s08)、[M21 · Communication Efficient Distributed Training](../ai-infra-sources.md#course-m21)。
- **论文与实现**：[PyTorch FSDP2 tutorial](../ai-infra-sources.md#source-fsdp)。
- **后续验证（未运行）**：多 GPU：按实际 PyTorch 版本追踪一层的状态；对照 reference 更新并记录通信 timeline。

(ai-08-7)=
## 08.7 CPU/NVMe Offload：把状态移出显存以后，拷贝、传输与更新成本在哪里发生？

- **先修节点**：[08.5 ZeRO-3](08-zero-fsdp-memory.md#ai-08-5)、[07.4 PCIe、NVLink、InfiniBand/RDMA](07-nccl-model-parallelism.md#ai-07-4)
- **课程出处**：**论文补充**；[M21 · Communication Efficient Distributed Training](../ai-infra-sources.md#course-m21)。
- **论文与实现**：[ZeRO-Offload](../ai-infra-sources.md#source-zero-offload)、[ZeRO-Infinity](../ai-infra-sources.md#source-zero-infinity)、[DeepSpeed ZeRO](../ai-infra-sources.md#source-deepspeed)。
- **后续验证（未运行）**：有足够主存的单/多 GPU；NVMe 方案另需设备：记录状态容量、I/O 和时间，分别说明配置。

(ai-08-8)=
## 08.8 Distributed Checkpoint：模型、optimizer、RNG 与数据进度怎样保存，恢复后如何核对训练语义？

- **先修节点**：[08.6 FSDP / FSDP2](08-zero-fsdp-memory.md#ai-08-6)、[03.3 Tokenization、Dataset Sharding 与 DataLoader](03-data-sequence-packing.md#ai-03-3)、[02.6 AdamW](02-pytorch-training-step.md#ai-02-6)
- **课程出处**：**工程补充**；[S08 · L08 · Parallelism (Percy)](../ai-infra-sources.md#course-s08)、[M21 · Communication Efficient Distributed Training](../ai-infra-sources.md#course-m21)。
- **论文与实现**：[PyTorch Distributed Checkpoint](../ai-infra-sources.md#source-dcp)。
- **后续验证（未运行）**：多 GPU：在短训练中保存并恢复，与连续运行比较状态和后续更新；记录数据/RNG 的额外保存方式。

## 回到实际学习

选一个节点，先复述当前解释，再核查材料或代码并预测实验结果。实验前记录硬件、依赖版本、源码 commit、输入、同步与计时方法；重复测量保留原始记录。具体解释与证据逐步补到 topic 主笔记，未运行的方案保持标注。

[返回总地图](../ai-infra-map.md) · [上一章：07](07-nccl-model-parallelism.md) · [下一章：09](09-quantization-peft.md)
