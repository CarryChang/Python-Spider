# coding=utf-8
import datetime
from selenium import webdriver
from bs4 import BeautifulSoup
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
#开始下载页面
def gethtml(url):
    time.sleep(1)
    driver.get(url)
    time.sleep(1)
    try:
        WebElement = driver.find_element_by_xpath('html/body/div[4]/div[1]/div/h1')
        print('标题为：'+WebElement.text)
        WebElement1 = driver.find_element_by_xpath('html/body/div[4]/div[1]/div/p[2]')
        print('发布时间：'+WebElement1.text)
        WebElement3 = driver.find_element_by_class_name('show_text')
        print('内容为：'+WebElement3.text)

    except Exception as e:
            pass
if __name__ == '__main__':
    starttime=datetime.datetime.now()
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
                driver =webdriver.Chrome()
                time.sleep(1)
                gethtml(url)
                time.sleep(1)
                driver.close()
    endtime=datetime.datetime.now()
    print('所用时间为：')
    print(endtime-starttime)

