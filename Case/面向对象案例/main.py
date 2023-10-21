from file_define import TextFileReader, JsonFileReader
from data_define import Record
from pyecharts.charts import Bar
from pyecharts.options import *
from pyecharts.globals import ThemeType
from typing import List

text_file_reader = TextFileReader()
json_file_reader = JsonFileReader()

jan_data: List[Record] = text_file_reader.read_data('2011年1月销售数据.txt')
feb_data: List[Record] = json_file_reader.read_data('2011年2月销售数据JSON.txt')

# 数据合并
all_data: List[Record] = jan_data + feb_data

# day_money_sum记录每天的总金额
day_money_sum = {}
for record in all_data:
    try:
        day_money_sum[record.date] += record.money
    except KeyError:
        day_money_sum[record.date] = record.money

keys = list(day_money_sum.keys())
# 可视化开发
bar = Bar()
bar.add_xaxis(keys)
bar.add_yaxis('每日销售额', [day_money_sum[key] for key in keys], label_opts=LabelOpts(is_show=False))
bar.set_global_opts(title_opts=TitleOpts(title='每日销售额'))
bar.render('每日销售额.html')
