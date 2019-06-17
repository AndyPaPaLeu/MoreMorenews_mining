# coding:utf8
import jieba
import jieba.analyse
import csv
import math
import re
import pandas as pd
import pymysql

# Open database connection
conn = pymysql.connect(host='192.168.35.168'
                       ,port=3306
                       ,user='andy'
                       ,passwd='andy'
                       ,db='news')
# prepare a cursor object using cursor() method
cursor = conn.cursor()
sql = "SELECT * FROM news_test_per2000 WHERE type_final LIKE '政治'"

cursor.execute(sql)
results = cursor.fetchall()

'''
#######################   findall   #########################

final_dic={}
for news in results: 
    
    #combine the text
    text = news[0]+news[1]
    #print(text)
    
    #encode the tags
    tags = news[5].split('、')
    for tag in tags: 
        print(tag)
        pattern = re.compile(tag)   # 查找数字
        word_tf = len(pattern.findall(text))
        print(word_tf)
        print(pattern.findall(text))
        final_dic[tag] = final_dic.get(tag,0) + word_tf

print(final_dic)
############################################################
'''
'''
###############   get result for update   ##################
#result_list=[]  #1.1批次更新時使用
for news in results: 
    #combine the text
    text = news[0]+news[1]
    final_dic={}
    tags = news[3].split('、')
    
    # 使用外部字典+停用詞使用
    jieba.load_userdict("C:/Users/Student/Desktop/new/userdict0602.txt")
    jieba.analyse.set_stop_words('C:/Users/Student/Desktop/new/stopword0601.txt')
    max_weight = 0.0
    for x, w in jieba.analyse.extract_tags(text, topK=20, withWeight=True):  ## withWeight=True: get weight
        if w > max_weight:
            max_weight = w
        final_dic[x]=final_dic.get(x,0.0)+w
    for tag in tags:
        final_dic[tag]=max_weight
    print(final_dic)        
    sql = 'UPDATE news_test_per2000 SET weight = "'+str(final_dic)+'" where title = "'+news[0]+'"'
    print(sql)
    cursor.execute(sql)
    print(cursor.rowcount)

     
    #result_list.append(str(final_dic))    #1.2批次更新時使用
    #print(result_list)        
    
    conn.commit()
conn.close()    


############################################################
'''

###############   bubble   ##################
#select tags, weight from news_total
x=(("國民黨、吳敦義、黨主席、黨主席選舉","{'漢堡': 0.5803285195582524, '電影院': 0.5803285195582524, '不合格': 0.34819711173495144, '何修蘭': 0.34819711173495144, '雜物': 0.34819711173495144, '影城': 0.28420027938582526, '外食': 0.23213140782330097, '聯合稽查': 0.23213140782330097, '戲院': 0.23213140782330097, '裁罰': 0.23213140782330097, '龍翔百老匯': 0.23213140782330097, '法務局': 0.23213140782330097, '沈永華': 0.23213140782330097, '薯條': 0.23213140782330097, '熱湯': 0.23213140782330097, '濃郁': 0.23213140782330097, '食物': 0.18418123459514563, '朝代': 0.16374014584155341, '安全梯': 0.1349580354563107, '北市': 0.12429189673106797}"),("國民黨、吳敦義、黨主席、黨主席選舉、媽祖婆","{'跳鍾馗': 0.3919595902590164, '儀式': 0.3919595902590164, '鍾馗': 0.34296464147663935, '媽祖婆': 0.2939696926942623, '地藏庵': 0.20149573343442623, '男童': 0.17578071838688522, '普後押': 0.14698484634713116, '林俊': 0.14698484634713116, 'Fan': 0.14698484634713116, '原PO': 0.14698484634713116, '孤魂': 0.13290535080245902, '扮演': 0.1257086825480328, '普渡': 0.11393998075409836, '鬼門關': 0.0979898975647541, '農曆7月': 0.0979898975647541, '地藏王菩薩': 0.0979898975647541, '聖誕': 0.0979898975647541, '法會': 0.0979898975647541, '演員': 0.0979898975647541, '電影院': 0.5803285195582524, '無厘頭': 0.0979898975647541}"),)

tag_tf={}
for i in x:
    for k,v in eval(i[1]).items():
        tag_tf[k]=tag_tf.get(k,0.0)+float(v)
print(sorted(tag_tf.items(),key=lambda item:item[1])[-20:])

        
#tf_result = pd.DataFrame.from_dict(tag_tf)#.sort_values(by='col1', ascending=False)
#print(tf_result)
############################################################
    

             










