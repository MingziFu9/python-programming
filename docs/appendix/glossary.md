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
| <span id="g-转义字符"></span>转义字符 | Escape Character | 以反斜杠 \ 开头、表示特殊字符的写法 | `\n` 换行、`\t` 制表符、`\\` 反斜杠 |
| <span id="g-原始字符串"></span>原始字符串 | Raw String | 在引号前加 r，让反斜杠不再转义，原样保留 | `r"C:\new\data"` |
| <span id="g-索引"></span>索引 | Index | 字符在字符串中的位置编号，从 0 开始；负数表示从末尾往前数 | `s[0]` 第一个字符，`s[-1]` 最后一个 |
| <span id="g-切片"></span>切片 | Slice | 用 [开始:结束:步长] 取出一段，包含开始、不包含结束 | `"街坊便利店"[0:2]` 得到 `'街坊'` |
| <span id="g-方法"></span>方法 | Method | 属于某种数据、用“数据.方法名()”调用的函数 | `s.strip()`、`s.split(",")` |
| <span id="g-Unicode"></span>Unicode | Unicode | 给世界上几乎所有字符统一编号的标准 | “街”的编号是 `ord("街")` |
| <span id="g-字符编码"></span>字符编码 | Character Encoding | 把字符编号存成字节的规则；存和读用的编码不一致就会乱码 | UTF-8、GBK |
| <span id="g-UTF-8"></span>UTF-8 | UTF-8 | 最常用的 Unicode 编码方式，英文占 1 字节，常用汉字占 3 字节 | `"街".encode("utf-8")` 是 3 个字节 |
| <span id="g-词元"></span>词元 | Token | 大模型处理文字的最小单位，一个汉字可能是一个或几个词元 | 大模型按词元计算长度和费用 |

## 第 4 章 条件判断：让程序做选择

| 术语 | 英文 | 定义 | 例子 |
|---|---|---|---|
| <span id="g-比较运算符"></span>比较运算符 | Comparison Operator | 比较两个值、结果为 True 或 False 的运算符，共 6 个 | `>`、`<`、`>=`、`<=`、`==`、`!=` |
| <span id="g-布尔表达式"></span>布尔表达式 | Boolean Expression | 结果是 True 或 False 的式子，常用作 if 的条件 | `total >= 100` |
| <span id="g-顺序结构"></span>顺序结构 | Sequential Structure | 程序从上往下一行一行执行的结构 | 没有 if、循环的程序 |
| <span id="g-分支结构"></span>分支结构 | Branch Structure | 根据条件决定执行哪些代码、跳过哪些代码的结构 | if、if-else、if-elif-else |
| <span id="g-条件表达式"></span>条件表达式 | Conditional Expression | 用一行写成的二选一：条件成立取前一个值，否则取后一个 | `"箱" if qty >= 12 else "瓶"` |
| <span id="g-逻辑运算符"></span>逻辑运算符 | Logical Operator | 把几个条件组合起来的运算符：and 并且、or 或者、not 取反 | `age >= 18 and member` |
| <span id="g-真值测试"></span>真值测试 | Truth Value Testing | 把任意值当作真或假：False、None、0、空字符串等为假，其余为真 | `if name:` 表示 name 不为空 |
| <span id="g-流程图"></span>流程图 | Flowchart | 用起止框、输入输出框、处理框、判断框和箭头画出程序步骤的图 | 判断框是菱形 |
| <span id="g-嵌套"></span>嵌套 | Nesting | 在一个语句的代码块里再写同类语句，如 if 里面再写 if | 会员里再分满 50 和不满 50 |
| <span id="g-输入检查"></span>输入检查 | Input Validation | 在使用输入之前先检查它是否合法，不合法就提示 | 先 `isdigit()` 再 `int()` |

## 第 5 章 循环：让程序重复做事

| 术语 | 英文 | 定义 | 例子 |
|---|---|---|---|
| <span id="g-循环"></span>循环 | Loop | 让一段代码重复执行的结构，Python 有 while 和 for 两种 | `for i in range(3):` |
| <span id="g-循环体"></span>循环体 | Loop Body | 循环语句下面缩进的、每圈都要执行的代码 | while 下面缩进的几行 |
| <span id="g-计数器"></span>计数器 | Counter | 记录次数的变量，要有初始值、条件和更新三要素 | `count += 1` |
| <span id="g-死循环"></span>死循环 | Infinite Loop | 条件永远成立又没有 break、停不下来的循环 | 忘了写 `count += 1` |
| <span id="g-循环变量"></span>循环变量 | Loop Variable | for 循环每圈自动取出的那个值所放的变量 | `for ch in "街坊":` 中的 `ch` |
| <span id="g-累加器"></span>累加器 | Accumulator | 循环前清零、每圈加上一个值，用来求和的变量 | `total += money` |
| <span id="g-蒙特卡洛方法"></span>蒙特卡洛方法 | Monte Carlo Method | 用大量随机数模拟一件事，从而估算结果的方法 | 随机撒点估算圆周率 |
| <span id="g-嵌套循环"></span>嵌套循环 | Nested Loop | 循环里面再写循环，外层转一圈、内层转一整遍 | 九九乘法表 |
| <span id="g-二分查找"></span>二分查找 | Binary Search | 每次猜剩下范围的正中间，把范围缩小一半的查找方法 | 1～100 最多猜 7 次 |

## 第 6 章 列表与元组：批量管理数据

| 术语 | 英文 | 定义 | 例子 |
|---|---|---|---|
| <span id="g-列表"></span>列表 | List | 用方括号括起来、按顺序存放多个元素的数据类型，可以修改 | `["可乐", "面包", "牛奶"]` |
| <span id="g-元素"></span>元素 | Element | 列表、元组等容器里存放的每一个数据 | `goods[0]` 取第一个元素 |
| <span id="g-遍历"></span>遍历 | Traversal | 把容器里的元素一个一个取出来处理 | `for v in money:` |
| <span id="g-列表推导式"></span>列表推导式 | List Comprehension | 用一行 `[表达式 for 变量 in 列表 if 条件]` 生成新列表的写法 | `[p * 0.9 for p in prices]` |
| <span id="g-二维列表"></span>二维列表 | Two-dimensional List | 元素也是列表的列表，用来存放有行有列的表格 | `table[1][0]` 第 2 行第 1 列 |
| <span id="g-一维数据"></span>一维数据 | One-dimensional Data | 排成一行或一列的一组数据 | 一周 7 天的营业额 |
| <span id="g-二维数据"></span>二维数据 | Two-dimensional Data | 有行有列的表格数据 | Excel 表格、CSV 文件 |
| <span id="g-元组"></span>元组 | Tuple | 用圆括号括起来、创建后不能修改的有序数据 | `("可乐", 3.5)` |
| <span id="g-解包"></span>解包 | Unpacking | 把列表或元组里的多个元素一次赋给多个变量 | `name, price = ("可乐", 3.5)` |

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
