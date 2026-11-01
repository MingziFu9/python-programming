---
title: 附录 C 常见报错速查表
description: 初学者最常见的 30 多种 Python 报错，给出报错原文、中文意思、常见原因和改法，报错原文均为 Python 3.14 实际运行所得
---

# 附录 C 常见报错速查表

程序出错时，先看报错信息的**最后一行**（报错类型和说明），再往上找带 `line 几` 的那一行（出错位置），这是第 1 章 [1.6 读懂报错信息](../chapters/01-getting-started/index.md#16) 讲过的“三步读法”。

下表中的报错原文都是编者用 Python 3.14 实际运行得到的。不同版本的说明文字可能略有差别，但报错类型（冒号前面的英文单词）是一样的。按报错类型的字母顺序排列，方便查找。

## C.1 语法错误：程序还没运行就报错 { #c1 }

`SyntaxError`、`IndentationError`、`TabError` 是 Python 在运行前检查代码时发现的错误，程序一行都不会执行。报错中的 `^` 指向出错的大致位置，真正的错误有时在它的**前一行**。

| 报错原文（最后一行） | 中文意思 | 常见原因 | 改法 |
|---|---|---|---|
| `SyntaxError: invalid character '（' (U+FF08)` | 无效字符“（” | 用了中文括号；同类的还有中文逗号 `'，' (U+FF0C)`、中文冒号 `'：' (U+FF1A)`、中文引号 `'“' (U+201C)` | 切换到英文输入法重新输入这个符号 |
| `SyntaxError: '(' was never closed` | 左括号没有配对的右括号 | 漏写了右括号，常见于 `print(` 和 `int(input(...)` | 数一数左右括号是否一样多 |
| `SyntaxError: unterminated string literal (detected at line 1)` | 字符串没有结束 | 少了一个引号，如 `print("你好)` | 补上引号，注意前后引号要一样 |
| `SyntaxError: unterminated triple-quoted string literal (detected at line 1)` | 三引号字符串没有结束 | `"""` 只写了开头 | 在字符串末尾补上 `"""` |
| `SyntaxError: expected ':'` | 这里应该有冒号 | if、elif、else、for、while、def、class 行末漏了冒号 | 在行末加英文冒号 `:` |
| `SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?` | 语法错误，你是不是想写 `==` | 在 if 条件中把“等于”写成了 `=` | 比较是否相等用 `==` |
| `SyntaxError: invalid syntax` | 语法错误（没有更具体的提示） | 用保留字当变量名（如 `class = 3`）；else 前面没有 if；上一行少了括号或引号 | 检查这一行和上一行；变量名不要用保留字 |
| `IndentationError: expected an indented block after 'if' statement on line 1` | if 语句后面应该有缩进的代码块 | if、for、def 等冒号下面的代码没有缩进 | 下面的代码统一缩进 4 个空格 |
| `IndentationError: unexpected indent` | 意外的缩进 | 不该缩进的行前面多了空格 | 删掉行首多余的空格 |
| `TabError: inconsistent use of tabs and spaces in indentation` | 缩进中混用了 Tab 和空格 | 从网上复制的代码和自己敲的混在一起 | 在 Thonny 中全选后用“格式 → 取消缩进”再重新缩进，或统一用 4 个空格 |

## C.2 运行时错误：运行到某一行才报错 { #c2 }

这些错误发生在程序运行过程中，出错之前的代码已经执行了。可以用 try-except 处理的就是这一类（第 9 章 [9.5 异常处理](../chapters/09-files/index.md#95)）。

| 报错原文（最后一行） | 中文意思 | 常见原因 | 改法 |
|---|---|---|---|
| `AttributeError: 'list' object has no attribute 'push'` | 列表没有 push 这个方法 | 方法名写错（列表添加元素是 append） | 查一下正确的方法名（附录 B） |
| `AttributeError: 'str' object has no attribute 'append'` | 字符串没有 append 方法 | 把字符串当成了列表 | 字符串拼接用 `+`；要用 append，先建一个列表 |
| `AttributeError: module 'random' has no attribute 'randint' (consider renaming '...random.py' since it has the same name as the standard library module named 'random' ...)` | random 模块里没有 randint | 自己的文件起名叫 random.py，挡住了标准库 | 把自己的文件改名，如 my_random.py（[10.1.2](../chapters/10-modules-oop/index.md#1012)） |
| `EOFError: EOF when reading a line` | 读取输入时遇到了结尾 | 在不能输入的环境（如某些在线平台）中运行了 input | 在 Thonny 中运行 |
| `FileNotFoundError: [Errno 2] No such file or directory: '没有这个文件.txt'` | 找不到文件或文件夹 | 文件名写错；程序和文件不在同一个文件夹（工作目录不对） | 核对文件名和扩展名；把程序和数据放在约定的位置（[9.1](../chapters/09-files/index.md#91)） |
| `IndexError: list index out of range` | 列表下标超出范围 | 下标从 0 开始，3 个元素的列表最大下标是 2 | 用 `len()` 检查长度；最后一个元素用 `a[-1]` |
| `json.decoder.JSONDecodeError: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)` | 应该是用双引号括起来的键名 | JSON 中用了单引号 | JSON 中的字符串必须用双引号；用 `json.dumps` 生成 JSON |
| `KeyError: '雪碧'` | 字典里没有这个键 | 键写错，或这个键还没有加入字典 | 用 `in` 先判断，或用 `d.get(键, 默认值)`（[7.1.3](../chapters/07-dicts/index.md#713)） |
| `KeyError: '销售额'`（pandas） | 表中没有这一列 | 列名写错或多了空格 | 用 `print(df.columns)` 查看准确的列名 |
| `ModuleNotFoundError: No module named 'panda'` | 找不到这个模块 | 库名拼错（应为 pandas）；没有安装；装到了另一个 Python 里 | 核对拼写；在 Thonny 的“工具 → 管理包”中安装（附录 A） |
| `NameError: name 'prnt' is not defined. Did you mean: 'print'?` | 名字 prnt 没有定义 | 函数名、变量名拼错 | 按提示改正拼写 |
| `NameError: name 'total' is not defined` | 变量 total 没有定义 | 变量在使用前没有赋值；在 Jupyter 中没有先运行定义它的单元格 | 先赋初值，如 `total = 0` |
| `PermissionError` | 没有权限 | 要写入的 Excel、CSV 文件正在被别的软件打开 | 先关闭打开该文件的软件 |
| `RecursionError: maximum recursion depth exceeded` | 超过了最大递归深度 | 递归函数没有结束条件，或结束条件永远达不到 | 检查递归的结束条件（[8.6](../chapters/08-functions/index.md#86)） |
| `TypeError: can only concatenate str (not "int") to str` | 字符串只能和字符串拼接 | `input()` 得到的是字符串，直接和数字相加；`"合计" + 100` | 用 `int()`、`float()` 转换，或用 f-string 输出 |
| `TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'` | None 不能和整数相加 | 函数忘了写 return，返回了 None | 在函数中用 return 返回结果 |
| `TypeError: f() missing 1 required positional argument: 'b'` | 调用 f 时少了参数 b | 调用函数时参数个数不够 | 按函数定义补齐参数 |
| `TypeError: Goods.__init__() takes 2 positional arguments but 3 were given` | 参数个数不对 | 定义方法时漏写了 self | 方法的第一个参数写 self（[10.5.2](../chapters/10-modules-oop/index.md#1052)） |
| `TypeError: 'str' object does not support item assignment` | 字符串不能修改其中的字符 | 字符串是不可变的，如 `s[0] = "A"`；元组同理 | 用 `replace` 或切片拼出新字符串 |
| `TypeError: object of type 'int' has no len()` | 整数没有长度 | 对数字用了 `len()` | 先 `str()` 转成字符串再求长度 |
| `TypeError: list indices must be integers or slices, not str` | 列表下标必须是整数 | 把列表当成字典取值，如 `result["choices"]["message"]` | 先用整数下标取出元素，如 `result["choices"][0]` |
| `UnboundLocalError: cannot access local variable 'n' where it is not associated with a value` | 局部变量 n 还没有值就被使用 | 在函数里修改了全局变量 | 把值作为参数传进来、用 return 返回（[8.4](../chapters/08-functions/index.md#84)） |
| `UnicodeDecodeError: 'utf-8' codec can't decode byte 0xd6 in position 0: invalid continuation byte` | 不能按 UTF-8 解码 | 文件是 GBK 编码（如 Excel 另存的 CSV），却按 UTF-8 读 | 改用 `encoding="gbk"` 打开 |
| `ValueError: invalid literal for int() with base 10: '3.5'` | 不能把 '3.5' 转成整数 | 输入了小数、空字符串、中文（如“两”） | 小数用 `float()`；用 try-except 处理输入错误 |
| `ValueError: The truth value of a Series is ambiguous. ...`（pandas） | 一整列的真假值不明确 | pandas 筛选中用了 and、or | 用 `&`、<code>&#124;</code>，并给每个条件加圆括号（[11.4.2](../chapters/11-data-libs/index.md#1142)） |
| `ZeroDivisionError: division by zero` | 除数为零 | 计算平均值时个数为 0 | 先判断除数是否为 0 |

## C.3 不报错但结果不对 { #c3 }

最难找的是“不报错的错误”，这时报错表帮不上忙，要用 print 输出中间结果，或在 Thonny 中用“调试”一步一步看变量的变化（[1.3.2](../chapters/01-getting-started/index.md#132)）。

| 现象 | 常见原因 | 改法 |
|---|---|---|
| 输入 3 和 5，“相加”得到 35 | input 得到的是字符串，`"3" + "5"` 是拼接 | 用 `int()` 或 `float()` 转换 |
| `0.1 + 0.2` 得到 `0.30000000000000004` | 浮点数是近似值 | 输出时用 `round()` 或 `:.2f` 保留小数 |
| 循环停不下来（死循环） | while 的条件一直为真，比如忘了让计数变量变化 | 在 Thonny 中点红色“停止”按钮；检查循环变量的修改 |
| 累加结果只有最后一个数 | 把 `total = 0` 写在了循环里面，每次都被清零 | 初始化放在循环前面 |
| 只处理了第一条数据就结束 | `return` 或 `break` 缩进到了循环里面 | 检查缩进 |
| 用 Excel 打开 CSV，中文是乱码 | Excel 默认不按 UTF-8 识别 | 写文件时用 `encoding="utf-8-sig"`（附录 A） |
| Matplotlib 图中的中文是方框 | 没有设置中文字体 | 设置 `font.sans-serif`（[11.5.1](../chapters/11-data-libs/index.md#1151)） |
| 保存的图片是空白的 | `savefig` 写在了 `show` 后面 | 先 savefig 再 show |
| 大模型的回答中数字不对 | 大模型会写错、会编造 | 把真实数据写进提示词，并和原始数据核对（[12.3.1](../chapters/12-ai-project/index.md#1231)） |
