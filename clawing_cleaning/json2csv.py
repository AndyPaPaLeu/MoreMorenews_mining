
#json to CSV
import json
import csv
import re

with open ("C:/Users/PeiYu/Desktop/data/newtalk_2019.json","r",encoding='utf8') as jsonfile:
    data = json.load(jsonfile)
    with open("C:/Users/PeiYu/Desktop/newtalk_2019.csv", "w",encoding='utf8',newline="") as outfile:
        csv_out = csv.writer(outfile, delimiter=',')
        csv_out.writerow(["title","date","author","text","url","tags", "type_list","source","views","share","like"])
        #print(data.keys())

        for i in data.keys():
            tags=""
            if data[i]['tags']:
                for tagstring in data[i]['tags']:
                    tags = tags + tagstring + "、"
                tags = tags[0:-1]
                # print(tags)

            type_list=""
            if data[i]['type_list']:
                for type_liststring in data[i]['type_list']:
                    type_list = type_list + tagstring + "、"
                type_list = type_list[0:-1]
                # print(type_list)

            row = [data[i]['title'] , data[i]['time'].split('_')[0] , data[i]['author'] , data[i]['text'], data[i]['url']+" "  , tags , type_list , data[i]['source'] , data[i]['like'] , data[i]['share'] , data[i]['views']]
            ILLEGAL_CHARACTERS_RE = re.compile(r'[\000-\010]|[\013-\014]|[\016-\037]')
            count=0
            for i in row:
                row[count] = ILLEGAL_CHARACTERS_RE.sub(r'', i)
                count+=1

            csv_out.writerow(row)

         
         