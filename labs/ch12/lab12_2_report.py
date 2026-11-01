# 实验 12-2 让大模型根据一周销售数据写经营小结
# 需要先安装：pip install pandas requests
# 默认连接本机的模拟服务器（先运行 mock_llm_server.py）；换成真实大模型的方法见教材 12.3 节
import os
import pandas as pd
import requests

# ---------- 第一步：用 pandas 算出一周的数据 ----------
df = pd.read_csv("../data/sales_2025.csv")
week = df[(df["日期"] >= "2025-12-22") & (df["日期"] <= "2025-12-28")]
total = week["金额"].sum()
orders = week["单号"].nunique()
top3 = week.groupby("商品名称")["金额"].sum().sort_values(ascending=False).head(3)
by_day = week.groupby("日期")["金额"].sum()

facts = (f"统计时间：2025-12-22 至 2025-12-28\n"
         f"营业额：{total:.1f} 元\n"
         f"订单数：{orders} 单\n"
         f"销售额前三：{'、'.join(f'{k}{v:.0f}元' for k, v in top3.items())}\n"
         f"营业额最高的一天：{by_day.idxmax()}（{by_day.max():.1f} 元）\n"
         f"顾客意见：排队太久（8 条评价提到）")
print(facts)

# ---------- 第二步：组装请求 ----------
BASE_URL = os.environ.get("LLM_BASE_URL", "http://127.0.0.1:8000")   # 接口地址
API_KEY = os.environ.get("LLM_API_KEY", "test-key")                  # 密钥：从环境变量读，不写在代码里
MODEL = os.environ.get("LLM_MODEL", "mock-model")                    # 模型名称

prompt = ("你是一家社区便利店的经营助理。请根据下面的数据，用不超过 150 字写一段本周经营小结，"
          "分“总体情况、亮点、建议”三点：\n" + facts)
headers = {"Authorization": "Bearer " + API_KEY, "Content-Type": "application/json"}
data = {"model": MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7}

# ---------- 第三步：发送请求，取出回复 ----------
try:
    resp = requests.post(BASE_URL + "/chat/completions", headers=headers, json=data, timeout=60)
except requests.exceptions.ConnectionError:
    print("连接失败：请检查模拟服务器是否已启动，或网络、地址是否正确")
else:
    if resp.status_code == 200:
        result = resp.json()                                   # 把回复的 JSON 变成字典
        answer = result["choices"][0]["message"]["content"]   # 一层层取出回复内容
        print("\n" + answer)
        print("\n本次用量：", result["usage"]["total_tokens"], "个 token")
        with open("本周经营小结.txt", "w", encoding="utf-8") as f:
            f.write(answer + "\n\n（本内容由人工智能生成，请人工核对后使用）\n")
        print("已保存到 本周经营小结.txt")
    else:
        print("请求失败，状态码", resp.status_code, "：", resp.json()["error"]["message"])
