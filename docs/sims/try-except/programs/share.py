text = input("分给几个人：")
try:
    n = int(text)
    each = 12 / n
except ValueError:
    print("请输入整数")
except ZeroDivisionError:
    print("人数不能为 0")
else:
    print("每人分", each, "个")
finally:
    print("分包子结束")
print("程序继续运行")
