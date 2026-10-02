---
title: 分布式运行时与资源编排
---

# 分布式运行时与资源编排

任务在哪里执行、依赖怎样满足、进程状态怎样保留，CPU/GPU 资源怎样分配？

[主题索引](../README.md) · [开始一次学习](../../paths/start-here.md)

## 分类边界

Ray 的 Actor 表示有状态进程；RL 的 actor 通常指 policy 角色。张量 collective 的主位置在通信与分布式训练。

## 已有教学 Notebook

[Ray Core · CPU](ray/cpu.ipynb) · [Ray GPU](ray/gpu.ipynb)：讲解、预测、代码和观察交替组织；实验未运行。

## Topic 与材料入口

下表按机制归类已有材料节点。材料页保留具体问题、先修与来源；教学 Notebook 在实际学习后逐步展开。条目不表示个人掌握度。

| Topic | 要解释的问题 | 材料入口 |
| --- | --- | --- |
| Ray Task 与 ObjectRef | 提交、执行、结果等待怎样分开？ | [Ray 1](ray/cpu.ipynb) |
| Ray 对象依赖与背压 | 引用怎样连接工作，怎样限制在途任务？ | [Ray 2](ray/cpu.ipynb) |
| Ray Actor | 持久进程怎样保留实例状态？ | [Ray 3](ray/cpu.ipynb) |
| Ray Actor 并发 | 线程与协程在哪一层并发，状态怎样保护？ | [Ray 4](ray/cpu.ipynb) |
| Ray CPU/GPU 资源 | 逻辑资源与设备可见性怎样对应实际执行？ | [Ray 5](ray/gpu.ipynb) |
| Rollout Engine 与权重同步 | 训练更新后的 policy 怎样传到生成侧，每条轨迹怎样对应策略版本？ | [14.6](../../paths/ai-infra/14-post-training-rlhf.md#ai-14-6) |
| ReaLHF / verl | 角色部署、资源重分配与执行流水线怎样组合训练和生成？ | [14.7](../../paths/ai-infra/14-post-training-rlhf.md#ai-14-7) |
| 同步/异步 Rollout 与策略版本 | 增加并发或异步程度怎样改变数据新鲜度、资源竞争和学习结果？ | [14.8](../../paths/ai-infra/14-post-training-rlhf.md#ai-14-8) |

Ray 的先修可以按需回顾 Python 进程、线程、`asyncio` 与 future；从 Task 提交与结果等待开始，不要求先完成 RLHF 算法课程。

关联分类：[通信与分布式训练](../distributed-training/README.md) · [生成执行与推理服务](../inference-serving/README.md) · [训练目标与评估](../training-evaluation/README.md)。
