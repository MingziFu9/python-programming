# 实验 1-2 打印小店开业海报和个人名片
# 第一部分：用 print 打印一张开业海报
print("=" * 30)
print("      街坊便利店  开业大吉")
print("=" * 30)
print("营业时间：每天 7:00 - 23:00")
print("开业三天：全场饮料 9 折")
print("地址：幸福路 18 号（地铁站 B 出口）")
print("=" * 30)
print()                          # 空一行

# 第二部分：用 input 问几个问题，再把答案打印成一张名片
name = input("请输入你的名字：")
job = input("请输入你的职务：")
phone = input("请输入你的联系电话：")

print()
print("+" + "-" * 28 + "+")
print("  姓名：" + name)
print("  职务：" + job)
print("  电话：" + phone)
print("  街坊便利店 · 欢迎光临")
print("+" + "-" * 28 + "+")
