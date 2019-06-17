import jieba
import openpyxl
import jieba.analyse

wb = openpyxl.load_workbook("C:/Users/PeiYu/Desktop/newtalk_2019.xlsx")
sheet = wb.get_sheet_names()
sheet_first = sheet[0]
ws = wb.get_sheet_by_name(sheet_first)

rows = ws.rows
columns = ws.columns



#[0]title、[1]date、[2]author、[3]text、[4]url、[5]tags、[6]type_list、[7]source、[8]views、[9]share、[10]like

# ##多篇關鍵字提取
# cont =""
# for i in list(columns)[0]:
#   cont+=i.value+'\n'
# print(cont)
# for x, w in jieba.analyse.extract_tags(cont, withWeight=True):
#     print('%s %s' % (x, w))

#個別關鍵字提取
# cont =""
for i in list(columns)[3]:
  if i.value:
    print(i.value)
    print(jieba.analyse.extract_tags(i.value, topK=20, withWeight=False, allowPOS=()))
