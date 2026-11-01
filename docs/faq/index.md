---
title: 常见问题
description: 按类别整理的学习《Python 编程》时最常遇到的问题，每个答案都链接回教材正文
---

# 常见问题

这里按类别整理了学习本课程时最常遇到的问题。点开问题查看简短的回答，想深入了解，就顺着链接回到正文对应的小节。

| 类别 | 问题数 |
|---|---|
| [课程与学习方法](#faq-1) | 5 |
| [实验环境与排错](#faq-2) | 6 |
| [AI 与数据安全](#faq-3) | 3 |

## 课程与学习方法 { #faq-1 }

??? question "完全没学过编程，年纪也不小了，能学会吗？"

    能。本书从“程序是什么”讲起，不要求任何基础，例子都来自小店的日常事务。关键是动手：每学一节，就把例子在 Thonny 里敲一遍、改一改、运行一下。看十遍不如敲一遍。见[第 1 章](../chapters/01-getting-started/index.md)。

??? question "每周时间不多，怎样安排学习？"

    每章建议分 3 次：第一次读正文、看动画、敲例子（约 2 小时）；第二次做 ★ 实验（约 1 小时）；第三次做课后练习，错题点“回看”复习（约 1 小时）。每周至少有两次在电脑上写代码，比一次学很久效果好。

??? question "书上标着“待实测”是什么意思？"

    编者编写本书时无法运行的部分（如在 Windows 上打包 exe、调用付费的大模型服务）标为“待实测”，没有给出运行结果，而是给了操作步骤和记录表，请你运行后自己填写。全书只有两处，见 [10.2.4](../chapters/10-modules-oop/index.md#1024) 和 [12.3.3](../chapters/12-ai-project/index.md#1233)。

??? question "期末考试怎么考？能带书吗？"

    期末为闭卷考试，不能带书和资料。题型有单选、多选、判断、读程序与简答、编程题。考前可以做两套[模拟卷](../mock-exam.md)，并对照[证书考点对照](../certificate.md)查漏补缺。

??? question "课本上的代码能直接复制吗？"

    网页版的代码块右上角有复制按钮，配套资源 `labs` 文件夹里也有全部实验代码。但建议初学阶段**自己敲**：敲错、改错的过程正是学习的过程。

## 实验环境与排错 { #faq-2 }

??? question "用 Thonny 还是用 python.org 的 Python？"

    本书统一使用 Thonny 5.0.1，它自带 Python 3.14，装好就能用。等级考试使用 Python 自带的 IDLE，用法和 Thonny 差不多。见 [1.3 安装 Thonny](../chapters/01-getting-started/index.md#13) 和[附录 A](../appendix/a-environment.md)。

??? question "在命令行中输入 pip，提示“不是内部或外部命令”"

    请用 Thonny 菜单“工具 → 打开系统 shell”打开命令行窗口，或者在 Thonny 的“工具 → 管理包”中安装。见[附录 A.3](../appendix/a-environment.md#a3)。

??? question "程序报错了，看不懂英文怎么办？"

    先看最后一行的报错类型，再找 `line 几` 定位出错的行，然后查[附录 C 常见报错速查表](../appendix/c-errors.md)，那里有 30 多种常见报错的中文解释和改法。也可以把报错信息发给 AI 编程助手，请它解释（[1.7](../chapters/01-getting-started/index.md#17)）。

??? question "程序读数据时报 FileNotFoundError"

    多数是文件夹结构被改了，或者程序和数据不在约定的位置。保持 `labs` 文件夹的结构不变，用 Thonny 打开 `labs/chNN/` 里的程序直接运行。见 [9.1 文件路径](../chapters/09-files/index.md#91) 和[附录 A.2](../appendix/a-environment.md#a2)。

??? question "用 Excel 打开程序生成的 CSV 文件，中文是乱码"

    写文件时把编码改成 `utf-8-sig`，或在 Excel 中用“数据 → 从文本/CSV”导入并选择 UTF-8。见[附录 A.5](../appendix/a-environment.md#a5)。

??? question "Matplotlib 画的图里中文是方框"

    画图前设置中文字体：`plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei"]`。见 [11.5.1](../chapters/11-data-libs/index.md#1151)。

## AI 与数据安全 { #faq-3 }

??? question "有了 AI 写代码，还需要学编程吗？"

    需要。AI 写的代码会出错，你要读得懂、改得了；把需求说清楚、拆成模块，也要靠编程思维。而且期末考试和证书考试都是闭卷的。见 [1.7](../chapters/01-getting-started/index.md#17) 和 [12.6](../chapters/12-ai-project/index.md#126)。

??? question "能把工作中的客户表格发给 AI 帮忙分析吗？"

    不要把含有姓名、手机号、身份证号等个人信息的真实数据发给在线 AI。可以只发表头和几行虚构的示例数据，让 AI 写代码，再在自己电脑上运行。见 [11.6](../chapters/11-data-libs/index.md#116) 和 [12.5](../chapters/12-ai-project/index.md#125)。

??? question "调用大模型一定要花钱吗？"

    学习本书不需要花钱：第 12 章提供了在自己电脑上运行的模拟服务器，请求和回复的格式与真实服务相同。想体验真实的大模型，各服务商一般都有面向新用户的免费额度，以其官网说明为准；记得设置消费上限，保管好 API Key。见 [12.3](../chapters/12-ai-project/index.md#123)。
