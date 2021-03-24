# pip install pandas
# pip install pandasql
# pip install jieba
# pip install wordcloud
import pandas as pd
import pandasql as ps
import glob
import matplotlib.pyplot as plt

from IPython.core.pylabtools import figsize


def start():
    print('')
    print('~~~~😊家庭物品位置记录器·首页~~~~~~')
    print('')
    actions = ['查看物品位置信息', '查看区域和位置', '补全excel', '调查重复物品、生成词云', '退出']
    print('---------功能----------')
    i = 0
    for a in actions:
        print(i, '.' + a)
        i += 1
    action = int(input('请输入数字：'))
    checkAct(actions, action)
    print('')


def searchLoc():
    print('')
    print('---------☀查看物品位置信息----------')
    print('')
    target = input('输入物品名称,输入r返回：')
    if target != 'r':
        figsize(10, 5)
        viewImg(target)
        sqlq = "select * from maindf where 物品 like '%" + target + "%'"
        ret = ps.sqldf(sqlq)
        print(ret)
        repeat = input('是否继续搜索？[y/n]')
        while repeat != 'stop':
            if repeat == 'y':
                repeat == 'stop'
                searchLoc()
                return
            elif repeat == 'n':
                repeat == 'stop'
                start()
                return
            else:
                repeat = input('是否继续搜索？[y/n]')
    else:
        start()
        return


def look(place, file):
    target = input('搜索' + place + '名称：')
    proce = "select * from maindf where 区域 like '%" + target + "%' OR 位置 like '%" + target + "%'"
    if file == 'placedf':
        figsize(40, 20)
        viewImg(target)
        proce = "select * from maindf" + " where " + place + " like '%" + target + "%'"
    result = ps.sqldf(proce)
    print(result)
    repeat = input('是否继续搜索？[y/n]')
    while repeat != 'stop':
        if repeat == 'y':
            repeat == 'stop'
            look(place, file)
            return
        elif repeat == 'n':
            repeat == 'stop'
            searchIt()
            return
        else:
            repeat = input('是否继续搜索？[y/n]')


def viewImg(target):
    tar_path = imgFolder + '\\*' + target + '*.*'
    files = glob.glob(tar_path,
                      recursive=True)
    for f in files:
        im = plt.imread(f)
        plt.imshow(im)
        plt.axis('off')
        plt.show()


def check2(action2, actions2):
    wait = 0
    while wait != 1:
        if action2 == 0:
            wait = 1
            look('区域', 'placedf')
        elif action2 == 1:
            wait = 1
            look('区域或位置', 'maindf')
        elif action2 == 2:
            wait = 1
            look('位置', 'maindf')
        elif action2 == 3:
            wait = 1
            start()
            return


def searchIt():
    print('')
    print('-------------------🌙查看区域和位置--------------------')
    print('**所有区域和位置总览，超出50条的部分请使用搜索查看**')
    print(placedf[:50])
    print('**所有区域和位置总览结束**')
    actions2 = ['搜索区域的位置信息（附图）', '搜索区域或位置的物品', '搜索位置的物品', '返回']
    print('---------功能----------')
    i = 0
    for a in actions2:
        print(i, '.' + a)
        i += 1
    action2 = int(input('请输入数字：'))
    check2(action2, actions2)


def fillForm():
    print('')
    print('-------------------🐟补充没有填写区域的Excel文件--------------------')
    sqlstr = "select * from maindf where 区域 is NULL"
    res = ps.sqldf(sqlstr)
    if res.empty == False:
        print('察觉到如下没有填写区域的实例：')
        print(res)
        sqlstr = "select distinct p.区域\
                , r.位置\
                from placedf p join res r on p.位置 = r.位置;"
        res2 = ps.sqldf(sqlstr)
        print('如果进行修改，改动如下：')
        print(res2)
        wait = 0
        while wait == 0:
            ask = input('是否进行修改？(如要进行修改请确保原文件已经关闭)[y/n]：')
            if ask == 'y':
                wait = 1
                sqlstr = "select p.区域\
                        , m.位置\
                        , m.物品\
                        from placedf p join maindf m on p.位置 = m.位置;"
                res3 = ps.sqldf(sqlstr)
                res3.to_excel(main, index=False)
                print('成功将结果写入' + main)
            elif ask == 'n':
                wait = 1
                print('不改了')
    else:
        print('没有需要补充的')
    start()
    return


def cloud(list_all):
    import jieba
    empty_str = " "
    str_all = empty_str.join(list_all)
    seg_list = jieba.cut(str_all, cut_all=False)
    object_list = []
    for word in seg_list:
        if word != ' ' and word != '\xa0':
            object_list.append(word)
    import wordcloud
    w = wordcloud.WordCloud(width=1000,
                            height=700,
                            background_color='white',
                            font_path='STZHONGS.TTF')
    str_empty = " "
    str_all2 = str_empty.join(object_list)
    w.generate(str_all2)
    import datetime
    cloudName = '词云' + str(datetime.date.today()) + '.png'
    w.to_file(cloudName)
    print('下载完毕')
    figsize(40, 20)
    im = plt.imread(cloudName)
    plt.imshow(im)
    plt.axis('off')
    plt.show()


def freqWords():
    print('------------调查重复出现的物品-----------')
    splidf = maindf['物品'].str.split('、')
    list_all = []
    for i in splidf[:-1]:
        list_all += i
    import numpy as np
    num = 1000000
    summary = dict(zip(*np.unique(list_all, return_counts=True)))
    summary = dict(sorted(summary.items(), key=lambda d: d[1], reverse=True))
    import itertools
    print('物品的出现次数排名如下：')
    summary = dict(itertools.islice(summary.items(), 10))
    print(summary)
    wait = 0
    while wait == 0:
        ask = input('此处有一份词云报告，是否下载？[y/n]')
        if ask == 'y':
            wait = 1
            cloud(list_all)
        elif ask == 'n':
            wait = 1
    print('')
    print('返回上级界面......')
    start()
    return


def checkAct(actions, action):
    if action == 0:
        searchLoc()
    elif action == 1:
        searchIt()
    elif action == 2:
        fillForm()
    elif action == 3:
        freqWords()
    elif action == 4:
        print('选择了' + actions[action])
        print('自己关掉')
        return

# 开始
main = 'sample_main.xlsx'
maindf = pd.read_excel(main,header=0)
place = 'sample_place.xlsx'
placedf = pd.read_excel(place,header=0)
imgFolder = 'sample_image'
start()

