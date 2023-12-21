from pyecharts import options as opts
from pyecharts.charts import Bar, Grid, Line, Liquid, Page, Pie, Map, Geo, Radar
from pyecharts.commons.utils import JsCode
from pyecharts.components import Table
from pyecharts.globals import ThemeType
import random


def b_right1():
    pie_Energyanalysis = Pie(init_opts=opts.InitOpts(
        theme=ThemeType.CHALK, width='754px', height='310px'))
    pie_Energyanalysis.add(
        '',
        [["煤炭", 9.26], ["电", 18.52], ["蒸汽", 25.93], ["天然气", 46.3]],
        radius=["30%", "70%"],
        center=["50%", "50%"],
        rosetype="radius"
    )
    pie_Energyanalysis.set_global_opts(
        title_opts=opts.TitleOpts(
            title="重点用能单位的能耗分析（单位：吨 标准煤）",
            pos_left="27",
            pos_top="10",
            title_textstyle_opts=opts.TextStyleOpts(
                font_size=20,
                color="#000"
            )
        ),
        legend_opts=opts.LegendOpts(
            orient="vertical", pos_top="15%", pos_left="2%"),
        tooltip_opts=opts.TooltipOpts(
            trigger="item", formatter="{a} <br/>{b}: {c} ({d}%)")
    )
    pie_Energyanalysis.set_series_opts(
        label_opts=opts.LabelOpts(formatter="{b}: {c}"))

    return pie_Energyanalysis


def b_right2():  # UnFinish_Style##
    bar_energyconsumption = Bar(init_opts=opts.InitOpts(
        theme=ThemeType.CHALK, width='754px', height='310px'))
# 添加 X 轴数据
    bar_energyconsumption.add_xaxis(["电", "煤炭", "天然气", "蒸汽"])
# 添加 Y 轴数据，这里需要您提供实际的数据值
    bar_energyconsumption.add_yaxis(["电", "煤炭", "天然气", "蒸汽"], [
                                    312, 614, 880, 300], bar_width=13)
    bar_energyconsumption.add_yaxis(["电", "煤炭", "天然气", "蒸汽"], [
                                    356, 550, 200, 400], bar_width=13)
