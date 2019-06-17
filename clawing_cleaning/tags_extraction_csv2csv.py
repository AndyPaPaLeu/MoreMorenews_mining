import jieba
import csv
import jieba.analyse

with open("C:/Users/PeiYu/Desktop/news/data/newtalk_2019.csv" , 'r' , encoding='utf8') as wb:
    with open("C:/Users/PeiYu/Desktop/news/data/text.csv", 'w', encoding='utf_8_sig', newline='') as wbb:
        csvlist = csv.reader(wb,delimiter=',')
        cont = ''
        for i in csvlist:
            if i[0] == r'title':
                continue
            cont+=i[0]+'___'+i[3]+'\n' #吃str，切\n


# # 無使用停用詞與字典
#         writer = csv.writer(wbb,delimiter=',')
#         for x, w in jieba.analyse.extract_tags(cont,topK=100, withWeight=True):
#             #result= [x,w] 要權重
#             result = [x]
#             writer.writerow(result)


# # 使用外部字典
#         writer = csv.writer(wbb,delimiter=',')
#         jieba.load_userdict("C:/Users/Student/Desktop/pycharm/venv36/userdict.txt")
#         for x, w in jieba.analyse.extract_tags(cont,topK=100, withWeight=True):
#             #result= [x,w] 要權重
#             result= [x]
#             writer.writerow(result)


# # 使用外部字典+停用詞使用
#         writer = csv.writer(wbb,delimiter=',')
#         jieba.load_userdict("C:/Users/Student/Desktop/pycharm/venv36/userdict.txt")
#         jieba.analyse.set_stop_words('C:/Users/Student/Desktop/pycharm/venv36/text/stop_words.txt')
#         for x, w in jieba.analyse.extract_tags(cont, topK=100, withWeight=True):
#             #result= [x,w] 要權重
#             result= [x]
#             writer.writerow(result)

# 使用外部字典+停用詞使用+IDF影響(IDF為空，原有內建)
        writer = csv.writer(wbb, delimiter=',')
        jieba.load_userdict("C:/Users/PeiYu/Desktop/news/tags_set.txt")
        jieba.analyse.set_stop_words('C:/Users/PeiYu/Desktop/news/hard.txt')
        #jieba.analyse.set_idf_path('C:/Users/Student/Desktop/pycharm/venv36/text/idf.txt')
        for x, w in jieba.analyse.extract_tags(cont, topK=500, withWeight=True):
            # result= [x,w] 要權重
            result = [x]
            writer.writerow(result)

# # 使用外部字典+停用詞使用+IDF影響(IDF有資料)
#         writer = csv.writer(wbb, delimiter=',')
#         jieba.load_userdict("C:/Users/Student/Desktop/pycharm/venv36/userdict.txt")
#         jieba.analyse.set_stop_words('C:/Users/Student/Desktop/pycharm/venv36/text/stop_words.txt')
#         jieba.analyse.set_idf_path('C:/Users/Student/Desktop/pycharm/venv36/text/idf2.txt')
#         for x, w in jieba.analyse.extract_tags(cont, topK=100, withWeight=True):
#             # result= [x,w] 要權重
#             result = [x]
#             writer.writerow(result)

# #個別關鍵字提取
#         writer = csv.writer(wbb, delimiter=',')
#         conts = cont.split('\n')
#         for i in conts:
#             if i:
#                 title =i.split('___')[0]
#                 result = jieba.analyse.extract_tags(i, topK=100, withWeight=False, allowPOS=())
#                 result.insert(0, title)
#                 writer.writerow(result)
