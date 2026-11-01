---
title: 列表操作台
description: 点按钮对列表做 append、insert、pop、remove、del、sort、reverse 等操作，看列表和索引怎样变化，并看到对应的 Python 代码和报错（第 6 章）
---

# 列表操作台

<iframe class="sim-frame" src="main.html" height="640" loading="lazy" title="列表操作台"></iframe>

[全屏打开](main.html){ target=_blank } · 对应教材：[6.2 增删改：让列表变起来](../../chapters/06-lists/index.md#62)

## 教学说明

**学习目标**

1. 能说出 append、insert、pop、remove、del 各自从哪里加、按什么删（理解）；
2. 能预测一串列表操作之后列表的内容和长度（应用）；
3. 认识 IndexError、ValueError 两种常见报错的原因（理解）。

**画面与操作**

- 上方方框显示列表当前的样子，每个元素下面有正向索引（蓝）和反向索引（橙），刚变化的元素是浅黄色。
- 先在“元素 x”和“位置 i”里选好参数，再点操作按钮。黑框里记录每一步对应的 Python 代码，有返回值的显示返回值，出错的显示报错信息（与 Python 3.14 的真实报错一致）。
- 可以切换为数字列表或空列表，试试对空列表 pop 会怎样。

**课堂用法建议**

1. 教师在黑板上写一串操作（如先 append 再 insert(0, …) 再 pop()），让学生先预测结果，再用操作台验证。
2. 让学生故意制造两种报错：对空列表 pop()、remove 一个不存在的元素，读一读报错信息。
