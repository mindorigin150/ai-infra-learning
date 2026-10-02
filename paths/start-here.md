---
title: 开始一次学习
---

# 开始一次学习

先选择一个你希望解释的现象，例如“为什么增加 batch size 后吞吐提升，但延迟也增加”。学习路线保存这些目标及先修关系，主题笔记保存不断更新的知识。

## 从具体技术节点开始

打开 [topic 分类索引](../topics/README.md)，先按要解释的机制定位，再进入主笔记或具体材料节点。例如任务编排进入 [Ray](../topics/distributed-runtime/ray/README.md)，算子执行进入 [GPU 执行](../topics/gpu-execution/README.md)，生成请求进入 [推理服务](../topics/inference-serving/README.md)。

每个节点都有具体问题、先修链接、课程出处、论文/实现和未运行的验证方案。先定位它在系统中的作用，再挑一个问题进入机制；遇到先修缺口时沿链接回顾。目录不是掌握度记录，也不要求按编号先修完所有课。

[CS336 × CMU 11-868 学习地图](ai-infra-map.md)继续提供课程材料和先修链；[来源页](ai-infra-sources.md)区分课程拆分、论文补充和工程补充。分类决定内容的主位置，路径决定本次学习的先后。

## 当前路线：Ray Core 与 CPU／GPU

1. 从 [Task 与 ObjectRef](../topics/distributed-runtime/ray/README.md#ray-tasks)解释提交、执行和等待，预测两种 `get` 写法的执行区间。
2. 在服务器运行 CPU `tasks` 用例，读取事件与数值结果；再进入[对象依赖](../topics/distributed-runtime/ray/README.md#ray-objects)、[Actor 状态](../topics/distributed-runtime/ray/README.md#ray-actors)和[并发](../topics/distributed-runtime/ray/README.md#ray-concurrency)。
3. 解释[逻辑资源与 GPU 编号](../topics/distributed-runtime/ray/README.md#ray-resources)，预测两个 Actor 的设备映射，再运行单卡 Task 和双卡 Actor。
4. 按[实验说明](../topics/distributed-runtime/ray/README.md#ray-labs)取回结果，比较预测与观察，把复述、修正和剩余问题补回主笔记与 GAPS。

服务器双卡 RTX6000 Pro、96 核 CPU 来自用户自述。实验代码已准备，CPU/GPU 实验未运行；默认使用 4 个逻辑 CPU，实际环境由记录确认。

## 性能模型示例路线

1. 打开 [性能模型示例](../topics/foundations/performance-model/README.md)，先尝试回答开头的诊断问题。
2. 用交互图改变一个参数，预测变化，然后核对模型给出的结果。
3. 在远程服务器完成 [向量加法实验](../topics/foundations/performance-model/lab.ipynb)，保存真实结果。
4. 复述模型能解释什么、不能解释什么；把剩余问题记入 [GAPS](../GAPS.md)。

这是示例路线。后续依据你的目标和回答调整，不视为完整课程或掌握度评价。

## 与 LLM 开始会话

把下面这一段作为对话起点，替换方括号内容：

> 我想解释：[一个具体问题]。请先阅读 AGENTS.md、相关主题和 GAPS。
> 如果对应学习地图，请先打开该 section 的问题与先修节点，按需要阅读材料。
> 先列出最小的先修关系，标出可能需要诊断的前提，再用 1–3 个问题了解我的当前理解。
> 每次只讲一个概念单元，讲清机制和假设。设计一个我能在当前服务器上运行的小实验，先让我预测结果。
> 结合我的复述、真实代码和一手资料找遗漏；区分待诊断缺口和已经发现的误解。

如果需要知识地图，先让 LLM 说明每个节点**为什么与目标有关**、依赖什么、需要理解到什么深度，再挑一个节点开始。不要一次生成全部笔记。

## 一次会话应留下什么

| 成果 | 去哪里 |
| --- | --- |
| 当前解释、关键假设、修正理由 | 对应 topic 主笔记 |
| 输入、计时方法、运行记录与结果 | Notebook 和 `results/` |
| 可重复运行的实现 | 主题或项目中的脚本 |
| 无法解释的现象、候选先修主题 | GAPS |
| 下一步目标与顺序 | 相应 `paths/` 文件 |

原始会话可以临时留在 `inbox/`；整理成理解与证据后再归档。周期性拿现有主题与外部课程、框架文档和实际代码做 coverage audit，要求每项缺口提供具体依据。
