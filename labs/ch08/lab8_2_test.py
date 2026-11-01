# 实验 8-2 用 assert 自测工具函数库
from shop_tools import mask_phone, is_valid_phone, electricity_fee, stats

# assert 条件：条件成立就什么也不做；不成立就报 AssertionError，提醒“这里有错”
assert mask_phone("13800138000") == "138****8000"
assert mask_phone(" 138 0013-8000 ") == "138****8000"
print("mask_phone 通过")

assert is_valid_phone("13800138000") == True
assert is_valid_phone("1380013800") == False        # 少一位
assert is_valid_phone("138O0138000") == False       # 字母 O
print("is_valid_phone 通过")

assert electricity_fee(150) == 88.5
assert electricity_fee(200) == 118.0                 # 边界值
assert electricity_fee(350) == 214.0
assert electricity_fee(520) == 352.8
print("electricity_fee 通过")

total, avg, high, low = stats([1280, 1150.5, 1320])
assert total == 3750.5 and high == 1320 and low == 1150.5
print("stats 通过：", total, avg, high, low)

print("全部测试通过！")
