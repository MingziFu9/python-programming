# 实验 6-2 购物车菜单程序
# 商品表是一个二维列表：每一行是 [商品名, 单价]
goods = [
    ["可乐", 3.5],
    ["面包", 6.8],
    ["牛奶", 4.5],
    ["鸡蛋", 12.0],
    ["矿泉水", 2.0],
]
cart = []          # 购物车：每一项是 [商品名, 单价, 数量]

while True:
    print("\n===== 街坊便利店 =====")
    print("1 看商品  2 加入购物车  3 删除商品  4 查看购物车并结账  0 退出")
    choice = input("请选择：").strip()

    if choice == "1":
        for i, g in enumerate(goods, start=1):       # enumerate 同时给出序号和元素
            print(f"{i}. {g[0]}  {g[1]:.2f} 元")
    elif choice == "2":
        no = input("商品序号：").strip()
        qty = input("数量：").strip()
        if no.isdigit() and qty.isdigit() and 1 <= int(no) <= len(goods):
            name, price = goods[int(no) - 1]          # 解包：一行取出两个值
            cart.append([name, price, int(qty)])
            print(f"已加入：{name} × {qty}")
        else:
            print("输入有误")
    elif choice == "3":
        if len(cart) == 0:
            print("购物车是空的")
        else:
            for i, item in enumerate(cart, start=1):
                print(f"{i}. {item[0]} × {item[2]}")
            no = input("删除第几项：").strip()
            if no.isdigit() and 1 <= int(no) <= len(cart):
                removed = cart.pop(int(no) - 1)
                print("已删除：", removed[0])
            else:
                print("输入有误")
    elif choice == "4":
        total = 0
        for name, price, qty in cart:                 # 每一项直接解包成三个变量
            print(f"{name:<6}{price:>6.2f} × {qty} = {price * qty:>7.2f}")
            total += price * qty
        print(f"合计 {total:.2f} 元，共 {len(cart)} 项")
    elif choice == "0":
        print("再见！")
        break
    else:
        print("没有这个选项")
