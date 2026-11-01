---
title: 学习图谱
description: 全书核心概念及其先修关系，点一个概念就能看到学习路径
---

# 学习图谱

学习图谱把全书的核心概念和它们之间的“先修关系”画在一张图上：要理解一个概念，得先懂哪些更基础的概念；顺着箭头往回找，就是一条学习路径。

<iframe class="sim-frame" src="main.html" height="900" loading="lazy" title="学习图谱"></iframe>

[全屏打开](main.html){ target=_blank }

## 怎样使用

- **预习**：学新的一章前，点开本章的概念，看看橙色的先修概念自己是否都掌握了，没掌握的先回去复习；
- **复习**：期末复习时，从最后几章的概念出发，顺着学习路径往回梳理，就能把全书串起来；
- **查漏补缺**：做练习时遇到不懂的概念，在搜索框里输入它，看它依赖哪些更基础的概念。

<!-- graph:start -->

图谱共有 **123 个概念、176 条先修关系**，概念按章排列，颜色表示 6 个类别（Python 入门、字符串与流程控制、组合数据类型、函数与程序组织、文件与数据处理、AI 应用）。概念的定义都来自[附录 D 术语表](../appendix/glossary.md)，先修关系由编者根据各章内容整理。

## 文字版

下面按章列出每个概念的直接先修概念，便于打印或用读屏软件阅读。

