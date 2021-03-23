# pip install pandas
# pip install pandasql
import pandas
import pandasql
import glob
import matplotlib.pyplot as plt

from IPython.core.pylabtools import figsize


def start():
    print('')
    print('~~~~😊家庭物品位置记录器·首页~~~~~~')
    print('')
    actions = ['查看物品位置信息', '查看区域和位置', '补全excel', '退出']
    count = len(actions)
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
    tar_path = 'sample_image\\*' + target + '*.*'
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
    count = len(actions2)
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
                res3.to_excel(main)
                print('成功将结果写入' + main)
            elif ask == 'n':
                wait = 1
                print('不改了')
    else:
        print('没有需要补充的')
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
        print('选择了' + actions[action])
        print('自己关掉')
        return

# 开始
main = 'sample_main.xlsx'
maindf = pd.read_excel(main,header=0)
place = 'sample_place.xlsx'
placedf = pd.read_excel(place,header=0)
start()

