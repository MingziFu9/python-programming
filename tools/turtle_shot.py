"""在无显示器的环境里运行 turtle 程序并截图（需要 Xvfb、ImageMagick 和带 Xft 的 Tk）。
用法：xvfb-run -s "-screen 0 800x600x24" python3 tools/turtle_shot.py 程序.py 输出.png
"""
import sys, os, runpy, subprocess, turtle
out = os.path.abspath(sys.argv[2])
def done():
    turtle.update()
    cv = turtle.getcanvas(); cv.update(); import time; time.sleep(1); cv.update()
    subprocess.run(["import", "-window", "root", "-crop", "%dx%d+0+0" % (W, H), out], check=True)
    os._exit(0)
W, H = 520, 340
turtle.setup(W, H, 0, 0)
turtle.done = done
turtle.mainloop = done
runpy.run_path(os.path.abspath(sys.argv[1]), run_name="__main__")
