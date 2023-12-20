from pyecharts.charts import Bar, Scatter, Line, Grid, Pie, Tab
from pyecharts import options as opts
from pyecharts.faker import Faker

# bar = (
#     Bar()
#     .add_xaxis(["衬衫", "毛衣", "领带", "裤子", "风衣", "高跟鞋", "袜子"])
#     .add_yaxis("商家A", [114, 55, 27, 101, 125, 27, 105])
#     .add_yaxis("商家B", [57, 134, 137, 129, 145, 60, 49])
#     .set_global_opts(title_opts=opts.TitleOpts(title="某商场销售情况"))
# )
# bar.render()


# scatter = (
#     Scatter()
#         .add_xaxis(Faker.choose())
#         .add_yaxis("商家A", Faker.values())
#         .add_yaxis("商家B", Faker.values())
#         .set_global_opts(
#         title_opts=opts.TitleOpts(title="Grid-Scatter"),
#         legend_opts=opts.LegendOpts(pos_left="20%"),
#     )
# )
line = (
    Line()
        .add_xaxis(Faker.choose())
        .add_yaxis("商家A", Faker.values())
        .add_yaxis("商家B", Faker.values())
        .set_global_opts(
        title_opts=opts.TitleOpts(title="Grid-Line", pos_right="5%"),
        legend_opts=opts.LegendOpts(pos_right="20%"),
    )
)
#
# (
#     Grid()
#         .add(scatter, grid_opts=opts.GridOpts(pos_left="55%"))
#         .add(line, grid_opts=opts.GridOpts(pos_right="55%"))
#         .render()
# )


# def bar_datazoom_slider() -> Bar:
#     c = (
#         Bar()
#             .add_xaxis(Faker.days_attrs)
#             .add_yaxis("商家A", Faker.days_values)
#             .set_global_opts(
#             title_opts=opts.TitleOpts(title="Bar-DataZoom（slider-水平）"),
#             datazoom_opts=[opts.DataZoomOpts()],
#         )
#     )
#     return c
#
#
# def line_markpoint() -> Line:
#     c = (
#         Line()
#             .add_xaxis(Faker.choose())
#             .add_yaxis(
#             "商家A",
#             Faker.values(),
#             markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="min")]),
#         )
#             .add_yaxis(
#             "商家B",
#             Faker.values(),
#             markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max")]),
#         )
#             .set_global_opts(title_opts=opts.TitleOpts(title="Line-MarkPoint"))
#     )
#     return c
#
#
# def pie_rosetype() -> Pie:
#     v = Faker.choose()
#     c = (
#         Pie()
#             .add(
#             "",
#             [list(z) for z in zip(v, Faker.values())],
#             radius=["30%", "75%"],
#             center=["25%", "50%"],
#             rosetype="radius",
#             label_opts=opts.LabelOpts(is_show=False),
#         )
#             .add(
#             "",
#             [list(z) for z in zip(v, Faker.values())],
#             radius=["30%", "75%"],
#             center=["75%", "50%"],
#             rosetype="area",
#         )
#             .set_global_opts(title_opts=opts.TitleOpts(title="Pie-玫瑰图示例"))
#     )
#     return c
#
#
# def grid_mutil_yaxis() -> Grid:
#     x_data = ["{}月".format(i) for i in range(1, 13)]
#     bar = (
#         Bar()
#             .add_xaxis(x_data)
#             .add_yaxis(
#             "蒸发量",
#             [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3],
#             yaxis_index=0,
#             color="#d14a61",
#         )
#             .add_yaxis(
#             "降水量",
#             [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3],
#             yaxis_index=1,
#             color="#5793f3",
#         )
#             .extend_axis(
#             yaxis=opts.AxisOpts(
#                 name="蒸发量",
#                 type_="value",
#                 min_=0,
#                 max_=250,
#                 position="right",
#                 axisline_opts=opts.AxisLineOpts(
#                     linestyle_opts=opts.LineStyleOpts(color="#d14a61")
#                 ),
#                 axislabel_opts=opts.LabelOpts(formatter="{value} ml"),
#             )
#         )
#             .extend_axis(
#             yaxis=opts.AxisOpts(
#                 type_="value",
#                 name="温度",
#                 min_=0,
#                 max_=25,
#                 position="left",
#                 axisline_opts=opts.AxisLineOpts(
#                     linestyle_opts=opts.LineStyleOpts(color="#675bba")
#                 ),
#                 axislabel_opts=opts.LabelOpts(formatter="{value} °C"),
#                 splitline_opts=opts.SplitLineOpts(
#                     is_show=True, linestyle_opts=opts.LineStyleOpts(opacity=1)
#                 ),
#             )
#         )
#             .set_global_opts(
#             yaxis_opts=opts.AxisOpts(
#                 name="降水量",
#                 min_=0,
#                 max_=250,
#                 position="right",
#                 offset=80,
#                 axisline_opts=opts.AxisLineOpts(
#                     linestyle_opts=opts.LineStyleOpts(color="#5793f3")
#                 ),
#                 axislabel_opts=opts.LabelOpts(formatter="{value} ml"),
#             ),
#             title_opts=opts.TitleOpts(title="Grid-多 Y 轴示例"),
#             tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
#         )
#     )
#
#     line = (
#         Line()
#             .add_xaxis(x_data)
#             .add_yaxis(
#             "平均温度",
#             [2.0, 2.2, 3.3, 4.5, 6.3, 10.2, 20.3, 23.4, 23.0, 16.5, 12.0, 6.2],
#             yaxis_index=2,
#             color="#675bba",
#             label_opts=opts.LabelOpts(is_show=False),
#         )
#     )
#
#     bar.overlap(line)
#     return Grid().add(
#         bar, opts.GridOpts(pos_left="5%", pos_right="20%"), is_control_axis_index=True
#     )
#
#
# tab = Tab()
# tab.add(bar_datazoom_slider(), "bar-example")
# tab.add(line_markpoint(), "line-example")
# tab.add(pie_rosetype(), "pie-example")
# tab.add(grid_mutil_yaxis(), "grid-example")
# tab.render()


