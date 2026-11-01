# 实验 5-3 用 turtle 画小店招牌
import turtle

t = turtle.Turtle()
t.speed(0)                          # 0 表示最快
turtle.bgcolor("white")

# 1. 画招牌的长方形边框
t.penup()
t.goto(-200, 60)
t.pendown()
t.pensize(4)
t.color("darkred", "lightyellow")
t.begin_fill()
for i in range(2):                  # 长方形：长边、短边各画 2 次
    t.forward(400)
    t.right(90)
    t.forward(120)
    t.right(90)
t.end_fill()

# 2. 写店名
t.penup()
t.goto(0, -20)
t.color("darkred")
t.write("街坊便利店", align="center", font=("Microsoft YaHei", 36, "bold"))

# 3. 在招牌下方画一排 5 颗小星星
t.color("orange")
for k in range(5):
    t.penup()
    t.goto(-160 + k * 80, -110)
    t.pendown()
    t.begin_fill()
    for i in range(5):              # 五角星：前进、右转 144 度，重复 5 次
        t.forward(30)
        t.right(144)
    t.end_fill()

t.hideturtle()
turtle.done()                       # 保持窗口打开，关闭窗口后程序结束
