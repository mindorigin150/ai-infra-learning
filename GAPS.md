---
title: 问题与认知边界
---

# 问题与认知边界

这里记录下一步要验证的问题。初始条目是示例提出的**待诊断问题**，不表示已经判断了你的知识水平。回答问题时链接到笔记或实验；解决后移入下方记录，保留证据。

## 已明确的疑问

以下来自用户 2026-10-02 的自述，只记录学习目标，不推断其他能力。

- [ ] 使用过 vLLM，但不清楚具体实现。入口：[11.4 请求的执行路径](paths/ai-infra/11-vllm-serving.md#ai-11-4)。下一步：按实际版本追踪 scheduler、KV manager 和 model runner。
- [ ] 接触过 GPU 视图与简单 kernel，目前 kernel 编写需要回顾。入口：[04.1 执行组织](paths/ai-infra/04-gpu-profiling.md#ai-04-1)、[05.1 CUDA Vector Add](paths/ai-infra/05-cuda-triton-kernels.md#ai-05-1)。下一步：先解释线程索引与边界，再预测最小实验。

其他接触经历已放在[学习地图](paths/ai-infra-map.md)的个人入口中。DeepSpeed、FlashAttention、packing、communication 与 KV/page 不因出现在经历列表中而被判为已掌握或存在误解。

## 待诊断区域

- [ ] **Ray：待诊断**。能否从代码解释提交与等待分离、顶层 ObjectRef 的依赖、在途工作与运行并发度？依据：[Ray 主笔记](topics/distributed-runtime/ray/README.md#ray-tasks)及官方 Task/Object 文档。先修：函数调用与 future。验证：先预测两种 `get` 写法，再观察 CPU 事件；实验未运行。
- [ ] **Actor 并发：待诊断**。能否区分串行、线程与协程的执行位置，以及跨等待的共享状态更新？依据：[并发单元](topics/distributed-runtime/ray/README.md#ray-concurrency)。先修：进程地址空间、GIL 与 `await`。验证：复述 PID/线程 ID 的预测并观察三组用例；实验未运行。
- [ ] **GPU 资源：待诊断**。能否解释两个 GPU Actor 都使用 `cuda:0`，以及逻辑资源声明与实际计算的关系？依据：[资源单元](topics/distributed-runtime/ray/README.md#ray-resources)及官方资源文档。先修：设备可见性与进程。验证：核查 Ray ID、环境变量与双卡 Actor 记录；实验未运行。
- [ ] 能否区分“有效数据流量估计”与硬件实际 DRAM 流量？关联：[性能模型](topics/foundations/performance-model/README.md)。验证：解释向量加法实验里缓存如何影响结果。
- [ ] 能否解释一个操作远低于 Roofline 上界的原因？验证：指出模型遗漏的假设，并提出下一项观测。

## 项目中遇到的问题

开始真实项目后填写，并链接到对应项目与复现记录。

## 新发现的候选主题

记录发现来源、为什么可能重要、关联主题与先修条件。由外部资料提出的主题先标“待诊断”。

本轮新增的候选学习范围与出处见[课程、论文与工程来源](paths/ai-infra-sources.md)。这些是待进入的主题，不是已经诊断出的个人缺口；学习实验均未运行。

## 已解决与证据

记录问题、解释或实验链接，以及仍然适用的前提。
