# -*- coding: UTF-8 -*-

#json to excel
import json
import openpyxl
import re

workbook = openpyxl.Workbook()
sheet = workbook.worksheets[0]
listtitle=["title","date","author","text","url","tags", "type_list","source","views","share","like"]
sheet.append(listtitle)
ILLEGAL_CHARACTERS_RE = re.compile(r'[\000-\010]|[\013-\014]|[\016-\037]')
ILLEGAL_CHARACTERS_EMOJI = re.compile(u'[\U00010000-\U0010ffff]')
with open ("C:/Users/PeiYu/Desktop/data2/newtalk_2018_0406.json","r",encoding='utf8') as jsonfile:
    data = json.load(jsonfile)
    for i in data.keys():

        # -------刪除不要的文章-------
        if "創夢實驗室》" in data[i]['title']:
            continue
        if "親情芬多精》" in data[i]['title']:
            continue
        if "職場多巴胺》" in data[i]['title']:
            continue
        if "小鎮之旅》" in data[i]['title']:
            continue
        if "立院LIVE》" in data[i]['title']:
            continue
        if not data[i]['text']:
            continue

        # -------轉換tags、type--------
        tags = ""
        if data[i]['tags']:
            for tagstring in data[i]['tags']:
                if tagstring == data[i]['tags'][0]:
                    type_list = tagstring
                    continue
                if tagstring == "nownews":
                    continue
                tags = tags + tagstring + "、"
            tags = tags[0:-1]
            # print(tags)

        # type_list = ""
        # if data[i]['type_list']:
        #     for type_liststring in data[i]['type_list']:
        #         type_list = type_list + type_liststring + "、"
        #     type_list = type_list[0:-1]
        #     # print(type_list)

        rawTitle = data[i]['title']
        pattern = re.compile(r'^.{0,9}((戰報)|(觀點)|(投書)|(補選)|(財訊)||(新聞)|(LIVE)|(點將錄)|(最新)|(專訪)|(快訊)|(側寫)|(焦點人物))》')
        title = re.sub(pattern,"",rawTitle)
        pattern = re.compile(r"(((（|\()圖(）|\)))|((（|\()影(）|\)))| (羽球／)|(更新)|(NOW人物／)|(（獨家）)|(影／)|(影）)|(羽球／)|((（|\(){0,1}直播(）|\))))")
        title = re.sub(pattern,"",title)
        print(title)

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
        pattern = re.compile(r'(（|\()記者.{0,10}(/|／).{0,10}(）|\))')
        text = re.sub(pattern, "", text)
        pattern = re.compile(r'(http://|https://|www)[a-zA-Z0-9\\./_]+')
        text = re.sub(pattern, "", text)
        pattern = re.compile(r'(▲)')
        text = re.sub(pattern, "", text)

        row = [title, data[i]['time'].split('_')[0], author, text, data[i]['url']+" ", tags, type_list, data[i]['source'], data[i]['like'], data[i]['share'], data[i]['views']]
        count = 0
        for i in row:
            row[count] = ILLEGAL_CHARACTERS_RE.sub(r'', row[count])
            row[count] = ILLEGAL_CHARACTERS_EMOJI.sub(r'', row[count])
            count += 1
        sheet.append(row)
workbook.save("C:/Users/PeiYu/Desktop/data2/newtalk_2018_0406.xlsx")

