# 实验 10-3 用类写“商品”和“购物车”


class Goods:
    """商品：有名称、单价、库存三个属性。"""

    def __init__(self, name, price, stock=0):
        self.name = name
        self.price = price
        self.stock = stock

    def sell(self, qty):
        """卖出 qty 件，库存不够时返回 False。"""
        if qty > self.stock:
            return False
        self.stock -= qty
        return True

    def info(self):
        return f"{self.name}（{self.price:.2f} 元，库存 {self.stock}）"


class Cart:
    """购物车：记录买了哪些商品、各几件。"""

    def __init__(self):
        self.items = []                      # 每一项是 (商品对象, 数量)

    def add(self, goods, qty=1):
        if goods.sell(qty):                  # 先从库存里扣
            self.items.append((goods, qty))
            print(f"加入 {goods.name} × {qty}")
        else:
            print(f"{goods.name} 库存不足，只剩 {goods.stock} 件")

    def total(self):
        return sum(g.price * q for g, q in self.items)


cola = Goods("可乐", 3.5, 24)                # 用类创建对象
egg = Goods("鸡蛋", 12.5, 2)
print(cola.info(), egg.info())

cart = Cart()
cart.add(cola, 6)
cart.add(egg, 3)                             # 库存只有 2，加不进去
cart.add(egg)                                # qty 默认 1
print(f"合计 {cart.total():.2f} 元")
print("结账后：", cola.info(), egg.info())
