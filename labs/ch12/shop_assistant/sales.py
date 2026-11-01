# sales.py 销售查询模块（组员 A 负责）
import pandas as pd

DATA = "../../data/sales_2025.csv"


def load():
    """读入全年销售表，返回 DataFrame"""
    return pd.read_csv(DATA)


def day_summary(df, day):
    """返回某一天的 (营业额, 订单数, 销售额最高的商品)；这天没有记录时返回 None"""
    d = df[df["日期"] == day]
    if len(d) == 0:
        return None
    best = d.groupby("商品名称")["金额"].sum().idxmax()
    return float(round(d["金额"].sum(), 2)), d["单号"].nunique(), best


def monthly(df):
    """返回各月营业额（Series，索引是 1～12 月）"""
    month = df["日期"].str[5:7].astype(int)
    return df.groupby(month)["金额"].sum().round(1)


def week_facts(df, start, end):
    """把 start～end 这几天的数据整理成几行文字，供大模型写小结"""
    w = df[(df["日期"] >= start) & (df["日期"] <= end)]
    top3 = w.groupby("商品名称")["金额"].sum().sort_values(ascending=False).head(3)
    by_day = w.groupby("日期")["金额"].sum()
    return (f"统计时间：{start} 至 {end}\n"
            f"营业额：{w['金额'].sum():.1f} 元\n"
            f"订单数：{w['单号'].nunique()} 单\n"
            f"销售额前三：{'、'.join(top3.index)}\n"
            f"营业额最高的一天：{by_day.idxmax()}")


if __name__ == "__main__":          # 组员自测：直接运行本文件
    df = load()
    print(day_summary(df, "2025-03-08"))
    print(day_summary(df, "2025-13-01"))
    print(monthly(df).head(3).to_dict())
