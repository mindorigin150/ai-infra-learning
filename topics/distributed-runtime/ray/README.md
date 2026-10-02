---
title: Ray · 教材与实验入口
---

# Ray

从一个读取八条记录的 Python 程序开始，逐步学习怎样提交远程任务、传递结果、连接依赖和保留实例状态。主要阅读材料已选定，本地 CPU Notebook 提供所选入门范围的完整中文改编、注释与练习。

## 主材料与阅读范围

**主要教材：[《Learning Ray》公开版第 2 章](https://maxpumperla.com/learning_ray/ch_02_ray_core/)**，作者 Max Pumperla、Edward Oakes、Richard Liaw。采用其中 **A Ray Core Intro**：Your First Ray API Example、Ray Tasks、The Object Store、Non-blocking calls、Task dependencies、Ray Actors。

选择它是因为这些部分沿用同一个数据读取程序，每个新工具都回应上一阶段出现的需要。默认先修是基本 Python 函数、循环和类；装饰器、进程和异步返回在本地首次使用时解释。所选范围的正文与代码已阅读；系统内部、故障恢复和 MapReduce 不在本轮改编范围。

改编依据：[作者公开 Notebook](https://github.com/maxpumperla/learning_ray/blob/321ebe5fdab451f75f2736683fd40921feffdf27/notebooks/ch_02_ray_core.ipynb)，提交 `321ebe5fdab451f75f2736683fd40921feffdf27`。原示例基于 Ray 2.2.0，本地代码面向 Ray 2.59.0；核查日期为 2026-10-02。公开仓库的 [MIT 许可与版权声明](LICENSE.learning-ray.txt)随改编保留，许可不延伸到出版书全文；本页采用公开版，不声称完整翻译了出版书。

**辅助对照：[官方 Gentle Introduction](https://docs.ray.io/en/latest/ray-core/examples/gentle_walkthrough.html)**，同一书籍案例的简化版。API 语义另对照官方 [Tasks](https://docs.ray.io/en/latest/ray-core/tasks.html)、[Objects](https://docs.ray.io/en/latest/ray-core/objects.html)、[Actors](https://docs.ray.io/en/latest/ray-core/actors.html)及相应接口文档；它们用于技术核查。

## 本地阅读与实验

| 顺序 | Notebook | 内容与环境 |
| --- | --- | --- |
| 1 | [Ray Core · CPU](cpu.ipynb) | 完整中文入门改编，四组练习、待填写代码及紧接的测试；4 份逻辑 CPU，无需 GPU |
| 可选 | [CPU Notebook 末尾](cpu.ipynb#ray-cpu-advanced) | 原有背压、线程与协程实验；保留为进阶内容，尚未按新标准展开 |
| 后续 | [Ray GPU](gpu.ipynb) | 原有单卡 Task、双卡 Actor 与设备映射实验；本轮未改写正文 |

本仓库补充了逐步的中文解释、核心代码注释、等待位置与传参方式的对照、普通类到 Actor 的过渡，以及四道迁移练习。任务依赖示例用大写转换代替原文相邻记录查询，便于追踪数据流。修正了原文的 GIL 归因、等待超时描述和 Actor 更新等待关系；具体依据与章节对应在 Notebook 文末。

**状态：CPU 示范与进阶已有 6000pro 实测输出；四道练习待学习者实现并运行测试；GPU 本轮未验证。** 不把原书计时作为本仓库输出。默认在远程 kernel 执行，网站仅展示讲解与已保存输出。双卡 RTX6000 Pro、96 核 CPU 来自用户自述，实际环境以运行记录为准。

## 当前结论与证据

本次 CPU 工程校验使用 Python 3.13.5、Ray 2.59.0 和 4 份逻辑 CPU。示范验证了结果一致性、顶层引用传参、下游依赖，以及同一 Actor 累加与不同 Actor 状态独立。计数集成示例等待各次更新完成后得到与读取条数一致的计数。可选背压和并发实验也通过各自的语义检查。

[入门环境与计时记录](results/2026-10-02-intro-run.json) · [进阶事件记录](results/2026-10-02-advanced-run.json) · [Actor 时间线 SVG](results/actor-timeline.svg)。计时包含教学等待和运行时开销，不据此比较机器算力；原始输出保存在 Notebook。每道练习均为“题目 → TODO → 测试”，默认没有参考实现和预填的通过输出。测试有效性验证使用独立临时实现，不代表学习者完成了练习；学习者自己的练习、复述与修正仍待填写。

[运行时分类](../README.md) · [topic 索引](../../README.md) · [当前路线](../../../paths/start-here.md) · [GAPS](../../../GAPS.md)
