score = int(input("成绩："))
if score >= 90:
    level = "优秀"
elif score >= 80:
    level = "良好"
elif score >= 70:
    level = "中等"
elif score >= 60:
    level = "及格"
else:
    level = "不及格"
print("等级：", level)
