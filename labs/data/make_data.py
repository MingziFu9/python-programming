"""生成“街坊便利店”的虚构数据（全书实验共用）。

用法：在 labs/data 目录下运行  python make_data.py
所有数据由随机数生成（随机种子固定为 42），人名、手机号都是虚构的，不对应任何真实的人。
生成的文件：
    products.csv      30 种商品：编号、名称、品类、进价、售价、库存
    sales_2025.csv    2025 年全年的销售明细，每行是一件商品的一次购买
    members.csv       60 位会员：会员号、姓名、手机号、注册日期、积分
    reviews.txt       80 条顾客评价，每行一条
"""
import csv
import random
from datetime import date, timedelta

random.seed(42)

PRODUCTS = [
    ("P01", "矿泉水550ml", "饮料", 0.9, 2.0), ("P02", "可乐330ml", "饮料", 1.8, 3.5),
    ("P03", "绿茶500ml", "饮料", 2.0, 3.5), ("P04", "鲜牛奶250ml", "饮料", 2.6, 4.5),
    ("P05", "酸奶200g", "饮料", 3.2, 6.0), ("P06", "豆浆粉", "饮料", 9.0, 15.8),
    ("P07", "方便面", "零食", 2.8, 4.5), ("P08", "薯片", "零食", 4.2, 7.5),
    ("P09", "饼干", "零食", 3.5, 6.0), ("P10", "巧克力", "零食", 6.0, 10.0),
    ("P11", "坚果礼包", "零食", 25.0, 39.9), ("P12", "辣条", "零食", 1.2, 2.5),
    ("P13", "面包", "早餐", 3.0, 5.5), ("P14", "包子(2个)", "早餐", 2.2, 4.0),
    ("P15", "茶叶蛋", "早餐", 0.8, 1.5), ("P16", "肠粉", "早餐", 3.5, 7.0),
    ("P17", "大米5kg", "粮油", 22.0, 32.8), ("P18", "花生油1.8L", "粮油", 28.0, 39.9),
    ("P19", "鸡蛋(10个)", "粮油", 8.0, 12.5), ("P20", "挂面", "粮油", 3.6, 6.5),
    ("P21", "生抽500ml", "粮油", 6.5, 10.9), ("P22", "纸巾(10包)", "日用", 9.0, 15.9),
    ("P23", "洗洁精", "日用", 5.5, 9.9), ("P24", "牙膏", "日用", 6.8, 12.9),
    ("P25", "洗衣液2kg", "日用", 18.0, 29.9), ("P26", "垃圾袋", "日用", 3.0, 5.9),
    ("P27", "雨伞", "日用", 12.0, 25.0), ("P28", "电池(4节)", "日用", 6.0, 11.0),
    ("P29", "冰淇淋", "冷饮", 2.5, 5.0), ("P30", "雪糕", "冷饮", 1.5, 3.0),
]
# 各品类每单被买到的权重；冷饮夏天多、雨伞雨季多
WEIGHT = {"饮料": 30, "零食": 22, "早餐": 18, "粮油": 10, "日用": 12, "冷饮": 8}
SURNAMES = "陈李张黄王刘林吴何郑梁谢罗周叶许"
GIVEN = ["伟", "芳", "敏", "静", "丽", "强", "磊", "洋", "艳", "勇", "军", "杰", "娟", "涛", "明", "超", "霞", "平", "刚", "桂英"]
REVIEW_GOOD = ["老板很热情", "东西很新鲜", "价格实惠", "离家近很方便", "早餐好吃", "牛奶每天都有新货",
               "店里很干净", "找零很快", "肠粉味道不错", "营业时间长很方便", "会员积分很划算", "包子很香"]
REVIEW_BAD = ["排队太久", "有时候缺货", "价格有点贵", "店里有点挤", "冷饮不够冰", "晚上没有面包了"]


def write_csv(name, header, rows):
    with open(name, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(rows)


def main():
    stock = [random.randint(10, 120) for _ in PRODUCTS]
    write_csv("products.csv", ["编号", "名称", "品类", "进价", "售价", "库存"],
              [(*p, s) for p, s in zip(PRODUCTS, stock)])

    members = []
    for i in range(1, 61):
        name = random.choice(SURNAMES) + random.choice(GIVEN)
        phone = "1" + random.choice("3589") + "".join(random.choice("0123456789") for _ in range(9))
        reg = date(2023, 1, 1) + timedelta(days=random.randint(0, 700))
        members.append((f"M{i:03d}", name, phone, reg.isoformat(), 0))

    rows, order_no = [], 0
    day = date(2025, 1, 1)
    while day.year == 2025:
        weekend = day.weekday() >= 5
        n_orders = random.randint(10, 16) + (3 if weekend else 0)
        if day.month == 2 and day.day <= 10:          # 春节前后人少
            n_orders -= 5
        for _ in range(n_orders):
            order_no += 1
            hour = random.choice([7, 7, 8, 8, 8, 9, 11, 12, 12, 13, 17, 18, 18, 19, 19, 20, 21, 22])
            t = f"{hour:02d}:{random.randint(0, 59):02d}"
            member = random.choice(members)[0] if random.random() < 0.35 else ""
            pay = random.choices(["微信", "支付宝", "现金"], [55, 35, 10])[0]
            for _ in range(random.choice([1, 1, 1, 2, 2, 3])):
                w = []
                for p in PRODUCTS:
                    x = WEIGHT[p[2]] / sum(1 for q in PRODUCTS if q[2] == p[2])
                    if p[2] == "冷饮":
                        x *= 3 if day.month in (6, 7, 8, 9) else 0.3
                    if p[2] == "早餐" and hour > 10:
                        x *= 0.1
                    if p[0] == "P27":
                        x *= 4 if day.month in (5, 6) else 0.5
                    w.append(x)
                p = random.choices(PRODUCTS, w)[0]
                qty = random.choices([1, 2, 3, 4], [70, 20, 7, 3])[0]
                rows.append((day.isoformat(), t, f"D{order_no:05d}", p[0], p[1], p[2], p[4], qty,
                             round(p[4] * qty, 2), member, pay))
        day += timedelta(days=1)
    write_csv("sales_2025.csv", ["日期", "时间", "单号", "商品编号", "商品名称", "品类", "单价", "数量", "金额",
                                 "会员号", "支付方式"], rows)

    points = {}
    for r in rows:
        if r[9]:
            points[r[9]] = points.get(r[9], 0) + int(r[8])
    members = [(m[0], m[1], m[2], m[3], points.get(m[0], 0)) for m in members]
    write_csv("members.csv", ["会员号", "姓名", "手机号", "注册日期", "积分"], members)

    with open("reviews.txt", "w", encoding="utf-8") as f:
        for _ in range(80):
            k = random.choice([1, 1, 2])
            parts = random.sample(REVIEW_GOOD, k)
            if random.random() < 0.35:
                parts.append(random.choice(REVIEW_BAD))
            f.write("，".join(parts) + "。\n")
    print("商品", len(PRODUCTS), "种；会员", len(members), "位；销售明细", len(rows), "行；订单", order_no, "单")


if __name__ == "__main__":
    main()
