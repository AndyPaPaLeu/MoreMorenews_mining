

import datetime

day_range=7
tg_type='政治'


關鍵熱詞、第二層熱詞  day_range(預設為7天)  tg_type(預設為所有類別) func_num = 1

def select(req, day_range=7, tg_type=None, func_num=1, tags=None):
    timelists=[(datetime.datetime.now()-datetime.timedelta(days=(i))).strftime('%Y/%m/%d') for i in range(day_range)]
    if tg_type == None:
        query_set=News_total.objects.filter(time__in=timelists).order_by('-time')
    if tg_type != None:
        query_set=News_total.objects.filter(time__in=timelists,type=tg_type).order_by('-time')
    if tags != None:
        tg_tags = tags//取關鍵字
        query_set = News_total.objects.filter(time__in=timelists, type=tg_type, final_tags__contains=tg_tags).order_by('-time')

    func={1:'熱詞',2:'第二'}
    tg_func = func.get(func_num,1)
    result=tg_func(query_set)

    #回傳tag熱門結果、QuerySet 至 indexj網頁
    return render(req,'index',{'result':result,'q_set':query_set})

(熱詞找tag計數)
def 熱詞(ret):
    dic = {}
    for i in ret:
        tag_text = i.value('tag')
        tags = tag_text.split('、')
        if i in dic:
            dic[i]=dic[i]+1
        else:
            dic[i]=0
    return dic

(第二)
def 第二(ret):
    dic = {'a':2}
    return dic

    #[0]title, [1]date,  [2]author,  [3]text,  [4]url,  [5]tags,  [6]type_list,  [7]source,  [8]views,  [9]share,  [10]like

