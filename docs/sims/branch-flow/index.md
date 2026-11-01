---
title: 分支流程走一遍
description: 单步执行 if-else 和 if-elif-else 程序，输入不同的值，看程序走了哪条路、跳过了哪些分支（第 4 章）
---

# 分支流程走一遍

<iframe class="sim-frame" src="main.html" height="600" loading="lazy" title="分支流程走一遍"></iframe>

[全屏打开](main.html){ target=_blank } · 对应教材：[4.2 if 语句：让程序做选择](../../chapters/04-conditions/index.md#42)

## 教学说明

**学习目标**

1. 能说出 if-else 两条路只走一条，以及条件为 True、False 时分别执行哪些行（理解）；
2. 能预测 if-elif-else 在给定输入下判断了几次、进入了哪个分支（应用）。

**画面与操作**

- 左边是代码，橙色是下一步要执行的行；右边上方是变量表，右下是输出。
- 三个标签是三组输入：“128 元，会员”两个 if 都成立；“86 元，非会员”走 else、跳过打折；“75 分”演示 elif 一旦成立，后面的分支全部跳过。

**数据来源**：三段程序都由 `tools/make_trace.py` 在 Python 3.14 中真实运行生成。

**课堂用法建议**

1. 在每个 if 行暂停，让学生先说出条件是 True 还是 False，再点“下一步”验证。
2. 让学生数一数“75 分”一共判断了几次条件（3 次），再问输入 95 时判断几次（1 次）。
