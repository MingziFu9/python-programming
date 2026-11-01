# 实验 4-3 成绩等级评定（带输入检查）
# 90 分及以上：优秀；80～89：良好；70～79：中等；60～69：及格；60 以下：不及格

text = input("请输入成绩（0～100 的整数）：").strip()

if not text.isdigit():                 # 先检查：是不是全由数字组成
    print("输入有误：请输入整数，不要带小数点、字母或空格")
else:
    score = int(text)
    if score > 100:                    # 再检查：是否超出范围
        print("输入有误：成绩不能超过 100")
    elif score >= 90:
        print("等级：优秀")
    elif score >= 80:
        print("等级：良好")
    elif score >= 70:
        print("等级：中等")
    elif score >= 60:
        print("等级：及格")
    else:
        print("等级：不及格")
