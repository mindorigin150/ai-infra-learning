---
title: Ray · 教学 Notebook 入口
---

# Ray

教学材料按“讲解 → 预测 → 代码 → 观察与复述”组织在 Jupyter Notebook 中。

| 顺序 | 教学 Notebook | 内容与环境 |
| --- | --- | --- |
| 1 | [Ray Core · CPU](cpu.ipynb) | Task、ObjectRef、依赖、背压、Actor、线程与协程；默认 4 个逻辑 CPU |
| 2 | [Ray GPU](gpu.ipynb) | 单卡 Task、双卡 Actor、设备编号与状态；服务器 CUDA 版 PyTorch 环境 |

**实验状态：两份 Notebook 均未运行。** 双卡 RTX6000 Pro、96 核 CPU 来自用户自述；实际设备、版本与资源由 Notebook 的运行记录确认。

依赖准备、kernel 选择、工作目录、错误记录、清理和结果回收都在各 Notebook 内。核心定义与调用直接写在代码单元中。网站展示讲解、代码与已保存输出；运行在服务器 Jupyter kernel 完成。

## 当前结论与证据

尚无服务器实测或学习者复述。学习后将精选结论、修正依据与限制摘要补到这里，详细解释和真实输出继续维护在 Notebook。

[运行时分类](../README.md) · [topic 索引](../../README.md) · [GAPS](../../../GAPS.md)
