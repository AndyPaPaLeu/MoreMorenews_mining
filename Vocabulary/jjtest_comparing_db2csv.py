import jieba
import jieba.analyse
import requests
import pymysql
import csv


# Open database connection
conn = pymysql.connect(host='192.168.35.168'
                       ,port=3306
                       ,user='andy'
                       ,passwd='andy'
                       ,db='news')
# prepare a cursor object using cursor() method
cursor = conn.cursor()
sql = "SELECT * FROM tvbs WHERE type_final LIKE '生活'"

output_csv_file = 'C:/Users/student/Desktop/newsdata/text6_tvbs.txt'
userdict_txt = "C:/Users/Student/Desktop/news/tags_set.txt"
stop_txt = ''

try:
   # Execute the SQL command
   cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   with open(output_csv_file, 'w', encoding='utf_8_sig', newline='') as wbb:  # 寫成csv
       with open(userdict_txt, 'r', encoding='utf8') as stopword:  # (此處可用萬用辭庫(功用:篩選未知詞) or  停用詞庫(功用:篩選關鍵字))
           stop = stopword.readlines()
           stopwords = []
           for i in stop:
               stopwords.append(i.replace('\n', ''))

           writer = csv.writer(wbb, delimiter=',')

           for row in results:
               if row[0] == r'title':
                   continue
               text = row[0] + '，' + row[3]

               word = jieba.cut(text)
               result1 = [i for i in word]
               result2 = set(result1) - set(stopwords)
               writer.writerow(result1)
               writer.writerow(result2)
               print(">")
               all_len = len(result1)
               final_len = len(result2)
               wbb.write(
                   str(all_len) + "=>" + str(final_len) + '  ' + str(int(final_len / all_len * 100)) + "%" + '\n\n')

except:
# # Rollback in case there is any error
    print('unable to fetch data')
