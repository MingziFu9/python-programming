# 模拟大模型服务器：在自己电脑上假装是一个大模型接口，供实验 12-2 离线练习
# 运行：python mock_llm_server.py，看到“模拟服务器已启动”后不要关闭这个窗口
# 注意：它不会真正“思考”，只是按固定模板回复，但请求和回复的格式与真实接口相同
import json
import time
from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = 8000


class Handler(BaseHTTPRequestHandler):
    def send_json(self, code, data):
        body = json.dumps(data, ensure_ascii=False).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_POST(self):
        if self.path.rstrip("/") not in ("/chat/completions", "/v1/chat/completions"):
            self.send_json(404, {"error": {"message": "地址不存在：" + self.path, "type": "not_found"}})
            return
        # 1. 检查 API Key：请求头里要有 Authorization: Bearer 密钥
        auth = self.headers.get("Authorization", "")
        if not auth.startswith("Bearer ") or len(auth) <= len("Bearer "):
            self.send_json(401, {"error": {"message": "缺少或错误的 API Key", "type": "authentication_error"}})
            return
        # 2. 读取请求体中的 JSON
        length = int(self.headers.get("Content-Length", 0))
        try:
            req = json.loads(self.rfile.read(length).decode("utf-8"))
            question = req["messages"][-1]["content"]
        except (ValueError, KeyError, IndexError):
            self.send_json(400, {"error": {"message": "请求格式不正确，需要 model 和 messages", "type": "invalid_request_error"}})
            return
        # 3. 按模板生成回复（真实的大模型会根据问题“写”出内容）
        # 只挑出“营业额：2446.9 元”这样冒号前面很短的行，当作数据
        lines = [l.strip() for l in question.splitlines() if 0 < l.find("：") <= 8]
        facts = "；".join(lines) if lines else "未提供数据"
        answer = ("【本周经营小结】\n"
                  "1. 总体情况：" + facts + "。\n"
                  "2. 亮点：销售额最高的商品可以继续保证货源，周末客流大，可提前备货。\n"
                  "3. 建议：针对顾客反映的问题（如排队）安排高峰时段加开收银。\n"
                  "（以上内容由模拟服务器按模板生成，仅用于练习。）")
        self.send_json(200, {
            "id": "chatcmpl-mock-" + str(int(time.time())),
            "object": "chat.completion",
            "created": int(time.time()),
            "model": req.get("model", "mock-model"),
            "choices": [{"index": 0,
                         "message": {"role": "assistant", "content": answer},
                         "finish_reason": "stop"}],
            "usage": {"prompt_tokens": len(question), "completion_tokens": len(answer),
                      "total_tokens": len(question) + len(answer)},
        })

    def log_message(self, fmt, *args):          # 在窗口里简单记录每个请求
        print("收到请求：", self.command, self.path, "→", args[1])


if __name__ == "__main__":
    print(f"模拟服务器已启动：http://127.0.0.1:{PORT}  （按 Ctrl+C 停止）")
    HTTPServer(("127.0.0.1", PORT), Handler).serve_forever()