# from pyecharts import options as opts
# from pyecharts.charts import Bar, Geo, Grid
# from pyecharts.faker import Faker
#
# bar = (
#     Bar()
#     .add_xaxis(Faker.choose())
#     .add_yaxis("商家A", Faker.values())
#     .add_yaxis("商家B", Faker.values())
#     .set_global_opts(legend_opts=opts.LegendOpts(pos_left="20%"))
# )
# geo = (
#     Geo()
#     .add_schema(maptype="china")
#     .add("geo", [list(z) for z in zip(Faker.provinces, Faker.values())])
#     .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
#     .set_global_opts(
#         visualmap_opts=opts.VisualMapOpts(),
#         title_opts=opts.TitleOpts(title="Grid-Geo-Bar"),
#     )
# )
#
# grid = (
#     Grid()
#     .add(bar, grid_opts=opts.GridOpts(pos_top="50%", pos_right="75%"))
#     .add(geo, grid_opts=opts.GridOpts(pos_left="60%"))
#     .render("grid_geo_bar.html")
# )


# from pyecharts.charts import Pie
# import pyecharts.options as opts
#
# cate = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu']
# data = [123, 109, 67, 87, 98, 43]
# pie1_x_data = ["煤炭", "电", "蒸汽", "天然气"]
# pie1_y_data = [9.26, 18.52, 25.93, 46.3]
# pie1 = (
#     Pie()
#         .add(series_name='饼图', data_pair=[list(z) for z in zip(pie1_x_data, pie1_y_data)], radius=["50%", "70%"],
#              label_opts=opts.LabelOpts(formatter="{b}{c}%", color="red"))
#         .set_global_opts(title_opts=opts.TitleOpts(title='重点用能单位的能耗分析（单位：吨 标准煤）', pos_left='center',
#                                                    title_textstyle_opts=opts.TextStyleOpts(color='red', font_size=20)),
#                          legend_opts=opts.LegendOpts(pos_right='right'))
#     # .render()
# )
# (
#     Grid()
#         .add(line, grid_opts=opts.GridOpts(pos_left="20%", width="30%"))
#         .add(pie1, grid_opts=opts.GridOpts(pos_right="20%", width="30%"))
#         .render()
# )
from pyecharts import options as opts
from pyecharts.charts import Bar, Grid, Line, Liquid, Page, Pie
from pyecharts.commons.utils import JsCode
from pyecharts.components import Table
from pyecharts.faker import Faker


def bar_datazoom_slider() -> Bar:
    c = (
        Bar()
            .add_xaxis(Faker.days_attrs)
            .add_yaxis("商家A", Faker.days_values)
            .set_global_opts(
            title_opts=opts.TitleOpts(title="Bar-DataZoom（slider-水平）"),
            datazoom_opts=[opts.DataZoomOpts()],
        )
    )
    return c


def line_markpoint() -> Line:
    c = (
        Line()
            .add_xaxis(Faker.choose())
            .add_yaxis(
            "商家A",
            Faker.values(),
            markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="min")]),
        )
            .add_yaxis(
            "商家B",
            Faker.values(),
            markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max")]),
        )
            .set_global_opts(title_opts=opts.TitleOpts(title="Line-MarkPoint"))
    )
    return c


