---
title: 主题索引
---

# 主题索引

按**系统机制**寻找具体 topic：先确定希望解释的行为，再进入教学 Notebook 或材料节点。分类不是学习顺序；先修关系与目标路线放在 `paths/`。

## 按 topic 进入

| 分类 | 要解释的机制 |
| --- | --- |
| [模型表示与生成机制](models/README.md) | 输入怎样变成模型表示，模型结构怎样决定训练与生成的计算？ |
| [数据组织与流水线](data-pipelines/README.md) | 样本怎样经过处理、采样、组合与搬运，成为模型消费的输入？ |
| [张量计算与自动微分](tensor-autograd/README.md) | 张量怎样组织存储和计算，梯度与训练状态怎样完成一次更新？ |
| [GPU 执行与算子优化](gpu-execution/README.md) | 一个算子怎样映射到 GPU 的线程、存储和指令，执行如何被融合或编译？ |
| [性能模型与观测](performance/README.md) | 哪些成本约束执行，怎样可靠测量并用证据定位瓶颈？ |
| [通信与分布式训练](distributed-training/README.md) | 多个设备怎样交换张量、划分模型与训练状态，并保持一次更新的语义？ |
| [分布式运行时与资源编排](distributed-runtime/README.md) | 任务在哪里执行、依赖怎样满足、进程状态怎样保留，CPU/GPU 资源怎样分配？ |
| [数值表示与模型适配](model-efficiency/README.md) | 怎样改变数值精度、表示或可训练参数，成本与模型质量怎样变化？ |
| [训练目标与评估](training-evaluation/README.md) | 优化的目标是什么，预算与数据怎样影响学习，怎样验证模型质量？ |
| [生成执行与推理服务](inference-serving/README.md) | 请求怎样进入生成循环，缓存、批处理与调度怎样组织模型执行？ |

## 已有教学材料

| 主题 | 主位置 | 内容状态 |
| --- | --- | --- |
| [Ray CPU](distributed-runtime/ray/cpu.ipynb) · [Ray GPU](distributed-runtime/ray/gpu.ipynb) | 分布式运行时与资源编排 | CPU 为《Learning Ray》公开章节的中文改编；GPU 保留原实验，运行状态见主题入口 |
| [性能模型教学 Notebook](foundations/performance-model/lab.ipynb) | 性能模型与观测 | 重写后的代码未运行；原真实 CPU 输出另存历史 Notebook |

这些状态描述内容与证据，不评价学习者掌握度。

## 主题如何连接

每个材料节点有一个主要归属，跨领域关系通过链接连接。例如 MoE 结构在模型表示、Expert Parallelism 在分布式训练、Grouped GEMM 在 GPU 优化。Ray 的 GPU 资源分配连接模型执行，张量通信连接 NCCL，生成循环与 KV 调度连接 vLLM。

分类页覆盖现有 143 个材料节点，并增加 Ray 教学 Notebook 入口。[课程学习地图](../paths/ai-infra-map.md)与[来源对照](../paths/ai-infra-sources.md)继续保留，便于查先修与出处。新的解释、修正和实测证据补回 topic 的 Notebook；README 保存精选结论摘要。

## 新主题的最小结构

```text
topics/<机制分类>/<主题>/
    README.md        Notebook 入口、来源定位与精选结论摘要
    lab.ipynb        依据主教材展开的中文讲解、注释代码与练习
    requirements.txt 主题实验依赖
    assets/          主题插图及绘图源码
    results/         精选小结果及环境记录
```

分类页维护具体 topic 的 Notebook 与材料入口。先选定并阅读主材料、核查改编许可，再从 `templates/lab.ipynb` 展开教学内容，README 从 `templates/topic.md` 开始，保留学习者自己的解释并区分来源、推断与实测。使用相对链接，新增公开 Notebook 时更新相关路径和 `myst.yml`；已有主题入口路径保持稳定。
