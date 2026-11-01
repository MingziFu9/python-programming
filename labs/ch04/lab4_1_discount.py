# 实验 4-1 满减与会员折扣计算
# 规则：消费满 100 元减 15 元；会员在满减之后再打 9.5 折

total = float(input("商品合计（元）："))
is_member = input("是否会员（y/n）：").strip().lower()

pay = total                      # 先假设没有任何优惠
if total >= 100:                 # 规则一：满 100 减 15
    pay = pay - 15
    print("已满 100 元，减 15 元")
else:
    print(f"还差 {100 - total:.2f} 元可享满减")

if is_member == "y":             # 规则二：会员 9.5 折
    pay = pay * 0.95
    print("会员 9.5 折")

print(f"原价 {total:.2f} 元，实付 {pay:.2f} 元，共优惠 {total - pay:.2f} 元")