def pie_rosetype() -> Pie:
    v = Faker.choose()
    c = (
        Pie()
            .add(
            "",
            [list(z) for z in zip(v, Faker.values())],
            radius=["30%", "75%"],
            center=["25%", "50%"],
            rosetype="radius",
            label_opts=opts.LabelOpts(is_show=False),
        )
            .add(
            "",
            [list(z) for z in zip(v, Faker.values())],
            radius=["30%", "75%"],
            center=["75%", "50%"],
            rosetype="area",
        )
            .set_global_opts(title_opts=opts.TitleOpts(title="Pie-玫瑰图示例"))
    )
    return c


def grid_mutil_yaxis() -> Grid:
    x_data = ["{}月".format(i) for i in range(1, 13)]
    bar = (
        Bar()
            .add_xaxis(x_data)
            .add_yaxis(
            "蒸发量",
            [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3],
            yaxis_index=0,
            color="#d14a61",
        )
            .add_yaxis(
            "降水量",
            [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3],
            yaxis_index=1,
            color="#5793f3",
        )
            .extend_axis(
            yaxis=opts.AxisOpts(
                name="蒸发量",
                type_="value",
                min_=0,
                max_=250,
                position="right",
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(color="#d14a61")
                ),
                axislabel_opts=opts.LabelOpts(formatter="{value} ml"),
            )
        )
            .extend_axis(
            yaxis=opts.AxisOpts(
                type_="value",
                name="温度",
                min_=0,
                max_=25,
                position="left",
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(color="#675bba")
                ),
                axislabel_opts=opts.LabelOpts(formatter="{value} °C"),
                splitline_opts=opts.SplitLineOpts(
                    is_show=True, linestyle_opts=opts.LineStyleOpts(opacity=1)
                ),
            )
        )
            .set_global_opts(
            yaxis_opts=opts.AxisOpts(
                name="降水量",
                min_=0,
                max_=250,
                position="right",
                offset=80,
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(color="#5793f3")
                ),
                axislabel_opts=opts.LabelOpts(formatter="{value} ml"),
            ),
            title_opts=opts.TitleOpts(title="Grid-多 Y 轴示例"),
            tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
        )
    )

    line = (
        Line()
            .add_xaxis(x_data)
            .add_yaxis(
            "平均温度",
            [2.0, 2.2, 3.3, 4.5, 6.3, 10.2, 20.3, 23.4, 23.0, 16.5, 12.0, 6.2],
            yaxis_index=2,
            color="#675bba",
            label_opts=opts.LabelOpts(is_show=False),
        )
    )

    bar.overlap(line)
    return Grid().add(
        bar, opts.GridOpts(pos_left="5%", pos_right="20%"), is_control_axis_index=True
    )


def liquid_data_precision() -> Liquid:
    c = (
        Liquid()
            .add(
            "lq",
            [0.3254],
            label_opts=opts.LabelOpts(
                font_size=50,
                formatter=JsCode(
                    """function (param) {
                        return (Math.floor(param.value * 10000) / 100) + '%';
                    }"""
                ),
                position="inside",
            ),
        )
            .set_global_opts(title_opts=opts.TitleOpts(title="Liquid-数据精度"))
    )
    return c


def table_base() -> Table:
    table = Table()

    headers = ["City name", "Area", "Population", "Annual Rainfall"]
    rows = [
        ["Brisbane", 5905, 1857594, 1146.4],
        ["Adelaide", 1295, 1158259, 600.5],
        ["Darwin", 112, 120900, 1714.7],
        ["Hobart", 1357, 205556, 619.5],
        ["Sydney", 2058, 4336374, 1214.8],
        ["Melbourne", 1566, 3806092, 646.9],
        ["Perth", 5386, 1554769, 869.4],
    ]
    table.add(headers, rows).set_global_opts(
        title_opts=opts.ComponentTitleOpts(title="Table")
    )
    return table


def page_simple_layout():
    page = Page(layout=Page.SimplePageLayout)
    page.add(
        bar_datazoom_slider(),
        line_markpoint(),
        pie_rosetype(),
        grid_mutil_yaxis(),
        liquid_data_precision(),
        table_base(),
    )
    page.render("page_simple_layout.html")


if __name__ == "__main__":
    page_simple_layout()

page = Page(layout=Page.SimplePageLayout)
# 需要自行调整每个 chart 的 height/width，显示效果在不同的显示器上可能不同
page.add(bar_datazoom_slider(), line_markpoint(), pie_rosetype(), grid_mutil_yaxis(),liquid_data_precision())
page.render()
