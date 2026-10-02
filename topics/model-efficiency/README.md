---
title: 数值表示与模型适配
---

# 数值表示与模型适配

怎样改变数值精度、表示或可训练参数，成本与模型质量怎样变化？

[主题索引](../README.md) · [开始一次学习](../../paths/start-here.md)

## 分类边界

量化算子的执行连接 GPU 优化；训练目标与质量判断连接训练评估。

## Topic 与材料入口

下表按机制归类已有材料节点。材料页保留具体问题、先修与来源；主笔记在实际学习后逐步展开。条目不表示个人掌握度。

| Topic | 要解释的问题 | 材料入口 |
| --- | --- | --- |
| FP32、FP16、BF16 与 AMP | 存储、计算与累加采用不同 dtype 时，何处可能溢出或损失精度？ | [02.8](../../paths/ai-infra/02-pytorch-training-step.md#ai-02-8) |
| Quantization 的 Scale、Zero Point 与 Granularity | 连续数值怎样映射整数或低精度表示，误差怎样随分组改变？ | [09.1](../../paths/ai-infra/09-quantization-peft.md#ai-09-1) |
| PTQ 与 QAT | 校准和训练分别承担什么，校准数据怎样影响量化结果？ | [09.2](../../paths/ai-infra/09-quantization-peft.md#ai-09-2) |
| GPTQ | 逐块权重量化怎样处理误差，使用哪些校准信息？ | [09.3](../../paths/ai-infra/09-quantization-peft.md#ai-09-3) |
| SmoothQuant | activation outlier 的困难怎样转移到权重侧，哪些变换需要校准？ | [09.4](../../paths/ai-infra/09-quantization-peft.md#ai-09-4) |
| AWQ | activation 信息怎样识别权重的重要性，校准如何进入量化？ | [09.5](../../paths/ai-infra/09-quantization-peft.md#ai-09-5) |
| FP8、Weight/Activation/KV Quantization | 量化权重、激活或 KV 分别改变哪些容量、带宽与算术成本？ | [09.6](../../paths/ai-infra/09-quantization-peft.md#ai-09-6) |
| Adapters 与 LoRA | 附加模块或低秩更新训练哪些参数，与基座怎样连接？ | [09.7](../../paths/ai-infra/09-quantization-peft.md#ai-09-7) |
| QLoRA | 量化基座与可训练 adapter 怎样共同完成 forward/backward？ | [09.8](../../paths/ai-infra/09-quantization-peft.md#ai-09-8) |
| Quantized Kernel 与模型质量验证 | 容量减少怎样转成实际收益，怎样同时验证误差、任务质量和服务成本？ | [09.9](../../paths/ai-infra/09-quantization-peft.md#ai-09-9) |

关联分类：[GPU 执行与算子优化](../gpu-execution/README.md) · [训练目标与评估](../training-evaluation/README.md)。
