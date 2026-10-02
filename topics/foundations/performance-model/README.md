---
title: 计算与访存的性能模型
---

# 计算与访存的性能模型

**状态：骨架中的教学示例。** 本页不是你的掌握度记录。交互图使用示意参数；[实验页面](lab.ipynb) 的输出来自实际记录的 CPU 运行，环境和原始计时一起保存。

## 从一个问题开始

一个操作的 FLOPs 很少，为什么运行时间仍可能很长？在优化计算之前，我们需要理解执行中还有哪些成本。

先尝试回答三个问题，再让 LLM 按你的解释继续讲：

1. 做 `out = x + y` 时，除了加法，还需要做什么？
2. 什么情况下，把计算能力翻倍仍然不会让这个操作快一倍？
3. 如果从很小的输入换成大输入，你预计有效带宽会怎样变化？为什么？

## 当前 mental model

完成计算需要执行算术，也需要在相关内存层级移动数据。两个约束分别给出性能上界；当前操作的算术强度决定哪个约束更紧。

```{include} ../../../templates/diagram.md
```

图中的箭头表示数据流，是一个简化的机制示意；真实机器的缓存层级和执行调度没有画出。

定义算术强度 $I=F/B$：$F$ 是 FLOP 数，$B$ 是**指定内存层级**的数据流量。若计算峰值为 $P_{peak}$、该层级带宽为 $BW$，简单 Roofline 模型给出：

$$
P_{roof}=\min(P_{peak},\ BW\cdot I).
$$

当 $I<P_{peak}/BW$ 时，模型由带宽约束；更高算术强度下，计算峰值成为限制。两条线的交点称为 ridge point。[Berkeley Lab 的 Roofline 说明](https://amcr.lbl.gov/departments/computer-science-department/ppan/roofline-performance-model/)

这里的 $P_{roof}$ 是上界。它没有承诺实际操作能够达到这条线，也没有包含所有启动、依赖、调度和同步成本。

## 改一个参数，先预测再观察

预测：固定带宽和计算峰值，将算术强度提高十倍，什么时候上界会提高十倍？什么时候会停止增长？

```{anywidget} ./assets/roofline.mjs
:css: ../../../assets/styles/site.css
{
  "intensity": 1,
  "bandwidth": 100,
  "peak": 1000
}
```

初始参数是教学示意：1 FLOP/byte、100 GB/s、1000 GFLOP/s；没有绑定任何 CPU/GPU 型号。控件使用对数刻度。它在浏览器计算公式，服务器离线也可使用。

静态例子：这组参数的 ridge point 是 10 FLOP/byte；强度为 1 时，上界为 100 GFLOP/s；强度为 100 时，上界为 1000 GFLOP/s。以上是公式算出的数值。

## 最小实验：NumPy 向量加法

固定 float32、预分配输入输出，只改变数组长度。每轮用 `np.add(x, y, out=out)` 避免把输出分配混入计时。预热后重复测量，保存每次计时及中位数、四分位数。

以读两个输入、写一个输出估算 useful bytes：$B_{useful}=12N$。定义有效带宽为 $B_{useful}/t$，单位 GB/s。它使用十进制 GB，不是 GiB。

在服务器仓库根目录安装示例环境：

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r topics/foundations/performance-model/requirements.txt
```

随后在 VS Code Remote SSH 中打开 [lab.ipynb](lab.ipynb)，选择这个环境的 kernel。仓库的 VS Code 设置让 Notebook 从所在目录运行；其他 Jupyter 前端也请使用这个工作目录。

直接运行脚本也可以。在仓库根目录：

```bash
.venv/bin/python topics/foundations/performance-model/benchmark.py \
  --output .runs/vector-add-first \
  --context "CPU experiment on my current compute server"
```

输出 `run.json` 和 `summary.csv`；JSON 包含原始计时、环境、代码版本、参数和运行命令。Notebook 完成同一运行后会导出 SVG/PNG 并显示图表。

## 结果能够说明什么

比较不同规模的耗时与有效带宽，提出下一步观测。不要预设一定存在单调关系；不同机器和系统负载会给出不同曲线。

这里的 useful bytes 不是硬件计数器测到的 DRAM 流量。小输入可能反复命中缓存，输出写入可能引入额外流量，短操作还受调用和计时开销影响。因此不能把这个实验的最高有效带宽当作真实 DRAM 峰值，更不能套用到 GPU。

## 检验理解与下一步

- 用自己的话解释：减少计算量为什么可能几乎没有加速？
- 指出一个会让 $12N$ 流量估计不足的前提。
- 一个实测点远低于 Roofline 上界时，你下一步会测什么，而不是立即改代码？

把无法回答的问题放入 [GAPS](../../../GAPS.md)，后续可以沿缓存、tensor layout、GPU 计时或 kernel launch 继续学习。

## 来源

- [Roofline performance model — Berkeley Lab](https://amcr.lbl.gov/departments/computer-science-department/ppan/roofline-performance-model/)
- [numpy.add](https://numpy.org/doc/stable/reference/generated/numpy.add.html)
- [time.perf_counter_ns](https://docs.python.org/3/library/time.html#time.perf_counter_ns)

本示例组织与接口查阅日期：2026-10-02。
