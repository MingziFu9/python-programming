# 实验 7-2 顾客评价词频统计
# 评价已经用分词工具切好词、用空格隔开（第 12 章学习怎样用 jieba 自动分词）
reviews = """老板 很 热情 ， 找零 很 快 ， 排队 太 久 。
包子 很 香 。
牛奶 每天 都 有 新货 。
离家 近 很 方便 ， 包子 很 香 。
找零 很 快 。
价格 实惠 ， 老板 很 热情 。
排队 太 久 ， 但是 包子 很 香 。
店里 很 干净 ， 价格 实惠 。"""

stop = ["，", "。", "很", "太", "都", "有", "但是"]   # 停用词：标点和没有实际意义的词

counts = {}
for word in reviews.split():               # split() 不带参数，按空格和换行拆开
    if word in stop:
        continue
    counts[word] = counts.get(word, 0) + 1  # 词频统计的核心一行

print("一共有", len(counts), "个不同的词")
print(counts)

# 按次数从多到少排序（key=lambda 的写法第 8 章解释，这里先照着写）
items = sorted(counts.items(), key=lambda x: x[1], reverse=True)
print("出现最多的 5 个词：")
for word, n in items[:5]:
    print(f"{word:<4}{n:>2} 次  " + "■" * n)
