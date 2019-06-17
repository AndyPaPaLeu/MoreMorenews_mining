# -*- coding: utf-8 -*-
"""
Created on Fri May  3 11:49:16 2019

@author: Student
"""

import requests
from bs4 import BeautifulSoup
import  datetime
import  re
import json


##生成日期列表
def generateDatelist(dateForm = '%Y%m%d',start=datetime.datetime.now().strftime('%Y%m%d'),end=datetime.datetime.now().strftime('%Y%m%d')):
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
#'https://tw.appledaily.com/appledaily/archive/20190415'
##將日期轉成所需的url
def generateURL(datelist):
    url_list = ["https://tw.appledaily.com/appledaily/archive/" + date  for date in datelist]
    return  url_list



#獲得日期列表

dayStart ="20180501"
dayEnd = "20180630"
dateForm = "%Y%m%d"

content ={}

url_list = generateDatelist(dateForm,dayStart,dayEnd)

for url in url_list:
    #print(url)
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    count = 0
    eee =['nclns eclnms5','nclns eclnms9','nclns eclnms7','nclns eclnms10','nclns eclnms8','nclns eclnmsSub']
    for jj in eee :
        title_list = soup.find_all('article', class_= jj)
        for i in title_list:
            type_list = i.find('h2').text
            news_list = i.find_all('a')

            for i in news_list:
                if i.attrs.get('href')[0] == 'h':
                    new_url = i.attrs.get('href')

                    # print('type_list :'+type_list)
                    print('url :'+new_url)
                    session = requests.Session()
                    session.headers.update({
                        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/a",
                        "Accept-Encoding": "gzip, deflate, br",
                        "Accept-Language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7",
                        "Cache-Control": "max-age=0",
                        "Connection": "keep-alive",
                        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
                    })
                    i3 = session.post(url=new_url)
                    # print(i3.text)
                    i3.encoding = i3.apparent_encoding
                    i4= i3.text.replace('<br>','').replace('<br/>','').replace('<br />','').replace('<BR>','')
                    # print(i4)
                    soup2 = BeautifulSoup(i4, features='html.parser')
                    # print(soup2)

                    targets = soup2.find('article',{'class':'ndArticle_leftColumn'})
                    title = targets.find('h1').get_text()
                    # print(title)
                    t1 = targets.find('div',{'class':'ndArticle_creat'}).get_text()
                    t2=t1.replace("出版時間：", "")
                    time = t2 + '_' +  str(count)
                    count += 1
                    # print(time)
                    text_auth = targets.find('div',{'class':'ndArticle_margin'})
                    # while text_auth.BR:
                    #     text_auth.BR.decompose()
                    text_auth2 = text_auth.prettify()
                    soup3 = BeautifulSoup(text_auth2, features='html.parser')
                    # print(soup3.get_text())
                    # print(ResultSet(text_auth2).prettify())
                    text66 = soup3.find_all('p')
                    text=""
                    for i in text66:
                        if i.string:
                            text += i.string
                    text2 = text.split()
                    text3 = "".join(text2)
                    # print(text3)


                   # patterns = re.compile(r'下載「蘋果新聞網APP」')
                   # ans = patterns.findall(text66)
                   # print(ans)
                   # pattern = re.compile(r'。記者.{2,7}')
                    patterns = re.compile(r'【.{2,11}╱.+報導】')
                    ans = patterns.findall(text3)
                    pattern = re.compile(r'。記者.{2,7}')
                    a1 = pattern.findall(text3)
                    if ans == []:
                        if a1 != []:
                            author = a1[0][3:]
                            # print('author:' + author )
                        else:

                            author = ""
                            # print('author:' + author)

                    else:
                        a = ans[0].split("╱")
                        author = a[0][1:]
                        # print ('author:'+author)


                #<div class="ndgKeyword"><h4>關鍵字</h4><



                # content = {}
                    dic = {}
                    dic['title'] = title
                    dic['time'] = time
                    dic['author'] = author
                    dic['text'] = text3
                    dic['url'] = new_url
                    dic['tags'] = ''
                    dic['type_list'] = type_list
                    dic['source'] = '蘋果'
                    dic['views'] = ''
                    dic['share'] = ''
                    dic['like'] = ''
                    if author:
                        conKey = time + '_' + author
                        content[conKey] = dic

                    else:
                        conKey = time + '_' + "無名氏"
                        content[conKey] = dic
                    # print(content)

                with open("C:/Users/Student/Desktop/201805_06.json", "w") as fjson:
                        json.dump(content, fjson)
                        print('.')