# 实验 9-2 让收银程序不怕输错


def input_number(prompt, kind=float):
    """反复输入，直到输入一个大于 0 的数为止，返回这个数。kind 可以是 float 或 int。"""
    while True:
        text = input(prompt)
        try:
            value = kind(text)            # 转换失败会抛出 ValueError
        except ValueError:
            print(f"  “{text}”不是有效的数字，请重新输入")
            continue
        if value <= 0:
            print("  必须大于 0，请重新输入")
            continue
        return value


total = 0
items = 0
while True:
    name = input("商品名（直接回车结账）：").strip()
    if name == "":
        break
    price = input_number("单价：")
    qty = input_number("数量：", int)
    total += price * qty
    items += 1

try:
    avg = total / items                   # 一件商品都没有时，items 是 0
    print(f"共 {items} 种商品，合计 {total:.2f} 元，平均每种 {avg:.2f} 元")
except ZeroDivisionError:
    print("购物车是空的，没有需要结账的商品")
finally:
    print("谢谢光临！")                   # 不管有没有出错，都会执行
