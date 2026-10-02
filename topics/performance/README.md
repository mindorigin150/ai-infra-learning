---
title: 性能模型与观测
---

# 性能模型与观测

哪些成本约束执行，怎样可靠测量并用证据定位瓶颈？

[主题索引](../README.md) · [开始一次学习](../../paths/start-here.md)

## 分类边界

这里集中性能量与测量方法；具体系统的缓存、并行与执行策略链接回各自主位置。

## 已有教学 Notebook

[性能模型教学 Notebook](../foundations/performance-model/lab.ipynb)：概念与代码交替；新增代码未运行。[历史 CPU 记录](../foundations/performance-model/recorded-cpu.ipynb)保留真实输出与原来源。

## Topic 与材料入口

下表按机制归类已有材料节点。材料页保留具体问题、先修与来源；教学 Notebook 在实际学习后逐步展开。条目不表示个人掌握度。

| Topic | 要解释的问题 | 材料入口 |
| --- | --- | --- |
| FLOPs、Bytes、Arithmetic Intensity 与 Roofline | 一个操作的上界怎样估算，哪些实际成本被模型省略？ | [04.7](../../paths/ai-infra/04-gpu-profiling.md#ai-04-7) |
| CUDA Events、Warmup 与 Synchronization | 怎样区分提交开销、GPU 执行时间和端到端时间？ | [04.8](../../paths/ai-infra/04-gpu-profiling.md#ai-04-8) |
| PyTorch Profiler、Nsight Systems 与 Nsight Compute | 算子时间、系统 timeline 与 kernel 指标分别帮助排查什么？ | [04.9](../../paths/ai-infra/04-gpu-profiling.md#ai-04-9) |
| Kernel Benchmark 与正确性比较 | 怎样避免用错误计时、单一 shape 或过宽误差阈值判断优化？ | [05.8](../../paths/ai-infra/05-cuda-triton-kernels.md#ai-05-8) |
| TTFT、TPOT、吞吐与尾延迟 | 各指标包含哪些时间，服务负载和缓存条件怎样影响比较？ | [11.11](../../paths/ai-infra/11-vllm-serving.md#ai-11-11) |
| 参数量、Token 数与训练 FLOPs | 训练预算怎样随架构、输入长度和有效 token 数变化？ | [13.1](../../paths/ai-infra/13-scaling-evaluation.md#ai-13-1) |
| MFU 与 Time-to-quality | 模型 FLOPs 利用率和达到目标质量的时间为什么是不同指标？ | [13.7](../../paths/ai-infra/13-scaling-evaluation.md#ai-13-7) |
| 视觉 Token 数量与显存/Attention 成本 | 分辨率改变哪些序列与计算，encoder 成本和语言侧成本怎样区分？ | [15.6](../../paths/ai-infra/15-multimodal-bagel.md#ai-15-6) |
| Image/Video Diffusion 的计算与显存账本 | 分辨率、帧数、latent shape 与采样步数分别增加哪些成本？ | [16.8](../../paths/ai-infra/16-diffusion-dit.md#ai-16-8) |

关联分类：[GPU 执行与算子优化](../gpu-execution/README.md) · [通信与分布式训练](../distributed-training/README.md) · [生成执行与推理服务](../inference-serving/README.md)。
