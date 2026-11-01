# 实验 9-3 会员通讯录存成 JSON
import csv
import json

# 1. 从 members.csv 读出前 3 位会员，变成“字典的列表”
members = []
with open("../data/members.csv", encoding="utf-8") as f:
    for r in csv.DictReader(f):
        members.append({"会员号": r["会员号"], "姓名": r["姓名"],
                        "手机号": r["手机号"], "积分": int(r["积分"])})
        if len(members) == 3:
            break

# 2. 新增一位会员（虚构），并给他加一个“标签”列表
members.append({"会员号": "M061", "姓名": "林小满", "手机号": "13900002222",
                "积分": 0, "标签": ["新会员", "爱喝咖啡"]})

# 3. 保存为 JSON 文件：ensure_ascii=False 让中文原样保存，indent=2 让文件好读
with open("members.json", "w", encoding="utf-8") as f:
    json.dump(members, f, ensure_ascii=False, indent=2)
print("已保存", len(members), "位会员到 members.json")

# 4. 重新读回来，验证数据完整
with open("members.json", encoding="utf-8") as f:
    data = json.load(f)
print("读回的类型：", type(data), "，第一位会员的类型：", type(data[0]))
for m in data:
    print(m["会员号"], m["姓名"], m["积分"], m.get("标签", []))
