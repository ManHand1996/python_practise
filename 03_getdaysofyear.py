#-*-coding:utf-8 -*-
# 输入日期， 判断这一天是这一年的第几天？
import datetime

d_input = input(">: input date of str like: 'yyyy-MM-dd', default:now\n")

date_input = datetime.datetime.strptime(d_input, "%Y-%m-%d")

date_start = datetime.datetime(year=date_input.year,month=1,day=1)
delta_days = date_input - date_start
print("this date is ",delta_days.days + 1, " days of this year")


