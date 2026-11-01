# 实验 1-1 第一个程序：检查环境，向世界问好
# 在 Thonny 里打开本文件，点绿色的“运行”按钮（或按 F5）

import sys                      # 导入 sys 模块，用来查看 Python 的版本

print("你好，Python！")
print("我正在用的 Python 版本是：", sys.version.split()[0])
print("1 + 1 =", 1 + 1)
print("街坊便利店", "开张啦", sep=" —— ")