# 设置全局配置项
    bar_energyconsumption.set_global_opts(
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
    return bar_energyconsumption


def b_right3_1():
    pie_industryanalysis1 = Pie(init_opts=opts.InitOpts(
        theme=ThemeType.CHALK, width='377px', height='400px'))
    pie_industryanalysis1.add(
        '',
        [["蒸汽", 21.43], ["电", 21.43], ["天然气", 14.29], ["煤炭", 42.86]],
        radius=["20%", "70%"],
        rosetype='rose_type'
    )
    pie_industryanalysis1.set_series_opts(
        label_opts=opts.LabelOpts(
            font_size=14,
            color="#fff",
            formatter="{b}\n{c}%",
            position="inside"
        ),
    )
    pie_industryanalysis1.set_global_opts(
        title_opts=opts.TitleOpts(
            title=['行业能耗结构分析（单位：标准煤）'],
            pos_left="27",
            pos_top="10",
            title_textstyle_opts=opts.TextStyleOpts(
                font_size=20,
                color="#000"
            ),
        ),
        legend_opts=opts.LegendOpts(pos_bottom="1%"),
    )
    return pie_industryanalysis1


def b_right3_2():
    pie_industryanalysis2 = Pie(init_opts=opts.InitOpts(
        theme=ThemeType.CHALK, width='400px', height='400px'))
    pie_industryanalysis2.add(
        '',
        [["限上批零业", 7.04], ["规上服务业", 42.25], ["非化工企业", 21.13], ["化工企业", 29.58]],
        radius=["20%", "70%"],
        rosetype='rose_type'
    )
    pie_industryanalysis2.set_series_opts(
        label_opts=opts.LabelOpts(
            font_size=14,
            color="#fff",
            formatter="{b}\n{c}%",
            position="inside"
        ),
    )
    pie_industryanalysis2.set_global_opts(
        title_opts=opts.TitleOpts(
            title=['能耗结构分析'],
            pos_left="27",
            pos_top="10",
            title_textstyle_opts=opts.TextStyleOpts(
                font_size=20,
                color="#000"
            ),
        ),
        legend_opts=opts.LegendOpts(pos_bottom="1%"),
    )
    return pie_industryanalysis2


def b_left3():  # 再议###
    line_energyconsumptionthismonth = Line(init_opts=opts.InitOpts(
        theme=ThemeType.CHALK, width='568px', height='311px'))
# 添加 X 轴数据
    line_energyconsumptionthismonth.add_xaxis([])
    line_energyconsumptionthismonth.add_xaxis(["电", "煤炭", "天然气", "蒸汽"])
# 添加 Y 轴数据，这里需要您提供实际的数据值
    line_energyconsumptionthismonth.add_yaxis(["电", "煤炭", "天然气", "蒸汽"], [
                                              50, 21, 32, 42, 31, 26, 28, 37, 45, 12, 36, 36, 39, 42, 50, 32,],)
    line_energyconsumptionthismonth.add_yaxis([], [])
    line_energyconsumptionthismonth.set_series_opts(
        areastyle_opts=opts.AreaStyleOpts(
            color="rgba(13,120,214,0.8)",
        )
    )
# 设置全局配置项
    line_energyconsumptionthismonth.set_global_opts(
        title_opts=opts.TitleOpts(
            title="园区本月能耗",
            title_textstyle_opts=opts.TextStyleOpts(
                font_size=20,
                color="#000"
            ),
            pos_left="27",
            pos_top="9"
        ),
        # 根据需要添加更多配置项
    )
    return line_energyconsumptionthismonth


def b_left1_Map():  # TODO##
    data_prov_city = [["兴化市", [119.930721, 32.826721]],
                      ["靖江市", [120.135391, 31.997629]]]
    Map_m = Map(init_opts=opts.InitOpts(
        theme=ThemeType.CHALK, width='1053px', height='634px'))
    Map_m.add("",
              data_prov_city,
              "泰州"
              )
    Map_m.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    # Map_m.set_global_opts(
    #     title_opts=opts.TitleOpts(title='Provinces of China'),
    #     visualmap_opts=opts.VisualMapOpts(
    #         min_=100,
    #         max_=200,
    #         is_piecewise=True)
    # )
    return Map_m


def b_left2():  # UnFinish##
    bar_energyconsumptionthisday = Bar(init_opts=opts.InitOpts(
        theme=ThemeType.CHALK, width='465px', height='311px'))
    bar_energyconsumptionthisday.add_xaxis([90, 74, 50, 40])
    bar_energyconsumptionthisday.add_yaxis(
        ["当日原煤量", "当日蒸汽量", "当日天然气量", "当月用电量"], [90, 74, 50, 40], bar_width=13)
    bar_energyconsumptionthisday.reversal_axis()
    bar_energyconsumptionthisday.set_global_opts(
        title_opts=opts.TitleOpts(
            title="园区当日能耗",
            title_textstyle_opts=opts.TextStyleOpts(
                font_size=20,
                color="#000",
            ),
            pos_left='27',
            pos_top='9',
        )
    )
    return bar_energyconsumptionthisday


def b_left1_Radar():
    v1 = [[4000, 10000, 20000, 30000, 20000, 20000]]
    c = (
        Radar(init_opts=opts.InitOpts(
            theme=ThemeType.CHALK, width='465px', height='311px'))
        .add_schema(
            schema=[
                opts.RadarIndicatorItem(name="临时访客", max_=6500),
                opts.RadarIndicatorItem(name="危废车辆", max_=16000),
                opts.RadarIndicatorItem(name="职工车辆", max_=30000),
                opts.RadarIndicatorItem(name="危化品车辆", max_=38000),
                opts.RadarIndicatorItem(name="普通车辆", max_=52000),
            ]
        )
        .add("统计值", v1)
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title="入园申报统计", pos_right='27', pos_top='9'),
            legend_opts=opts.LegendOpts(is_show=False),
        )
    )
    return c


# page = Page(layout=Page.DraggablePageLayout).add_js_funcs(
#     "document.body.style.backgroundColor = \"#101341\";")
# # 需要自行调整每个 chart 的 height/width，显示效果在不同的显示器上可能不同
# page.add(b_right1(), b_right2(), b_right3_1(),
#          b_right3_2(), b_left3(), b_left1_Map(), b_left2(), b_left1_Radar())
# page.render()
Page.save_resize_html("render.html", cfg_file="./json/chart_config.json")
