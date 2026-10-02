---
title: 主题索引
---

# 主题索引

主题是长期知识节点；新的观察补回节点，学习路线链接到节点。下面的领域是导航候选，创建具体主题时再建文件夹。

| 领域 | 可逐步加入的内容 | 已有主题 |
| --- | --- | --- |
| Foundations | 内存、进程、数值、网络、性能模型 | [计算与访存的性能模型](foundations/performance-model/README.md) |
| GPU | 执行模型、访存、streams、kernel、profiling | 待实际学习时创建 |
| Distributed | collectives、通信、DDP、FSDP、并行策略 | 待实际学习时创建 |
| Training runtime | autograd、allocator、数据加载、编译 | 待实际学习时创建 |
| Inference | KV cache、batching、量化、服务调度 | 待实际学习时创建 |

跨领域概念选择一个主位置，其他主题通过链接连接；分类有困难时先放 `inbox/`。只在理解和内容规模需要时拆分主题。

## 新主题的最小结构

```text
topics/<领域>/<主题>/
    README.md        当前知识模型与证据入口
    lab.ipynb        需要实验时再添加
    experiment.py    需要独立实现时再添加
    requirements.txt 实验依赖
    assets/          主题图片及绘图源码
    results/         精选小结果及环境记录
```

从根目录 `templates/` 复制模板，填写标题，使用相对链接，并在 `myst.yml` 中添加主笔记和需要公开的实验页面。网站 URL 保留文件夹结构；主题路径保持稳定。
