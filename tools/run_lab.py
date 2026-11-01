"""运行一个实验脚本，并把 input() 输入的内容像在 Thonny 里一样显示出来，用来生成教材里的“运行结果”。

用法：python tools/run_lab.py labs/ch02/lab2_1_receipt.py 3.5 2 50
在脚本所在的文件夹里运行（和学生在 Thonny 里打开文件后点“运行”一样）。
"""
import builtins
import os
import runpy
import sys

path = os.path.abspath(sys.argv[1])
answers = list(sys.argv[2:])


def fake_input(prompt=""):
    v = answers.pop(0) if answers else ""
    print(prompt + v)
    return v


builtins.input = fake_input
os.chdir(os.path.dirname(path))
sys.argv = [path]
sys.path.insert(0, os.path.dirname(path))
runpy.run_path(path, run_name="__main__")
