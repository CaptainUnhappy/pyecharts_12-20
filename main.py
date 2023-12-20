from pyecharts import options as opts
from pyecharts.charts import Bar, Grid, Line, Liquid, Page, Pie
from pyecharts.commons.utils import JsCode
from pyecharts.components import Table


def b_right1():
    pie1 = Pie()
    pie1.add(
        '',
        [["煤炭",9.26],["煤炭",9.26],["电",18.52],["蒸汽",25.93],["天然气",46.3]],
        radius=["30%", "70%"],
        center=["50%", "50%"],
        rosetype="radius"
    )
    pie1.set_global_opts(
        title_opts=opts.TitleOpts(
            title="重点用能单位的能耗分析（单位：吨 标准煤）",
            pos_left="27",
            pos_top="10",
            title_textstyle_opts=opts.TextStyleOpts(
                font_size=20,
                color="#000"
            )
        ),
        legend_opts=opts.LegendOpts(orient="vertical", pos_top="15%", pos_left="2%"),
        tooltip_opts=opts.TooltipOpts(trigger="item", formatter="{a} <br/>{b}: {c} ({d}%)")
    )
    pie1.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))

    return pie1


def b_right2():
    bar1 = Bar()
# 添加 X 轴数据
    bar1.add_xaxis(["电", "煤炭", "天然气", "蒸汽"])
# 添加 Y 轴数据，这里需要您提供实际的数据值
    bar1.add_yaxis(["电", "煤炭", "天然气", "蒸汽"],[312, 614, 880, 300],)
    bar1.add_yaxis(["电", "煤炭", "天然气", "蒸汽"],[356, 550, 200, 400],)
# 设置全局配置项
    bar1.set_global_opts(
        title_opts=opts.TitleOpts(
            title="规上工业增量存量能耗对比",
            title_textstyle_opts=opts.TextStyleOpts(
                font_size=20, 
                color="#000"
            ),
            pos_left="27",
            pos_top="10"
        ),
    # 根据需要添加更多配置项
)
    return bar1











# 接下来可以在 page_simple_layout() 中调用函数来添加这个图表


def page_simple_layout():
    page = Page(layout=Page.SimplePageLayout)
    page.add(
        b_right1(),
        b_right2(),
    )
    page.render("page_simple_layout.html")

if __name__ == "__main__":
    page_simple_layout()

page = Page(layout=Page.SimplePageLayout)
# 需要自行调整每个 chart 的 height/width，显示效果在不同的显示器上可能不同
page.add(b_right1(),b_right2(),)
page.render()
