# 12.2.2 体验：用 scikit-learn 训练一个“好评 / 差评”分类模型
# 需要先安装：pip install scikit-learn jieba pandas
import jieba
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

jieba.setLogLevel(20)                              # 不显示 jieba 的加载信息

df = pd.read_csv("../data/review_labels.csv")      # 32 条带标签的评价（虚构）
print(df.sample(3, random_state=1))

# 1. 把文字变成数字：统计每条评价里各个词出现的次数
vec = CountVectorizer(tokenizer=jieba.lcut, token_pattern=None)
X = vec.fit_transform(df["评价"])
print("一共认识", len(vec.vocabulary_), "个词")

# 2. 三步：创建模型、训练、预测（第 10 章见过的写法）
model = MultinomialNB()
model.fit(X, df["类别"])

new = ["包子很好吃，老板热情", "排队太久了，还缺货", "价格便宜，就是有点挤", "冷饮很冰"]
pred = model.predict(vec.transform(new))
prob = model.predict_proba(vec.transform(new))
for text, p, pr in zip(new, pred, prob):
    print(f"{text:<12} → {p}（好评可能性 {pr[0]:.0%}）")
