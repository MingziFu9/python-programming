# 实验 3-2 从身份证号中取出出生日期
# 注意：只用虚构号码练习，不要输入真实的身份证号！
# 18 位身份证号：第 1-6 位是地区码，第 7-14 位是出生日期，第 15-17 位是顺序码（第 17 位奇数为男、偶数为女），第 18 位是校验码

id_no = input("请输入 18 位身份证号（虚构）：").strip().upper()   # 末位的 x 统一转成大写 X

area = id_no[:6]
year = id_no[6:10]
month = id_no[10:12]
day = id_no[12:14]
seq = id_no[14:17]
gender_digit = int(id_no[16])            # 第 17 位，索引是 16

print("号码长度：", len(id_no))
print("地区码：", area)
print(f"出生日期：{year} 年 {month} 月 {day} 日")
print(f"出生日期（另一种格式）：{year}-{month}-{day}")
print("顺序码：", seq)
print(f"第 17 位是 {gender_digit}，除以 2 的余数是 {gender_digit % 2}（余 1 为男，余 0 为女）")
print("校验码：", id_no[-1])
print("脱敏显示：", id_no[:3] + "*" * 11 + id_no[-4:])
