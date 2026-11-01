"""街坊便利店的工具函数库（实验 8-2）。

把常用的小功能写成函数，放在一个文件里，别的程序可以导入使用（第 10 章详细讲）。
"""


def mask_phone(phone):
    """手机号脱敏：保留前 3 位和后 4 位，中间换成 4 个星号。"""
    phone = phone.strip().replace(" ", "").replace("-", "")
    return phone[:3] + "****" + phone[-4:]


def is_valid_phone(phone):
    """检查手机号：11 位、全是数字、以 1 开头，返回 True 或 False。"""
    return len(phone) == 11 and phone.isdigit() and phone.startswith("1")


def electricity_fee(kwh):
    """阶梯电费（教学用简化电价，同实验 4-2）。"""
    if kwh <= 200:
        fee = kwh * 0.59
    elif kwh <= 400:
        fee = 200 * 0.59 + (kwh - 200) * 0.64
    else:
        fee = 200 * 0.59 + 200 * 0.64 + (kwh - 400) * 0.89
    return round(fee, 2)


def stats(numbers):
    """返回一组数的合计、平均值、最大值、最小值（四个值一起返回）。"""
    total = sum(numbers)
    return total, round(total / len(numbers), 2), max(numbers), min(numbers)
