# 实验 3-1 会员信息整理与手机号脱敏
# 店员登记会员时，姓名前后常多打空格，手机号里夹着空格或横线。
# 本程序把输入整理干净，再把手机号中间四位换成星号，用于小票上显示。

name = input("会员姓名：")
phone = input("手机号：")

name = name.strip()                          # 去掉姓名前后的空格
phone = phone.strip()                        # 去掉手机号前后的空格
phone = phone.replace(" ", "").replace("-", "")   # 去掉中间的空格和横线

print("整理后的姓名：", name)
print("整理后的手机号：", phone)
print("手机号位数：", len(phone))
print("是否全是数字：", phone.isdigit())
print("是否以 1 开头：", phone.startswith("1"))

masked = phone[:3] + "****" + phone[-4:]     # 前 3 位 + 4 个星号 + 后 4 位
print("小票上显示：", masked)
print(f"会员 {name[0]}**，手机 {masked}，欢迎光临！")   # 姓名只显示第一个字
