# 实验 2-1 小店收银小票计算器
# 输入单价、数量和顾客付的钱，算出应收金额和找零，打印一张小票

print("====== 街坊便利店 收银 ======")
name = input("商品名称：")
price = float(input("单价（元）："))      # input 拿到的是字符串，用 float 转成小数
qty = int(input("数量："))               # 数量是整数，用 int 转换
total = price * qty                      # 应收金额
paid = float(input("顾客付款（元）："))
change = paid - total                    # 找零

print()
print("---------- 小 票 ----------")
print(f"商品：{name}")
print(f"单价：{price:.2f} 元 × {qty}")
print(f"应收：{total:.2f} 元")
print(f"实收：{paid:.2f} 元")
print(f"找零：{change:.2f} 元")
print("----------------------------")
print("谢谢惠顾，欢迎再来！")
