---
title: 异常捕获流程
description: 用三组不同的输入单步执行 try-except-else-finally 程序，观察出错时跳过哪些行、哪个 except 接住了异常、else 和 finally 何时执行（第 9 章）
---

# 异常捕获流程

<iframe class="sim-frame" src="main.html" height="620" loading="lazy" title="异常捕获流程"></iframe>

[全屏打开](main.html){ target=_blank } · 对应教材：[9.5 异常处理](../../chapters/09-files/index.md#95)

## 教学说明

**学习目标**

1. 能说出 try 中某一行出错后，后面的行不再执行、程序跳到匹配的 except（理解）；
2. 能说出 else 只在没有出错时执行、finally 无论如何都执行（记忆）；
3. 能预测给定输入时程序的输出（应用）。

**画面与操作**

- 左边是代码，橙色是下一步要执行的行；右边是变量表和输出。
- 三个标签是三组输入：3（正常，走 else）、abc（ValueError）、0（ZeroDivisionError）。三种情况最后都执行 finally，并且程序都“继续运行”，没有崩溃。

**数据来源**：程序由 `tools/make_trace.py` 在 Python 3.14 中真实运行生成。

**课堂用法建议**

1. 先让学生对三组输入分别写出预测的输出，再用动画核对。
2. 问学生：输入 abc 时，第 4 行为什么没有执行？如果去掉 try，程序会怎样？
