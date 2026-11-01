# 实验 2-2 单位换算与 BMI 计算
# 第一部分：斤和千克、华氏度和摄氏度的换算
jin = float(input("大米有多少斤？"))
kg = jin / 2                              # 1 千克 = 2 斤
print(f"{jin} 斤 = {kg} 千克")

f = float(input("进口冰淇淋包装上写的保存温度（华氏度）："))
c = (f - 32) * 5 / 9                      # 华氏度换算成摄氏度
print(f"{f} 华氏度 = {c:.1f} 摄氏度")

# 第二部分：BMI（身体质量指数）= 体重（千克）÷ 身高（米）的平方
height = float(input("身高（米，例如 1.70）："))
weight = float(input("体重（千克）："))
bmi = weight / height ** 2               # ** 是乘方，先算乘方再算除法
print(f"你的 BMI 是 {bmi:.1f}")
print("参考：我国成人 BMI 在 18.5～23.9 之间为正常")
