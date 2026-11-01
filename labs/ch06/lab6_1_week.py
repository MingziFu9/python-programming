# 实验 6-1 一周营业额统计
days = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
money = [1280, 1150.5, 1320, 1406, 1890, 2350.8, 2108]   # 虚构数据，单位：元

total = sum(money)
avg = total / len(money)
print(f"合计 {total:.2f} 元，日均 {avg:.2f} 元")

# 最高、最低是哪一天：先找出值，再用 index 找到它的位置
high = max(money)
low = min(money)
print(f"最高 {days[money.index(high)]} {high} 元，最低 {days[money.index(low)]} {low} 元")

# 高于平均值的有哪几天
above = []
for i in range(len(money)):
    if money[i] > avg:
        above.append(days[i])
print(f"高于平均的有 {len(above)} 天：{'、'.join(above)}")

# 排序：sorted 返回新列表，原列表不变
print("从高到低：", sorted(money, reverse=True))
print("原列表没变：", money)

# 周末（最后两天）占全周的比例：用切片取出
weekend = money[-2:]
print(f"周末营业额 {sum(weekend):.2f} 元，占 {sum(weekend) / total:.1%}")
