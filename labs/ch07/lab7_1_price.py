# 实验 7-1 商品价格表与收银
# 价格表是一个字典：键是商品名，值是售价（参考 labs/data/products.csv，名称做了简写）
prices = {
    "矿泉水": 2.0, "可乐": 3.5, "绿茶": 3.5, "鲜牛奶": 4.5, "酸奶": 6.0,
    "方便面": 4.5, "薯片": 7.5, "饼干": 6.0, "巧克力": 10.0, "鸡蛋": 12.0,
}
print("今日商品：", "、".join(prices.keys()))

cart = {}                                   # 购物车也是字典：商品名 -> 数量
while True:
    name = input("商品名（直接回车结账）：").strip()
    if name == "":
        break
    if name not in prices:                  # 先判断有没有这个键
        print("没有这个商品，请重新输入")
        continue
    qty = int(input("数量："))
    cart[name] = cart.get(name, 0) + qty    # 已经买过就累加数量
    print(f"{name} 单价 {prices[name]:.2f} 元，购物车里共 {cart[name]} 件")

print("\n------ 小票 ------")
total = 0
for name, qty in cart.items():              # 同时取出键和值
    money = prices[name] * qty
    total += money
    print(f"{name:<5}{qty:>3} 件 {money:>7.2f} 元")
print(f"合计 {total:.2f} 元")

# 调价：鸡蛋涨到 12.5 元；新增商品：面包
prices["鸡蛋"] = 12.5
prices["面包"] = 5.5
print("调价后鸡蛋", prices["鸡蛋"], "元；商品种数", len(prices))
