# Create your views here.
import json

from django.shortcuts import render
from django.views import View
from pyecharts.globals import ThemeType
from rest_framework.response import Response
from rest_framework.views import APIView

from .read_csv import ReadCsv


class ApiData(APIView):
    def get(self, request, name):
        data = ReadCsv(name).dump_as_json()
        return Response(data, status=data['status'])


class ApiCharts(APIView):
    def get(self, request, name='治愈人数'):
        from pyecharts.globals import CurrentConfig
        from pyecharts import options as opts
        from pyecharts.charts import Bar
        CurrentConfig.ONLINE_HOST = "https://cdn.jsdelivr.net/gh/pyecharts/pyecharts-assets@latest/assets/"
        data = ReadCsv(name).dump_as_json()
        c = (
            Bar(init_opts=opts.InitOpts(renderer="svg", width='400px', height='277px'))
                .add_xaxis(data['labels'])
                .add_yaxis("人数", data['data'], label_opts=opts.LabelOpts(is_show=False, color='white'))
                .set_series_opts(itemstyle_opts={
                "normal": {
                    "barBorderRadius": [25, 25, 25, 25],
                    "shadowColor": "#2f89cf",
                    "color": "#2f89cf"
                }
            })
                .set_global_opts(
                datazoom_opts=opts.DataZoomOpts(type_="inside"),
                tooltip_opts=opts.TooltipOpts(is_show=True,
                                              trigger_on='mousemove|click',
                                              axis_pointer_type='shadow',
                                              trigger='axis'),
                xaxis_opts=opts.AxisOpts(is_show=True, axislabel_opts=opts.LabelOpts(
                    color='rgba(255,255,255,.6)'),
                                         axisline_opts=opts.AxisLineOpts(is_show=True,
                                                                         linestyle_opts=opts.LineStyleOpts(
                                                                             color='rgba(255,255,255,.1)',
                                                                             type_='solid',
                                                                             width=1
                                                                         ))),
                yaxis_opts=opts.AxisOpts(is_show=True, axislabel_opts=opts.LabelOpts(color='rgba(255,255,255,.6)'),
                                         axisline_opts=opts.AxisLineOpts(is_show=True,
                                                                         linestyle_opts=opts.LineStyleOpts(
                                                                             color='rgba(255,255,255,.1)',
                                                                             type_='solid',
                                                                             width=1
                                                                            )),
                                         splitline_opts=opts.SplitLineOpts(is_show=True,
                                                                           linestyle_opts=opts.LineStyleOpts(color='rgba(255,255,255,.1)'))),
                legend_opts=opts.LegendOpts(is_show=False),
            )
        )
        return Response(json.loads(c.dump_options()))


class PageView(View):
    def get(self, request):
        return render(request, 'chart.html')
