# reviews.py 顾客评价分析模块（组员 B 负责）
import jieba

jieba.setLogLevel(20)               # 不显示 jieba 加载词典时的提示信息
STOP = {"很", "太", "都", "也", "就", "了", "的", "有", "是", "和"}


def top_words(path, n=5):
    """统计评价文件中出现最多的 n 个词，返回 [(词, 次数), ...]"""
    counts = {}
    with open(path, encoding="utf-8") as f:
        for line in f:
            for w in jieba.lcut(line.strip()):
                if w in STOP or len(w) < 2:
                    continue
                counts[w] = counts.get(w, 0) + 1
    return sorted(counts.items(), key=lambda x: x[1], reverse=True)[:n]


def count_keyword(path, word):
    """统计包含某个词的评价条数"""
    with open(path, encoding="utf-8") as f:
        return sum(1 for line in f if word in line)


if __name__ == "__main__":
    print(top_words("../../data/reviews.txt"))
    print(count_keyword("../../data/reviews.txt", "排队"))
