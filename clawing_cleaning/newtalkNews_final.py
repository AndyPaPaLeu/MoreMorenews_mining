# # 新頭殼
import requests
from bs4 import BeautifulSoup
import json
import  datetime


##資料儲存於字典
def info_input(title,ptime,author,text,textUrl,tags):
    source = '新頭殼'
    if not author:
        author = "無名氏"
    info = {'title': title, 'time': ptime, 'author': author, 'text': text, 'url': textUrl, 'tags': tags, 'type_list':[], 'source': source, 'views':'','share':'','like':''}  # 以dictionary儲存資訊
    if author:
        conKey = ptime +'_'+author
        content[conKey] = info
        print(info)

    else:
        conKey = ptime +'_'+"無名氏"
        content[conKey] = info
        print(info)

##爬取內文
def CrawlingText (url):
    response = requests.get(url=url,verify = False)                                    #以requests的get承接url
    response.encoding = response.apparent_encoding 
    soup2 = BeautifulSoup(response.text, features='html.parser')           #將response以.text獲得文檔，再用好湯接，宣告為html型式解讀

    targets1 = soup2.find('div',{'class':'contentBox'})
    author = targets1.find('a').string
    posttime_raw = targets1.find('div',{'class':'content_date'}).get_text().strip()[3:21]  # 以string獲得標籤內文，並以[2:12]擷取所要的資訊
    posttime_raw2 = posttime_raw.replace(" | ", "_")
    ptime = posttime_raw2.replace(".", "/")

    text_tag = soup2.find(id='news_content')
    text_lists = text_tag.find_all('p')
    text = ""
    for i in text_lists:
        # print(i.string)
        if i.string:
            if i.string[0:] == "延伸閱讀：":
                # print("hi")
                break
            elif i.string[0:] =="▲":
                continue
            else:
                text += i.get_text()
				
        else:
#            print(i.get_text().split())            
            #print(i.get_text().split("\\n"))
            for j in i.get_text().split():
                if j[0] == "▲":
                    continue
                else:
                    text += j
                
    tags = []
    tag_tags = soup2.find('div',{'class':"tag_group2"})
    tag_lists = tag_tags.find_all('a')
    for i in tag_lists:
        tag_text = i.get_text()
        tags.append(tag_text)
    return ptime, author, text, tags


##爬取新聞列表
def CrawlingNews (url):
    print(">1")
    response = requests.get(url=url,verify = False)                                    #以requests的get承接url
    response.encoding = response.apparent_encoding                      #設定endoding與顯示的encoding相同
    soup = BeautifulSoup(response.text, features='html.parser')           #將response以.text獲得文檔，再用好湯接，宣告為html型式解讀

    ## 抓取 [所需資訊]
    target1 = soup.find('div',{'id':'summary'})                              #找到目標區塊標籤
    target1 = target1.find('div', {'class':'news-top2'})
    top2news = target1.find_all('div',{'class':'news-title'})
    # print(top2news)
    for i in top2news:
        # print(">1.1")
        title = i.string
        textUrl = i.find('a').attrs.get('href')
        ptime,author,text,tags = CrawlingText(textUrl)
        info_input(title, ptime, author, text, textUrl, tags)
        # print(">1.1<")

    news_tags = soup.find_all('div', {'class': 'text'}) # 找到目標區塊標籤
    # print(">1.2")

    for i in news_tags:
        div_tagA = i.find('a', {'class': 'newsBox'})
        if div_tagA:
            textUrl = div_tagA.attrs.get('href')
            title = div_tagA.get_text().strip()  # 擷取text，並以strip()剝去\n

            if textUrl[29:39] == url[32:42]:
                ptime,author,text,tags = CrawlingText(textUrl)
                info_input(title, ptime, author, text, textUrl, tags)
                # print(">1.2<")
            else: break


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


##啟程~!
#獲得日期列表
if __name__ == '__main__':
    dayStart ="2019-05-01"
    dayEnd = "2019-05-02"
    dateForm = "%Y-%m-%d"
    content ={}

    url_list = generateDatelist(dateForm,dayStart,dayEnd)
    for url in url_list:
        print(url)
        CrawlingNews(url)
        # print(content)

    with open("C:/Users/PeiYu/Desktop/newtalk_2019_05.json","w") as fjson:
        json.dump(content,fjson)

#     cont = 1
#
#
#     while True:
#         nextpage_link = CrawlingNews(url)
#         url = nextpage_link
#         if url == False:  #最後會回傳False
#             with open("C:/Users/Student/Desktop/newtalk.json","w") as fjson:
#                 json.dump(content,fjson)
#             break
#         cont += 1
#         if cont%200 == 0:
#             with open("C:/Users/Student/Desktop/newtalk"+str(cont)+".json","w") as fjson:
#                 json.dump(content,fjson)
#                 content ={}
#
#     print(content) ##檢視結果