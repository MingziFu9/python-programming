# 实验 10-1 按扩展名批量整理文件
# 为了安全，程序先自己造一个“杂乱文件夹”做练习，只整理这个文件夹里的文件
from pathlib import Path
import shutil

demo = Path("杂乱文件夹")

# 第一步：准备练习用的文件（如果文件夹已存在，先删掉重建）
if demo.exists():
    shutil.rmtree(demo)
demo.mkdir()
names = ["进货单.xlsx", "价目表.xlsx", "开业海报.png", "招牌.jpg", "会员.csv",
         "销售.csv", "通知.docx", "笔记.txt", "收银.py", "说明"]
for n in names:
    (demo / n).write_text("练习文件", encoding="utf-8")
print("整理前：", sorted(p.name for p in demo.iterdir()))

# 第二步：扩展名和文件夹的对应关系（一个字典）
rules = {".xlsx": "表格", ".csv": "表格", ".png": "图片", ".jpg": "图片",
         ".docx": "文档", ".txt": "文档", ".py": "代码"}

# 第三步：逐个文件判断扩展名，移动到对应的子文件夹
count = 0
for p in list(demo.iterdir()):           # 先转成列表，因为移动过程中文件夹内容会变
    if p.is_file():
        folder = rules.get(p.suffix.lower(), "其他")   # 不认识的扩展名放进“其他”
        target = demo / folder
        target.mkdir(exist_ok=True)       # 子文件夹已存在也不报错
        shutil.move(str(p), str(target / p.name))
        count += 1

print(f"共移动 {count} 个文件，整理后：")
for sub in sorted(demo.iterdir()):
    print(" ", sub.name, "：", sorted(f.name for f in sub.iterdir()))
