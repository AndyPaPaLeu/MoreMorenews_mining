# coding:utf8
import jieba
import jieba.analyse
import csv
import re

input_csv_file = 'C:/Users/Student/Desktop/data2/newtalk_2019.csv'
output_csv_file = 'C:/Users/Student/Desktop/text22.csv'
userdict_txt = "C:/Users/Student/Desktop/words/userdict525.txt"
stop_txt = 'C:/Users/Student/Desktop/words/stopword525.txt'

with open(input_csv_file, 'r', encoding='utf8')as csvfile: #讀csv
    with open(output_csv_file, 'w', encoding='utf_8_sig', newline='') as wbb:  #寫成csv
        data = csv.reader(csvfile)

        # 增加csv的讀取句數
        csv.field_size_limit(100000000)

        with open(userdict_txt, 'r', encoding='utf8')as stopword: #(此處可用萬用辭庫(功用:篩選未知詞) or  停用詞庫(功用:篩選關鍵字))
            stop = stopword.readlines()
            stopwords=[]
            for i in stop:
                stopwords.append(i.replace('\n',''))

            writer = csv.writer(wbb, delimiter=',')

            def sub_chi(result1):
                pattern = re.compile(r'[a-zA-Z0-9]+')
                x = pattern.findall(result1)
                if x:
                   return ''.join(x)
                else:
                    return " "

            jieba.load_userdict(userdict_txt)  # 載入萬用辭庫來切新聞
            for texts in data:
                if texts[0] == r'title':
                    continue
                text = texts[0] + '，' + texts[3]

                word = jieba.cut(text)

                result1 = [i for i in word if i.isalpha() or i.isalpha()]
                result2 = list(map(sub_chi,result1))
                # result2 = pattern.findall(result1)
                # result2 = set(result1)-set(stopwords)
                # print(result1)
                print(result2)
                # writer.writerow(result1)
                result_txt = ''.join(result2)+'\n'
                wbb.write(result_txt)

                # writer.writerow(result2)
                print(">")
                # all_len = len(result1)
                # final_len = len(result2)
                # wbb.write(str(all_len)+"=>"+str(final_len)+'  '+str(int(final_len/all_len*100))+"%"+'\n\n')


