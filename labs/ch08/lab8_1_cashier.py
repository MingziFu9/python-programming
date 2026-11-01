# 实验 8-1 把收银程序改写成函数
# 规则（同实验 4-1）：满 100 减 15；会员在满减之后再打 9.5 折

def discount(total, is_member=False):
    """根据合计金额和是否会员，返回实付金额（保留两位小数）。"""
    pay = total
    if total >= 100:
        pay = pay - 15
    if is_member:
        pay = pay * 0.95
    return round(pay, 2)


def print_receipt(total, pay):
    """打印小票的最后两行。"""
    print(f"原价 {total:.2f} 元，实付 {pay:.2f} 元，优惠 {total - pay:.2f} 元")


# 主程序：一段一段调用函数
pay1 = discount(128, True)
print_receipt(128, pay1)

pay2 = discount(86)                    # 不是会员，用默认值 False
print_receipt(86, pay2)

pay3 = discount(total=260, is_member=True)    # 关键字参数，意思更清楚
print_receipt(260, pay3)

# 规则改了，只需要改 discount 一处；所有用到它的地方都跟着变
print("三位顾客一共付了", round(pay1 + pay2 + pay3, 2), "元")
