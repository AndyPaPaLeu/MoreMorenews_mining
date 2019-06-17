
import  datetime
import time

def generateDatelist(dateForm = '%Y-%m-%d',start=datetime.datetime.now().strftime('%Y-%m-%d'),end=datetime.datetime.now().strftime('%Y-%m-%d')):
    datelist = []
    datelist.append(start)
    start = datetime.datetime.strptime(start,dateForm)
    end = datetime.datetime.strptime(end,dateForm)
    while start < end:
        start = start+datetime.timedelta(days=+1)
        start = start.strftime(dateForm)
        datelist.append(start)
        start = datetime.datetime.strptime(start,dateForm)
    return datelist

#執行~!! 我很不愛寫 __main__  :P
daystart ="2017/01/01"
dayend ="2019/04/15"
datelist = generateDatelist('%Y/%m/%d',daystart,dayend)
print(datelist)
