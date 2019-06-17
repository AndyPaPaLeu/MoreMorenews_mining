# coding:utf8
import jieba
import jieba.analyse
import csv
import math

input_csv_file = 'C:/Users/PeiYu/Desktop/news/data/newtalk_2019.csv'
output_csv_file = 'C:/Users/PeiYu/Desktop/news/data/text222.csv'
userdict_txt = "C:/Users/PeiYu/Desktop/newss/userdict525.txt"
stop_txt = 'C:/Users/PeiYu/Desktop/newss/stopword525.txt'

with open(input_csv_file, 'r', encoding='utf8')as csvfile: #讀csv
    with open(output_csv_file, 'w', encoding='utf_8_sig', newline='') as wbb:  #寫成csv
        data = csv.reader(csvfile)
        writer = csv.writer(wbb, delimiter=',')
        # 增加csv的讀取句數
        csv.field_size_limit(100000000)

        with open(stop_txt, 'r', encoding='utf8')as stopword:
            stop = stopword.readlines()
            stopwords=set([i.replace('\n','') for i in stop])

            jieba.load_userdict(userdict_txt)  # 載入萬用辭庫來切新聞
            idf={}
            ret=[]
            counter = 0
            for texts in data:
                counter +=1
                if texts[0] == r'title':
                    continue
                text = texts[0] + '，' + texts[3]
                words = jieba.cut(text)

                word_list =set([ word for word in words])
                ret.extend(list(word_list-stopwords))

            for word in ret:
                idf[word] = idf.get(word, 0.0) + 1.0

            for i in idf:
                idf[i] = math.log(counter/idf[i])
                result1 = i + ' ' + str(idf[i]) + '\n'
                wbb.write(result1)
            print(idf)





