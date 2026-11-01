# 实验 8-3 按销量、价格给商品排序
# 每种商品是一个字典（数据为虚构）
goods = [
    {"名称": "矿泉水", "售价": 2.0, "销量": 412},
    {"名称": "可乐", "售价": 3.5, "销量": 365},
    {"名称": "鲜牛奶", "售价": 4.5, "销量": 298},
    {"名称": "薯片", "售价": 7.5, "销量": 156},
    {"名称": "鸡蛋", "售价": 12.5, "销量": 203},
    {"名称": "坚果礼包", "售价": 39.9, "销量": 37},
]


def show(title, items):
    print(title)
    for g in items:
        print(f"  {g['名称']:<5}{g['售价']:>6.2f} 元  销量 {g['销量']:>3}  销售额 {g['售价'] * g['销量']:>8.2f}")


# 写法一：先写一个普通函数，告诉 sorted 按什么排
def by_sales(g):
    return g["销量"]


show("按销量从高到低：", sorted(goods, key=by_sales, reverse=True))

# 写法二：用 lambda 写一个没有名字的小函数，效果一样
show("按售价从低到高：", sorted(goods, key=lambda g: g["售价"]))

# 按销售额（售价 × 销量）排序，取前 3 名
top3 = sorted(goods, key=lambda g: g["售价"] * g["销量"], reverse=True)[:3]
print("销售额前三：", [g["名称"] for g in top3])
