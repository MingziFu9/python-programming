best = 0
count = 0
while count < 3:
    money = int(input("营业额："))
    if money > best:
        best = money
    count += 1
print("最高", best)
