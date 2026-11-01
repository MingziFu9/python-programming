# 实验 11-3 用 NumPy 做会员消费统计
import numpy as np
import pandas as pd

df = pd.read_csv("../data/sales_2025.csv")
# 用 pandas 按会员号汇总每位会员全年的消费额，再转成 NumPy 数组
spend = df.groupby("会员号")["金额"].sum().to_numpy()
print("会员人数：", spend.size)
print("前 5 位：", spend[:5])

print(f"人均消费 {spend.mean():.2f} 元，中位数 {np.median(spend):.2f} 元")
print(f"最高 {spend.max():.2f} 元，最低 {spend.min():.2f} 元，标准差 {spend.std():.2f}")

# 布尔筛选：消费超过 800 元的会员有几位，他们的消费占会员总消费的多少
rich = spend[spend > 800]
print(f"消费超过 800 元的有 {rich.size} 位，占会员总消费的 {rich.sum() / spend.sum():.1%}")

# 向量化运算：全部会员按消费额的 1% 返现，不用写循环
cashback = np.round(spend * 0.01, 2)
print("返现总额：", cashback.sum().round(2), "元")

# 分段统计：消费额落在各区间的人数
bins = [0, 300, 600, 900, 2000]
counts, _ = np.histogram(spend, bins=bins)
for i in range(len(counts)):
    print(f"  {bins[i]}～{bins[i + 1]} 元：{counts[i]} 人")
