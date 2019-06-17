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
sql = "SELECT * FROM news_total WHERE type_final LIKE '國際'"


try:
   # Execute the SQL command
   cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   print('>')
   content=''
   for row in results:
       if row[0] =='title':
          continue
       cont = row[0]+'。'+row[3]+'\n'
       content = content + cont

   with open("C:\\Users\\Student\\Desktop\\new\\text6_perA.txt", 'w', encoding='utf_8_sig', newline='') as wbb:
       writer = csv.writer(wbb, delimiter=',')
# 使用外部字典+停用詞使用+IDF影響(IDF有資料)
       jieba.load_userdict("C:\\Users\\Student\\Desktop\\new\\userdict0602.txt")
       jieba.analyse.set_stop_words('C:\\Users\\Student\\Desktop\\new\\stopword0601.txt')
       jieba.analyse.set_idf_path('C:\\Users\\Student\\Desktop\\new\\num\\idf.txt')
       '''
       for x, w in jieba.analyse.extract_tags(content, topK=1000, withWeight=True):
            # result= [x,w] 要權重
           print(x,w)
           result = [x]
           writer.writerow(result)
           '''

 #個別關鍵字提取
         #writer = csv.writer(wbb, delimiter=',')
 
       conts = content.split('\n')
       for i in conts:
           if i:
               result = jieba.analyse.extract_tags(i, topK=20, withWeight=False, allowPOS=())
               writer.writerow(result)

except:
# # Rollback in case there is any error
    print('unable to fetch data')
