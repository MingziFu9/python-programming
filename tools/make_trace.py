"""把一段 Python 代码一行一行地执行，记录每一步的状态，生成交互动画用的 JSON。

用法：python tools/make_trace.py 代码文件.py [输入1 输入2 ...] > trace.json
每一步记录：即将执行的行号 line、调用栈 frames（每层的函数名和变量）、到目前为止的输出 out。
动画里显示的数字全部来自真实运行，不手写。
"""
import io
import json
import sys


def short(v):
    if isinstance(v, (int, float, bool, type(None))):
        return repr(v)
    if isinstance(v, str):
        return repr(v)
    if isinstance(v, (list, tuple, dict, set)):
        r = repr(v)
        return r if len(r) <= 60 else r[:57] + "..."
    if callable(v):
        return "函数 " + getattr(v, "__name__", "?")
    return repr(v)[:60]


def main():
    path = sys.argv[1]
    inputs = list(sys.argv[2:])
    code = open(path, encoding="utf-8").read()
    out = io.StringIO()
    steps = []
    real_stdout = sys.stdout

    def fake_input(prompt=""):
        v = inputs.pop(0) if inputs else ""
        out.write(str(prompt) + v + "\n")
        return v

    def snap(frame):
        frames = []
        f = frame
        while f is not None and f.f_code.co_filename == "<trace>":
            loc = f.f_locals if f.f_code.co_name != "<module>" else f.f_globals
            vs = {k: short(v) for k, v in loc.items()
                  if not k.startswith("__") and k not in ("input",) and not isinstance(v, type(sys))}
            frames.append({"name": "全局" if f.f_code.co_name == "<module>" else f.f_code.co_name + "()", "vars": vs})
            f = f.f_back
        return list(reversed(frames))

    def tracer(frame, event, arg):
        if frame.f_code.co_filename != "<trace>":
            return None
        if event == "line":
            steps.append({"line": frame.f_lineno, "frames": snap(frame), "out": out.getvalue()})
        elif event == "return" and frame.f_code.co_name != "<module>":
            steps.append({"line": frame.f_lineno, "frames": snap(frame), "out": out.getvalue(),
                          "ret": short(arg)})
        return tracer

    g = {"__name__": "__main__", "input": fake_input}
    sys.stdout = out
    sys.settrace(tracer)
    err = None
    try:
        exec(compile(code, "<trace>", "exec"), g)
    except Exception as e:  # noqa: BLE001
        err = f"{type(e).__name__}: {e}"
    finally:
        sys.settrace(None)
        sys.stdout = real_stdout
    final = {"line": None, "frames": [{"name": "全局", "vars": {k: short(v) for k, v in g.items()
                                                              if not k.startswith("__") and k != "input"}}],
             "out": out.getvalue()}
    if err:
        final["error"] = err
    steps.append(final)
    json.dump({"code": code.rstrip("\n").split("\n"), "steps": steps}, real_stdout, ensure_ascii=False)


if __name__ == "__main__":
    main()
