---
title: 证书考点对照
description: 本课程对应的“信息技术水平-人工智能（Python）”证书，以及按计算机二级 Python 大纲整理的考点与本书章节对照表
---

# 证书考点对照

本页列出本课程对应的证书，以及每个考点在本书中的位置。正文中带紫色“证书考点”提示框的小节，就是下表列出的考点。

## 对应证书

| 证书 | 发证机构 | 考核依据 | 考核形式 |
|---|---|---|---|
| 信息技术水平-人工智能（Python） | 工业和信息化部教育与考试中心 | 见下方说明 | 以发证机构当期通知为准 |

!!! note "关于考纲"
    编者于 2026 年 11 月 1 日联网查找，没有找到这本证书公开的考试大纲或样题。工业和信息化部教育与考试中心官网上与之最接近的是“信息素养提升工程”中的《Python 应用师》《人工智能应用师》两个科目，官网只公布了考试时间（每场约 1 小时），没有公布大纲。<sup class="cite">[[1]](#ref-c1)</sup>

    因此，本书以教育部教育考试院公开发布的《全国计算机等级考试二级 Python 语言程序设计考试大纲（2025 年版）》作为知识点对照依据。<sup class="cite">[[2]](#ref-c2)</sup> 它是国内最通行的 Python 入门考试大纲，覆盖面和难度与本课程相当。学校如果从报名平台或培训方拿到正式考纲，可以按本页格式补充对照。

## 考点对照

下表按计算机二级 Python 大纲的 8 个部分逐条对照。二级考试是上机考试（120 分钟，100 分，单选 40 分、操作题 60 分），本书每章的选择题、判断题、“读程序写结果”题和实操题都按这个思路设计。

| 大纲部分 | 主要知识点 | 本书章节 | 实验 | 覆盖程度 |
|---|---|---|---|---|
| 一、基本语法元素 | 程序格式、缩进、注释；变量、命名、保留字；赋值语句；`input`、`eval`、`print` | [1.4](chapters/01-getting-started/index.md#14)、[1.5](chapters/01-getting-started/index.md#15)、[2.1](chapters/02-variables/index.md#21)、[2.5](chapters/02-variables/index.md#25) | 实验 1-2、2-1 | 本书完整覆盖 |
| 二、基本数据类型 | 整数、浮点数及运算；`True`、`False`、`None`；字符串及格式化；类型判断与转换；比较与逻辑运算 | [第 2 章](chapters/02-variables/index.md)、[第 3 章](chapters/03-strings/index.md)、[4.1](chapters/04-conditions/index.md#41) | 实验 2-1～3-3 | 本书完整覆盖 |
| 三、程序控制结构 | 顺序、分支、循环结构；`break`、`continue`；异常处理 `try-except` | [第 4 章](chapters/04-conditions/index.md)、[第 5 章](chapters/05-loops/index.md)、[9.5](chapters/09-files/index.md#95) | 实验 4-1～5-3、9-2 | 本书完整覆盖 |
| 四、函数和代码复用 | 函数定义与调用、参数、返回值、作用域；递归 | [第 8 章](chapters/08-functions/index.md) | 实验 8-1～8-3 | 本书完整覆盖（递归只讲入门例子） |
| 五、组合数据类型 | 列表、元组、集合、字典的创建、索引、切片和常用操作 | [第 6 章](chapters/06-lists/index.md)、[第 7 章](chapters/07-dicts/index.md) | 实验 6-1～7-3 | 本书完整覆盖 |
| 六、文件和数据格式化 | 文件的打开、读写、关闭；一维、二维数据的存储与处理；CSV 格式 | [第 9 章](chapters/09-files/index.md) | 实验 9-1～9-3 | 本书完整覆盖 |
| 七、程序设计方法 | 过程式与函数式编程；蒙特卡洛方法；递归计算 | [5.4](chapters/05-loops/index.md#54)、[8.6](chapters/08-functions/index.md#86) | 实验 5-2 | 本书部分覆盖（讲到会用即可） |
| 八、Python 计算生态 | `turtle`、`random`、`time` 等标准库；`pip` 安装第三方库；`jieba`、`PyInstaller`、`NumPy`；各领域常用库的名称 | [5.7](chapters/05-loops/index.md#57)、[第 10 章](chapters/10-modules-oop/index.md)、[第 11 章](chapters/11-data-libs/index.md)、[12.2](chapters/12-ai-project/index.md#122) | 实验 5-3、10-1、10-2、12-1 | 本书完整覆盖 |

二级大纲还有一部分“公共基础知识”（计算机系统、数据结构与算法、软件工程、数据库的基础知识，10 分），不在本课程范围内。

## 参考文献

<div class="refs" markdown>

- <span id="ref-c1"></span>[1] 工业和信息化部教育与考试中心. “信息素养提升工程”考试通知[EB/OL]. [2026-11-01]. https://www.miiteec.org.cn/news_details?code=2060.
- <span id="ref-c2"></span>[2] 教育部教育考试院. 全国计算机等级考试二级 Python 语言程序设计考试大纲（2025 年版）[EB/OL]. [2026-11-01]. https://jxjy.yznu.edu.cn/_upload/article/files/ba/d9/7ef53e5f49a6a178b0032e40f6b9/5809d0d3-3b83-4bf5-8017-e09cc366138a.pdf.

</div>
