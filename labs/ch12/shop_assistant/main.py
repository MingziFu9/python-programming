# main.py 街坊便利店管理助手 主程序（组长负责，把各组员的模块组合起来）
# 运行前：在 shop_assistant 文件夹中运行本文件；使用功能 4 前先启动 ../mock_llm_server.py
import sales
import reviews
import report

REVIEWS = "../../data/reviews.txt"
MENU = """
===== 街坊便利店管理助手 =====
1. 查询某天的销售情况
2. 查看各月营业额
3. 顾客评价关键词
4. 生成本周经营小结（大模型）
0. 退出"""


def main():
    df = sales.load()
    while True:
        print(MENU)
        choice = input("请选择：").strip()
        if choice == "1":
            day = input("日期（如 2025-03-08）：").strip()
            r = sales.day_summary(df, day)
            if r is None:
                print("这一天没有销售记录，请检查日期格式")
            else:
                print(f"{day} 营业额 {r[0]} 元，{r[1]} 单，卖得最好的是 {r[2]}")
        elif choice == "2":
            for m, money in sales.monthly(df).items():
                print(f"{m:>2} 月 {money:>9.1f} 元 " + "■" * int(money // 1000))
        elif choice == "3":
            for w, n in reviews.top_words(REVIEWS):
                print(f"  {w}：{n} 次")
        elif choice == "4":
            facts = sales.week_facts(df, "2025-12-22", "2025-12-28")
            n = reviews.count_keyword(REVIEWS, "排队")
            text = report.weekly_report(facts, f"有 {n} 条评价提到排队太久")
            print(text)
            if not text.startswith("出错"):
                with open("本周经营小结.txt", "w", encoding="utf-8") as f:
                    f.write(text + "\n\n（本内容由人工智能生成，请人工核对后使用）\n")
                print("已保存到 本周经营小结.txt")
        elif choice == "0":
            print("再见！")
            break
        else:
            print("没有这个选项，请输入 0～4")


if __name__ == "__main__":
    main()
