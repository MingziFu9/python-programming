---
title: 附录 D 术语表
description: 本书主要术语的中英文名称、简明定义和例子，按章节顺序排列
---

# 附录 D 术语表

本表按章节顺序列出本书的主要术语，每个术语给出英文名称、简明定义和例子。正文中带虚线下划线的术语，把鼠标停在上面就能看到定义，点击可以跳到本表。

通用术语（如“过拟合”“精确率”）的译名和定义以本系列教材共用的《系列公共术语表》为准，各书保持一致。

## 第 1 章 初识 Python：搭好环境，写出第一个程序

| 术语 | 英文 | 定义 | 例子 |
|---|---|---|---|
| <span id="g-程序"></span>程序 | Program | 让计算机按顺序完成任务的一条条指令 | 收银系统、微信都是程序 |
| <span id="g-编程"></span>编程 | Programming | 用编程语言编写程序的过程 | 小周为便利店写收银小程序 |
| <span id="g-编程语言"></span>编程语言 | Programming Language | 人和计算机都能理解、用来编写程序的语言 | Python、C、Java、JavaScript |
| <span id="g-解释器"></span>解释器 | Interpreter | 把 Python 代码逐行翻译并执行的程序，遇到错误就停止 | 安装 Python 主要就是安装解释器 |
| <span id="g-集成开发环境"></span>集成开发环境 | Integrated Development Environment, IDE | 把编辑、运行、调试等功能集成在一起的编程软件 | Thonny、VS Code、IDLE |
| <span id="g-函数"></span>函数 | Function | 有名字、能完成一项功能的代码，用“名字(内容)”的形式调用 | `print("你好")`、`input("姓名：")` |
| <span id="g-字符串"></span>字符串 | String | 用引号括起来的一段文字，也就是文本数据 | `"街坊便利店"`、`'13800001234'` |
| <span id="g-注释"></span>注释 | Comment | 以 # 开头、写给人看的说明，运行时被忽略 | `# 计算找零` |
| <span id="g-交互模式"></span>交互模式 | Interactive Mode | 在 >>> 提示符后输入一行代码、立即得到结果的使用方式 | 在 Shell 中输入 `3.5 * 2` 得到 7.0 |
| <span id="g-脚本"></span>脚本 | Script | 保存在 .py 文件里、可以反复运行的程序 | `lab1_2_poster.py` |
| <span id="g-缩进"></span>缩进 | Indentation | 代码行开头的空格，在 Python 中表示代码的层次，不能随意添加 | `if` 下面的语句缩进 4 个空格 |
| <span id="g-PEP-8"></span>PEP 8 | PEP 8 | Python 官方的代码风格建议 | 逗号后加空格：`print("合计", 100)` |
| <span id="g-追踪信息"></span>追踪信息 | Traceback | 程序出错时 Python 给出的报告，包括出错位置和错误类型 | `NameError: name 'shop_nmae' is not defined` |
| <span id="g-语法错误"></span>语法错误 | Syntax Error | 代码不符合 Python 语法规则的错误，运行前就会被发现 | 少了右括号、用了中文引号 |
| <span id="g-AI-编程助手"></span>AI 编程助手 | AI Coding Assistant | 基于大模型、能解释代码、排查报错、生成代码的工具 | 通义灵码、文心快码 |

## 第 2 章 变量、数据类型与运算

| 术语 | 英文 | 定义 | 例子 |
|---|---|---|---|
| <span id="g-变量"></span>变量 | Variable | 贴在数据上的名字标签，通过名字可以找到和修改数据 | `price = 3.5` 中的 `price` |
| <span id="g-赋值语句"></span>赋值语句 | Assignment Statement | 用 = 把右边算出的值存起来、贴上左边名字的语句，先算右边再赋值 | `total = price * qty` |
| <span id="g-保留字"></span>保留字 | Keyword | Python 自己使用的专用词，不能用作变量名，3.14 共 35 个 | `if`、`for`、`True`、`class` |
| <span id="g-数据类型"></span>数据类型 | Data Type | 数据的种类，决定了数据能做哪些运算 | 整数、浮点数、字符串、布尔值 |
| <span id="g-整数"></span>整数 | Integer, int | 没有小数部分的数 | `2`、`-5`、`2025` |
| <span id="g-浮点数"></span>浮点数 | Floating-point Number, float | 带小数点的数，内部保存的是近似值 | `3.5`、`7.0`、`1e3` |
| <span id="g-布尔值"></span>布尔值 | Boolean, bool | 表示真假的值，只有 True 和 False 两个 | `3 > 2` 的结果是 `True` |
| <span id="g-复合赋值运算符"></span>复合赋值运算符 | Augmented Assignment Operator | 把运算和赋值合在一起的简写，如 +=、-=、*= | `count += 1` 等于 `count = count + 1` |
| <span id="g-类型转换"></span>类型转换 | Type Conversion | 把数据从一种类型变成另一种类型 | `int("12")` 得到 12，`str(100)` 得到 "100" |
| <span id="g-f-string"></span>f-string | Formatted String Literal | 以 f 开头、用花括号插入变量和格式说明的字符串 | `f"{price:.2f}"` 显示 3.50 |

## 第 3 章 字符串：处理文字信息

| 术语 | 英文 | 定义 | 例子 |
|---|---|---|---|

## 第 4 章 条件判断：让程序做选择

| 术语 | 英文 | 定义 | 例子 |
|---|---|---|---|

## 第 5 章 循环：让程序重复做事

| 术语 | 英文 | 定义 | 例子 |
|---|---|---|---|

## 第 6 章 列表与元组：批量管理数据

| 术语 | 英文 | 定义 | 例子 |
|---|---|---|---|

## 第 7 章 字典与集合：按名字找数据

| 术语 | 英文 | 定义 | 例子 |
|---|---|---|---|

## 第 8 章 函数：把代码打包复用

| 术语 | 英文 | 定义 | 例子 |
|---|---|---|---|

## 第 9 章 文件读写与异常处理

| 术语 | 英文 | 定义 | 例子 |
|---|---|---|---|

## 第 10 章 模块、第三方库与面向对象入门

| 术语 | 英文 | 定义 | 例子 |
|---|---|---|---|

## 第 11 章 数据处理初体验：NumPy、pandas 与 Matplotlib

| 术语 | 英文 | 定义 | 例子 |
|---|---|---|---|

## 第 12 章 Python 与人工智能：综合项目

| 术语 | 英文 | 定义 | 例子 |
|---|---|---|---|
