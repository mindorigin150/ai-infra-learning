---
title: 视觉规范
---

# 视觉规范

暖色笔记风：米白纸面、深灰正文、低饱和语义配色。笔记默认中文，图表标签默认英文。图要服务于一个具体解释，保存可以重画的源码。

夜间模式使用暖炭灰背景、暖白文字和更明亮的语义色。页面、导航、表格和交互图随同一个主题开关切换。

## 颜色是语义

唯一颜色值来源为 `assets/styles/tokens.json`。下表说明含义；实际绘图从配置读取，不手工另建一套色板。

`colors` 定义白天与导出图表的色板；`dark_colors` 覆盖网站和交互图在夜间使用的颜色。

| 角色 | 颜色 | 典型用途 |
| --- | --- | --- |
| Background / Surface | 米白 / 暖白 | 页面和绘图画布 |
| Text / Muted | 深灰 / 灰褐 | 正文、图注和辅助标签 |
| Compute | 蓝 | 计算单元、计算上界 |
| Memory | 赭黄 | 缓冲区、访存、带宽上界 |
| Communication | 青绿 | 数据传输、通信、流程连接 |
| Warning | 铁锈红 | 瓶颈、失败、待关注的观测点 |

角色含义需要结合图例：Roofline 的绿色组合线表示计算与访存两个约束的共同作用。普通类别比较图用同一色板区分系列，并给系列写清名称。不能让读者仅通过颜色判断含义。

## 字体与排版

- 网页：系统 sans-serif 与中文字体栈，默认正文 18px、行高 1.8。优先保证设备上清晰阅读。
- 桌面导航与正文之间保留约 40–48px 的空隙，标题、正文与图表沿同一网格对齐。
- 代码：系统等宽字体栈。
- 实验图：DejaVu Sans，默认正文/坐标轴 11pt、标题 13pt、图例 10pt，画布 7.2 × 4.2 inch。
- 图表默认英文技术标签，远程环境可以直接使用 matplotlib 自带字体。用户要求中文标签时，安装并显式配置中文字体，再检查导出。

## 根据问题选择图

| 要说明什么 | 默认工具 | 保存内容 |
| --- | --- | --- |
| 依赖、数据流、执行流程 | Mermaid | Markdown 中的图源码 |
| 实验数据、分布、趋势 | matplotlib | Python/Notebook 与 SVG |
| 参数变化的机制 | 浏览器 widget | JavaScript、共享 CSS、模型公式 |

概念图默认左到右；实线箭头表示实际流向，虚线用于关联或假设，并在图注说明。保持短标签，复杂机制拆成几张图。数据图包含轴名、单位、系列图例和条件；重复测量注明汇总方法。

模型预测、测量与示意数据必须标明。交互图注明假设与参数来源，显示单位；需要拖动参数才能理解的问题适合交互，固定结论适合静态图。

## 如何复用

修改颜色或基础字体：编辑 tokens 后在根目录执行 `npm run style`，提交生成的样式和 Mermaid 模板。开发和构建命令也会同步这些文件。

远程 matplotlib 实验：

```python
from pathlib import Path
import matplotlib.pyplot as plt

# 在仓库根目录运行时
plt.style.use(Path("assets/styles/plots.mplstyle"))
```

配色有具体语义时，从 tokens JSON 读取相应颜色。例如带宽曲线使用 `colors["memory"]`。主题内实验使用明确的相对路径定位样式，不依赖当前机器的字体目录。

Mermaid 从 `templates/diagram.md` 复制图块，保留角色 class，替换节点和连线。修改 tokens 后，已有内嵌图源码与导出图需要同步重画；生成脚本不会自动改写所有主题笔记。

网站由 `myst.yml` 加载共享 CSS，并通过 `project.static_files` 发布样式目录。Notebook 的 matplotlib 单元加载共享 mplstyle，并从 tokens 读取语义配色；改变模型参数后用同一单元重画，保存 SVG 与 Notebook 内的 PNG 输出。

若后续确需浏览器交互，组件内部也加载共享 CSS，资源路径按模块发布位置解析，并继承页面颜色变量。教学参数和硬件参数必须明确区分。

静态图优先 SVG，Notebook 保留 PNG 输出。当前 SVG 将字形转为路径，方便跨机器显示；可编辑的文字与数据保留在绘图源码中。

## 参照成品

参照 [性能模型 Notebook](topics/foundations/performance-model/lab.ipynb)的 Mermaid 与模型绘图代码，以及[历史 CPU 记录](topics/foundations/performance-model/recorded-cpu.ipynb)的真实曲线。网站图表、课堂解释和导出素材使用相同约定。[MyST 样式说明](https://mystmd.org/guide/website-style)
