
import  datetime

##生成日期列表
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
    return generateURL(datelist)

##將日期轉成所需的url
def generateURL(datelist):
    url_list = ["https://newtalk.tw/news/summary/" + date + "/#cal" for date in datelist]
    return  url_list


#執行~!! 我很不愛寫 __main__  :P
#獲得日期列表

dayStart ="2019-01-01"
dayEnd = "2019-01-31"
dateForm = "%Y-%m-%d"
content ={}

url_list = generateDatelist(dateForm,dayStart,dayEnd)
for url in url_list:
    print(url)