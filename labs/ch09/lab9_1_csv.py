# 实验 9-1 把每日销售记录存入 CSV，再读回来统计
import csv

# 第一部分：把今天的几笔销售记录（二维列表）写入 today.csv
header = ["时间", "商品名称", "单价", "数量", "金额"]
rows = [
    ["08:05", "鲜牛奶", 4.5, 2, 9.0],
    ["08:12", "面包", 5.5, 1, 5.5],
    ["12:30", "方便面", 4.5, 3, 13.5],
    ["18:46", "可乐", 3.5, 6, 21.0],
]
# newline="" 防止 Windows 上多出空行；utf-8-sig 让 Excel 打开不乱码
with open("today.csv", "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.writer(f)
    writer.writerow(header)       # 写一行
    writer.writerows(rows)        # 写多行
print("已写入 today.csv，共", len(rows), "笔")

# 第二部分：读回 today.csv，算出今天的营业额
total = 0
with open("today.csv", encoding="utf-8-sig") as f:
    reader = csv.reader(f)
    next(reader)                  # 跳过表头
    for row in reader:            # 每一行是一个列表，里面全是字符串
        total += float(row[4])
print(f"今天营业额 {total:.2f} 元")

# 第三部分：读全年销售表（8437 行），按支付方式汇总金额
pay_sum = {}
with open("../data/sales_2025.csv", encoding="utf-8") as f:
    for r in csv.DictReader(f):   # 每一行是一个字典，键是表头
        way = r["支付方式"]
        pay_sum[way] = pay_sum.get(way, 0) + float(r["金额"])
for way, money in sorted(pay_sum.items(), key=lambda x: x[1], reverse=True):
    print(f"{way:<4}{money:>12,.2f} 元")
