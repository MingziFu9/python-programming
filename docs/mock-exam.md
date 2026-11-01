---
title: 在线模拟卷
description: 按期末闭卷考试的题型和分值，从各章课后练习中组成的两套在线模拟卷，可以直接作答并查看解析
---

# 在线模拟卷

本课程期末为闭卷考试，题目侧重基础知识、读程序和编程应用，与“信息技术水平-人工智能（Python）”证书考试的要求相衔接（见[证书考点对照](certificate.md)）。下面两套模拟卷按期末考试的题型和分值，从各章课后练习中抽题组成，覆盖全书 12 章：

| 题型 | 题数 | 每题分值 | 合计 |
|---|---|---|---|
| 单项选择题 | 20 | 2 | 40 |
| 多项选择题 | 5 | 4 | 20 |
| 判断题 | 10 | 1 | 10 |
| 简答题 | 2 | 10 | 20 |
| 实操题 | 1 | 10 | 10 |

建议限时 90 分钟，合上书本、不查资料，先独立做完一整套，再展开“答案与解析”核对。简答题和实操题按参考答案的要点自评。实操题要在电脑上运行代码完成。选择题和判断题可以直接点击作答；每道题解析下方的“回看”链接可以跳回对应章节复习。

## 模拟卷一

**一、单项选择题**（每题 2 分）

<div class="quiz" data-answer="C" markdown>

**1.** 把 Python 程序“翻译”给电脑并逐行执行的是（　　）。

- A. 编辑器
- B. 操作系统
- C. 解释器
- D. 浏览器

</div>

