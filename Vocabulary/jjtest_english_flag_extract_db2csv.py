import jieba
import jieba.analyse
import requests
import pymysql
import csv
import re

# Open database connection
conn = pymysql.connect(host='192.168.35.168'
                       ,port=3306
                       ,user='andy'
                       ,passwd='andy'
                       ,db='news')
# prepare a cursor object using cursor() method
cursor = conn.cursor()
sql = "SELECT * FROM newtalk WHERE type_final LIKE '生活'"

output_csv_file = 'C:/Users/student/Desktop/words/text66.txt'
userdict_txt = "C:/Users/Student/Desktop/words/userdict525.txt"
stop_txt = 'C:/Users/Student/Desktop/words/stopword525.txt'

try:
    # Execute the SQL command
    cursor.execute(sql)
    # Fetch all the rows in a list of lists.
    data = cursor.fetchall()
    with open(output_csv_file, 'w', encoding='utf_8_sig', newline='') as wbb:  # 寫成csv
       with open(userdict_txt, 'r', encoding='utf8') as stopword:  # (此處可用萬用辭庫(功用:篩選未知詞) or  停用詞庫(功用:篩選關鍵字))
           stop = stopword.readlines()
           stopwords = []
           for i in stop:
               stopwords.append(i.replace('\n', ''))


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
               print(result1)
               result2 = list(map(sub_chi, result1))

               # result2 = pattern.findall(result1)
               # result2 = set(result1)-set(stopwords)
               # print(result1)
               print(result2)
               # writer.writerow(result1)
               result_txt = ''.join(result2) + '\n'
               wbb.write(result_txt)

               # writer.writerow(result2)
               print(">")
               # all_len = len(result1)
               # final_len = len(result2)
               # wbb.write(str(all_len)+"=>"+str(final_len)+'  '+str(int(final_len/all_len*100))+"%"+'\n\n')

except:
# # Rollback in case there is any error
    print('unable to fetch data')
