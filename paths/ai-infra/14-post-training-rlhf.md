---
title: '14 · SFT、DPO、PPO、GRPO 与 RLHF 系统'
---

# 14 · SFT、DPO、PPO、GRPO 与 RLHF 系统

先区分算法目标与角色，再把训练、rollout、评分和权重同步接成系统；角色按算法出现。

[完整地图](../ai-infra-map.md) · [课程与论文出处](../ai-infra-sources.md) · [GAPS](../../GAPS.md)

本页是学习导航。节点问题、先修与验证方案由本仓库编排；课程栏链接材料入口，补充节点另行标注。**本章验证均未运行；没有个人掌握度判断或性能实测。**

(ai-14-1)=
## 14.1 SFT：instruction、chat template 与 loss mask 怎样定义一次监督微调？

- **先修节点**：[01.3 Special Tokens、BOS/EOS 与 Chat Template](01-tokenizer-transformer.md#ai-01-3)、[02.5 Cross-entropy 与 Next-token Prediction](02-pytorch-training-step.md#ai-02-5)、[03.6 Packed Attention Mask、Position IDs 与 Loss Mask](03-data-sequence-packing.md#ai-03-6)
- **课程出处**：**课程拆分**；[S15 · L15 · Alignment - SFT/RLHF (Tatsu)](../ai-infra-sources.md#course-s15)。
- **论文与实现**：[InstructGPT](../ai-infra-sources.md#source-instructgpt)、[Transformers chat templates](../ai-infra-sources.md#source-chat)。
- **后续验证（未运行）**：CPU/单 GPU：展开一条对话的输入和监督位置，比较按样本/token 加权的训练目标。

(ai-14-2)=
## 14.2 Preference Data 与 Reward Model：偏好对、评分与 reward 的含义是什么，数据怎样进入训练？

- **先修节点**：[14.1 SFT](14-post-training-rlhf.md#ai-14-1)、[02.6 AdamW](02-pytorch-training-step.md#ai-02-6)
- **课程出处**：**课程拆分**；[S15 · L15 · Alignment - SFT/RLHF (Tatsu)](../ai-infra-sources.md#course-s15)。
- **论文与实现**：[InstructGPT](../ai-infra-sources.md#source-instructgpt)。
- **后续验证（未运行）**：CPU：画 chosen/rejected 数据与 reward 训练目标，检查 prompt 和回答边界。

(ai-14-3)=
## 14.3 DPO：policy/reference 怎样参与偏好目标，与 reward-model-based 流程有何不同？

- **先修节点**：[14.2 Preference Data 与 Reward Model](14-post-training-rlhf.md#ai-14-2)、[02.5 Cross-entropy 与 Next-token Prediction](02-pytorch-training-step.md#ai-02-5)
- **课程出处**：**课程拆分**；[S15 · L15 · Alignment - SFT/RLHF (Tatsu)](../ai-infra-sources.md#course-s15)。
- **论文与实现**：[Direct Preference Optimization](../ai-infra-sources.md#source-dpo)。
- **后续验证（未运行）**：CPU/单 GPU：对一组教学 log probabilities 核对目标，追踪有梯度和无梯度的参数。

(ai-14-4)=
## 14.4 PPO / InstructGPT：rollout、reward、value 与 policy update 怎样组成一轮优化？

- **先修节点**：[14.2 Preference Data 与 Reward Model](14-post-training-rlhf.md#ai-14-2)、[02.6 AdamW](02-pytorch-training-step.md#ai-02-6)、[10.1 Greedy、Temperature、Top-k、Top-p 与 Beam Search](10-kv-cache-decoding.md#ai-10-1)
- **课程出处**：**课程拆分**；[S15 · L15 · Alignment - SFT/RLHF (Tatsu)](../ai-infra-sources.md#course-s15)、[S16 · L16 · Alignment - RL (Tatsu)](../ai-infra-sources.md#course-s16)。
- **论文与实现**：[Proximal Policy Optimization Algorithms](../ai-infra-sources.md#source-ppo)、[InstructGPT](../ai-infra-sources.md#source-instructgpt)。
- **后续验证（未运行）**：复述/小模型：画角色、数据与更新顺序，单独注明 clipping、KL 和训练批次的定义。

(ai-14-5)=
## 14.5 GRPO / RLVR：group sampling、优势估计与可验证奖励怎样连接，GRPO 与 RLVR 为何不是同义词？

- **先修节点**：[14.4 PPO / InstructGPT](14-post-training-rlhf.md#ai-14-4)
- **课程出处**：**课程拆分与论文补充**；[S16 · L16 · Alignment - RL (Tatsu)](../ai-infra-sources.md#course-s16)、[S17 · L17 · Alignment - RL (Percy)](../ai-infra-sources.md#course-s17)。
- **论文与实现**：[DeepSeekMath / GRPO](../ai-infra-sources.md#source-grpo)。
- **后续验证（未运行）**：CPU：手算一组 rewards 的优势；分别说明算法与奖励来源，检查零方差等边界。

(ai-14-6)=
## 14.6 Rollout Engine 与权重同步：训练更新后的 policy 怎样传到生成侧，每条轨迹怎样对应策略版本？

- **先修节点**：[14.4 PPO / InstructGPT](14-post-training-rlhf.md#ai-14-4)、[11.4 vLLM Scheduler → KV Manager → Model Runner](11-vllm-serving.md#ai-11-4)、[07.2 AllReduce、ReduceScatter 与 AllGather](07-nccl-model-parallelism.md#ai-07-2)
- **课程出处**：**工程补充**；[MREAL · Efficient Reinforcement Learning System for LLMs](../ai-infra-sources.md#course-mreal)。
- **论文与实现**：[ReaL / ReaLHF](../ai-infra-sources.md#source-realhf)、[verl documentation](../ai-infra-sources.md#source-verl)。
- **后续验证（未运行）**：代码阅读/单 GPU或多 GPU：追踪一次参数更新、传输与 rollout，记录角色放置和版本号。

(ai-14-7)=
## 14.7 ReaLHF / verl：角色部署、资源重分配与执行流水线怎样组合训练和生成？

- **先修节点**：[14.6 Rollout Engine 与权重同步](14-post-training-rlhf.md#ai-14-6)、[07.11 DP×TP×PP 组合与 Rank Placement](07-nccl-model-parallelism.md#ai-07-11)、[08.6 FSDP / FSDP2](08-zero-fsdp-memory.md#ai-08-6)；追踪 Ray 编排时先回顾 [Ray Actor 与资源模型](../../topics/distributed-runtime/ray/README.md#ray-actors)。
- **课程出处**：**课程拆分与工程补充**；[MREAL · Efficient Reinforcement Learning System for LLMs](../ai-infra-sources.md#course-mreal)。
- **论文与实现**：[ReaL / ReaLHF](../ai-infra-sources.md#source-realhf)、[HybridFlow / verl](../ai-infra-sources.md#source-hybridflow)、[verl documentation](../ai-infra-sources.md#source-verl)。
- **后续验证（未运行）**：论文/代码比较：分别画控制流、数据流与角色资源；不强配所有算法同样的角色。

(ai-14-8)=
## 14.8 同步/异步 Rollout 与策略版本：增加并发或异步程度怎样改变数据新鲜度、资源竞争和学习结果？

- **先修节点**：[14.7 ReaLHF / verl](14-post-training-rlhf.md#ai-14-7)、[11.11 TTFT、TPOT、吞吐与尾延迟](11-vllm-serving.md#ai-11-11)
- **课程出处**：**工程补充**；[MREAL · Efficient Reinforcement Learning System for LLMs](../ai-infra-sources.md#course-mreal)、[S17 · L17 · Alignment - RL (Percy)](../ai-infra-sources.md#course-s17)。
- **论文与实现**：[verl documentation](../ai-infra-sources.md#source-verl)、[HybridFlow / verl](../ai-infra-sources.md#source-hybridflow)。
- **后续验证（未运行）**：小规模 GPU 环境：明确允许的策略 lag，分别测吞吐、轨迹分布与学习指标。

## 回到实际学习

选一个节点，先复述当前解释，再核查材料或代码并预测实验结果。实验前记录硬件、依赖版本、源码 commit、输入、同步与计时方法；重复测量保留原始记录。具体解释与证据逐步补到 topic 主笔记，未运行的方案保持标注。

[返回总地图](../ai-infra-map.md) · [上一章：13](13-scaling-evaluation.md) · [下一章：15](15-multimodal-bagel.md)
