# 实验 5-1 九九乘法表与一周对账汇总

# 第一部分：九九乘法表（嵌套循环）
for i in range(1, 10):              # 外层循环：第 i 行
    for j in range(1, i + 1):       # 内层循环：第 i 行有 i 个算式
        print(f"{j}×{i}={i * j:<3}", end="")   # end="" 表示不换行
    print()                         # 一行结束，换行

print()

# 第二部分：一周对账汇总
# 依次输入周一到周日的营业额，算出合计、日均和最高的一天
days = "一二三四五六日"
total = 0
best_day = ""
best_money = 0
for d in days:                      # 字符串也可以逐个字符循环
    money = float(input(f"周{d}营业额（元）："))
    total = total + money           # 套路一：累加
    if money > best_money:          # 套路三：找最大值
        best_money = money
        best_day = d

print(f"本周合计 {total:.2f} 元，日均 {total / 7:.2f} 元")
print(f"营业额最高的是周{best_day}，{best_money:.2f} 元")
