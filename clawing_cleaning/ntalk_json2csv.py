# -*- coding: UTF-8 -*-

#json to excel
import json
import csv
import re
import os


ILLEGAL_CHARACTERS_RE = re.compile(r'[\000-\010]|[\013-\014]|[\016-\037]')
ILLEGAL_CHARACTERS_EMOJI = re.compile(u'[\U00010000-\U0010ffff]')


#-------多重轉檔-----------
FolderPath = ('C:/Users/PeiYu/Desktop/news/data/')
filenames = os.listdir(FolderPath)

paths=[]
for i in filenames:
    paths.append(FolderPath+i)
print(paths)

for i in paths:    

#-------單個轉檔----------- 
#path = 'newtalk_2019'

#--------開始-----------
    with open (i,'r',encoding='utf8') as jsonfile:
        data = json.load(jsonfile)
        csvpath = i[:-5]+ '.csv'
        print(csvpath)
        with open(csvpath,'w',encoding='utf8', newline="") as outfile:
            csv_out = csv.writer(outfile, delimiter=',')
            csv_out.writerow(["title","date","author","text","url","tags", "type_list","source","views","share","like"])
    
            for i in data.keys():
                # -------刪除不要的文章-------
                if '創夢實驗室》' in data[i]['title']:
                    continue
                if '親情芬多精》' in data[i]['title']:
                    continue
                if '職場多巴胺》' in data[i]['title']:
                    continue
                if '小鎮之旅》' in data[i]['title']:
                    continue
                if '立院LIVE》' in data[i]['title']:
                    continue
                if not data[i]['text']:
                    continue
                if data[i]['author'] == '寵毛網petsmao資訊平台':
                    continue
    
                # -------轉換tags、type--------
                tags = ""
                if data[i]['tags']:
                    if '書評' in data[i]['tags']:
                        continue
                    for tagstring in data[i]['tags']:
                        if tagstring == data[i]['tags'][0]:
                            type_list = tagstring
                            continue
                        if tagstring == "nownews":
                            continue
                        tags = tags + tagstring + "、"
                    tags = tags[0:-1]
                    # print(tags)
    
    
                #--------資料清洗--------
                rawTitle = data[i]['title']
                pattern = re.compile(r'^.{0,9}((戰報)|(觀點)|(投書)|(補選)|(財訊)||(新聞)|(LIVE)|(點將錄)|(最新)|(專訪)|(快訊)|(側寫)|(焦點人物))》')
                title = re.sub(pattern, "", rawTitle)
                pattern = re.compile(
                    r"(((（|\()圖(）|\)))|((（|\()影(）|\)))| (羽球／)|(更新)|(NOW人物／)|(（獨家）)|(影／)|(影）)|(羽球／)|((（|\(){0,1}直播(）|\))))")
                title = re.sub(pattern, "", title)
                pattern = re.compile(r'【(司改爭鋒|讀者觀點|持續|快訊|最新|新聞快照)】')
                title = re.sub(pattern, "", title)

                #print(title)
    
                rawAuthor = data[i]['author']
                pattern = re.compile(r'.+／')
                author = re.sub(pattern, "", rawAuthor)
                rawText = data[i]['text']
                pattern = re.compile(r'(\(|（)[0-9１２３４５６７８９０]{1,2}(/[0-9]{1,2}){0,1}(）|\))')
                text = re.sub(pattern, "", rawText)
                pattern = re.compile(r'▲.{0,75}(\(|（)圖.{0,1}(／|/).{0,6}(攝.{0,2}[0-9]{3,4}\.[0-9]{1,2}\.[0-9]{1,2}|攝自.{0,25}|.{0,25}照片|.{0,5}提供)(）|\))')
                text = re.sub(pattern, "", text)
                pattern = re.compile(r'▲.{1,40}(／|/){0,1}.{1,20}▲')
                text = re.sub(pattern, "", text)
                pattern = re.compile(r'▲(.+｜圖片來源：|.+直播來源：|.*(（|\().{0,10}圖.{0,40}(）|\))|.*影片來源：|.*(（|\().{0,10}來源.{0,40}(）|\))|.*(\(|（).{0,10}圖.{0,6}(／|/).{0,30}(）|\))|.{0,40}影片{0,1}：|(（|\().{0,1}記者.{0,20}(）|\)))')
                text = re.sub(pattern, "", text)
                pattern = re.compile(r'(\(|（)(圖|作者|圖片來源)：.{1,30}(）|\))')
                text = re.sub(pattern, "", text)
                pattern = re.compile(r'(圖|作者|圖片來源)：.{1,30}(）|\)|照片)')
                text = re.sub(pattern, "", text)                
                pattern = re.compile(r'(\(|（)記者.{0,10}(/|／).{0,10}(）|\))')
                text = re.sub(pattern, "", text)
                pattern = re.compile(r'(http://|https://|www)[a-zA-Z0-9\\./_]+')
                text = re.sub(pattern, "", text)
                pattern = re.compile(r'(▲)')
                text = re.sub(pattern, "", text)

                if type_list == '政治' or '選舉':
                    type_list == '政治'
                if type_list == '社會' or '環保'or '司法':
                    type_list == '社會'
                if type_list == '國際' or '中國':
                    type_list == '國際'
                if type_list == '生活' or '旅遊'or '藝文'or '美食'or '科技':
                    type_list == '生活'
                if type_list == '體育':
                    type_list == '運動'
                if type_list == '電競' or '遊戲':
                    type_list == '娛樂'
                if type_list == '經濟':
                    type_list == '財經'

                #--------資料匯出---------
                row = [title, data[i]['time'].split('_')[0], author, text, data[i]['url']+" ", tags, type_list, data[i]['source'], data[i]['like'], data[i]['share'], data[i]['views']]
                count = 0
                for i in row:
                    row[count] = ILLEGAL_CHARACTERS_RE.sub(r'', row[count])
                    row[count] = ILLEGAL_CHARACTERS_EMOJI.sub(r'', row[count])
                    row[count] = row[count].replace("\u00A0", "")
                    # row[count] = row[count].replace("　","，")
                    # row[count] = row[count].replace("\\n","")
                    # row[count] = row[count].replace("\\r","")
                    count += 1
                csv_out.writerow(row)
    
    
