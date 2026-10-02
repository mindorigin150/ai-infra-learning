---
title: '16 · DDPM、Latent Diffusion、DiT 与扩散推理加速'
---

# 16 · DDPM、Latent Diffusion、DiT 与扩散推理加速

先建立训练目标和采样步骤，再把 DiT、联合 Attention、并行与缓存接到实际推理成本。

[完整地图](../ai-infra-map.md) · [课程与论文出处](../ai-infra-sources.md) · [GAPS](../../GAPS.md)

本页是学习导航。节点问题、先修与验证方案由本仓库编排；课程栏链接材料入口，补充节点另行标注。**本章验证均未运行；没有个人掌握度判断或性能实测。**

(ai-16-1)=
## 16.1 DDPM：怎样加噪、训练去噪器并逐步采样，训练 timestep 与推理 step 怎样不同？

- **先修节点**：[02.5 Cross-entropy 与 Next-token Prediction](02-pytorch-training-step.md#ai-02-5)、[02.6 AdamW](02-pytorch-training-step.md#ai-02-6)
- **课程出处**：**补充课程拆分**；[G07 · L07 · Diffusion models (Part I)](../ai-infra-sources.md#course-g07)、[G08 · L08 · Diffusion models (Part II) / VAE 前提](../ai-infra-sources.md#course-g08)。
- **论文与实现**：[Denoising Diffusion Probabilistic Models / DDPM](../ai-infra-sources.md#source-ddpm)。
- **后续验证（未运行）**：CPU：在教学用低维数据上画加噪和反向步骤，区分训练目标与采样算法。

(ai-16-2)=
## 16.2 DDIM / DPM-Solver：怎样改变采样轨迹和步数，求解器的速度与质量怎样比较？

- **先修节点**：[16.1 DDPM](16-diffusion-dit.md#ai-16-1)
- **课程出处**：**论文补充**；[G07 · L07 · Diffusion models (Part I)](../ai-infra-sources.md#course-g07)、[G08 · L08 · Diffusion models (Part II) / VAE 前提](../ai-infra-sources.md#course-g08)。
- **论文与实现**：[Denoising Diffusion Implicit Models / DDIM](../ai-infra-sources.md#source-ddim)、[DPM-Solver](../ai-infra-sources.md#source-dpmsolver)。
- **后续验证（未运行）**：CPU/单 GPU：固定模型、seed 和评价方式，记录步数/函数调用次数、耗时与质量。

(ai-16-3)=
## 16.3 Latent Diffusion 与 VAE：像素与 latent 之间怎样流动，encoder/decoder 与去噪器分别承担什么？

- **先修节点**：[16.1 DDPM](16-diffusion-dit.md#ai-16-1)、[15.1 ViT 与 Patch Tokens](15-multimodal-bagel.md#ai-15-1)
- **课程出处**：**补充课程拆分**；[G12 · L12 · Text-to-image / Latent diffusion 部分](../ai-infra-sources.md#course-g12)。
- **论文与实现**：[Latent Diffusion Models](../ai-infra-sources.md#source-ldm)。
- **后续验证（未运行）**：CPU 示意/单 GPU：追踪一次 encode、去噪、decode 的 shape 与时间；只回顾需要的 VAE 前提。

(ai-16-4)=
## 16.4 DiT：patch、timestep conditioning 与 adaLN 等模块怎样组织去噪 Transformer？

- **先修节点**：[16.1 DDPM](16-diffusion-dit.md#ai-16-1)、[15.1 ViT 与 Patch Tokens](15-multimodal-bagel.md#ai-15-1)、[01.7 RMSNorm、SwiGLU 与 Residual Connection](01-tokenizer-transformer.md#ai-01-7)
- **课程出处**：**论文补充**；[G25 · L25 · Generative Models for Videos](../ai-infra-sources.md#course-g25)。
- **论文与实现**：[Scalable Diffusion Models with Transformers / DiT](../ai-infra-sources.md#source-dit)。
- **后续验证（未运行）**：CPU/代码阅读：画一个 DiT block，追踪 latent patches、时间条件与输出目标。

(ai-16-5)=
## 16.5 Classifier-free Guidance：条件与无条件分支怎样组合，batch 组织与 guidance 值怎样影响成本和质量？

- **先修节点**：[16.1 DDPM](16-diffusion-dit.md#ai-16-1)、[16.3 Latent Diffusion 与 VAE](16-diffusion-dit.md#ai-16-3)
- **课程出处**：**论文补充**；[G12 · L12 · Text-to-image / Latent diffusion 部分](../ai-infra-sources.md#course-g12)。
- **论文与实现**：[Classifier-Free Diffusion Guidance](../ai-infra-sources.md#source-cfg)。
- **后续验证（未运行）**：CPU/单 GPU：核对两分支公式；固定采样条件，分别观察 batch 合并、耗时和质量。

(ai-16-6)=
## 16.6 Flow Matching / Rectified Flow：路径、速度目标与采样积分怎样连接，两者各自采用什么假设？

- **先修节点**：[16.1 DDPM](16-diffusion-dit.md#ai-16-1)、[02.3 Autograd 与 Backward Graph](02-pytorch-training-step.md#ai-02-3)
- **课程出处**：**论文补充**；[G07 · L07 · Diffusion models (Part I)](../ai-infra-sources.md#course-g07)、[G08 · L08 · Diffusion models (Part II) / VAE 前提](../ai-infra-sources.md#course-g08)。
- **论文与实现**：[Flow Matching for Generative Modeling](../ai-infra-sources.md#source-flow)、[Flow Straight and Fast / Rectified Flow](../ai-infra-sources.md#source-rectified)。
- **后续验证（未运行）**：CPU：画教学用插值路径和速度目标，区分方法的共同表达与具体训练设计。

(ai-16-7)=
## 16.7 MMDiT：text/image token 怎样进行联合 attention，不同流的参数与交互怎样组织？

- **先修节点**：[16.4 DiT](16-diffusion-dit.md#ai-16-4)、[16.6 Flow Matching / Rectified Flow](16-diffusion-dit.md#ai-16-6)、[15.2 Projector 与 Cross-attention](15-multimodal-bagel.md#ai-15-2)
- **课程出处**：**论文补充**；[G12 · L12 · Text-to-image / Latent diffusion 部分](../ai-infra-sources.md#course-g12)、[G14 · L14 · Vision-language models](../ai-infra-sources.md#course-g14)。
- **论文与实现**：[Scaling Rectified Flow Transformers / MMDiT](../ai-infra-sources.md#source-mmdit)。
- **后续验证（未运行）**：论文/代码阅读：追踪两类 token 的 QKV 与交互，和单流 DiT 比较 shape 与计算路径。

(ai-16-8)=
## 16.8 Image/Video Diffusion 的计算与显存账本：分辨率、帧数、latent shape 与采样步数分别增加哪些成本？

- **先修节点**：[16.3 Latent Diffusion 与 VAE](16-diffusion-dit.md#ai-16-3)、[16.4 DiT](16-diffusion-dit.md#ai-16-4)、[15.9 Video Tokens 与时空 Attention](15-multimodal-bagel.md#ai-15-9)、[04.7 FLOPs、Bytes、Arithmetic Intensity 与 Roofline](04-gpu-profiling.md#ai-04-7)
- **课程出处**：**工程补充**；[G25 · L25 · Generative Models for Videos](../ai-infra-sources.md#course-g25)。
- **论文与实现**：[Scalable Diffusion Models with Transformers / DiT](../ai-infra-sources.md#source-dit)、[xDiT implementation](../ai-infra-sources.md#source-xdit)。
- **后续验证（未运行）**：CPU 估算/单 GPU：分开核算 encoder、去噪步骤、attention 与 decoder；记录真实 shapes。

(ai-16-9)=
## 16.9 Diffusion 的训练 Batch、混合精度与 Checkpointing：随机 timestep、训练目标和显存策略怎样接回共同训练底座？

- **先修节点**：[16.1 DDPM](16-diffusion-dit.md#ai-16-1)、[16.6 Flow Matching / Rectified Flow](16-diffusion-dit.md#ai-16-6)、[02.8 FP32、FP16、BF16 与 AMP](02-pytorch-training-step.md#ai-02-8)、[08.2 Activation Checkpointing](08-zero-fsdp-memory.md#ai-08-2)
- **课程出处**：**工程补充**；[G07 · L07 · Diffusion models (Part I)](../ai-infra-sources.md#course-g07)、[G08 · L08 · Diffusion models (Part II) / VAE 前提](../ai-infra-sources.md#course-g08)。
- **论文与实现**：[Scalable Diffusion Models with Transformers / DiT](../ai-infra-sources.md#source-dit)、[PyTorch AMP](../ai-infra-sources.md#source-amp)、[PyTorch activation checkpoint](../ai-infra-sources.md#source-checkpoint)。
- **后续验证（未运行）**：单 GPU：用小训练步骤核对目标和梯度，比较精度/保存策略并记录随机状态。

(ai-16-10)=
## 16.10 DistriFusion / PipeFusion：patch 分配、流水线与跨 timestep 复用怎样组织多 GPU diffusion inference？

- **先修节点**：[16.4 DiT](16-diffusion-dit.md#ai-16-4)、[07.7 GPipe 与 Pipeline Parallelism](07-nccl-model-parallelism.md#ai-07-7)、[07.10 Ring Attention / Ulysses](07-nccl-model-parallelism.md#ai-07-10)
- **课程出处**：**论文补充**；[G25 · L25 · Generative Models for Videos](../ai-infra-sources.md#course-g25)。
- **论文与实现**：[DistriFusion](../ai-infra-sources.md#source-distrifusion)、[PipeFusion](../ai-infra-sources.md#source-pipefusion)、[xDiT implementation](../ai-infra-sources.md#source-xdit)。
- **后续验证（未运行）**：复述/多 GPU：分别画两种方案的通信与依赖，评估延迟和质量，避免视为完全相同方法。

(ai-16-11)=
## 16.11 TeaCache：跨 timestep 的计算复用怎样决定跳过哪些计算，怎样衡量累积误差与质量代价？

- **先修节点**：[16.4 DiT](16-diffusion-dit.md#ai-16-4)、[16.8 Image/Video Diffusion 的计算与显存账本](16-diffusion-dit.md#ai-16-8)
- **课程出处**：**论文补充**；[G25 · L25 · Generative Models for Videos](../ai-infra-sources.md#course-g25)。
- **论文与实现**：[Timestep Embedding Tells / TeaCache](../ai-infra-sources.md#source-teacache)、[TeaCache implementation](../ai-infra-sources.md#source-tea-code)。
- **后续验证（未运行）**：单 GPU：固定 prompt、seed、模型与采样器，比较多个缓存阈值的时间和质量。

(ai-16-12)=
## 16.12 Diffusers / xDiT 的执行优化：attention backend、compile、offload、VAE tiling 与并行组合分别改变哪个阶段？

- **先修节点**：[16.3 Latent Diffusion 与 VAE](16-diffusion-dit.md#ai-16-3)、[16.8 Image/Video Diffusion 的计算与显存账本](16-diffusion-dit.md#ai-16-8)、[06.8 torch.compile、Fusion 与 Graph Break](06-flashattention-compilation.md#ai-06-8)、[08.7 CPU/NVMe Offload](08-zero-fsdp-memory.md#ai-08-7)、[16.10 DistriFusion / PipeFusion](16-diffusion-dit.md#ai-16-10)
- **课程出处**：**工程补充**；[G25 · L25 · Generative Models for Videos](../ai-infra-sources.md#course-g25)。
- **论文与实现**：[Diffusers memory optimization](../ai-infra-sources.md#source-diffusers)、[xDiT implementation](../ai-infra-sources.md#source-xdit)。
- **后续验证（未运行）**：单/多 GPU：按实际硬件一次启用一种机制，保存配置、计时、内存与质量，再讨论组合。

## 回到实际学习

选一个节点，先复述当前解释，再核查材料或代码并预测实验结果。实验前记录硬件、依赖版本、源码 commit、输入、同步与计时方法；重复测量保留原始记录。具体解释与证据逐步补到 topic 主笔记，未运行的方案保持标注。

[返回总地图](../ai-infra-map.md) · [上一章：15](15-multimodal-bagel.md)
