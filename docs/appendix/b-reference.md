---
title: 附录 B 常用内置函数与方法速查
description: 本书用到的内置函数、字符串、列表、字典、集合方法、格式化写法、文件操作、常用标准库和第三方库的速查表，示例结果均为 Python 3.14 实际运行所得
---

# 附录 B 常用内置函数与方法速查

本附录把全书用到的函数和方法集中列出，做实验、复习备考时查阅。“示例”一栏的结果都是编者用 Python 3.14 实际运行得到的。标“考”的是全国计算机等级考试二级 Python 大纲涉及、但本书正文没有展开的内容，备考时请看一看。

## B.1 内置函数 { #b1 }

内置函数不用 import，直接就能用。

| 函数 | 作用 | 示例 → 结果 | 正文 |
|---|---|---|---|
| `print(…, sep=" ", end="\n")` | 输出 | `print("a", "b", sep="-")` → `a-b` | [1.4.1](../chapters/01-getting-started/index.md#141) |
| `input(提示)` | 输入，**得到的总是字符串** | | [1.4.2](../chapters/01-getting-started/index.md#142) |
| `int(x)` | 转成整数（小数直接去掉小数部分） | `int("42")` → `42`；`int(3.9)` → `3` | 第 2 章 |
| `float(x)` | 转成浮点数 | `float("3.5")` → `3.5` | 第 2 章 |
| `str(x)` | 转成字符串 | `str(100)` → `'100'` | 第 2 章 |
| `bool(x)` | 转成布尔值，0、空字符串、空列表、None 为 False | `bool(0)` → `False`；`bool("")` → `False` | 第 4 章 |
| `type(x)` | 查看类型 | `type(3.0)` → `<class 'float'>` | 第 2 章 |
| `isinstance(x, 类型)` 考 | 判断是不是某种类型 | `isinstance(3, int)` → `True` | |
| `eval(字符串)` | 把字符串当作表达式计算 | `eval("1 + 2 * 3")` → `7` | 第 2 章 |
| `abs(x)` | 绝对值 | `abs(-3.5)` → `3.5` | |
| `divmod(a, b)` 考 | 同时得到商和余数 | `divmod(17, 5)` → `(3, 2)` | |
| `pow(x, y)` 考 | x 的 y 次方，同 `x ** y` | `pow(2, 10)` → `1024` | |
| `round(x, n)` | 四舍五入保留 n 位小数 | `round(3.14159, 2)` → `3.14`；`round(2.5)` → `2`（恰好一半时取偶数） | 第 2 章 |
| `max(…)` / `min(…)` | 最大值 / 最小值 | `max(3, 8, 5)` → `8`；`min([3, 8, 5])` → `3` | 第 6 章 |
| `sum(列表)` | 求和 | `sum([1, 2, 3])` → `6` | 第 6 章 |
| `len(x)` | 长度（字符数、元素个数） | `len("街坊便利店")` → `5` | 第 3 章 |
| `range(起, 止, 步长)` | 整数序列，不含“止” | `list(range(1, 10, 3))` → `[1, 4, 7]` | 第 5 章 |
| `sorted(x, reverse=False, key=…)` | 排序，返回新列表 | `sorted([3, 1, 2], reverse=True)` → `[3, 2, 1]` | 第 6 章 |
| `reversed(x)` 考 | 反向 | `list(reversed([1, 2, 3]))` → `[3, 2, 1]` | |
| `enumerate(x)` | 同时得到序号和元素 | `list(enumerate(["a", "b"]))` → `[(0, 'a'), (1, 'b')]` | 第 6 章 |
| `zip(a, b)` | 把两个序列一一配对 | `list(zip(["可乐", "雪碧"], [3, 2.5]))` → `[('可乐', 3), ('雪碧', 2.5)]` | 第 11 章 |
| `map(函数, 序列)` 考 | 对每个元素调用函数 | `list(map(int, ["1", "2"]))` → `[1, 2]` | |
| `all(x)` / `any(x)` | 全部为真 / 有一个为真 | `all([True, 1, "a"])` → `True`；`any([0, "", None])` → `False` | 第 12 章 |
| `chr(编码)` / `ord(字符)` | 编码与字符互换 | `chr(65)` → `'A'`；`ord("A")` → `65` | 第 3 章 |
| `bin(x)` / `oct(x)` / `hex(x)` 考 | 转成二、八、十六进制字符串 | `bin(10)` → `'0b1010'`；`oct(8)` → `'0o10'`；`hex(255)` → `'0xff'` | |
| `complex(实部, 虚部)` 考 | 复数 | `complex(1, 2)` → `(1+2j)` | |
| `list()` / `tuple()` / `dict()` / `set()` | 创建或转换成列表、元组、字典、集合 | | 第 6、7 章 |
| `open(文件名, 模式, encoding=…)` | 打开文件 | 见 B.6 | 第 9 章 |

## B.2 字符串方法 { #b2 }

字符串不能修改，下面的方法都是**返回一个新字符串**（或其他结果），原字符串不变。

| 方法 | 作用 | 示例 → 结果 |
|---|---|---|
| `s.strip()` | 去掉两端的空格和换行 | `"  hi  ".strip()` → `'hi'` |
| `s.split(分隔符)` | 切分成列表 | `"a-b-c".split("-")` → `['a', 'b', 'c']` |
| `分隔符.join(列表)` | 用分隔符把列表中的字符串连起来 | `"、".join(["盐", "糖"])` → `'盐、糖'` |
| `s.replace(旧, 新)` | 替换 | `"abcabc".replace("b", "B")` → `'aBcaBc'` |
| `s.upper()` / `s.lower()` / `s.title()` | 转大写 / 小写 / 每个单词首字母大写 | `"Python".upper()` → `'PYTHON'`；`"hello world".title()` → `'Hello World'` |
| `s.count(子串)` | 出现次数 | `"abcabc".count("b")` → `2` |
| `s.find(子串)` | 第一次出现的位置，找不到返回 -1 | `"abcabc".find("c")` → `2`；`"abcabc".find("z")` → `-1` |
| `s.index(子串)` | 同 find，但找不到时报错 | |
| `s.startswith(x)` / `s.endswith(x)` | 是否以 x 开头 / 结尾 | `"A001".startswith("A")` → `True` |
| `s.isdigit()` | 是否全是数字 | `"123".isdigit()` → `True`；`"3.5".isdigit()` → `False` |
| `s.zfill(宽度)` | 左边补 0 | `"7".zfill(3)` → `'007'` |
| `s.center(宽度, 填充字符)` | 居中 | `"标题".center(8, "*")` → `'***标题***'` |
| `子串 in s` | 是否包含 | `"排队" in "排队太久"` → `True` |
| `s[起:止:步长]` | 切片，不含“止” | `"街坊便利店"[2:4]` → `'便利'`（[3.2](../chapters/03-strings/index.md#32)） |

## B.3 格式化输出 { #b3 }

| 写法 | 含义 | 示例 → 结果 |
|---|---|---|
| `f"{x:.2f}"` | 保留 2 位小数 | `f"{3.14159:.2f}"` → `'3.14'` |
| `f"{x:>5}"` / `f"{x:<5}"` / `f"{x:^5}"` | 占 5 格，右 / 左 / 居中对齐 | `f"{42:>5}"` → `'   42'` |
| `f"{x:.1%}"` | 百分数，保留 1 位小数 | `f"{0.256:.1%}"` → `'25.6%'` |
| `f"{x:,}"` | 千位分隔符 | `f"{1234567:,}"` → `'1,234,567'` |
| `"{:.2f}".format(x)` | format 方法，格式写法和 f-string 相同 | `"{:.2f}".format(3.14159)` → `'3.14'` |

## B.4 列表方法 { #b4 }

列表可以修改，下面多数方法**直接修改原列表**，本身返回 None（pop、index 除外）。以 `a = [3, 1, 2]` 为例：

| 方法 | 作用 | 执行后 a 的值 |
|---|---|---|
| `a.append(4)` | 末尾添加一个元素 | `[3, 1, 2, 4]` |
| `a.insert(0, 9)` | 在位置 0 插入 | `[9, 3, 1, 2]` |
| `a.extend([5, 6])` | 末尾添加多个元素 | `[3, 1, 2, 5, 6]` |
| `a.pop()` | 删除并返回最后一个元素（这里返回 2） | `[3, 1]` |
| `a.remove(1)` | 删除第一个值为 1 的元素 | `[3, 2]` |
| `del a[0]` | 删除位置 0 的元素 | `[1, 2]` |
| `a.sort()` / `a.sort(reverse=True)` | 从小到大 / 从大到小排序 | `[1, 2, 3]` |
| `a.reverse()` | 倒序 | `[2, 1, 3]` |
| `a.index(2)` | 值为 2 的元素在哪个位置（这里返回 2） | 不变 |
| `a.count(x)` | x 出现几次 | 不变 |
| `a.copy()` | 复制出一个新列表 | 不变 |

## B.5 字典与集合 { #b5 }

以 `d = {"可乐": 3}` 为例：

| 写法 | 作用 | 示例 → 结果 |
|---|---|---|
| `d[键]` | 取值，键不存在时报 KeyError | `d["可乐"]` → `3` |
| `d.get(键, 默认值)` | 取值，键不存在时返回默认值 | `d.get("雪碧", 0)` → `0` |
| `d[键] = 值` | 添加或修改 | |
| `d.pop(键)` | 删除并返回值 | |
| `d.update(另一个字典)` 考 | 合并 | `d.update({"雪碧": 2.5})` 后 d 为 `{'可乐': 3, '雪碧': 2.5}` |
| `d.keys()` / `d.values()` / `d.items()` | 所有键 / 值 / 键值对 | `list(d.items())` → `[('可乐', 3)]` |
| `键 in d` | 是否有这个键 | |

集合：`s.add(x)` 添加，`s.discard(x)` 删除（不存在也不报错）；以 `{1, 2}` 和 `{2, 3}` 为例，并集 <code>&#124;</code> 得 `{1, 2, 3}`，交集 `&` 得 `{2}`，差集 `-` 得 `{1}`，对称差 `^` 得 `{1, 3}`（[7.4](../chapters/07-dicts/index.md#74)）。

## B.6 文件读写 { #b6 }

```python
with open("文件.txt", "r", encoding="utf-8") as f:   # r 读（默认）
    text = f.read()          # 读出全部内容，得到一个字符串
    # lines = f.readlines()  # 或：读出所有行，得到一个列表
    # for line in f:         # 或：一行一行地读

with open("文件.txt", "w", encoding="utf-8") as f:   # w 写（会清空原内容），a 追加
    f.write("一行文字\n")
```

| 模式 | 含义 |
|---|---|
| `"r"` | 读（文件必须存在） |
| `"w"` | 写，文件不存在就新建，存在就**清空** |
| `"a"` | 追加，写在原内容后面 |

CSV 用 `csv.reader` / `csv.DictReader` 读，`csv.writer` 写（打开时加 `newline=""`）；JSON 用 `json.load` / `json.dump` 读写文件，`json.loads` / `json.dumps` 转换字符串，写中文时加 `ensure_ascii=False`（[第 9 章](../chapters/09-files/index.md)）。

## B.7 常用标准库 { #b7 }

| 库 | 常用函数 | 正文 |
|---|---|---|
| turtle | `forward` 前进、`left` / `right` 转向、`penup` / `pendown` 抬笔 / 落笔、`goto` 移动到、`color` 颜色、`pensize` 笔粗、`speed` 速度、`write` 写字、`done` 结束 | [5.7](../chapters/05-loops/index.md#57) |
| random | `randint(a, b)` a～b 之间的随机整数、`random()` 0～1 的随机小数、`choice(列表)` 随机选一个、`sample(列表, k)` 随机选 k 个不重复的、`shuffle(列表)` 打乱、`seed(n)` 设置随机种子 | 第 5、6 章 |
| math | `sqrt` 开平方、`ceil` 向上取整、`floor` 向下取整、`pi` 圆周率 | [10.2.1](../chapters/10-modules-oop/index.md#1021) |
| time | `time()` 当前时间戳、`sleep(秒)` 暂停、`perf_counter()` 计时 | [10.2.2](../chapters/10-modules-oop/index.md#1022) |
| datetime | `date(年, 月, 日)`、`date.today()`、`timedelta(days=n)`、`strptime` 文字转日期、`strftime` 日期转文字 | [10.2.2](../chapters/10-modules-oop/index.md#1022) |
| pathlib | `Path(路径)`、`.name`、`.suffix`、`.iterdir()`、`.mkdir()`、`.exists()` | [10.2.3](../chapters/10-modules-oop/index.md#1023) |
| csv、json | 见 B.6 | 第 9 章 |

## B.8 本书用到的第三方库 { #b8 }

| 库 | 最常用的写法 | 正文 |
|---|---|---|
| openpyxl | `Workbook()`、`wb.active`、`ws.append(一行)`、`wb.save(文件名)`、`load_workbook(文件名)` | [10.4](../chapters/10-modules-oop/index.md#104) |
| PyInstaller | 命令行：`pyinstaller -F 程序.py` | [10.2.4](../chapters/10-modules-oop/index.md#1024) |
| numpy | `np.array(列表)`、`a * 2`、`a[a > 4]`、`a.sum()`、`a.mean()`、`np.median(a)` | [11.3](../chapters/11-data-libs/index.md#113) |
| pandas | `pd.read_csv`、`df.head()`、`df.info()`、`df["列"]`、`df[条件]`、`df.sort_values("列")`、`df.groupby("列")["列"].sum()` | [11.4](../chapters/11-data-libs/index.md#114) |
| matplotlib | `plt.plot`、`plt.bar`、`plt.pie`、`plt.title`、`plt.savefig`、`plt.show` | [11.5](../chapters/11-data-libs/index.md#115) |
| jieba | `jieba.lcut(s)`、`jieba.lcut(s, cut_all=True)`、`jieba.lcut_for_search(s)`、`jieba.add_word(词)` | [12.2.1](../chapters/12-ai-project/index.md#1221) |
| scikit-learn | `model = 模型类()`、`model.fit(X, y)`、`model.predict(新X)` | [12.2.2](../chapters/12-ai-project/index.md#1222) |
| requests | `requests.post(地址, headers=…, json=…, timeout=…)`、`resp.status_code`、`resp.json()` | [12.3.2](../chapters/12-ai-project/index.md#1232) |

## B.9 保留字 { #b9 }

保留字不能用作变量名、函数名。Python 3.14 共有 35 个（`import keyword` 后 `keyword.kwlist` 可以列出）：

```text
False None True and as assert async await break class continue def del elif else
except finally for from global if import in is lambda nonlocal not or pass raise
return try while with yield
```

此外，`match`、`case` 等是“软关键字”，只在特定的写法中有特殊含义，平时可以当变量名，但最好避开。
