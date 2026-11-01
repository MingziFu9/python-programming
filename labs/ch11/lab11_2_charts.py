# 实验 11-2 画月度销售折线图和品类柱状图
import pandas as pd
import matplotlib.pyplot as plt

# 设置中文字体：按顺序找，找到哪个用哪个（Windows 一般有微软雅黑和黑体）
plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei", "PingFang SC", "WenQuanYi Zen Hei"]
plt.rcParams["axes.unicode_minus"] = False      # 让负号正常显示

df = pd.read_csv("../data/sales_2025.csv")
df["月份"] = df["日期"].str[5:7].astype(int)     # "2025-03-08" 取出 "03"，转成整数 3

# 图 1：月度营业额折线图
monthly = df.groupby("月份")["金额"].sum()
print(monthly.round(1).to_dict())
plt.figure(figsize=(7, 4))
plt.plot(monthly.index, monthly.values, marker="o")
plt.title("2025 年各月营业额")
plt.xlabel("月份")
plt.ylabel("营业额（元）")
plt.xticks(range(1, 13))
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("月度营业额.png", dpi=120)
plt.show()

# 图 2：各品类销售额柱状图（从高到低）
cat = df.groupby("品类")["金额"].sum().sort_values(ascending=False)
print(cat.round(1).to_dict())
plt.figure(figsize=(7, 4))
plt.bar(cat.index, cat.values, color="#3f51b5")
for x, y in zip(cat.index, cat.values):          # 在柱子上方标出数值
    plt.text(x, y, f"{y:.0f}", ha="center", va="bottom")
plt.title("2025 年各品类销售额")
plt.ylabel("销售额（元）")
plt.tight_layout()
plt.savefig("品类销售额.png", dpi=120)
plt.show()
