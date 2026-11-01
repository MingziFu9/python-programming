# 实验 2-3 分期付款月供计算（等额本息）
# 陈姐想分期买一台 12000 元的冷柜，算算每个月要还多少钱
# 等额本息月供公式：月供 = 本金 × 月利率 × (1 + 月利率)^期数 ÷ ((1 + 月利率)^期数 - 1)

principal = float(input("贷款金额（元）："))
year_rate = float(input("年利率（%，例如 6）："))
months = int(input("分几期（月）："))

r = year_rate / 100 / 12                  # 年利率换算成月利率（小数）
monthly = principal * r * (1 + r) ** months / ((1 + r) ** months - 1)
total = monthly * months                  # 一共要还多少
interest = total - principal              # 其中利息多少

print(f"每月还款：{monthly:,.2f} 元")
print(f"总共还款：{total:,.2f} 元")
print(f"其中利息：{interest:,.2f} 元")
print(f"利息占本金的 {interest / principal:.1%}")
