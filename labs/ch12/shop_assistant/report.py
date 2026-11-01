# report.py 经营小结模块（组员 C 负责）：调用大模型接口，失败时给出提示
import os
import requests

BASE_URL = os.environ.get("LLM_BASE_URL", "http://127.0.0.1:8000")
API_KEY = os.environ.get("LLM_API_KEY", "test-key")
MODEL = os.environ.get("LLM_MODEL", "mock-model")


def ask_llm(prompt):
    """把 prompt 发给大模型，成功返回回复文字，失败返回以“出错：”开头的说明"""
    headers = {"Authorization": "Bearer " + API_KEY}
    data = {"model": MODEL, "messages": [{"role": "user", "content": prompt}]}
    try:
        resp = requests.post(BASE_URL + "/chat/completions", headers=headers, json=data, timeout=60)
    except requests.exceptions.RequestException:
        return "出错：连接不上大模型服务，请检查服务器或网络"
    if resp.status_code != 200:
        return f"出错：状态码 {resp.status_code}"
    return resp.json()["choices"][0]["message"]["content"]


def weekly_report(facts, complaint):
    prompt = ("你是一家社区便利店的经营助理。请根据下面的数据，用不超过 150 字写本周经营小结，"
              "分“总体情况、亮点、建议”三点：\n" + facts + "\n顾客意见：" + complaint)
    return ask_llm(prompt)


if __name__ == "__main__":
    print(ask_llm("营业额：100 元"))
