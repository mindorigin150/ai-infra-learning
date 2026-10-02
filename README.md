---
title: AI Infra Learning
description: 一个随实际问题生长的 AI 系统学习工作台。
---

# AI Infra Learning

从一个问题出发，建立解释，做一个实验，再用结果修正理解。

这个仓库以 **Jupyter Notebook 中交替展开的讲解、预测、代码和观察** 保存学习材料。Markdown 维护分类导航、学习路线与结论摘要；需要独立运行的工程实现再提取为脚本。

| 从这里开始 | 用途 |
| --- | --- |
| [按 topic 学习](topics/README.md) | 10 个系统机制分类，连接具体问题、主笔记与材料 |
| [Ray Core · CPU](topics/distributed-runtime/ray/cpu.ipynb) | Task、ObjectRef、Actor、并发：讲解与代码交替 |
| [Ray GPU](topics/distributed-runtime/ray/gpu.ipynb) | 单卡 Task、双卡 Actor 与设备映射：讲解与代码交替 |
| [开始一次学习](paths/start-here.md) | 与 LLM 小步学习、诊断理解、安排实验 |
| [性能模型教学 Notebook](topics/foundations/performance-model/lab.ipynb) | Roofline 讲解、参数计算与 NumPy 计时；另保留历史 CPU 输出 |
| [学习地图：CS336 × CMU 11-868](paths/ai-infra-map.md) | 保留课程材料的 16 章、143 个具体技术节点及先修关系 |
| [课程、论文与工程来源](paths/ai-infra-sources.md) | 原课对照、材料入口与补充内容的来源 |
| [问题清单](GAPS.md) | 记录认知边界和下一步问题 |
| [视觉规范](STYLE.md) | 后续图表与交互演示保持一致 |

## 阅读与编辑

发布完成后的固定入口是 [GitHub Pages 网站](https://mindorigin150.github.io/ai-infra-learning/)。日常阅读无需启动 WSL，算力服务器也可以离线。网站展示 Notebook 的讲解、代码和已保存输出；执行与修改参数在服务器 Jupyter kernel 中完成。

编辑使用 VS Code。需要预览尚未发布的内容时，在仓库根目录执行：

```bash
npm ci
npm run dev
```

打开终端显示的网址。第一次启动会下载 MyST 主题；`npm run build` 构建静态网站并严格检查内部链接，输出位于 `_build/html/`。网站构建不会执行 Notebook。

## 仓库如何生长

```text
paths/       学习顺序和目标，链接到 topics
topics/      稳定知识主题：教学 Notebook、结论摘要、主题素材
projects/    跨主题的完整项目
inbox/       尚未归类的材料
templates/   创建笔记、实验和概念图的起点
assets/      跨主题共享的样式与素材
GAPS.md      问题与待诊断区域
AGENTS.md    LLM 在这个仓库工作的约定
```

同一主题的新发现补回它的 Notebook，Git 保存历史。[分类页](topics/README.md)按系统机制维护具体 topic 的入口；新主题从根目录的 `templates/lab.ipynb` 编写教学内容，`README.md` 从 [主题入口模板](https://github.com/mindorigin150/ai-infra-learning/blob/main/templates/topic.md) 开始；随后更新分类页、主题索引、相关学习路线和 `myst.yml` 的目录。暂时无法归类的材料先放 `inbox/`。

主题图片放在主题自己的 `assets/`；多个主题共用的素材再放根目录 `assets/`。Notebook 留下精选输出；可重复运行的实现提取到 `.py`、`.cu` 或 `.cpp`，并注明运行环境。

## 在流动算力服务器做实验

1. 在服务器上 clone 仓库，记下 `git rev-parse HEAD`。
2. 使用 VS Code Remote SSH 连接，在远程窗口安装 Python/Jupyter 扩展，打开服务器上的仓库。
3. 按实验自己的 `requirements.txt` 创建环境，在 Notebook 右上角选择远程 Python kernel。
4. 运行实验，保存 Notebook 输出、图表和环境记录；临时运行文件放 `.runs/<run-id>/`。
5. 回收服务器前，在本机取回结果，整理后提交到 GitHub。

例如，服务器上的仓库路径是 `~/ai-infra-learning`，SSH 别名是 `gpu-box`：

```bash
# 本机仓库根目录：取回结果到新目录，不覆盖正在编辑的源码
mkdir -p .runs/from-gpu-box
rsync -av gpu-box:~/ai-infra-learning/topics/foundations/performance-model/results/ .runs/from-gpu-box/results/
rsync -av gpu-box:~/ai-infra-learning/topics/foundations/performance-model/lab.ipynb .runs/from-gpu-box/
```

比较远程与本地的源码修改；把选定结果放回主题 `results/`、图表放回 `assets/`，保留 Notebook 用到的文件名与相对路径。再将 Notebook 和主笔记一起更新。原始大文件、数据集、权重不放 Git；需要复现时记录它们的位置与获取步骤。

代码变更也通过 Git 保存。两台机器同时修改时，先检查各自 `git status` 和差异，再合并；运行中的目录不直接用同步命令覆盖。

## 第一次发布

目标是公开仓库 `mindorigin150/ai-infra-learning`。如果还没有创建，在 GitHub 新建同名公开仓库，保留为空；本地首次推送：

```bash
git remote add origin git@github.com:mindorigin150/ai-infra-learning.git
git add .
git commit -m "Set up AI infra learning workspace"
git push -u origin main
```

在 GitHub 的 **Settings → Pages → Source** 选择 **GitHub Actions**，然后在 Actions 中运行 **Publish learning site**。以后推送 `main` 会自动更新网站。工作流从 Pages 配置读取部署子路径，图片和交互资源会随网站一起发布。[MyST 部署说明](https://mystmd.org/guide/deployment-github-pages)

仓库和网站均公开。提交内容以自己的学习笔记和可公开的精选结果为准。
