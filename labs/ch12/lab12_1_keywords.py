# 实验 12-1 用 jieba 找出顾客评价里的关键词
# 需要先安装：pip install jieba
import jieba

# 1. 读入评价，一行一条
with open("../data/reviews.txt", encoding="utf-8") as f:
    reviews = [line.strip() for line in f if line.strip()]
print("共", len(reviews), "条评价")

# 2. 先看看分词的效果
print(jieba.lcut(reviews[0]))

# 3. 停用词：没有实际意义、不想统计的词
stop = {"很", "太", "都", "也", "就", "了", "的", "有", "是", "和", "，", "。", "！", "、"}

# 4. 逐条分词，用字典计数（第 7 章的方法）
counts = {}
for r in reviews:
    for w in jieba.lcut(r):
        if w in stop or len(w) < 2:      # 去掉停用词和单个字
            continue
        counts[w] = counts.get(w, 0) + 1

# 5. 按次数从多到少排序，输出前 10 个
top = sorted(counts.items(), key=lambda x: x[1], reverse=True)[:10]
print("出现最多的 10 个词：")
for w, n in top:
    print(f"  {w:<6}{n:>3} 次")

# 6. 看看提到“排队”的评价有几条
queue = [r for r in reviews if "排队" in r]
print("提到“排队”的评价有", len(queue), "条，例如：", queue[0])
