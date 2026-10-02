---
title: '09 · GPTQ、AWQ、FP8、LoRA 与 QLoRA'
---

# 09 · GPTQ、AWQ、FP8、LoRA 与 QLoRA

把表示、校准、适配与硬件执行分开核查，再连接模型质量；压缩比例本身不等于加速。

[完整地图](../ai-infra-map.md) · [课程与论文出处](../ai-infra-sources.md) · [GAPS](../../GAPS.md)

本页是学习导航。节点问题、先修与验证方案由本仓库编排；课程栏链接材料入口，补充节点另行标注。**本章验证均未运行；没有个人掌握度判断或性能实测。**

(ai-09-1)=
## 09.1 Quantization 的 Scale、Zero Point 与 Granularity：连续数值怎样映射整数或低精度表示，误差怎样随分组改变？

- **先修节点**：[02.8 FP32、FP16、BF16 与 AMP](02-pytorch-training-step.md#ai-02-8)
- **课程出处**：**课程拆分**；[M16 · Model Quantization](../ai-infra-sources.md#course-m16)。
- **论文与实现**：[GPTQ](../ai-infra-sources.md#source-gptq)。
- **后续验证（未运行）**：CPU：手算 per-tensor/per-channel 教学样本，检查 clipping、舍入和重构误差。

(ai-09-2)=
## 09.2 PTQ 与 QAT：校准和训练分别承担什么，校准数据怎样影响量化结果？

- **先修节点**：[09.1 Quantization 的 Scale、Zero Point 与 Granularity](09-quantization-peft.md#ai-09-1)、[02.3 Autograd 与 Backward Graph](02-pytorch-training-step.md#ai-02-3)
- **课程出处**：**课程拆分**；[M16 · Model Quantization](../ai-infra-sources.md#course-m16)、[M17 · Model Quantization II](../ai-infra-sources.md#course-m17)。
- **论文与实现**：[GPTQ](../ai-infra-sources.md#source-gptq)、[SmoothQuant](../ai-infra-sources.md#source-smoothquant)。
- **后续验证（未运行）**：CPU/单 GPU：固定模型，对比不同校准分布；将数值误差与任务质量分开记录。

(ai-09-3)=
## 09.3 GPTQ：逐块权重量化怎样处理误差，使用哪些校准信息？

- **先修节点**：[09.2 PTQ 与 QAT](09-quantization-peft.md#ai-09-2)、[02.2 Broadcasting、Matmul 与 Einsum](02-pytorch-training-step.md#ai-02-2)
- **课程出处**：**课程拆分**；[M17 · Model Quantization II](../ai-infra-sources.md#course-m17)。
- **论文与实现**：[GPTQ](../ai-infra-sources.md#source-gptq)。
- **后续验证（未运行）**：CPU/单 GPU：对小权重块追踪量化与误差补偿，再比较朴素量化基线。

(ai-09-4)=
## 09.4 SmoothQuant：activation outlier 的困难怎样转移到权重侧，哪些变换需要校准？

- **先修节点**：[09.2 PTQ 与 QAT](09-quantization-peft.md#ai-09-2)、[01.5 Causal Attention、Q/K/V 与 Multi-head Attention](01-tokenizer-transformer.md#ai-01-5)
- **课程出处**：**论文补充**；[M17 · Model Quantization II](../ai-infra-sources.md#course-m17)。
- **论文与实现**：[SmoothQuant](../ai-infra-sources.md#source-smoothquant)。
- **后续验证（未运行）**：CPU/单 GPU：在小线性层检查等价变换，再量化并比较误差与任务指标。

(ai-09-5)=
## 09.5 AWQ：activation 信息怎样识别权重的重要性，校准如何进入量化？

- **先修节点**：[09.2 PTQ 与 QAT](09-quantization-peft.md#ai-09-2)
- **课程出处**：**论文补充**；[M17 · Model Quantization II](../ai-infra-sources.md#course-m17)。
- **论文与实现**：[AWQ](../ai-infra-sources.md#source-awq)。
- **后续验证（未运行）**：代码阅读/单 GPU：追踪校准、scale 搜索和量化，比较同精度与同工作负载基线。

(ai-09-6)=
## 09.6 FP8、Weight/Activation/KV Quantization：量化权重、激活或 KV 分别改变哪些容量、带宽与算术成本？

- **先修节点**：[09.1 Quantization 的 Scale、Zero Point 与 Granularity](09-quantization-peft.md#ai-09-1)、[04.4 Tensor Cores 与矩阵乘法指令](04-gpu-profiling.md#ai-04-4)、[10.4 KV Cache 显存估算](10-kv-cache-decoding.md#ai-10-4)
- **课程出处**：**工程补充**；[M16 · Model Quantization](../ai-infra-sources.md#course-m16)、[M17 · Model Quantization II](../ai-infra-sources.md#course-m17)。
- **论文与实现**：[NVIDIA Transformer Engine](../ai-infra-sources.md#source-transformer-engine)、[vLLM architecture](../ai-infra-sources.md#source-vllm)。
- **后续验证（未运行）**：需支持相应格式的单 GPU：逐项记录实际 dtype/backend，分开检查容量、质量和速度。

(ai-09-7)=
## 09.7 Adapters 与 LoRA：附加模块或低秩更新训练哪些参数，与基座怎样连接？

- **先修节点**：[02.6 AdamW](02-pytorch-training-step.md#ai-02-6)、[01.7 RMSNorm、SwiGLU 与 Residual Connection](01-tokenizer-transformer.md#ai-01-7)
- **课程出处**：**课程拆分**；[M18 · Efficient fine-tuning for Large Models](../ai-infra-sources.md#course-m18)。
- **论文与实现**：[LoRA](../ai-infra-sources.md#source-lora)、[Hugging Face PEFT](../ai-infra-sources.md#source-peft)。
- **后续验证（未运行）**：CPU/单 GPU：列出 trainable parameters，核对梯度；比较合并前后的输出。

(ai-09-8)=
## 09.8 QLoRA：量化基座与可训练 adapter 怎样共同完成 forward/backward？

- **先修节点**：[09.7 Adapters 与 LoRA](09-quantization-peft.md#ai-09-7)、[09.1 Quantization 的 Scale、Zero Point 与 Granularity](09-quantization-peft.md#ai-09-1)、[02.8 FP32、FP16、BF16 与 AMP](02-pytorch-training-step.md#ai-02-8)
- **课程出处**：**课程拆分**；[M18 · Efficient fine-tuning for Large Models](../ai-infra-sources.md#course-m18)。
- **论文与实现**：[QLoRA](../ai-infra-sources.md#source-qlora)、[Hugging Face PEFT](../ai-infra-sources.md#source-peft)。
- **后续验证（未运行）**：单 GPU：追踪基座与 adapter 的 dtype、梯度和内存，记录实际依赖版本。

(ai-09-9)=
## 09.9 Quantized Kernel 与模型质量验证：容量减少怎样转成实际收益，怎样同时验证误差、任务质量和服务成本？

- **先修节点**：[09.3 GPTQ](09-quantization-peft.md#ai-09-3)、[04.9 PyTorch Profiler、Nsight Systems 与 Nsight Compute](04-gpu-profiling.md#ai-04-9)、[13.5 Loss、Perplexity 与 Downstream Evaluation](13-scaling-evaluation.md#ai-13-5)
- **课程出处**：**工程补充**；[M17 · Model Quantization II](../ai-infra-sources.md#course-m17)、[S12 · L12 · Evaluation (Percy)](../ai-infra-sources.md#course-s12)。
- **论文与实现**：[AWQ](../ai-infra-sources.md#source-awq)、[vLLM architecture](../ai-infra-sources.md#source-vllm)。
- **后续验证（未运行）**：单 GPU：固定 workload/backend，分开记录显存、计时与评估；未支持的格式标为未运行。

## 回到实际学习

选一个节点，先复述当前解释，再核查材料或代码并预测实验结果。实验前记录硬件、依赖版本、源码 commit、输入、同步与计时方法；重复测量保留原始记录。具体解释与证据逐步补到 topic 主笔记，未运行的方案保持标注。

[返回总地图](../ai-infra-map.md) · [上一章：08](08-zero-fsdp-memory.md) · [下一章：10](10-kv-cache-decoding.md)
