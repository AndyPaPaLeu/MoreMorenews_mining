# # 痞客幫
import requests
from bs4 import BeautifulSoup
import re


##設立方法
def CrawlingNews (url):
    print(">>")
    ## 抓取 [下一頁] 的尾部連結
    response = requests.get(url=url)                                    #以requests的get承接url
    response.encoding = response.apparent_encoding                      #設定endoding與顯示的encoding相同
    soup = BeautifulSoup(response.text, features='html.parser')           #將response以.text獲得文檔，再用好湯接，宣告為html型式解讀
    nextpage_target = soup.find('div',{'class':'search-pagination'})         #找到唯一的<div> class=目標
    nextpage_tag = nextpage_target.find('a',{'class':'page-next'})          #找到唯一的<a> class=目標
    nextpage_link = nextpage_tag.attrs.get('href')                       #取得<a>  attrs中，href屬性內容(link)
    print(nextpage_link)

    ## 抓取 [所需資訊]
    txt_target = soup.find('div',{'class':'inner'})
    nextpage_tag = txt_target.find_all('li',{'class':'search-list'})
    print(">")
    for i in nextpage_tag:
        a = i.find('a')
        if a:
            link = a.attrs.get('href')
            title = i.find('li',{'class':'search-title'}).find('a').attrs.get('title')             #因為有些文章有標籤內文字，有些沒有，保險起見，直接找到目標list中的a標籤，獲取他的title
            text = i.find('li', {'class': 'search-desc'}).get_text().strip()                  #li中有文字，以get_text獲得所有文字，並以stip去除text中的\n
            veiwer_target = i.find('span', {'class': 'search-views'})
            veiwer = veiwer_target.find('span').string
            posttime = i.find('span',{'class':'search-postTime'}).string
            info = {'postTime':posttime,'title':title,'text':text,'veiwer':veiwer,'link':link}   #以dictionary儲存資訊
            content.append(info)                                                         #以append將新資訊塞入list中
            print(info)
    return nextpage_link #回傳 [下一頁] 尾部連結

##啟程~!
url='https://www.pixnet.net/searcharticle?g-recaptcha-response=03AOLTBLRoeLCJbwT_Pm0sAXGWT2NERNcuzDqa4_nQOZ9oqirQbIJTLqvKAmGu76xdQ6OFPc58HSWQxRn-BFstbNEJstnaIM4-4UjuZYQ44DpxZTX-YfltF_9DWkLsgYiBD-P6cUp1Vf3AMvI6_vqftjLpDLiUiUgkgwwv4pDCAJj8QOJGckyZoqHBf0a9_oVb8yxqXquj8DsUlWeP69UxQwNy0CB1TJY4PVIl526FuBseIkT0-vKMUhsQmB7klCX76WeOQN3VmYgUaYcinyjrnFSvPIceX-zCabLRgsVEE1HQFd3ToTdWTG2ViMbXl2l5kW7UcQBAPRUQ&q=%E6%97%A5%E6%9C%AC%E6%97%85%E9%81%8A&page=1'
content =[]
while True:
    nextpage_link = CrawlingNews(url)
    url = 'https://www.pixnet.net'+nextpage_link
    if re.search('searcharticle',nextpage_link) is None:  #最後會抓到javascritp:;，但都無法比對，所以使用正則判斷是否有searcharticle關鍵字，若無會回傳None
        break


print(content) ##檢視結果