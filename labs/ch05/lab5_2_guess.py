# 实验 5-2 猜数字游戏
import random

secret = random.randint(1, 100)     # 随机生成 1～100 之间的整数（含 1 和 100）
count = 0                           # 记录猜了几次

print("我想好了一个 1～100 之间的整数，你来猜！最多猜 7 次。")
while count < 7:
    text = input("你猜：").strip()
    if not text.isdigit():          # 输错不算次数，重新输
        print("请输入整数")
        continue
    guess = int(text)
    count += 1
    if guess > secret:
        print("大了")
    elif guess < secret:
        print("小了")
    else:
        print(f"猜对了！你用了 {count} 次")
        break
else:                               # while 正常结束（没有被 break）时执行
    print(f"7 次机会用完了，答案是 {secret}")
