---
title: 张量计算与自动微分
---

# 张量计算与自动微分

张量怎样组织存储和计算，梯度与训练状态怎样完成一次更新？

[主题索引](../README.md) · [开始一次学习](../../paths/start-here.md)

## 分类边界

混合精度与量化连接数值表示；多设备的梯度同步和状态分片连接分布式训练。

## Topic 与材料入口

下表按机制归类已有材料节点。材料页保留具体问题、先修与来源；教学 Notebook 在实际学习后逐步展开。条目不表示个人掌握度。

| Topic | 要解释的问题 | 材料入口 |
| --- | --- | --- |
| Tensor Storage、Stride、View 与 Contiguous | reshape、transpose 与 view 何时共享存储，何时产生拷贝？ | [02.1](../../paths/ai-infra/02-pytorch-training-step.md#ai-02-1) |
| Broadcasting、Matmul 与 Einsum | 怎样从表达式追踪 shape，避免把广播与矩阵乘法混淆？ | [02.2](../../paths/ai-infra/02-pytorch-training-step.md#ai-02-2) |
| Autograd 与 Backward Graph | 一个输入通过多条路径影响 loss 时，梯度怎样累加？ | [02.3](../../paths/ai-infra/02-pytorch-training-step.md#ai-02-3) |
| Saved Tensors 与显存生命周期 | backward 为什么需要某些前向结果，它们什么时候能够释放？ | [02.4](../../paths/ai-infra/02-pytorch-training-step.md#ai-02-4) |
| AdamW | 参数、梯度、动量与二阶状态怎样完成一次更新？ | [02.6](../../paths/ai-infra/02-pytorch-training-step.md#ai-02-6) |
| Gradient Accumulation | 多个 microbatch 怎样组成一次 optimizer step，loss 的权重怎样对齐？ | [02.7](../../paths/ai-infra/02-pytorch-training-step.md#ai-02-7) |
| Diffusion 的训练 Batch、混合精度与 Checkpointing | 随机 timestep、训练目标和显存策略怎样接回共同训练底座？ | [16.9](../../paths/ai-infra/16-diffusion-dit.md#ai-16-9) |

关联分类：[数值表示与模型适配](../model-efficiency/README.md) · [通信与分布式训练](../distributed-training/README.md)。
