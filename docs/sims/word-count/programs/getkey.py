prices = {"可乐": 3.5, "面包": 5.5}
print(prices["可乐"])
print(prices.get("雪碧", 0))
prices["牛奶"] = 4.5
prices["可乐"] = 3.8
print(prices)
print(prices["雪碧"])
