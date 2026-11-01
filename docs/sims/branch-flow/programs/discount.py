total = float(input("合计："))
member = input("会员？(y/n)：")
pay = total
if total >= 100:
    pay = pay - 15
else:
    print("还差", 100 - total, "元满减")
if member == "y":
    pay = pay * 0.95
print("实付", round(pay, 2))
