---
title: '01 · BPE、Tokenizer 与 LLaMA 风格 Transformer'
---

# 01 · BPE、Tokenizer 与 LLaMA 风格 Transformer

从文本进入模型开始，建立 tokenizer、tensor shape 和一个 Transformer block 的联系。

[完整地图](../ai-infra-map.md) · [课程与论文出处](../ai-infra-sources.md) · [GAPS](../../GAPS.md)

本页是学习导航。节点问题、先修与验证方案由本仓库编排；课程栏链接材料入口，补充节点另行标注。**本章验证均未运行；没有个人掌握度判断或性能实测。**

(ai-01-1)=
## 01.1 Byte-level BPE：词表与 merge 规则怎样把字节序列变成 token，又怎样还原？

- **先修节点**：本图入口；学习时按问题诊断必要的基础。
- **课程出处**：**课程拆分**；[S01 · L01 · Overview, tokenization (Percy)](../ai-infra-sources.md#course-s01)、[M08 · Tokenization](../ai-infra-sources.md#course-m08)。
- **论文与实现**：[BPE / Neural Machine Translation of Rare Words](../ai-infra-sources.md#source-bpe)、[Transformers tokenizers](../ai-infra-sources.md#source-hf-tokenizer)。
- **后续验证（未运行）**：CPU：手算一个小词表的 merge；预测含中文与空白的文本能否往返编码，再检查结果。

(ai-01-2)=
## 01.2 SentencePiece：SentencePiece 的文本处理与分词算法是什么关系，为什么不能把它直接等同于 BPE？

- **先修节点**：[01.1 Byte-level BPE](01-tokenizer-transformer.md#ai-01-1)
- **课程出处**：**课程拆分**；[M08 · Tokenization](../ai-infra-sources.md#course-m08)。
- **论文与实现**：[SentencePiece](../ai-infra-sources.md#source-sentencepiece)。
- **后续验证（未运行）**：CPU：比较 normalization、词表与编码结果，说明何时会影响原文往返。

(ai-01-3)=
## 01.3 Special Tokens、BOS/EOS 与 Chat Template：同一段对话怎样因模板和特殊 token 变成不同的模型输入？

- **先修节点**：[01.1 Byte-level BPE](01-tokenizer-transformer.md#ai-01-1)、[01.2 SentencePiece](01-tokenizer-transformer.md#ai-01-2)
- **课程出处**：**工程补充**；[S01 · L01 · Overview, tokenization (Percy)](../ai-infra-sources.md#course-s01)、[M08 · Tokenization](../ai-infra-sources.md#course-m08)。
- **论文与实现**：[Transformers chat templates](../ai-infra-sources.md#source-chat)、[Transformers tokenizers](../ai-infra-sources.md#source-hf-tokenizer)。
- **后续验证（未运行）**：CPU：展开两种 chat template；标出角色边界、BOS/EOS 和实际 token 序列。

(ai-01-4)=
## 01.4 Decoder-only Transformer：一个 decoder block 的输入、输出与每层 tensor shape 怎样对应？

- **先修节点**：[01.3 Special Tokens、BOS/EOS 与 Chat Template](01-tokenizer-transformer.md#ai-01-3)
- **课程出处**：**课程拆分**；[S03 · L03 · Architectures, hyperparameters (Tatsu)](../ai-infra-sources.md#course-s03)、[M06 · Transformer](../ai-infra-sources.md#course-m06)、[M07 · Pre-trained LLMs](../ai-infra-sources.md#course-m07)。
- **论文与实现**：[Attention Is All You Need](../ai-infra-sources.md#source-transformer)、[LLaMA](../ai-infra-sources.md#source-llama)。
- **后续验证（未运行）**：复述/CPU：给定教学用 batch、长度与 hidden size，画出 block 的 shape 流向。

(ai-01-5)=
## 01.5 Causal Attention、Q/K/V 与 Multi-head Attention：mask 和 head 怎样参与 QK、softmax 与 AV，哪些 token 能看到哪些 token？

- **先修节点**：[01.4 Decoder-only Transformer](01-tokenizer-transformer.md#ai-01-4)、[02.2 Broadcasting、Matmul 与 Einsum](02-pytorch-training-step.md#ai-02-2)
- **课程出处**：**课程拆分**；[S03 · L03 · Architectures, hyperparameters (Tatsu)](../ai-infra-sources.md#course-s03)、[M06 · Transformer](../ai-infra-sources.md#course-m06)。
- **论文与实现**：[Attention Is All You Need](../ai-infra-sources.md#source-transformer)。
- **后续验证（未运行）**：CPU：对短序列列出允许访问的 token；比较 causal 与全连接 mask 的结果。

(ai-01-6)=
## 01.6 RoPE 与位置编码：位置怎样进入 Q/K，哪些变换取决于 token 的位置？

- **先修节点**：[01.5 Causal Attention、Q/K/V 与 Multi-head Attention](01-tokenizer-transformer.md#ai-01-5)
- **课程出处**：**论文补充**；[S03 · L03 · Architectures, hyperparameters (Tatsu)](../ai-infra-sources.md#course-s03)、[M06 · Transformer](../ai-infra-sources.md#course-m06)。
- **论文与实现**：[RoFormer / RoPE](../ai-infra-sources.md#source-rope)。
- **后续验证（未运行）**：CPU：对教学用二维旋转写出不同位置的 Q/K，检查相对位置关系。

(ai-01-7)=
## 01.7 RMSNorm、SwiGLU 与 Residual Connection：Norm、FFN 与 residual 分别放在哪里，怎样改变 shape 和计算？

- **先修节点**：[01.4 Decoder-only Transformer](01-tokenizer-transformer.md#ai-01-4)、[02.2 Broadcasting、Matmul 与 Einsum](02-pytorch-training-step.md#ai-02-2)
- **课程出处**：**课程拆分**；[S03 · L03 · Architectures, hyperparameters (Tatsu)](../ai-infra-sources.md#course-s03)、[M07 · Pre-trained LLMs](../ai-infra-sources.md#course-m07)。
- **论文与实现**：[LLaMA](../ai-infra-sources.md#source-llama)、[RMSNorm](../ai-infra-sources.md#source-rmsnorm)、[GLU Variants Improve Transformer](../ai-infra-sources.md#source-swiglu)。
- **后续验证（未运行）**：CPU：追踪一个 block，分别替换 Norm/FFN；记录 shape 与参数计数，不预设质量结论。

(ai-01-8)=
## 01.8 GPT/LLaMA 模型配置：层数、宽度、head 与词表怎样决定参数量和主要计算？

- **先修节点**：[01.5 Causal Attention、Q/K/V 与 Multi-head Attention](01-tokenizer-transformer.md#ai-01-5)、[01.7 RMSNorm、SwiGLU 与 Residual Connection](01-tokenizer-transformer.md#ai-01-7)
- **课程出处**：**课程拆分**；[S02 · L02 · PyTorch, resource accounting (Percy)](../ai-infra-sources.md#course-s02)、[S03 · L03 · Architectures, hyperparameters (Tatsu)](../ai-infra-sources.md#course-s03)、[M07 · Pre-trained LLMs](../ai-infra-sources.md#course-m07)。
- **论文与实现**：[LLaMA](../ai-infra-sources.md#source-llama)。
- **后续验证（未运行）**：CPU：手算教学用小模型的参数，再和模型定义逐项核对。

## 回到实际学习

选一个节点，先复述当前解释，再核查材料或代码并预测实验结果。实验前记录硬件、依赖版本、源码 commit、输入、同步与计时方法；重复测量保留原始记录。具体解释与证据逐步补到 topic 主笔记，未运行的方案保持标注。

[返回总地图](../ai-infra-map.md) · [下一章：02](02-pytorch-training-step.md)