??? tip "答案与解析"
    **答案：C**

    解释器从第一行开始，翻译一行、执行一行。编辑器只负责写代码。

    考查：解释器 · 认知层次：记忆 · [回看 1.1.2](chapters/01-getting-started/index.md#112)
    { .quiz-meta }

<div class="quiz" data-answer="C" markdown>

**2.** 下列变量名中，合法的是（　　）。

- A. `2total`
- B. `my-price`
- C. `_total_2`
- D. `class`

</div>

??? tip "答案与解析"
    **答案：C**

    A 以数字开头，B 含减号，D 是保留字。C 只含字母、数字、下划线，且不以数字开头。

    考查：变量命名规则 · 认知层次：应用 · [回看 2.1.3](chapters/02-variables/index.md#213)
    { .quiz-meta }

<div class="quiz" data-answer="B" markdown>

**3.** 设 `s = "Python"`，`s[1]` 的值是（　　）。

- A. `'P'`
- B. `'y'`
- C. `'t'`
- D. `'n'`

</div>

??? tip "答案与解析"
    **答案：B**

    索引从 0 开始，`s[0]` 是 P，`s[1]` 是 y。

    考查：索引 · 认知层次：应用 · [回看 3.2.1](chapters/03-strings/index.md#321)
    { .quiz-meta }

<div class="quiz" data-answer="C" markdown>

**4.** 下列表示“x 等于 10”的条件，写法正确的是（　　）。

- A. `x = 10`
- B. `x === 10`
- C. `x == 10`
- D. `x =< 10`

</div>

??? tip "答案与解析"
    **答案：C**

    `==` 是比较是否相等；`=` 是赋值；Python 没有 `===` 和 `=<`。

    考查：比较运算符 · 认知层次：记忆 · [回看 4.1.1](chapters/04-conditions/index.md#411)
    { .quiz-meta }

<div class="quiz" data-answer="B" markdown>

**5.** `range(1, 5)` 生成的整数是（　　）。

- A. 1, 2, 3, 4, 5
- B. 1, 2, 3, 4
- C. 0, 1, 2, 3, 4
- D. 2, 3, 4, 5

</div>

??? tip "答案与解析"
    **答案：B**

    range 含起点、不含终点。

    考查：range · 认知层次：记忆 · [回看 5.2.2](chapters/05-loops/index.md#522)
    { .quiz-meta }

<div class="quiz" data-answer="C" markdown>

**6.** 设 `a = [10, 20, 30, 40]`，`a[-2]` 的值是（　　）。

- A. 10
- B. 20
- C. 30
- D. 40

</div>

??? tip "答案与解析"
    **答案：C**

    -1 是 40，-2 是 30。

    考查：列表索引 · 认知层次：应用 · [回看 6.1.2](chapters/06-lists/index.md#612)
    { .quiz-meta }

<div class="quiz" data-answer="C" markdown>

**7.** 执行 `d = {"a": 1, "b": 2}` 和 `d["c"] = 3` 后，`len(d)` 的值是（　　）。

- A. 1
- B. 2
- C. 3
- D. 6

</div>

??? tip "答案与解析"
    **答案：C**

    键 c 不存在，赋值即新增，字典有 3 个键值对。

    考查：字典新增 · 认知层次：应用 · [回看 7.1.2](chapters/07-dicts/index.md#712)
    { .quiz-meta }

<div class="quiz" data-answer="B" markdown>

**8.** Python 中定义函数使用的关键字是（　　）。

- A. `function`
- B. `def`
- C. `func`
- D. `define`

</div>

??? tip "答案与解析"
    **答案：B**

    def 是 define 的缩写。

    考查：定义函数 · 认知层次：记忆 · [回看 8.1.1](chapters/08-functions/index.md#811)
    { .quiz-meta }

<div class="quiz" data-answer="C" markdown>

**9.** 要在文件原有内容的末尾继续写入，打开方式应该是（　　）。

- A. `"r"`
- B. `"w"`
- C. `"a"`
- D. `"x"`

</div>

??? tip "答案与解析"
    **答案：C**

    a 是追加；w 会清空原内容。

    考查：打开方式 · 认知层次：记忆 · [回看 9.2.1](chapters/09-files/index.md#921)
    { .quiz-meta }

<div class="quiz" data-answer="B" markdown>

**10.** 执行 `import math` 后，`math.sqrt(16)` 的值是（　　）。

- A. 4
- B. 4.0
- C. 256
- D. 8.0

</div>

??? tip "答案与解析"
    **答案：B**

    sqrt 开平方，返回浮点数。

    考查：math 库 · 认知层次：应用 · [回看 10.2.1](chapters/10-modules-oop/index.md#1021)
    { .quiz-meta }

<div class="quiz" data-answer="B" markdown>

**11.** 执行下面的代码，输出是（　　）。

```python
import numpy as np
a = np.array([1, 2, 3])
print(a * 2)
```

- A. `[1, 2, 3, 1, 2, 3]`
- B. `[2 4 6]`
- C. `[2, 4, 6]`
- D. 报错

</div>

??? tip "答案与解析"
    **答案：B**

    数组乘以数，每个元素都乘 2。数组打印时元素之间没有逗号，所以不是 C；A 是列表乘 2 的结果。

    考查：向量化运算 · 认知层次：应用 · [回看 11.3.2](chapters/11-data-libs/index.md#1132)
    { .quiz-meta }

<div class="quiz" data-answer="C" markdown>

**12.** `jieba.lcut("会员积分很划算")` 的结果是（　　）。

- A. `"会员 积分 很 划算"`
- B. `('会员', '积分', '很', '划算')`
- C. `['会员', '积分', '很', '划算']`
- D. `{'会员', '积分', '很', '划算'}`

</div>

??? tip "答案与解析"
    **答案：C**

    lcut 返回列表（l 就是 list 的意思）。

    考查：jieba 分词 · 认知层次：记忆 · [回看 12.2.1](chapters/12-ai-project/index.md#1221)
    { .quiz-meta }

<div class="quiz" data-answer="B" markdown>

**13.** Python 中表示注释的符号是（　　）。

- A. `//`
- B. `#`
- C. `/* */`
- D. `--`

</div>

??? tip "答案与解析"
    **答案：B**

    Python 用 `#` 写注释。`//` 在 Python 里是整除运算符（第 2 章），`/* */` 是 C 语言、Java 的注释写法。

    考查：注释 · 认知层次：记忆 · [回看 1.4.3](chapters/01-getting-started/index.md#143)
    { .quiz-meta }

<div class="quiz" data-answer="B" markdown>

**14.** 执行下面的代码后，`total` 的值是（　　）。

```python
price = 3.5
qty = 2
total = price * qty
price = 5
```

- A. `10`
- B. `7.0`
- C. `10.0`
- D. 报错

</div>

??? tip "答案与解析"
    **答案：B**

    `total` 在第 3 行算出 7.0 后就固定了，第 4 行修改 `price` 不会让 `total` 自动重算。

    考查：赋值语句 · 认知层次：应用 · [回看 2.1.2](chapters/02-variables/index.md#212)
    { .quiz-meta }

<div class="quiz" data-answer="D" markdown>

**15.** 设 `s = "Python"`，`s[-2:]` 的值是（　　）。

- A. `'Py'`
- B. `'o'`
- C. `'nohtyP'`
- D. `'on'`

</div>

??? tip "答案与解析"
    **答案：D**

    -2 是倒数第二个字符 o，终点留空取到最后，得到 `'on'`。

    考查：切片 · 认知层次：应用 · [回看 3.2.2](chapters/03-strings/index.md#322)
    { .quiz-meta }

<div class="quiz" data-answer="B" markdown>

**16.** 表达式 `"10" < "9"` 的值是（　　）。

- A. `False`
- B. `True`
- C. 报错
- D. `None`

</div>

??? tip "答案与解析"
    **答案：B**

    两个都是字符串，从第一个字符比起，`"1"` 的编号小于 `"9"`，所以结果是 True。数字要先转成 int 再比较。

    考查：字符串比较 · 认知层次：理解 · [回看 4.1.2](chapters/04-conditions/index.md#412)
    { .quiz-meta }

<div class="quiz" data-answer="C" markdown>

**17.** 执行下面的代码，输出是（　　）。

```python
total = 0
for i in range(1, 6, 2):
    total += i
print(total)
```

- A. 15
- B. 6
- C. 9
- D. 5

</div>

??? tip "答案与解析"
    **答案：C**

    `range(1, 6, 2)` 生成 1、3、5，和为 9。

    考查：range 步长、累加 · 认知层次：应用 · [回看 5.4.1](chapters/05-loops/index.md#541)
    { .quiz-meta }

<div class="quiz" data-answer="B" markdown>

**18.** 执行 `a = [1, 2, 3]` 和 `a.append([4, 5])` 后，`len(a)` 的值是（　　）。

- A. 3
- B. 4
- C. 5
- D. 报错

</div>

??? tip "答案与解析"
    **答案：B**

    append 把整个 `[4, 5]` 作为一个元素加入，a 变成 `[1, 2, 3, [4, 5]]`。

    考查：append · 认知层次：理解 · [回看 6.2](chapters/06-lists/index.md#62)
    { .quiz-meta }

<div class="quiz" data-answer="B" markdown>

**19.** 设 `d = {"可乐": 3.5}`，`d.get("雪碧", 0)` 的值是（　　）。

- A. 3.5
- B. 0
- C. None
- D. 报 KeyError

</div>

??? tip "答案与解析"
    **答案：B**

    键不存在时 get 返回给定的默认值 0。

    考查：get · 认知层次：应用 · [回看 7.1.3](chapters/07-dicts/index.md#713)
    { .quiz-meta }

<div class="quiz" data-answer="C" markdown>

**20.** 定义 `def f(a, b=2): return a * b`，`f(3)` 的值是（　　）。

- A. 3
- B. 5
- C. 6
- D. 报错

</div>

??? tip "答案与解析"
    **答案：C**

    b 没有给出，使用默认值 2，3 × 2 = 6。

    考查：默认值 · 认知层次：应用 · [回看 8.2.2](chapters/08-functions/index.md#822)
    { .quiz-meta }

**二、多项选择题**（每题 4 分）

<div class="quiz quiz-multi" data-answer="ABD" markdown>

**1.** 下列代码中，运行时会报错的有（　　）。

- A. `print（"你好"）`
- B. `print("你好”)`
- C. `print('你好')`
- D. `Print("你好")`

</div>

??? tip "答案与解析"
    **答案：ABD**

    A 用了中文括号，B 后面用了中文引号，都是语法错误；D 的 `Print` 首字母大写，Python 区分大小写，不认识这个名字，报 `NameError`。C 用单引号是可以的。

    考查：print 函数、读懂报错 · 认知层次：分析 · [回看 1.4.1](chapters/01-getting-started/index.md#141)
    { .quiz-meta }

<div class="quiz quiz-multi" data-answer="ABC" markdown>

**2.** 设 `s = "abcdef"`，结果为 `'cde'` 的有（　　）。

- A. `s[2:5]`
- B. `s[-4:-1]`
- C. `s[2:-1]`
- D. `s[3:6]`

</div>

??? tip "答案与解析"
    **答案：ABC**

    c、d、e 的正向索引是 2、3、4，反向索引是 -4、-3、-2。A、B、C 都取这三个；D 取 d、e、f。

    考查：切片 · 认知层次：应用 · [回看 3.2.2](chapters/03-strings/index.md#322)
    { .quiz-meta }

<div class="quiz quiz-multi" data-answer="ABC" markdown>

**3.** 下列写法中，生成 0、1、2 三个数的有（　　）。

- A. `range(3)`
- B. `range(0, 3)`
- C. `range(0, 3, 1)`
- D. `range(1, 3)`

</div>

??? tip "答案与解析"
    **答案：ABC**

    D 生成 1、2。

    考查：range · 认知层次：应用 · [回看 5.2.2](chapters/05-loops/index.md#522)
    { .quiz-meta }

<div class="quiz quiz-multi" data-answer="ABD" markdown>

**4.** 关于字典，下列说法正确的有（　　）。

- A. 同一个字典中键不能重复
- B. 不同的键可以对应相同的值
- C. 列表可以作为字典的键
- D. 可以用 `in` 判断某个键是否存在

</div>

??? tip "答案与解析"
    **答案：ABD**

    列表可以修改，不能作键。

    考查：字典的规则 · 认知层次：理解 · [回看 7.1.4](chapters/07-dicts/index.md#714)
    { .quiz-meta }

<div class="quiz quiz-multi" data-answer="ABD" markdown>

**5.** 程序报 `FileNotFoundError`，可能的原因有（　　）。

- A. 文件名拼错了
- B. 工作目录不是你以为的文件夹，相对路径找不到
- C. 文件编码是 GBK
- D. 文件实际的扩展名和代码里写的不一样

</div>

??? tip "答案与解析"
    **答案：ABD**

    编码不对会报 UnicodeDecodeError，而不是找不到文件。

    考查：路径问题 · 认知层次：分析 · [回看 9.1.2](chapters/09-files/index.md#912)
    { .quiz-meta }

**三、判断题**（每题 1 分）

<div class="quiz quiz-judge" data-answer="×" markdown>

**1.** 程序中某一行出错后，解释器会跳过这一行，继续执行后面的代码。（　　）

- √
- ×

</div>

??? tip "答案与解析"
    **答案：×**

    解释器遇到错误就停止，后面的代码都不会执行。

    考查：解释器 · 认知层次：理解 · [回看 1.1.2](chapters/01-getting-started/index.md#112)
    { .quiz-meta }

<div class="quiz quiz-judge" data-answer="×" markdown>

**2.** 在 Python 中，`count = count + 1` 是错误的写法，因为等号两边不相等。（　　）

- √
- ×

</div>

??? tip "答案与解析"
    **答案：×**

    `=` 是赋值，不是相等。这句先算右边 `count + 1`，再存回 `count`，是常用的计数写法（前提是 `count` 之前已经赋过值）。

    考查：赋值语句 · 认知层次：理解 · [回看 2.1.2](chapters/02-variables/index.md#212)
    { .quiz-meta }

<div class="quiz quiz-judge" data-answer="√" markdown>

**3.** 长度为 5 的字符串，最后一个字符的索引是 4，也可以写成 -1。（　　）

- √
- ×

</div>

??? tip "答案与解析"
    **答案：√**

    索引从 0 开始，最大索引是长度减 1。

    考查：索引 · 认知层次：理解 · [回看 3.2.1](chapters/03-strings/index.md#321)
    { .quiz-meta }

<div class="quiz quiz-judge" data-answer="×" markdown>

**4.** `if x = 5:` 可以判断 x 是否等于 5。（　　）

- √
- ×

</div>

??? tip "答案与解析"
    **答案：×**

    `=` 是赋值，在 if 后面使用会报 `SyntaxError`，判断相等要用 `==`。

    考查：= 与 == · 认知层次：记忆 · [回看 4.5](chapters/04-conditions/index.md#45)
    { .quiz-meta }

<div class="quiz quiz-judge" data-answer="×" markdown>

**5.** `range(5)` 生成的整数中包括 5。（　　）

- √
- ×

</div>

??? tip "答案与解析"
    **答案：×**

    `range(5)` 生成 0～4，不含终点 5。

    考查：range · 认知层次：记忆 · [回看 5.2.2](chapters/05-loops/index.md#522)
    { .quiz-meta }

<div class="quiz quiz-judge" data-answer="√" markdown>

**6.** 同一个列表里可以存放不同类型的元素。（　　）

- √
- ×

</div>

??? tip "答案与解析"
    **答案：√**

    例如 `["可乐", 3.5, 2, True]`。

    考查：列表的创建 · 认知层次：记忆 · [回看 6.1.1](chapters/06-lists/index.md#611)
    { .quiz-meta }

<div class="quiz quiz-judge" data-answer="×" markdown>

**7.** `s = {}` 创建的是一个空集合。（　　）

- √
- ×

</div>

??? tip "答案与解析"
    **答案：×**

    `{}` 是空字典，空集合要写 `set()`。

    考查：空集合 · 认知层次：记忆 · [回看 7.4.1](chapters/07-dicts/index.md#741)
    { .quiz-meta }

<div class="quiz quiz-judge" data-answer="×" markdown>

**8.** 程序执行到 def 语句时，函数体中的代码就会被执行一遍。（　　）

- √
- ×

</div>

??? tip "答案与解析"
    **答案：×**

    def 只定义，调用时才执行。

    考查：定义与调用 · 认知层次：理解 · [回看 8.1.1](chapters/08-functions/index.md#811)
    { .quiz-meta }

<div class="quiz quiz-judge" data-answer="√" markdown>

**9.** 用 `"w"` 方式打开一个已经存在的文件，原来的内容会被清空。（　　）

- √
- ×

</div>

??? tip "答案与解析"
    **答案：√**

    要保留原内容，用 "a" 追加。

    考查：打开方式 · 认知层次：记忆 · [回看 9.2.1](chapters/09-files/index.md#921)
    { .quiz-meta }

<div class="quiz quiz-judge" data-answer="√" markdown>

**10.** 第三方库用 pip 安装以后，在程序中使用前仍然要 import。（　　）

- √
- ×

</div>

??? tip "答案与解析"
    **答案：√**

    安装是装到电脑上，import 是在程序中导入，两步都需要。

    考查：pip 与 import · 认知层次：理解 · [回看 10.3.1](chapters/10-modules-oop/index.md#1031)
    { .quiz-meta }

**四、简答题**（每题 10 分）

**1.** 读程序写结果。

```python
a = [5, 3, 8, 1]
a.append(6)
a.remove(3)
a.insert(0, 9)
x = a.pop()
print(a, x, len(a))
a.sort(reverse=True)
print(a[:2])
```

??? tip "答案与解析"
    **参考答案**

    ```text
    [9, 5, 8, 1] 6 4
    [9, 8]
    ```

    依次为：`[5, 3, 8, 1, 6]` → 删 3 得 `[5, 8, 1, 6]` → 头部插 9 得 `[9, 5, 8, 1, 6]` → pop 拿走 6。从大到小排序后是 `[9, 8, 5, 1]`，前两个是 `[9, 8]`。

    考查：列表增删与排序 · 认知层次：应用 · [回看 6.2](chapters/06-lists/index.md#62)
    { .quiz-meta }

**2.** 读程序写结果。

```python
import numpy as np
a = np.array([3, 8, 5, 10])
print(a[a > 4])
print(a.sum(), a.max())
```

??? tip "答案与解析"
    **参考答案**

    ```text
    [ 8  5 10]
    26 10
    ```

    `a > 4` 得到 `[False True True True]`，布尔索引保留 8、5、10，顺序不变。为了对齐，NumPy 在 8 和 5 前面多留了一个空格。

    考查：布尔索引与统计 · 认知层次：应用 · [回看 11.3.2](chapters/11-data-libs/index.md#1132)
    { .quiz-meta }

**五、实操题**（每题 10 分）

**1.** 输入一个年份，判断是否为闰年。规则：能被 4 整除但不能被 100 整除，或者能被 400 整除。用 2024、2025、1900、2000 测试。

??? tip "答案与解析"
    **参考答案**

    ```python
    year = int(input("年份："))
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print(year, "是闰年")
    else:
        print(year, "不是闰年")
    ```

    编者测试结果：2024 是闰年，2025 不是，1900 不是（能被 100 整除但不能被 400 整除），2000 是。

    考查：and、or 组合条件 · 认知层次：应用 · [回看 4.3.1](chapters/04-conditions/index.md#431)
    { .quiz-meta }

## 模拟卷二

**一、单项选择题**（每题 2 分）

<div class="quiz" data-answer="D" markdown>

**1.** 执行 `print("3 + 4 =", 3 + 4)`，输出是（　　）。

- A. `3 + 4 = 3 + 4`
- B. `7 = 7`
- C. `3 + 4 =7`
- D. `3 + 4 = 7`

</div>

??? tip "答案与解析"
    **答案：D**

    引号里的 `"3 + 4 ="` 原样输出；没有引号的 `3 + 4` 先算出 7；逗号隔开的两项之间自动加一个空格。

    考查：print 函数 · 认知层次：应用 · [回看 1.4.1](chapters/01-getting-started/index.md#141)
    { .quiz-meta }

<div class="quiz" data-answer="D" markdown>

**2.** `7 // 2` 和 `7 % 2` 的结果分别是（　　）。

- A. `3.5` 和 `1`
- B. `3` 和 `3.5`
- C. `1` 和 `3`
- D. `3` 和 `1`

</div>

??? tip "答案与解析"
    **答案：D**

    `//` 是整除，取商 3；`%` 是取余数，7 除以 2 余 1。

    考查：算术运算符 · 认知层次：应用 · [回看 2.4.1](chapters/02-variables/index.md#241)
    { .quiz-meta }

<div class="quiz" data-answer="A" markdown>

**3.** 设 `s = "13800138000"`，下列能取出前 3 位 `'138'` 的是（　　）。

- A. `s[:3]`
- B. `s[1:3]`
- C. `s[0:2]`
- D. `s[3]`

</div>

??? tip "答案与解析"
    **答案：A**

    `s[:3]` 取索引 0、1、2。B 取索引 1、2；C 取索引 0、1；D 只取索引 3 一个字符。

    考查：切片 · 认知层次：应用 · [回看 3.2.2](chapters/03-strings/index.md#322)
    { .quiz-meta }

<div class="quiz" data-answer="A" markdown>

**4.** 执行下面的代码，输出是（　　）。

```python
x = 15
if x > 10:
    print("大")
elif x > 5:
    print("中")
else:
    print("小")
```

- A. 大
- B. 中
- C. 大 和 中 两行
- D. 小

</div>

??? tip "答案与解析"
    **答案：A**

    15 > 10 成立，执行第一个分支后跳过其余分支。虽然 15 > 5 也成立，但不会再判断。

    考查：if-elif-else 执行规则 · 认知层次：应用 · [回看 4.2.3](chapters/04-conditions/index.md#423)
    { .quiz-meta }

<div class="quiz" data-answer="A" markdown>

**5.** 执行下面的代码，输出是（　　）。

```python
n = 10
while n > 0:
    n -= 3
print(n)
```

- A. -2
- B. 1
- C. 0
- D. -3

</div>

??? tip "答案与解析"
    **答案：A**

    n 依次变为 7、4、1、-2。n 为 1 时条件成立，再减 3 得 -2，此时条件不成立，循环结束。

    考查：while 执行过程 · 认知层次：应用 · [回看 5.1.1](chapters/05-loops/index.md#511)
    { .quiz-meta }

<div class="quiz" data-answer="D" markdown>

**6.** 执行下面的代码，输出是（　　）。

```python
a = [3, 1, 2]
b = a.sort()
print(b)
```

- A. `[1, 2, 3]`
- B. `[3, 1, 2]`
- C. `[3, 2, 1]`
- D. `None`

</div>

??? tip "答案与解析"
    **答案：D**

    `sort()` 直接修改原列表，返回值是 None。要得到排好序的新列表，用 `sorted(a)`。

    考查：sort 与 sorted · 认知层次：理解 · [回看 6.3.3](chapters/06-lists/index.md#633)
    { .quiz-meta }

<div class="quiz" data-answer="A" markdown>

**7.** 设 `d = {"可乐": 3.5}`，执行 `print(d["雪碧"])` 的结果是（　　）。

- A. 报 KeyError
- B. 输出 None
- C. 输出 0
- D. 输出空行

</div>

??? tip "答案与解析"
    **答案：A**

    用 `[键]` 取不存在的键会报 KeyError；不想报错用 get。

    考查：KeyError · 认知层次：理解 · [回看 7.1.1](chapters/07-dicts/index.md#711)
    { .quiz-meta }

<div class="quiz" data-answer="A" markdown>

**8.** 一个函数中没有 return 语句，调用它得到的返回值是（　　）。

- A. `None`
- B. `0`
- C. `""`
- D. 报错

</div>

??? tip "答案与解析"
    **答案：A**

    没有 return 或 return 后面不写值，返回 None。

    考查：返回值 · 认知层次：记忆 · [回看 8.3.1](chapters/08-functions/index.md#831)
    { .quiz-meta }

<div class="quiz" data-answer="D" markdown>

**9.** 文件 notes.txt 有 3 行，执行 `lines = f.readlines()` 后，lines 的类型是（　　）。

- A. 字符串
- B. 整数
- C. 字典
- D. 列表

</div>

??? tip "答案与解析"
    **答案：D**

    readlines 返回一个列表，每个元素是一行（带 \n 的字符串）。

    考查：读文件 · 认知层次：记忆 · [回看 9.2.2](chapters/09-files/index.md#922)
    { .quiz-meta }

<div class="quiz" data-answer="A" markdown>

**10.** 安装第三方库 jieba 的命令是（　　）。

- A. `pip install jieba`
- B. `import jieba`
- C. `python jieba`
- D. `install jieba`

</div>

??? tip "答案与解析"
    **答案：A**

    pip install 安装；import 是在程序中导入已安装的库。

    考查：pip · 认知层次：记忆 · [回看 10.3.1](chapters/10-modules-oop/index.md#1031)
    { .quiz-meta }

<div class="quiz" data-answer="D" markdown>

**11.** `df.shape` 的结果是 `(8437, 11)`，它表示（　　）。

- A. 8437 列、11 行
- B. 数据占用 8437 KB
- C. 一共有 8437 个格子
- D. 8437 行、11 列

</div>

??? tip "答案与解析"
    **答案：D**

    shape 是“(行数, 列数)”。

    考查：查看数据 · 认知层次：理解 · [回看 11.4.1](chapters/11-data-libs/index.md#1141)
    { .quiz-meta }

<div class="quiz" data-answer="A" markdown>

**12.** 在 scikit-learn 中，用数据训练模型的方法通常叫（　　）。

- A. `fit`
- B. `predict`
- C. `train`
- D. `learn`

</div>

??? tip "答案与解析"
    **答案：A**

    三步：创建模型对象、fit 训练、predict 预测。

    考查：机器学习体验 · 认知层次：记忆 · [回看 12.2.2](chapters/12-ai-project/index.md#1222)
    { .quiz-meta }

<div class="quiz" data-answer="D" markdown>

**13.** 能够立即结束整个循环的语句是（　　）。

- A. `continue`
- B. `pass`
- C. `else`
- D. `break`

</div>

??? tip "答案与解析"
    **答案：D**

    break 结束整个循环；continue 只跳过本圈。

    考查：break · 认知层次：记忆 · [回看 5.3](chapters/05-loops/index.md#53)
    { .quiz-meta }

<div class="quiz" data-answer="A" markdown>

**14.** 执行下面的代码，输出是（　　）。

```python
a = [1, 2, 3]
b = a
b[0] = 9
print(a)
```

- A. `[9, 2, 3]`
- B. `[1, 2, 3]`
- C. `[9]`
- D. 报错

</div>

??? tip "答案与解析"
    **答案：A**

    `b = a` 让 a、b 指向同一个列表，通过 b 修改，a 也看到变化。

    考查：列表的复制 · 认知层次：分析 · [回看 6.7](chapters/06-lists/index.md#67)
    { .quiz-meta }

<div class="quiz" data-answer="D" markdown>

**15.** 设 `d = {"可乐": 3.5, "面包": 5.5}`，执行 `for k in d: print(k)` 输出的是（　　）。

- A. 3.5 和 5.5
- B. ('可乐', 3.5) 和 ('面包', 5.5)
- C. 报错
- D. 可乐 和 面包

</div>

??? tip "答案与解析"
    **答案：D**

    直接遍历字典，取出的是键。要值用 `d.values()`，要键值对用 `d.items()`。

    考查：遍历字典 · 认知层次：理解 · [回看 7.2.1](chapters/07-dicts/index.md#721)
    { .quiz-meta }

<div class="quiz" data-answer="D" markdown>

**16.** 执行下面的代码，输出是（　　）。

```python
def f(x):
    x = x + 1
    return x

a = 5
f(a)
print(a)
```

- A. 6
- B. None
- C. 报错
- D. 5

</div>

??? tip "答案与解析"
    **答案：D**

    函数里的 x 是局部变量，改它不影响外面的 a；而且返回值 6 没有被接收。

    考查：局部变量 · 认知层次：分析 · [回看 8.4.1](chapters/08-functions/index.md#841)
    { .quiz-meta }

<div class="quiz" data-answer="A" markdown>

**17.** 执行 `int("两瓶")` 会产生的异常是（　　）。

- A. `ValueError`
- B. `TypeError`
- C. `NameError`
- D. `KeyError`

</div>

??? tip "答案与解析"
    **答案：A**

    参数是字符串类型没错，但值“两瓶”不能转成整数，是值错误。

    考查：常见异常 · 认知层次：理解 · [回看 9.5.1](chapters/09-files/index.md#951)
    { .quiz-meta }

<div class="quiz" data-answer="D" markdown>

**18.** 类中用于在创建对象时初始化属性的方法名是（　　）。

- A. `init`
- B. `_init_`
- C. `__new__`
- D. `__init__`

</div>

??? tip "答案与解析"
    **答案：D**

    init 前后各两个下划线。

    考查：初始化方法 · 认知层次：记忆 · [回看 10.5.2](chapters/10-modules-oop/index.md#1052)
    { .quiz-meta }

<div class="quiz" data-answer="C" markdown>

**19.** 要从 df 中筛选出“金额”大于 100 的行，正确的写法是（　　）。

- A. `df["金额" > 100]`
- B. `df["金额"] > 100`
- C. `df[df["金额"] > 100]`
- D. `df.filter(金额 > 100)`

</div>

??? tip "答案与解析"
    **答案：C**

    B 只得到一列 True/False，还要放进 `df[...]` 才能取出行。A 会先比较字符串和数字，直接报错。

    考查：筛选 · 认知层次：应用 · [回看 11.4.2](chapters/11-data-libs/index.md#1142)
    { .quiz-meta }

<div class="quiz" data-answer="D" markdown>

**20.** 调用大模型接口时，服务器返回状态码 401，最可能的原因是（　　）。

- A. 网络断了
- B. 请求太频繁
- C. 服务器内部故障
- D. API Key 错误或没有带上

</div>

??? tip "答案与解析"
    **答案：D**

    401 是认证失败；网络断了根本收不到状态码，requests 会抛出 ConnectionError；请求太频繁是 429；服务器故障是 500。

    考查：HTTP 状态码 · 认知层次：理解 · [回看 12.3.2](chapters/12-ai-project/index.md#1232)
    { .quiz-meta }

**二、多项选择题**（每题 4 分）

<div class="quiz quiz-multi" data-answer="BC" markdown>

**1.** 下列数据中，适合用字符串保存的有（　　）。

- A. 商品单价
- B. 顾客手机号
- C. 邮政编码
- D. 库存数量

</div>

??? tip "答案与解析"
    **答案：BC**

    手机号、邮编是编号，不需要计算，且可能以 0 开头，用字符串；单价和库存要参与计算，用数字。

    考查：数据类型 · 认知层次：应用 · [回看 2.3.4](chapters/02-variables/index.md#234)
    { .quiz-meta }

<div class="quiz quiz-multi" data-answer="AC" markdown>

**2.** 下列 if 语句写法正确的有（　　）。

- A. `if a > b:`
- B. `if a > b`
- C. `if a != b and b > 0:`
- D. `if a > b：`（冒号是中文的）

</div>

??? tip "答案与解析"
    **答案：AC**

    if 的条件后必须有英文冒号。B 漏写冒号，D 用了中文冒号，都会报 SyntaxError。

    考查：if 语法 · 认知层次：记忆 · [回看 4.2.1](chapters/04-conditions/index.md#421)
    { .quiz-meta }

<div class="quiz quiz-multi" data-answer="ABC" markdown>

**3.** 下列表达式的结果是 `[1, 2, 3]` 的有（　　）。

- A. `sorted([3, 2, 1])`
- B. `[1, 2] + [3]`
- C. `list(range(1, 4))`
- D. `[3, 2, 1].reverse()`

</div>

??? tip "答案与解析"
    **答案：ABC**

    D：reverse 和 sort 一样直接修改列表，返回 None。

    考查：列表运算 · 认知层次：应用 · [回看 6.3.3](chapters/06-lists/index.md#633)
    { .quiz-meta }

<div class="quiz quiz-multi" data-answer="ABC" markdown>

**4.** 关于类和对象，下列说法正确的有（　　）。

- A. 一个类可以创建多个对象
- B. 同一个类的不同对象，可以有不同的属性值
- C. 创建对象时会自动调用 `__init__` 方法
- D. 类中定义方法时不需要写 self

</div>

??? tip "答案与解析"
    **答案：ABC**

    方法的第一个参数必须留给 self，否则调用时报 TypeError。

    考查：类与对象 · 认知层次：理解 · [回看 10.5.2](chapters/10-modules-oop/index.md#1052)
    { .quiz-meta }

<div class="quiz quiz-multi" data-answer="ACD" markdown>

**5.** 下列做法中，符合个人信息保护要求的有（　　）。

- A. 把会员表交给 AI 分析前，删掉姓名、手机号，只保留编号
- B. 写爬虫批量抓取网上别人的手机号，卖给推销公司
- C. 只收集业务需要的信息，并告知顾客用途
- D. 让 AI 写代码时，只发表头和几行虚构的示例数据

</div>

??? tip "答案与解析"
    **答案：ACD**

    B 是违法行为。

    考查：个人信息保护 · 认知层次：评价 · [回看 12.5](chapters/12-ai-project/index.md#125)
    { .quiz-meta }

**三、判断题**（每题 1 分）

<div class="quiz quiz-judge" data-answer="×" markdown>

**1.** `s[2:5]` 会取出索引为 2、3、4、5 的四个字符。（　　）

- √
- ×

</div>

??? tip "答案与解析"
    **答案：×**

    切片含起点不含终点，只取 2、3、4 三个。

    考查：切片 · 认知层次：理解 · [回看 3.2.2](chapters/03-strings/index.md#322)
    { .quiz-meta }

<div class="quiz quiz-judge" data-answer="√" markdown>

**2.** `else` 后面不写条件，它下面的代码在前面所有条件都不成立时执行。（　　）

- √
- ×

</div>

??? tip "答案与解析"
    **答案：√**

    else 表示“否则”，不带条件。

    考查：if-else · 认知层次：理解 · [回看 4.2.2](chapters/04-conditions/index.md#422)
    { .quiz-meta }

<div class="quiz quiz-judge" data-answer="√" markdown>

**3.** 在 print 中写 `end=""`，可以让下一次输出接在同一行。（　　）

- √
- ×

</div>

??? tip "答案与解析"
    **答案：√**

    print 默认以换行结尾，`end=""` 把结尾改成空字符串。

    考查：print 的 end 参数 · 认知层次：记忆 · [回看 5.3](chapters/05-loops/index.md#53)
    { .quiz-meta }

<div class="quiz quiz-judge" data-answer="×" markdown>

**4.** `a.sort()` 会返回一个排好序的新列表，原列表 a 不变。（　　）

- √
- ×

</div>

??? tip "答案与解析"
    **答案：×**

    这是 `sorted(a)` 的特点。`a.sort()` 直接修改 a，返回 None。

    考查：sort 与 sorted · 认知层次：理解 · [回看 6.3.3](chapters/06-lists/index.md#633)
    { .quiz-meta }

<div class="quiz quiz-judge" data-answer="√" markdown>

**5.** 创建字典时同一个键写了两次，后面的值会覆盖前面的值。（　　）

- √
- ×

</div>

??? tip "答案与解析"
    **答案：√**

    `{"a": 1, "a": 2}` 的结果是 `{'a': 2}`。

    考查：键的规则 · 认知层次：理解 · [回看 7.1.4](chapters/07-dicts/index.md#714)
    { .quiz-meta }

<div class="quiz quiz-judge" data-answer="√" markdown>

**6.** 定义函数时，有默认值的参数必须放在没有默认值的参数后面。（　　）

- √
- ×

</div>

??? tip "答案与解析"
    **答案：√**

    否则报 `SyntaxError: parameter without a default follows parameter with a default`。

    考查：默认值 · 认知层次：记忆 · [回看 8.2.2](chapters/08-functions/index.md#822)
    { .quiz-meta }

<div class="quiz quiz-judge" data-answer="×" markdown>

**7.** 从文本文件中读出的 `"25"`，可以直接和数字 5 相加得到 30。（　　）

- √
- ×

</div>

??? tip "答案与解析"
    **答案：×**

    读出的是字符串，`"25" + 5` 报 TypeError，要先 `int("25")`。

    考查：读出的是字符串 · 认知层次：理解 · [回看 9.2.2](chapters/09-files/index.md#922)
    { .quiz-meta }

<div class="quiz quiz-judge" data-answer="×" markdown>

**8.** 为了方便，推荐用 `from 模块 import *` 导入模块中的全部内容。（　　）

- √
- ×

</div>

??? tip "答案与解析"
    **答案：×**

    容易和自己的变量名重名，也看不出函数来自哪里，不推荐。

    考查：import 写法 · 认知层次：理解 · [回看 10.1.1](chapters/10-modules-oop/index.md#1011)
    { .quiz-meta }

<div class="quiz quiz-judge" data-answer="√" markdown>

**9.** `df["金额"]` 取出的是表中的一列，它的类型是 Series。（　　）

- √
- ×

</div>

??? tip "答案与解析"
    **答案：√**

    整张表是 DataFrame，一列是 Series；用两层方括号 `df[["金额"]]` 取出的则是只有一列的 DataFrame。

    考查：DataFrame 与 Series · 认知层次：记忆 · [回看 11.4.2](chapters/11-data-libs/index.md#1142)
    { .quiz-meta }

<div class="quiz quiz-judge" data-answer="√" markdown>

**10.** 网络不通时调用 `requests.post()`，程序会抛出异常，而不是返回一个状态码。（　　）

- √
- ×

</div>

??? tip "答案与解析"
    **答案：√**

    请求根本没送到服务器，就没有状态码，requests 抛出 ConnectionError，要用 try-except 接住。

    考查：异常处理 · 认知层次：理解 · [回看 12.3.2](chapters/12-ai-project/index.md#1232)
    { .quiz-meta }

**四、简答题**（每题 10 分）

**1.** 读程序写结果，并解释为什么 a 没变而 b 变了。

```python
def change(n, items):
    n = n + 1
    items.append(n)
    return n

a = 1
b = [1]
c = change(a, b)
print(a, b, c)
```

??? tip "答案与解析"
    **参考答案**

    ```text
    1 [1, 2] 2
    ```

    n 是局部变量，`n = n + 1` 只是让局部变量 n 指向 2，外面的 a 不受影响。items 和外面的 b 是同一个列表的两个名字，`items.append(n)` 修改的就是 b 指向的列表，所以 b 变了。返回值 2 赋给 c。

    考查：参数传递、局部变量 · 认知层次：分析 · [回看 8.4.2](chapters/08-functions/index.md#842)
    { .quiz-meta }

**2.** 读程序写结果。

```python
result = {"choices": [{"message": {"role": "assistant", "content": "你好"}}],
          "usage": {"total_tokens": 12}}
print(result["choices"][0]["message"]["content"], result["usage"]["total_tokens"])
```

??? tip "答案与解析"
    **参考答案**

    ```text
    你好 12
    ```

    按“列表用下标、字典用键”一层层取下去。

    考查：解析 JSON 回复 · 认知层次：应用 · [回看 12.3.2](chapters/12-ai-project/index.md#1232)
    { .quiz-meta }

**五、实操题**（每题 10 分）

**1.** 输入一段文字，统计其中每个字出现的次数（例如输入“街坊街坊便利店”，输出 `{'街': 2, '坊': 2, '便': 1, '利': 1, '店': 1}`）。

??? tip "答案与解析"
    **参考答案**

    ```python
    text = input("一段文字：")
    counts = {}
    for ch in text:
        counts[ch] = counts.get(ch, 0) + 1
    print(counts)
    ```

    编者用“街坊街坊便利店”测试，输出与题目一致。

    考查：字频统计 · 认知层次：应用 · [回看 7.2.2](chapters/07-dicts/index.md#722)
    { .quiz-meta }
