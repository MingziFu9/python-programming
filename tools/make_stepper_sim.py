"""根据 docs/sims/<名称>/spec.json 生成“代码单步执行”类动画的 main.html。

spec.json 格式：
{"title": "动画标题", "sub": "副标题（怎么操作）",
 "programs": [{"title": "标签名", "file": "programs/xxx.py", "inputs": ["小周"], "notes": {"1": "这一行……"}}],
 "after": "可选：放在执行器下面的 HTML"}
每个程序都用 tools/make_trace.py 真实运行一遍，动画里的变量和输出都来自真实运行结果。
用法：python tools/make_stepper_sim.py docs/sims/<名称>
"""
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

TEMPLATE = """<!doctype html>
<html lang="zh">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<link rel="stylesheet" href="../common/sim.css">
</head>
<body>
<h1>{title}</h1>
<div class="sub">{sub}</div>
<div id="stepper"></div>
{after}
<script src="../common/stepper.js"></script>
<script>
// 以下数据由 tools/make_stepper_sim.py 根据 spec.json 真实运行代码生成，请勿手改
var PROGRAMS = {programs};
Stepper(document.getElementById("stepper"), PROGRAMS);
</script>
<script src="../common/sim.js"></script>
</body>
</html>
"""


def main():
    d = Path(sys.argv[1])
    spec = json.loads((d / "spec.json").read_text(encoding="utf-8"))
    progs = []
    for p in spec["programs"]:
        r = subprocess.run([sys.executable, str(ROOT / "tools/make_trace.py"), str(d / p["file"]), *p.get("inputs", [])],
                           capture_output=True, text=True, check=True)
        progs.append({"title": p["title"], "trace": json.loads(r.stdout),
                      "notes": {int(k): v for k, v in p.get("notes", {}).items()}})
    html = TEMPLATE.format(title=spec["title"], sub=spec["sub"], after=spec.get("after", ""),
                           programs=json.dumps(progs, ensure_ascii=False))
    (d / "main.html").write_text(html, encoding="utf-8")
    print("已生成", d / "main.html", "：", ", ".join(f"{p['title']} {len(p['trace']['steps'])} 步" for p in progs))


if __name__ == "__main__":
    main()
