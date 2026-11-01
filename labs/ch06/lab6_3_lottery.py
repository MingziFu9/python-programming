# 实验 6-3 会员抽奖程序
import random

# 用列表推导式生成 60 个会员编号 M001～M060（虚构）
members = [f"M{i:03d}" for i in range(1, 61)]
print("参加抽奖的会员共", len(members), "人，前 5 个是：", members[:5])

# 不在抽奖名单里的：本店员工的家属（虚构）
staff_family = ["M007", "M023"]
pool = [m for m in members if m not in staff_family]
print("去掉员工家属后剩", len(pool), "人")

# random.sample 一次抽出 k 个，不会重复
winners = random.sample(pool, 6)
prizes = ["一等奖：大米 10 斤", "二等奖：食用油一桶", "二等奖：食用油一桶",
          "三等奖：鸡蛋一盒", "三等奖：鸡蛋一盒", "三等奖：鸡蛋一盒"]
for i in range(len(winners)):
    print(winners[i], prizes[i])
