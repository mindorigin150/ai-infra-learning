---
title: '02 · PyTorch Tensor、Autograd 与一次训练更新'
---

# 02 · PyTorch Tensor、Autograd 与一次训练更新

把模型表达式连接到存储、梯度和 optimizer step；数值格式也是训练语义的一部分。

[完整地图](../ai-infra-map.md) · [课程与论文出处](../ai-infra-sources.md) · [GAPS](../../GAPS.md)

本页是学习导航。节点问题、先修与验证方案由本仓库编排；课程栏链接材料入口，补充节点另行标注。**本章验证均未运行；没有个人掌握度判断或性能实测。**

(ai-02-1)=
## 02.1 Tensor Storage、Stride、View 与 Contiguous：reshape、transpose 与 view 何时共享存储，何时产生拷贝？

- **先修节点**：[01.4 Decoder-only Transformer](01-tokenizer-transformer.md#ai-01-4)
- **课程出处**：**课程拆分**；[S02 · L02 · PyTorch, resource accounting (Percy)](../ai-infra-sources.md#course-s02)、[M05 · Deep Learning Frameworks Design](../ai-infra-sources.md#course-m05)。
- **论文与实现**：[PyTorch tensor views](../ai-infra-sources.md#source-tensor)、[PyTorch: An Imperative Style, High-Performance Deep Learning Library](../ai-infra-sources.md#source-pytorch)。
- **后续验证（未运行）**：CPU：先预测 transpose 后的 stride 与 alias，再查看 storage 和 contiguous 的变化。

(ai-02-2)=
## 02.2 Broadcasting、Matmul 与 Einsum：怎样从表达式追踪 shape，避免把广播与矩阵乘法混淆？

- **先修节点**：[02.1 Tensor Storage、Stride、View 与 Contiguous](02-pytorch-training-step.md#ai-02-1)
- **课程出处**：**课程拆分**；[S02 · L02 · PyTorch, resource accounting (Percy)](../ai-infra-sources.md#course-s02)、[M06 · Transformer](../ai-infra-sources.md#course-m06)。
- **论文与实现**：[PyTorch: An Imperative Style, High-Performance Deep Learning Library](../ai-infra-sources.md#source-pytorch)。
- **后续验证（未运行）**：CPU：对一组教学用 shapes 预测输出；用 broadcast、matmul 和 einsum 相互核对。

(ai-02-3)=
## 02.3 Autograd 与 Backward Graph：一个输入通过多条路径影响 loss 时，梯度怎样累加？

- **先修节点**：[02.2 Broadcasting、Matmul 与 Einsum](02-pytorch-training-step.md#ai-02-2)
- **课程出处**：**课程拆分**；[M04 · Learning algorithm and Auto Differentiation](../ai-infra-sources.md#course-m04)、[M05 · Deep Learning Frameworks Design](../ai-infra-sources.md#course-m05)。
- **论文与实现**：[PyTorch autograd](../ai-infra-sources.md#source-autograd)、[PyTorch: An Imperative Style, High-Performance Deep Learning Library](../ai-infra-sources.md#source-pytorch)。
- **后续验证（未运行）**：CPU：手算共享输入的两条计算路径，再与 autograd 比较，解释 zero_grad 的作用。

(ai-02-4)=
## 02.4 Saved Tensors 与显存生命周期：backward 为什么需要某些前向结果，它们什么时候能够释放？

- **先修节点**：[02.3 Autograd 与 Backward Graph](02-pytorch-training-step.md#ai-02-3)
- **课程出处**：**工程补充**；[M04 · Learning algorithm and Auto Differentiation](../ai-infra-sources.md#course-m04)、[M05 · Deep Learning Frameworks Design](../ai-infra-sources.md#course-m05)。
- **论文与实现**：[PyTorch autograd](../ai-infra-sources.md#source-autograd)、[PyTorch performance tuning](../ai-infra-sources.md#source-tuning)。
- **后续验证（未运行）**：CPU/单 GPU：追踪一个小计算图的保存对象；GPU 环境准备好后再观察显存生命周期。

(ai-02-5)=
## 02.5 Cross-entropy 与 Next-token Prediction：输入、标签移位、padding 与 loss mask 怎样定义训练目标？

- **先修节点**：[01.3 Special Tokens、BOS/EOS 与 Chat Template](01-tokenizer-transformer.md#ai-01-3)、[01.4 Decoder-only Transformer](01-tokenizer-transformer.md#ai-01-4)、[02.2 Broadcasting、Matmul 与 Einsum](02-pytorch-training-step.md#ai-02-2)
- **课程出处**：**课程拆分**；[S03 · L03 · Architectures, hyperparameters (Tatsu)](../ai-infra-sources.md#course-s03)、[M07 · Pre-trained LLMs](../ai-infra-sources.md#course-m07)。
- **论文与实现**：[LLaMA](../ai-infra-sources.md#source-llama)。
- **后续验证（未运行）**：CPU：逐 token 写出输入与标签；验证被 mask 的位置如何影响 loss 的分子和归一化。

(ai-02-6)=
## 02.6 AdamW：参数、梯度、动量与二阶状态怎样完成一次更新？

- **先修节点**：[02.3 Autograd 与 Backward Graph](02-pytorch-training-step.md#ai-02-3)、[02.5 Cross-entropy 与 Next-token Prediction](02-pytorch-training-step.md#ai-02-5)
- **课程出处**：**课程拆分**；[S03 · L03 · Architectures, hyperparameters (Tatsu)](../ai-infra-sources.md#course-s03)。
- **论文与实现**：[Decoupled Weight Decay Regularization / AdamW](../ai-infra-sources.md#source-adamw)。
- **后续验证（未运行）**：CPU：手算一个参数的更新，与实现比较；区分 weight decay 与梯度中的正则项。

(ai-02-7)=
## 02.7 Gradient Accumulation：多个 microbatch 怎样组成一次 optimizer step，loss 的权重怎样对齐？

- **先修节点**：[02.5 Cross-entropy 与 Next-token Prediction](02-pytorch-training-step.md#ai-02-5)、[02.6 AdamW](02-pytorch-training-step.md#ai-02-6)
- **课程出处**：**工程补充**；[S08 · L08 · Parallelism (Percy)](../ai-infra-sources.md#course-s08)、[M14 · Distributed Model Training II](../ai-infra-sources.md#course-m14)。
- **论文与实现**：[PyTorch DDP tutorial](../ai-infra-sources.md#source-ddp)、[PyTorch performance tuning](../ai-infra-sources.md#source-tuning)。
- **后续验证（未运行）**：CPU：比较整 batch 与拆分后的梯度；固定随机性并核对样本/token 加权。

(ai-02-8)=
## 02.8 FP32、FP16、BF16 与 AMP：存储、计算与累加采用不同 dtype 时，何处可能溢出或损失精度？

- **先修节点**：[02.2 Broadcasting、Matmul 与 Einsum](02-pytorch-training-step.md#ai-02-2)、[02.6 AdamW](02-pytorch-training-step.md#ai-02-6)
- **课程出处**：**课程拆分**；[S02 · L02 · PyTorch, resource accounting (Percy)](../ai-infra-sources.md#course-s02)、[M16 · Model Quantization](../ai-infra-sources.md#course-m16)。
- **论文与实现**：[Mixed Precision Training](../ai-infra-sources.md#source-mixed)、[PyTorch AMP](../ai-infra-sources.md#source-amp)。
- **后续验证（未运行）**：CPU/单 GPU：先解释指数范围和有效精度；GPU 上再比较 dtype 与 loss scaling，保留误差。

## 回到实际学习

选一个节点，先复述当前解释，再核查材料或代码并预测实验结果。实验前记录硬件、依赖版本、源码 commit、输入、同步与计时方法；重复测量保留原始记录。具体解释与证据逐步补到 topic 主笔记，未运行的方案保持标注。

[返回总地图](../ai-infra-map.md) · [上一章：01](01-tokenizer-transformer.md) · [下一章：03](03-data-sequence-packing.md)
