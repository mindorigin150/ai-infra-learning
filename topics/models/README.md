---
title: 模型表示与生成机制
---

# 模型表示与生成机制

输入怎样变成模型表示，模型结构怎样决定训练与生成的计算？

[主题索引](../README.md) · [开始一次学习](../../paths/start-here.md)

## 分类边界

数据边界连接数据管线；硬件上的算子实现连接 GPU 执行；生成阶段的缓存与请求组织连接推理服务。

## Topic 与材料入口

下表按机制归类已有材料节点。材料页保留具体问题、先修与来源；教学 Notebook 在实际学习后逐步展开。条目不表示个人掌握度。

| Topic | 要解释的问题 | 材料入口 |
| --- | --- | --- |
| Byte-level BPE | 词表与 merge 规则怎样把字节序列变成 token，又怎样还原？ | [01.1](../../paths/ai-infra/01-tokenizer-transformer.md#ai-01-1) |
| SentencePiece | SentencePiece 的文本处理与分词算法是什么关系，为什么不能把它直接等同于 BPE？ | [01.2](../../paths/ai-infra/01-tokenizer-transformer.md#ai-01-2) |
| Special Tokens、BOS/EOS 与 Chat Template | 同一段对话怎样因模板和特殊 token 变成不同的模型输入？ | [01.3](../../paths/ai-infra/01-tokenizer-transformer.md#ai-01-3) |
| Decoder-only Transformer | 一个 decoder block 的输入、输出与每层 tensor shape 怎样对应？ | [01.4](../../paths/ai-infra/01-tokenizer-transformer.md#ai-01-4) |
| Causal Attention、Q/K/V 与 Multi-head Attention | mask 和 head 怎样参与 QK、softmax 与 AV，哪些 token 能看到哪些 token？ | [01.5](../../paths/ai-infra/01-tokenizer-transformer.md#ai-01-5) |
| RoPE 与位置编码 | 位置怎样进入 Q/K，哪些变换取决于 token 的位置？ | [01.6](../../paths/ai-infra/01-tokenizer-transformer.md#ai-01-6) |
| RMSNorm、SwiGLU 与 Residual Connection | Norm、FFN 与 residual 分别放在哪里，怎样改变 shape 和计算？ | [01.7](../../paths/ai-infra/01-tokenizer-transformer.md#ai-01-7) |
| GPT/LLaMA 模型配置 | 层数、宽度、head 与词表怎样决定参数量和主要计算？ | [01.8](../../paths/ai-infra/01-tokenizer-transformer.md#ai-01-8) |
| Dense FFN → MoE Experts | 总参数和每 token 激活参数怎样不同，模型容量怎样连接实际工作量？ | [12.1](../../paths/ai-infra/12-moe-expert-parallelism.md#ai-12-1) |
| Router 与 Top-k Routing | token 怎样选择 experts，routing weights 怎样参与输出和训练？ | [12.2](../../paths/ai-infra/12-moe-expert-parallelism.md#ai-12-2) |
| Capacity、Token Dropping 与 Dropless MoE | 某个 expert 收到过多 token 时，容量规则怎样影响计算与训练？ | [12.3](../../paths/ai-infra/12-moe-expert-parallelism.md#ai-12-3) |
| Load-balancing Loss 与 Router 稳定性 | 负载、路由偏好与学习目标怎样互相影响，哪些平衡机制属于不同设计？ | [12.4](../../paths/ai-infra/12-moe-expert-parallelism.md#ai-12-4) |
| GShard / Switch Transformer | 两种稀疏设计在 routing、并行和训练稳定性上怎样取舍？ | [12.5](../../paths/ai-infra/12-moe-expert-parallelism.md#ai-12-5) |
| DeepSeek MoE | fine-grained experts 与 shared experts 怎样划分工作，怎样影响计算和路由？ | [12.6](../../paths/ai-infra/12-moe-expert-parallelism.md#ai-12-6) |
| ViT 与 Patch Tokens | 图像怎样分成 patches 并进入 Transformer，分辨率怎样影响序列长度？ | [15.1](../../paths/ai-infra/15-multimodal-bagel.md#ai-15-1) |
| Projector 与 Cross-attention | 视觉表示怎样连接语言 hidden space，拼接和 cross-attention 的计算路径怎样不同？ | [15.2](../../paths/ai-infra/15-multimodal-bagel.md#ai-15-2) |
| Flamingo / LLaVA | 两类视觉语言连接方式分别怎样组织输入、适配与训练？ | [15.3](../../paths/ai-infra/15-multimodal-bagel.md#ai-15-3) |
| Qwen-VL 风格动态分辨率与多模态位置编码 | 动态图像/video token 怎样组织，M-RoPE 怎样表达文本与时空位置？ | [15.4](../../paths/ai-infra/15-multimodal-bagel.md#ai-15-4) |
| BAGEL 的理解与生成路径 | 自回归理解与连续生成如何共用模型，哪些 token、mask 与目标不同？ | [15.8](../../paths/ai-infra/15-multimodal-bagel.md#ai-15-8) |
| Video Tokens 与时空 Attention | 帧数、分辨率和时空布局怎样改变 token 数与 attention 执行？ | [15.9](../../paths/ai-infra/15-multimodal-bagel.md#ai-15-9) |
| DDPM | 怎样加噪、训练去噪器并逐步采样，训练 timestep 与推理 step 怎样不同？ | [16.1](../../paths/ai-infra/16-diffusion-dit.md#ai-16-1) |
| DDIM / DPM-Solver | 怎样改变采样轨迹和步数，求解器的速度与质量怎样比较？ | [16.2](../../paths/ai-infra/16-diffusion-dit.md#ai-16-2) |
| Latent Diffusion 与 VAE | 像素与 latent 之间怎样流动，encoder/decoder 与去噪器分别承担什么？ | [16.3](../../paths/ai-infra/16-diffusion-dit.md#ai-16-3) |
| DiT | patch、timestep conditioning 与 adaLN 等模块怎样组织去噪 Transformer？ | [16.4](../../paths/ai-infra/16-diffusion-dit.md#ai-16-4) |
| Classifier-free Guidance | 条件与无条件分支怎样组合，batch 组织与 guidance 值怎样影响成本和质量？ | [16.5](../../paths/ai-infra/16-diffusion-dit.md#ai-16-5) |
| Flow Matching / Rectified Flow | 路径、速度目标与采样积分怎样连接，两者各自采用什么假设？ | [16.6](../../paths/ai-infra/16-diffusion-dit.md#ai-16-6) |
| MMDiT | text/image token 怎样进行联合 attention，不同流的参数与交互怎样组织？ | [16.7](../../paths/ai-infra/16-diffusion-dit.md#ai-16-7) |

关联分类：[数据组织与流水线](../data-pipelines/README.md) · [GPU 执行与算子优化](../gpu-execution/README.md) · [生成执行与推理服务](../inference-serving/README.md)。
