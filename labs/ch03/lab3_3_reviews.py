# 实验 3-3 商品评价文本统计与敏感词替换
# 从小店的线上评价里抄了一段，统计字数、关键词出现次数，并把不文明用语换成星号

reviews = """老板很热情，东西很新鲜。
价格实惠，离家近很方便，就是排队太久，真烦人！
早餐好吃，包子很香，肠粉味道不错。
有时候缺货，晚上没有面包了，烦死了。
店里很干净，找零很快，老板人很好。"""

print("评价全文共", len(reviews), "个字符（含标点和换行）")
print("其中换行符有", reviews.count("\n"), "个，所以一共", reviews.count("\n") + 1, "条评价")
print("“老板”出现了", reviews.count("老板"), "次")
print("“很”出现了", reviews.count("很"), "次")
print("第一次提到“排队”的位置（索引）：", reviews.find("排队"))
print("有没有提到“价格”：", "价格" in reviews)
print("有没有提到“送货”：", "送货" in reviews)

clean = reviews.replace("真烦人", "***").replace("烦死了", "***")   # 不文明用语换成星号
print()
print("替换后的评价：")
print(clean)

first = reviews.split("\n")[0]          # 按换行符拆开，取第一条
print()
print("第一条评价：", first)
print("第一条评价按逗号拆开：", first.split("，"))
print("用“ | ”重新连起来：", " | ".join(first.split("，")))
