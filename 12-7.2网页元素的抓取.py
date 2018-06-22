# coding=utf-8
import datetime
from selenium import webdriver
import pymysql
import time
def getnext(a,next):
    al = len(a)
    next[0] = -1
    k = -1
    j = 0
    while j < al-1:
        if k == -1 or a[j] == a[k]:
            j += 1
            k += 1
            next[j] = k
        else:
            k = next[k]
def KmpSearch(a,b):
    i = j = 0
    al = len(a)
    bl = len(b)
    while i < al and j < bl:
        if j == -1 or a[i] == b[j]:
            i += 1
            j += 1
        else:
            j = next[j]
    if j == bl:
        return i-j
    else:
        return -1



#####################################################################################
#页面元素抓取
#开始下载页面
def gethtml(url):
    time.sleep(1)
    driver.get(url)
    time.sleep(1)
    WebElement1 = driver.find_element_by_xpath('html/body/div[7]/div[1]/div/h1')
    WebElement2 = driver.find_element_by_class_name('sou')
    WebElement3 = driver.find_element_by_class_name('show_text')
    WebElement4 = driver.find_element_by_class_name('edit')
    sql = "INSERT INTO `article7`(标题,链接,文章信息,内容,编辑) VALUES(%s,%s,%s,%s,%s)"
    cursor.execute(sql,(WebElement1.text,url,WebElement2.text,WebElement3.text,WebElement4.text))
    cnn.commit()
    print('success')


#####################################################################################
if __name__ == '__main__':
    starttime=datetime.datetime.now()
    #数据库操作
    cnn = pymysql.connect(host="localhost",user="root",password="9527",db="test",charset="utf8")
    cursor = cnn.cursor()
    cursor.execute("DROP TABLE IF EXISTS article7")
    createTab = """CREATE TABLE article7(
        编号 INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        标题 VARCHAR(50) NOT NULL,
        链接 VARCHAR(500) NOT NULL,
        文章信息 VARCHAR(50) NOT NULL,
        内容 TEXT NOT NULL,
        编辑  VARCHAR(20) NOT NULL
    )"""
    cursor.execute(createTab)
#############################################################################################
    #输入你要加链接的个数
    i=0
    num1=input('输入你要加进链接的个数,并按回车键结束或者使用内置的地址不输入直接按回车键：\n')
    if num1 !=(''):
        #######回车直接输出
        while i<int(num1):
            i+=1
            count=0
            #判断的主要功能就是有的不操作，没有的就加进去
            URL=input('第%s个地址：\n'%i)
            if URL !=(''):
                #KMP找出已存在的地址
                L1= open('C:/Users/Administrator/Desktop/使用搜索引擎/党建地址.txt')
                for a in L1:
                    b =URL
                    next = [0]*len(b)
                    getnext(b,next)
                    t=KmpSearch(a,b)
                    if  t >-1:
                        count+=1
                if count!=0:
                    print('您输入的地址已存在于内定的链接中，无需添加')
                    # X=input('Enter Ur need:')
                    # num=input('输入要翻页数目：\n')
                    print('地址一览：\n')
                    R= open('C:/Users/Administrator/Desktop/使用搜索引擎/党建地址.txt','r')
                    for url in R:
                        if url.startswith('http'):
                            print(url)
                            #         driver =webdriver.Chrome()
                            #         time.sleep(1)
                            #         html1=gethtml(url)
                            #         time.sleep(1)
                            #         printhtml(html1)
                            # driver.close()
                else:
                    print('您输入的地址属于新的链接已经加到地址链表，链接详情请查看C:/Users/Administrator/Desktop/使用搜索引擎对应的txt文件')
                    L = open('C:/Users/Administrator/Desktop/使用搜索引擎/党建地址.txt','a',encoding='utf-8')
                    L.write('\n'+URL)
                    print('地址已经存到了链接列表之中！')
                    # X=input('Enter Ur need:')
                    # num=input('输入要翻页数目：\n')
                    print('地址一览：\n')
                    R= open('C:/Users/Administrator/Desktop/使用搜索引擎/党建地址.txt','r')
                    for url in R:
                        if url.startswith('http'):
                            print(url)
                            #         driver =webdriver.Chrome()
                            #         time.sleep(1)
                            #         html1=gethtml(url)
                            #         time.sleep(1)
                            #         printhtml(html1)
                            # driver.close()
            else:
                print('地址一览：\n')
                R= open('C:/Users/Administrator/Desktop/使用搜索引擎/党建地址.txt','r')
                for url in R:
                    if url.startswith('http'):
                        print(url)
    else:
        # X=input('Enter Ur need:')
        # num=input('输入要翻页数目：\n')
        print('地址一览：\n')
        R= open('C:/Users/Administrator/Desktop/使用搜索引擎/党建地址.txt','r')
        for url in R:
            if url.startswith('http'):
                print(url)
                driver =webdriver.PhantomJS()
                time.sleep(1)
                gethtml(url)
                time.sleep(1)
                driver.close()
    cursor.close()
    cnn.close()
    endtime=datetime.datetime.now()
    print('所用时间为：')
    print(endtime-starttime)

