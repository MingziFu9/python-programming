# 实验 10-2 用 openpyxl 生成销售日报 Excel
# 需要先安装：pip install openpyxl
import csv
from openpyxl import Workbook, load_workbook
from openpyxl.styles import Font

day = "2025-03-08"                       # 要做日报的日期

# 1. 从全年销售表中找出这一天的记录
rows = []
with open("../data/sales_2025.csv", encoding="utf-8") as f:
    for r in csv.DictReader(f):
        if r["日期"] == day:
            rows.append([r["时间"], r["商品名称"], float(r["单价"]), int(r["数量"]), float(r["金额"])])
rows.sort()                              # 按时间排序（每行第一项是时间）
print(day, "共", len(rows), "条记录")

# 2. 新建工作簿，写表头和数据
wb = Workbook()
ws = wb.active                           # 默认的第一张工作表
ws.title = "销售日报"
ws.append(["时间", "商品名称", "单价", "数量", "金额"])
for row in rows:
    ws.append(row)

# 3. 最后加一行合计：直接写 Excel 公式，打开文件时由 Excel 计算
last = ws.max_row                        # 当前最后一行的行号
ws.append(["合计", "", "", f"=SUM(D2:D{last})", f"=SUM(E2:E{last})"])

# 4. 简单美化：表头和合计行加粗，设置列宽
for cell in ws[1]:
    cell.font = Font(bold=True)
for cell in ws[ws.max_row]:
    cell.font = Font(bold=True)
ws.column_dimensions["B"].width = 16

wb.save(f"销售日报_{day}.xlsx")
print("已保存", f"销售日报_{day}.xlsx")

# 5. 读回来检查
wb2 = load_workbook(f"销售日报_{day}.xlsx")
ws2 = wb2["销售日报"]
print("行数：", ws2.max_row, "列数：", ws2.max_column)
print("第 2 行：", [c.value for c in ws2[2]])
print("合计行：", [c.value for c in ws2[ws2.max_row]])