??? note "第 1 章 初识 Python（15 个概念）"

    | 概念 | 类别 | 直接先修 |
    |---|---|---|
    | [程序](../appendix/glossary.md#g-程序) | Python 入门 | — |
    | [编程](../appendix/glossary.md#g-编程) | Python 入门 | [程序](../appendix/glossary.md#g-程序) |
    | [编程语言](../appendix/glossary.md#g-编程语言) | Python 入门 | [编程](../appendix/glossary.md#g-编程) |
    | [解释器](../appendix/glossary.md#g-解释器) | Python 入门 | [编程语言](../appendix/glossary.md#g-编程语言) |
    | [集成开发环境](../appendix/glossary.md#g-集成开发环境) | Python 入门 | [解释器](../appendix/glossary.md#g-解释器) |
    | [函数](../appendix/glossary.md#g-函数) | Python 入门 | [程序](../appendix/glossary.md#g-程序) |
    | [字符串](../appendix/glossary.md#g-字符串) | Python 入门 | [程序](../appendix/glossary.md#g-程序) |
    | [注释](../appendix/glossary.md#g-注释) | Python 入门 | [脚本](../appendix/glossary.md#g-脚本) |
    | [交互模式](../appendix/glossary.md#g-交互模式) | Python 入门 | [解释器](../appendix/glossary.md#g-解释器) |
    | [脚本](../appendix/glossary.md#g-脚本) | Python 入门 | [集成开发环境](../appendix/glossary.md#g-集成开发环境) |
    | [缩进](../appendix/glossary.md#g-缩进) | Python 入门 | [脚本](../appendix/glossary.md#g-脚本) |
    | [PEP 8](../appendix/glossary.md#g-PEP-8) | Python 入门 | [缩进](../appendix/glossary.md#g-缩进)、[注释](../appendix/glossary.md#g-注释) |
    | [追踪信息](../appendix/glossary.md#g-追踪信息) | Python 入门 | [解释器](../appendix/glossary.md#g-解释器) |
    | [语法错误](../appendix/glossary.md#g-语法错误) | Python 入门 | [追踪信息](../appendix/glossary.md#g-追踪信息) |
    | [AI 编程助手](../appendix/glossary.md#g-AI-编程助手) | Python 入门 | [编程](../appendix/glossary.md#g-编程)、[追踪信息](../appendix/glossary.md#g-追踪信息) |

??? note "第 2 章 变量与运算（10 个概念）"

    | 概念 | 类别 | 直接先修 |
    |---|---|---|
    | [变量](../appendix/glossary.md#g-变量) | Python 入门 | [赋值语句](../appendix/glossary.md#g-赋值语句) |
    | [赋值语句](../appendix/glossary.md#g-赋值语句) | Python 入门 | [脚本](../appendix/glossary.md#g-脚本) |
    | [保留字](../appendix/glossary.md#g-保留字) | Python 入门 | [变量](../appendix/glossary.md#g-变量) |
    | [数据类型](../appendix/glossary.md#g-数据类型) | Python 入门 | [变量](../appendix/glossary.md#g-变量) |
    | [整数](../appendix/glossary.md#g-整数) | Python 入门 | [数据类型](../appendix/glossary.md#g-数据类型) |
    | [浮点数](../appendix/glossary.md#g-浮点数) | Python 入门 | [数据类型](../appendix/glossary.md#g-数据类型) |
    | [布尔值](../appendix/glossary.md#g-布尔值) | Python 入门 | [数据类型](../appendix/glossary.md#g-数据类型) |
    | [复合赋值运算符](../appendix/glossary.md#g-复合赋值运算符) | Python 入门 | [赋值语句](../appendix/glossary.md#g-赋值语句) |
    | [类型转换](../appendix/glossary.md#g-类型转换) | Python 入门 | [数据类型](../appendix/glossary.md#g-数据类型)、[字符串](../appendix/glossary.md#g-字符串) |
    | [f-string](../appendix/glossary.md#g-f-string) | Python 入门 | [字符串](../appendix/glossary.md#g-字符串)、[浮点数](../appendix/glossary.md#g-浮点数) |

??? note "第 3 章 字符串（9 个概念）"

    | 概念 | 类别 | 直接先修 |
    |---|---|---|
    | [转义字符](../appendix/glossary.md#g-转义字符) | 字符串与流程控制 | [字符串](../appendix/glossary.md#g-字符串) |
    | [原始字符串](../appendix/glossary.md#g-原始字符串) | 字符串与流程控制 | [转义字符](../appendix/glossary.md#g-转义字符) |
    | [索引](../appendix/glossary.md#g-索引) | 字符串与流程控制 | [字符串](../appendix/glossary.md#g-字符串) |
    | [切片](../appendix/glossary.md#g-切片) | 字符串与流程控制 | [索引](../appendix/glossary.md#g-索引) |
    | [方法](../appendix/glossary.md#g-方法) | 字符串与流程控制 | [函数](../appendix/glossary.md#g-函数)、[字符串](../appendix/glossary.md#g-字符串) |
    | [Unicode](../appendix/glossary.md#g-Unicode) | 字符串与流程控制 | [字符串](../appendix/glossary.md#g-字符串) |
    | [字符编码](../appendix/glossary.md#g-字符编码) | 字符串与流程控制 | [Unicode](../appendix/glossary.md#g-Unicode) |
    | [UTF-8](../appendix/glossary.md#g-UTF-8) | 字符串与流程控制 | [字符编码](../appendix/glossary.md#g-字符编码) |
    | [词元](../appendix/glossary.md#g-词元) | 字符串与流程控制 | [字符串](../appendix/glossary.md#g-字符串)、[AI 编程助手](../appendix/glossary.md#g-AI-编程助手) |

??? note "第 4 章 条件判断（10 个概念）"

    | 概念 | 类别 | 直接先修 |
    |---|---|---|
    | [比较运算符](../appendix/glossary.md#g-比较运算符) | 字符串与流程控制 | [数据类型](../appendix/glossary.md#g-数据类型) |
    | [布尔表达式](../appendix/glossary.md#g-布尔表达式) | 字符串与流程控制 | [比较运算符](../appendix/glossary.md#g-比较运算符)、[布尔值](../appendix/glossary.md#g-布尔值) |
    | [顺序结构](../appendix/glossary.md#g-顺序结构) | 字符串与流程控制 | [脚本](../appendix/glossary.md#g-脚本) |
    | [分支结构](../appendix/glossary.md#g-分支结构) | 字符串与流程控制 | [布尔表达式](../appendix/glossary.md#g-布尔表达式)、[缩进](../appendix/glossary.md#g-缩进)、[顺序结构](../appendix/glossary.md#g-顺序结构) |
    | [条件表达式](../appendix/glossary.md#g-条件表达式) | 字符串与流程控制 | [分支结构](../appendix/glossary.md#g-分支结构) |
    | [逻辑运算符](../appendix/glossary.md#g-逻辑运算符) | 字符串与流程控制 | [布尔表达式](../appendix/glossary.md#g-布尔表达式) |
    | [真值测试](../appendix/glossary.md#g-真值测试) | 字符串与流程控制 | [布尔值](../appendix/glossary.md#g-布尔值)、[分支结构](../appendix/glossary.md#g-分支结构) |
    | [流程图](../appendix/glossary.md#g-流程图) | 字符串与流程控制 | [顺序结构](../appendix/glossary.md#g-顺序结构) |
    | [嵌套](../appendix/glossary.md#g-嵌套) | 字符串与流程控制 | [分支结构](../appendix/glossary.md#g-分支结构) |
    | [输入检查](../appendix/glossary.md#g-输入检查) | 字符串与流程控制 | [分支结构](../appendix/glossary.md#g-分支结构)、[类型转换](../appendix/glossary.md#g-类型转换) |

??? note "第 5 章 循环（9 个概念）"

    | 概念 | 类别 | 直接先修 |
    |---|---|---|
    | [循环](../appendix/glossary.md#g-循环) | 字符串与流程控制 | [分支结构](../appendix/glossary.md#g-分支结构) |
    | [循环体](../appendix/glossary.md#g-循环体) | 字符串与流程控制 | [循环](../appendix/glossary.md#g-循环) |
    | [计数器](../appendix/glossary.md#g-计数器) | 字符串与流程控制 | [循环](../appendix/glossary.md#g-循环)、[复合赋值运算符](../appendix/glossary.md#g-复合赋值运算符) |
    | [死循环](../appendix/glossary.md#g-死循环) | 字符串与流程控制 | [循环](../appendix/glossary.md#g-循环) |
    | [循环变量](../appendix/glossary.md#g-循环变量) | 字符串与流程控制 | [循环](../appendix/glossary.md#g-循环) |
    | [累加器](../appendix/glossary.md#g-累加器) | 字符串与流程控制 | [循环](../appendix/glossary.md#g-循环)、[复合赋值运算符](../appendix/glossary.md#g-复合赋值运算符) |
    | [蒙特卡洛方法](../appendix/glossary.md#g-蒙特卡洛方法) | 字符串与流程控制 | [循环](../appendix/glossary.md#g-循环)、[累加器](../appendix/glossary.md#g-累加器) |
    | [嵌套循环](../appendix/glossary.md#g-嵌套循环) | 字符串与流程控制 | [循环](../appendix/glossary.md#g-循环)、[嵌套](../appendix/glossary.md#g-嵌套) |
    | [二分查找](../appendix/glossary.md#g-二分查找) | 字符串与流程控制 | [循环](../appendix/glossary.md#g-循环)、[比较运算符](../appendix/glossary.md#g-比较运算符) |

??? note "第 6 章 列表与元组（9 个概念）"

    | 概念 | 类别 | 直接先修 |
    |---|---|---|
    | [列表](../appendix/glossary.md#g-列表) | 组合数据类型 | [变量](../appendix/glossary.md#g-变量)、[索引](../appendix/glossary.md#g-索引) |
    | [元素](../appendix/glossary.md#g-元素) | 组合数据类型 | [列表](../appendix/glossary.md#g-列表) |
    | [遍历](../appendix/glossary.md#g-遍历) | 组合数据类型 | [列表](../appendix/glossary.md#g-列表)、[循环变量](../appendix/glossary.md#g-循环变量) |
    | [列表推导式](../appendix/glossary.md#g-列表推导式) | 组合数据类型 | [列表](../appendix/glossary.md#g-列表)、[循环](../appendix/glossary.md#g-循环) |
    | [二维列表](../appendix/glossary.md#g-二维列表) | 组合数据类型 | [列表](../appendix/glossary.md#g-列表)、[嵌套循环](../appendix/glossary.md#g-嵌套循环) |
    | [一维数据](../appendix/glossary.md#g-一维数据) | 组合数据类型 | [列表](../appendix/glossary.md#g-列表) |
    | [二维数据](../appendix/glossary.md#g-二维数据) | 组合数据类型 | [二维列表](../appendix/glossary.md#g-二维列表)、[一维数据](../appendix/glossary.md#g-一维数据) |
    | [元组](../appendix/glossary.md#g-元组) | 组合数据类型 | [列表](../appendix/glossary.md#g-列表) |
    | [解包](../appendix/glossary.md#g-解包) | 组合数据类型 | [元组](../appendix/glossary.md#g-元组)、[赋值语句](../appendix/glossary.md#g-赋值语句) |

??? note "第 7 章 字典与集合（9 个概念）"

    | 概念 | 类别 | 直接先修 |
    |---|---|---|
    | [字典](../appendix/glossary.md#g-字典) | 组合数据类型 | [列表](../appendix/glossary.md#g-列表) |
    | [键](../appendix/glossary.md#g-键) | 组合数据类型 | [字典](../appendix/glossary.md#g-字典) |
    | [值](../appendix/glossary.md#g-值) | 组合数据类型 | [字典](../appendix/glossary.md#g-字典) |
    | [键值对](../appendix/glossary.md#g-键值对) | 组合数据类型 | [键](../appendix/glossary.md#g-键)、[值](../appendix/glossary.md#g-值) |
    | [词频统计](../appendix/glossary.md#g-词频统计) | 组合数据类型 | [字典](../appendix/glossary.md#g-字典)、[遍历](../appendix/glossary.md#g-遍历) |
    | [停用词](../appendix/glossary.md#g-停用词) | 组合数据类型 | [词频统计](../appendix/glossary.md#g-词频统计) |
    | [JSON](../appendix/glossary.md#g-JSON) | 组合数据类型 | [字典](../appendix/glossary.md#g-字典)、[列表](../appendix/glossary.md#g-列表) |
    | [集合](../appendix/glossary.md#g-集合) | 组合数据类型 | [列表](../appendix/glossary.md#g-列表) |
    | [去重](../appendix/glossary.md#g-去重) | 组合数据类型 | [集合](../appendix/glossary.md#g-集合) |

??? note "第 8 章 函数（12 个概念）"

    | 概念 | 类别 | 直接先修 |
    |---|---|---|
    | [参数](../appendix/glossary.md#g-参数) | 函数与程序组织 | [函数](../appendix/glossary.md#g-函数) |
    | [函数体](../appendix/glossary.md#g-函数体) | 函数与程序组织 | [函数](../appendix/glossary.md#g-函数)、[缩进](../appendix/glossary.md#g-缩进) |
    | [位置参数](../appendix/glossary.md#g-位置参数) | 函数与程序组织 | [参数](../appendix/glossary.md#g-参数) |
    | [默认值](../appendix/glossary.md#g-默认值) | 函数与程序组织 | [参数](../appendix/glossary.md#g-参数) |
    | [关键字参数](../appendix/glossary.md#g-关键字参数) | 函数与程序组织 | [参数](../appendix/glossary.md#g-参数) |
    | [返回值](../appendix/glossary.md#g-返回值) | 函数与程序组织 | [函数](../appendix/glossary.md#g-函数) |
    | [局部变量](../appendix/glossary.md#g-局部变量) | 函数与程序组织 | [函数体](../appendix/glossary.md#g-函数体)、[变量](../appendix/glossary.md#g-变量) |
    | [全局变量](../appendix/glossary.md#g-全局变量) | 函数与程序组织 | [局部变量](../appendix/glossary.md#g-局部变量) |
    | [文档字符串](../appendix/glossary.md#g-文档字符串) | 函数与程序组织 | [函数](../appendix/glossary.md#g-函数)、[注释](../appendix/glossary.md#g-注释) |
    | [匿名函数](../appendix/glossary.md#g-匿名函数) | 函数与程序组织 | [函数](../appendix/glossary.md#g-函数)、[返回值](../appendix/glossary.md#g-返回值) |
    | [递归](../appendix/glossary.md#g-递归) | 函数与程序组织 | [函数](../appendix/glossary.md#g-函数)、[返回值](../appendix/glossary.md#g-返回值) |
    | [工具调用](../appendix/glossary.md#g-工具调用) | 函数与程序组织 | [函数](../appendix/glossary.md#g-函数)、[AI 编程助手](../appendix/glossary.md#g-AI-编程助手) |

??? note "第 9 章 文件与异常（9 个概念）"

    | 概念 | 类别 | 直接先修 |
    |---|---|---|
    | [路径](../appendix/glossary.md#g-路径) | 文件与数据处理 | [字符串](../appendix/glossary.md#g-字符串) |
    | [绝对路径](../appendix/glossary.md#g-绝对路径) | 文件与数据处理 | [路径](../appendix/glossary.md#g-路径) |
    | [相对路径](../appendix/glossary.md#g-相对路径) | 文件与数据处理 | [路径](../appendix/glossary.md#g-路径) |
    | [工作目录](../appendix/glossary.md#g-工作目录) | 文件与数据处理 | [相对路径](../appendix/glossary.md#g-相对路径) |
    | [CSV](../appendix/glossary.md#g-CSV) | 文件与数据处理 | [二维数据](../appendix/glossary.md#g-二维数据)、[字符编码](../appendix/glossary.md#g-字符编码) |
    | [表头](../appendix/glossary.md#g-表头) | 文件与数据处理 | [CSV](../appendix/glossary.md#g-CSV) |
    | [异常](../appendix/glossary.md#g-异常) | 文件与数据处理 | [追踪信息](../appendix/glossary.md#g-追踪信息) |
    | [断点](../appendix/glossary.md#g-断点) | 文件与数据处理 | [异常](../appendix/glossary.md#g-异常)、[集成开发环境](../appendix/glossary.md#g-集成开发环境) |
    | [JSON Lines](../appendix/glossary.md#g-JSON-Lines) | 文件与数据处理 | [JSON](../appendix/glossary.md#g-JSON) |

??? note "第 10 章 模块与类（11 个概念）"

    | 概念 | 类别 | 直接先修 |
    |---|---|---|
    | [模块](../appendix/glossary.md#g-模块) | 函数与程序组织 | [函数](../appendix/glossary.md#g-函数)、[脚本](../appendix/glossary.md#g-脚本) |
    | [标准库](../appendix/glossary.md#g-标准库) | 函数与程序组织 | [模块](../appendix/glossary.md#g-模块) |
    | [第三方库](../appendix/glossary.md#g-第三方库) | 函数与程序组织 | [模块](../appendix/glossary.md#g-模块) |
    | [pip](../appendix/glossary.md#g-pip) | 函数与程序组织 | [第三方库](../appendix/glossary.md#g-第三方库) |
    | [虚拟环境](../appendix/glossary.md#g-虚拟环境) | 函数与程序组织 | [pip](../appendix/glossary.md#g-pip) |
    | [PyInstaller](../appendix/glossary.md#g-PyInstaller) | 函数与程序组织 | [第三方库](../appendix/glossary.md#g-第三方库) |
    | [类](../appendix/glossary.md#g-类) | 函数与程序组织 | [数据类型](../appendix/glossary.md#g-数据类型)、[函数](../appendix/glossary.md#g-函数) |
    | [对象](../appendix/glossary.md#g-对象) | 函数与程序组织 | [类](../appendix/glossary.md#g-类) |
    | [属性](../appendix/glossary.md#g-属性) | 函数与程序组织 | [对象](../appendix/glossary.md#g-对象)、[变量](../appendix/glossary.md#g-变量) |
    | [初始化方法](../appendix/glossary.md#g-初始化方法) | 函数与程序组织 | [类](../appendix/glossary.md#g-类)、[参数](../appendix/glossary.md#g-参数) |
    | [继承](../appendix/glossary.md#g-继承) | 函数与程序组织 | [类](../appendix/glossary.md#g-类) |

??? note "第 11 章 数据处理初体验（10 个概念）"

    | 概念 | 类别 | 直接先修 |
    |---|---|---|
    | [向量化运算](../appendix/glossary.md#g-向量化运算) | 文件与数据处理 | [数组](../appendix/glossary.md#g-数组)、[循环](../appendix/glossary.md#g-循环) |
    | [数组](../appendix/glossary.md#g-数组) | 文件与数据处理 | [列表](../appendix/glossary.md#g-列表)、[第三方库](../appendix/glossary.md#g-第三方库) |
    | [布尔索引](../appendix/glossary.md#g-布尔索引) | 文件与数据处理 | [数组](../appendix/glossary.md#g-数组)、[布尔表达式](../appendix/glossary.md#g-布尔表达式) |
    | [Jupyter](../appendix/glossary.md#g-Jupyter) | 文件与数据处理 | [第三方库](../appendix/glossary.md#g-第三方库)、[交互模式](../appendix/glossary.md#g-交互模式) |
    | [单元格](../appendix/glossary.md#g-单元格) | 文件与数据处理 | [Jupyter](../appendix/glossary.md#g-Jupyter) |
    | [DataFrame](../appendix/glossary.md#g-DataFrame) | 文件与数据处理 | [二维数据](../appendix/glossary.md#g-二维数据)、[数组](../appendix/glossary.md#g-数组)、[CSV](../appendix/glossary.md#g-CSV) |
    | [Series](../appendix/glossary.md#g-Series) | 文件与数据处理 | [DataFrame](../appendix/glossary.md#g-DataFrame) |
    | [分组汇总](../appendix/glossary.md#g-分组汇总) | 文件与数据处理 | [DataFrame](../appendix/glossary.md#g-DataFrame)、[词频统计](../appendix/glossary.md#g-词频统计) |
    | [缺失值](../appendix/glossary.md#g-缺失值) | 文件与数据处理 | [DataFrame](../appendix/glossary.md#g-DataFrame) |
    | [数据可视化](../appendix/glossary.md#g-数据可视化) | 文件与数据处理 | [第三方库](../appendix/glossary.md#g-第三方库)、[Series](../appendix/glossary.md#g-Series) |

??? note "第 12 章 AI 综合项目（10 个概念）"

    | 概念 | 类别 | 直接先修 |
    |---|---|---|
    | [机器学习](../appendix/glossary.md#g-机器学习) | AI 应用 | [对象](../appendix/glossary.md#g-对象)、[DataFrame](../appendix/glossary.md#g-DataFrame) |
    | [分词](../appendix/glossary.md#g-分词) | AI 应用 | [字符串](../appendix/glossary.md#g-字符串)、[第三方库](../appendix/glossary.md#g-第三方库)、[词频统计](../appendix/glossary.md#g-词频统计) |
    | [文本分类](../appendix/glossary.md#g-文本分类) | AI 应用 | [机器学习](../appendix/glossary.md#g-机器学习)、[分词](../appendix/glossary.md#g-分词) |
    | [API](../appendix/glossary.md#g-API) | AI 应用 | [函数](../appendix/glossary.md#g-函数)、[JSON](../appendix/glossary.md#g-JSON) |
    | [API Key](../appendix/glossary.md#g-API-Key) | AI 应用 | [API](../appendix/glossary.md#g-API) |
    | [HTTP 状态码](../appendix/glossary.md#g-HTTP-状态码) | AI 应用 | [API](../appendix/glossary.md#g-API)、[异常](../appendix/glossary.md#g-异常) |
    | [提示词](../appendix/glossary.md#g-提示词) | AI 应用 | [大语言模型](../appendix/glossary.md#g-大语言模型) |
    | [大语言模型](../appendix/glossary.md#g-大语言模型) | AI 应用 | [词元](../appendix/glossary.md#g-词元)、[机器学习](../appendix/glossary.md#g-机器学习) |
    | [智能体](../appendix/glossary.md#g-智能体) | AI 应用 | [大语言模型](../appendix/glossary.md#g-大语言模型)、[工具调用](../appendix/glossary.md#g-工具调用) |
    | [需求分析](../appendix/glossary.md#g-需求分析) | AI 应用 | [模块](../appendix/glossary.md#g-模块)、[函数](../appendix/glossary.md#g-函数) |

<!-- graph:end -->
