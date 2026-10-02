---
title: 计算与访存的性能模型
---

# 计算与访存的性能模型

| 材料 | 内容与状态 |
| --- | --- |
| [性能模型教学 Notebook](lab.ipynb) | Roofline 讲解、教学参数计算、绘图、NumPy 测量代码交替组织；重写后的代码未运行 |
| [历史 CPU 实验记录](recorded-cpu.ipynb) | 保留原始代码与真实输出，环境和计时见 `results/example-cpu/run.json` |

## 当前结论与证据摘要

Roofline 给出指定计算与访存条件下的上界；向量加法的 useful bytes 估计不等于硬件 DRAM 流量。详细假设、反例、代码和观察问题都在教学 Notebook 中。

历史 CPU 样本只描述其记录环境，不代表学习者服务器，也不是新代码的实测结果。学习者的复述、修正及新实验结论在完成后补充。

[性能分类](../../performance/README.md) · [GAPS](../../../GAPS.md)
