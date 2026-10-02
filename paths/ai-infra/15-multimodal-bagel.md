---
title: '15 · ViT、Flamingo、LLaVA、Qwen-VL 与 BAGEL'
---

# 15 · ViT、Flamingo、LLaVA、Qwen-VL 与 BAGEL

沿视觉表示、语言连接和混合序列理解多模态；每种模型的 token、位置与 mask 规则分别核查。

[完整地图](../ai-infra-map.md) · [课程与论文出处](../ai-infra-sources.md) · [GAPS](../../GAPS.md)

本页是学习导航。节点问题、先修与验证方案由本仓库编排；课程栏链接材料入口，补充节点另行标注。**本章验证均未运行；没有个人掌握度判断或性能实测。**

(ai-15-1)=
## 15.1 ViT 与 Patch Tokens：图像怎样分成 patches 并进入 Transformer，分辨率怎样影响序列长度？

- **先修节点**：[01.4 Decoder-only Transformer](01-tokenizer-transformer.md#ai-01-4)、[02.2 Broadcasting、Matmul 与 Einsum](02-pytorch-training-step.md#ai-02-2)
- **课程出处**：**补充课程拆分**；[G05 · L05 · Vision Transformers 部分](../ai-infra-sources.md#course-g05)。
- **论文与实现**：[An Image is Worth 16x16 Words / ViT](../ai-infra-sources.md#source-vit)。
- **后续验证（未运行）**：CPU：对教学用图像尺寸计算 patch 数和 shape，检查边界与 positional embedding。

(ai-15-2)=
## 15.2 Projector 与 Cross-attention：视觉表示怎样连接语言 hidden space，拼接和 cross-attention 的计算路径怎样不同？

- **先修节点**：[15.1 ViT 与 Patch Tokens](15-multimodal-bagel.md#ai-15-1)、[01.5 Causal Attention、Q/K/V 与 Multi-head Attention](01-tokenizer-transformer.md#ai-01-5)
- **课程出处**：**补充课程与论文**；[G14 · L14 · Vision-language models](../ai-infra-sources.md#course-g14)、[MMULTI · Multimodal LLMs](../ai-infra-sources.md#course-mmulti)。
- **论文与实现**：[Flamingo](../ai-infra-sources.md#source-flamingo)、[Visual Instruction Tuning / LLaVA](../ai-infra-sources.md#source-llava)。
- **后续验证（未运行）**：CPU 示意/小模型：画两条连接路径，核对 shape、可训练参数与 token 访问关系。

(ai-15-3)=
## 15.3 Flamingo / LLaVA：两类视觉语言连接方式分别怎样组织输入、适配与训练？

- **先修节点**：[15.2 Projector 与 Cross-attention](15-multimodal-bagel.md#ai-15-2)、[14.1 SFT](14-post-training-rlhf.md#ai-14-1)
- **课程出处**：**课程拆分与论文补充**；[MMULTI · Multimodal LLMs](../ai-infra-sources.md#course-mmulti)、[G14 · L14 · Vision-language models](../ai-infra-sources.md#course-g14)。
- **论文与实现**：[Flamingo](../ai-infra-sources.md#source-flamingo)、[Visual Instruction Tuning / LLaVA](../ai-infra-sources.md#source-llava)。
- **后续验证（未运行）**：论文比较：按 encoder、连接模块、语言模型、训练数据/目标列出实际设计。

(ai-15-4)=
## 15.4 Qwen-VL 风格动态分辨率与多模态位置编码：动态图像/video token 怎样组织，M-RoPE 怎样表达文本与时空位置？

- **先修节点**：[15.1 ViT 与 Patch Tokens](15-multimodal-bagel.md#ai-15-1)、[01.6 RoPE 与位置编码](01-tokenizer-transformer.md#ai-01-6)
- **课程出处**：**论文补充**；[G14 · L14 · Vision-language models](../ai-infra-sources.md#course-g14)。
- **论文与实现**：[Qwen2-VL](../ai-infra-sources.md#source-qwen2vl)。
- **后续验证（未运行）**：CPU/代码阅读：为两种分辨率和短视频追踪 token 与位置 ID；注明具体 Qwen2-VL 实现。

(ai-15-5)=
## 15.5 多模态 Sequence Packing：text/image/video 的边界、attention mask、position 与不同 loss 怎样放进一个 batch？

- **先修节点**：[03.6 Packed Attention Mask、Position IDs 与 Loss Mask](03-data-sequence-packing.md#ai-03-6)、[15.2 Projector 与 Cross-attention](15-multimodal-bagel.md#ai-15-2)、[02.5 Cross-entropy 与 Next-token Prediction](02-pytorch-training-step.md#ai-02-5)
- **课程出处**：**工程补充**；[G14 · L14 · Vision-language models](../ai-infra-sources.md#course-g14)。
- **论文与实现**：[BAGEL implementation](../ai-infra-sources.md#source-bagel)。
- **后续验证（未运行）**：CPU/单 GPU：画混合样本的边界和各损失位置，核对模型定义的独立/联合访问语义。

(ai-15-6)=
## 15.6 视觉 Token 数量与显存/Attention 成本：分辨率改变哪些序列与计算，encoder 成本和语言侧成本怎样区分？

- **先修节点**：[15.1 ViT 与 Patch Tokens](15-multimodal-bagel.md#ai-15-1)、[04.7 FLOPs、Bytes、Arithmetic Intensity 与 Roofline](04-gpu-profiling.md#ai-04-7)、[10.4 KV Cache 显存估算](10-kv-cache-decoding.md#ai-10-4)
- **课程出处**：**论文补充**；[G14 · L14 · Vision-language models](../ai-infra-sources.md#course-g14)。
- **论文与实现**：[Qwen2-VL](../ai-infra-sources.md#source-qwen2vl)、[An Image is Worth 16x16 Words / ViT](../ai-infra-sources.md#source-vit)。
- **后续验证（未运行）**：CPU 估算/单 GPU：分开核算视觉与语言阶段，改变分辨率并记录实际 shape。

(ai-15-7)=
## 15.7 多模态 Prefill、Encoder Cache 与请求 Batch：视觉处理如何接入 prefill，encoder 结果怎样缓存、共享或重新计算？

- **先修节点**：[15.2 Projector 与 Cross-attention](15-multimodal-bagel.md#ai-15-2)、[10.2 Prefill 与 Decode](10-kv-cache-decoding.md#ai-10-2)、[11.4 vLLM Scheduler → KV Manager → Model Runner](11-vllm-serving.md#ai-11-4)
- **课程出处**：**工程补充**；[MMULTI · Multimodal LLMs](../ai-infra-sources.md#course-mmulti)。
- **论文与实现**：[vLLM architecture](../ai-infra-sources.md#source-vllm)。
- **后续验证（未运行）**：代码阅读/单 GPU：固定模型/backend，追踪图像预处理、encoder、cache 和语言 prefill。

(ai-15-8)=
## 15.8 BAGEL 的理解与生成路径：自回归理解与连续生成如何共用模型，哪些 token、mask 与目标不同？

- **先修节点**：[15.5 多模态 Sequence Packing](15-multimodal-bagel.md#ai-15-5)、[16.4 DiT](16-diffusion-dit.md#ai-16-4)、[16.6 Flow Matching / Rectified Flow](16-diffusion-dit.md#ai-16-6)
- **课程出处**：**工程补充**；[G14 · L14 · Vision-language models](../ai-infra-sources.md#course-g14)。
- **论文与实现**：[BAGEL implementation](../ai-infra-sources.md#source-bagel)。
- **后续验证（未运行）**：代码阅读：沿理解与生成各走一遍，连接文本/图像表示、训练目标与推理步骤。

(ai-15-9)=
## 15.9 Video Tokens 与时空 Attention：帧数、分辨率和时空布局怎样改变 token 数与 attention 执行？

- **先修节点**：[15.4 Qwen-VL 风格动态分辨率与多模态位置编码](15-multimodal-bagel.md#ai-15-4)、[15.6 视觉 Token 数量与显存/Attention 成本](15-multimodal-bagel.md#ai-15-6)、[01.5 Causal Attention、Q/K/V 与 Multi-head Attention](01-tokenizer-transformer.md#ai-01-5)
- **课程出处**：**补充课程拆分**；[G25 · L25 · Generative Models for Videos](../ai-infra-sources.md#course-g25)。
- **论文与实现**：[Qwen2-VL](../ai-infra-sources.md#source-qwen2vl)。
- **后续验证（未运行）**：CPU 估算/单 GPU：画时空索引与可见区域；分别改变帧数和分辨率观察成本。

## 回到实际学习

选一个节点，先复述当前解释，再核查材料或代码并预测实验结果。实验前记录硬件、依赖版本、源码 commit、输入、同步与计时方法；重复测量保留原始记录。具体解释与证据逐步补到 topic 主笔记，未运行的方案保持标注。

[返回总地图](../ai-infra-map.md) · [上一章：14](14-post-training-rlhf.md) · [下一章：16](16-diffusion-dit.md)
