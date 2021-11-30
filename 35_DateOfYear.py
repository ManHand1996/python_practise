# Date Of Year for input date(year, month, day)

import datetime
def getDateOfYear():
    input_date = input("输入年月日（yyyy-MM-dd）")
    input_date = datetime.datetime.strptime(input_date, "%Y-%m-%d")
    first_date = datetime.datetime(year=input_date.year, month=input_date.month, day=input_date.day)
    print(input_date.day - input_date.day + 1)
    

getDateOfYear()

