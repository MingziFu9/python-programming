---
title: 附录 A 编程环境安装与常见问题
description: Thonny 的安装与设置、配套资源的使用、用 pip 和国内镜像安装第三方库、本书用到的库和版本、Excel 打开 CSV 乱码等环境问题的解决办法
---

# 附录 A 编程环境安装与常见问题

本附录是第 1 章 [1.3 安装 Thonny](../chapters/01-getting-started/index.md#13) 和第 10 章 [10.3 用 pip 安装第三方库](../chapters/10-modules-oop/index.md#103) 的补充，遇到环境问题时查阅。

## A.1 安装 Thonny { #a1 }

本书使用 Thonny 5.0.1，它自带 Python 3.14，装好就能写程序，不需要另外安装 Python<sup class="cite">[[1]](#refa-1)</sup>。

**Windows 10/11**

1. 打开 thonny.org，在页面右上角的下载区点 Windows 的安装包（一般电脑选 x64）；
2. 双击下载的 .exe 文件。如果弹出“Windows 已保护你的电脑”，点“更多信息 → 仍要运行”（只对从官网下载的安装包这样做）；
3. 选择安装位置时，建议用**不含中文和空格**的路径，例如 `D:\Thonny`；然后一路“Next”，最后“Install”；
4. 从开始菜单打开 Thonny，第一次运行时语言选“简体中文”，点“Let's go!”。

**macOS**

在 thonny.org 下载 macOS 的 .pkg 安装包，双击后按提示安装，在“应用程序”中打开 Thonny。

**装好后检查**：在 Thonny 下方的 Shell 中输入下面两行，能看到 3.14 开头的版本号就说明一切正常：

```python
>>> import sys
>>> sys.version
```

**界面设置建议**

| 设置 | 操作 | 作用 |
|---|---|---|
| 显示变量 | 视图 → 变量 | 运行时在右侧显示每个变量的值 |
| 字体大小 | 工具 → 选项 → 主题和字体 | 投影上课时把编辑器字号调到 16 以上 |
| 显示行号 | 工具 → 选项 → 编辑器，勾选“显示行号” | 对照报错信息中的 `line 几` 找到出错的行 |

## A.2 配套资源的放法 { #a2 }

配套资源中的 `labs` 文件夹按章存放实验代码：

```text
labs/
├── README.md          使用说明
├── requirements.txt   第三方库清单
├── data/              全书共用的数据（虚构）
├── ch01/              第 1 章的实验
├── ……
└── ch12/              第 12 章的实验
```

建议把整个 `labs` 文件夹复制到 `D:\python-labs\` 这样的纯英文路径下，**不要改变里面的文件夹结构**。读取数据的程序用 `../data/文件名` 找数据，意思是“上一级文件夹里的 data 文件夹”，结构变了就会报 `FileNotFoundError`。

Thonny 运行程序时，会把程序所在的文件夹作为工作目录（[9.1 文件路径](../chapters/09-files/index.md#91)），所以只要用 Thonny 打开 `labs/chNN/` 里的程序直接运行，相对路径就是对的。

## A.3 命令行窗口与 pip { #a3 }

第 10 章起要在命令行中执行 pip 等命令。用 Thonny 自带的 Python 时，请用 Thonny 菜单“**工具 → 打开系统 shell**”打开命令行窗口，在这个窗口里 `python` 和 `pip` 指的就是 Thonny 自带的 Python。

| 你想做的事 | 命令 |
|---|---|
| 安装一个库 | `pip install openpyxl` |
| 安装指定版本 | `pip install pandas==3.1.0` |
| 按清单一次装好本书全部的库 | 先 `cd` 到 labs 文件夹，再 `pip install -r requirements.txt` |
| 查看已安装的库 | `pip list` |
| 卸载 | `pip uninstall 库名` |
| 命令找不到时 | 在前面加 `python -m`，如 `python -m pip install openpyxl` |

也可以不用命令行：Thonny 菜单“工具 → 管理包”，搜索库名，点“安装”。

**用国内镜像加速**

PyPI 的服务器在国外，下载慢或失败时，改用国内镜像。临时使用，在命令后加 `-i 镜像地址`：

```text
pip install openpyxl -i https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple
```

设为默认，以后不用每次都加 `-i`：

```text
pip config set global.index-url https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple
```

编者实测，这条命令会把设置写进 pip 的配置文件，并显示 `Writing to ...pip.conf`（Windows 上是 `pip.ini`）的提示。常用的镜像地址：

| 镜像 | 地址 |
|---|---|
| 清华大学 | `https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple`<sup class="cite">[[2]](#refa-2)</sup> |
| 阿里云 | `http://mirrors.aliyun.com/pypi/simple/`<sup class="cite">[[3]](#refa-3)</sup> |

阿里云镜像的地址是 http 开头的，pip 可能提示“不是受信任的网站”，这时在命令后再加上 `--trusted-host mirrors.aliyun.com`。

## A.4 本书用到的第三方库 { #a4 }

第 1～9 章只用 Python 自带的功能，不需要安装任何库。下表是编者编写本书时实际使用、全部实验已运行通过的版本（`labs/requirements.txt`）。用更新的版本一般也能运行，个别输出的格式可能略有不同。

| 库 | 编者使用的版本 | 用途 | 首次用到 |
|---|---|---|---|
| openpyxl | 3.1.5 | 读写 Excel 文件 | 第 10 章 |
| pyinstaller | 6.22.3 | 把程序打包成可执行文件 | 第 10 章 |
| numpy | 2.5.4 | 数组与数值计算 | 第 11 章 |
| pandas | 3.1.0 | 表格数据处理 | 第 11 章 |
| matplotlib | 3.11.2 | 画图 | 第 11 章 |
| jupyterlab | 4.6.5 | Jupyter 笔记本 | 第 11 章 |
| jieba | 0.42.1 | 中文分词 | 第 12 章 |
| scikit-learn | 1.9.1 | 机器学习 | 第 12 章 |
| requests | 2.34.2 | 发送网络请求 | 第 12 章 |
| openai | 3.42.0 | 调用大模型（可选） | 第 12 章 |

## A.5 Excel 打开 CSV 文件中文乱码 { #a5 }

本书的数据文件都用 UTF-8 编码保存。在 Windows 上双击用 Excel 打开 UTF-8 编码的 CSV 文件，中文可能显示成乱码，这是因为 Excel 默认按本地编码（简体中文系统一般是 GBK）读取。数据本身没有坏，有三种解决办法：

1. **用程序写 CSV 时加 BOM**：把 `encoding="utf-8"` 改成 `encoding="utf-8-sig"`。utf-8-sig 会在文件开头加一个特殊标记，Excel 看到它就知道这是 UTF-8 文件（[9.3 节](../chapters/09-files/index.md#93)）。用 pandas 写文件时同样：`df.to_csv("文件.csv", index=False, encoding="utf-8-sig")`；
2. **在 Excel 中导入**：新建空白工作簿，用“数据 → 从文本/CSV”选择文件，在“文件原始格式”中选 UTF-8，再加载；
3. **用 WPS 或 Thonny 打开**：WPS 表格一般能自动识别编码；只是查看内容，也可以直接在 Thonny 中打开 CSV 文件。

反过来，用 Excel“另存为”CSV 得到的文件常常是 GBK 编码，Python 按 UTF-8 读取会报 `UnicodeDecodeError`，这时要用 `encoding="gbk"` 打开（附录 C）。

## A.6 其他常见问题 { #a6 }

??? question "Thonny 打开后报错，或者运行任何程序都失败"

    多数是安装路径或 Windows 用户名中有中文造成的。把 Thonny 卸载后重新安装到 `D:\Thonny` 这样的纯英文路径；程序文件也放在纯英文路径下。

??? question "在 cmd 中输入 pip 或 python，提示“不是内部或外部命令”"

    Thonny 自带的 Python 没有加到系统的 PATH 中，直接打开的 cmd 找不到它。请用 Thonny 的“工具 → 打开系统 shell”打开命令行窗口（A.3 节）。

??? question "pip 安装时出现红色的 ReadTimeoutError 或 SSL 错误"

    网络慢或连不上国外服务器。改用国内镜像（A.3 节），或换一个网络再试。

??? question "电脑上装了好几个 Python，库装上了却 import 不到"

    pip 把库装到了另一个 Python 里。在 Thonny 的“工具 → 管理包”中安装，或者在“工具 → 打开系统 shell”打开的窗口中安装，可以保证装到 Thonny 正在用的 Python 里。在 Shell 中执行 `import sys` 再看 `sys.executable`，可以知道当前用的是哪个 Python。

??? question "PyInstaller 打包出来的 exe 被杀毒软件删除了"

    这是常见的误报。可以把 `dist` 文件夹加入杀毒软件的信任区；发给别人使用时，要说明情况。

??? question "没有电脑，只有手机，能学吗？"

    本书网页版的很多代码块下有“▶ 试一试”按钮，在手机浏览器中也能修改、运行，适合随时练习。但实验和考试需要在电脑上完成，建议至少每周在电脑上练习两次。

## 参考文献

<div class="refs" markdown>

**在线资源与数据**

- <span id="refa-1"></span>[1] Thonny. Thonny: Python IDE for beginners[EB/OL]. [2026-11-01]. https://thonny.org/.
    <span class="ref-note">Thonny 官网，提供 Windows、macOS、Linux 的安装包，对应 A.1 节。</span>
- <span id="refa-2"></span>[2] 清华大学开源软件镜像站. PyPI 软件仓库镜像使用帮助[EB/OL]. [2026-11-01]. https://mirrors.tuna.tsinghua.edu.cn/help/pypi/.
    <span class="ref-note">清华大学 PyPI 镜像的官方使用说明，含临时使用和设为默认的命令，对应 A.3 节。</span>
- <span id="refa-3"></span>[3] 阿里云. PyPI 镜像[EB/OL]. [2026-11-01]. https://developer.aliyun.com/mirror/pypi.
    <span class="ref-note">阿里云 PyPI 镜像的配置说明，对应 A.3 节。</span>

</div>
