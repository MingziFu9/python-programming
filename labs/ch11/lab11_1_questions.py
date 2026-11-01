# 实验 11-1 读入小店全年销售表，回答 5 个问题
# 建议在 Jupyter 中按“# %%”分成几个单元格逐个运行；直接用 Thonny 运行也可以
import pandas as pd

pd.set_option("display.unicode.east_asian_width", True)   # 让中文列对齐

# %% 读入数据，先看看长什么样
df = pd.read_csv("../data/sales_2025.csv")
print(df.shape)                        # (行数, 列数)
print(df[["日期", "商品名称", "数量", "金额", "支付方式"]].head(3))

# %% 问题 1：全年营业额是多少？一共多少单？
print("问题 1：全年营业额", round(df["金额"].sum(), 2), "元，共", df["单号"].nunique(), "单")

# %% 问题 2：卖得最多（按金额）的 5 种商品是什么？
top5 = df.groupby("商品名称")["金额"].sum().sort_values(ascending=False).head(5)
print("问题 2：销售额前 5 的商品")
print(top5)

# %% 问题 3：会员消费的金额占全部营业额的百分之几？
member = df[df["会员号"].notna()]      # 会员号不为空的行
print(f"问题 3：会员消费 {member['金额'].sum():.2f} 元，占 {member['金额'].sum() / df['金额'].sum():.1%}")

# %% 问题 4：一次买 3 件及以上同一种商品的记录有多少条？最常见的是哪些商品？
big = df[df["数量"] >= 3]
print("问题 4：共", len(big), "条，最常见的是")
print(big["商品名称"].value_counts().head(3))

# %% 问题 5：一周中哪一天营业额最高？
df["日期"] = pd.to_datetime(df["日期"])
df["星期"] = df["日期"].dt.day_of_week  # 0 是星期一，6 是星期日
by_week = df.groupby("星期")["金额"].sum()
names = ["一", "二", "三", "四", "五", "六", "日"]
print("问题 5：")
for i, money in by_week.items():
    print(f"  星期{names[i]} {money:>10.2f} 元")
print("最高的是星期" + names[by_week.idxmax()])
