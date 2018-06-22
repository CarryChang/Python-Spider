# coding=utf-8
from urllib import request
from bs4 import BeautifulSoup
import os
from selenium import webdriver
import random
import time
def gethtml(url):
    driver =webdriver.Chrome()
    time.sleep(1)
    driver.get(url)
    driver.set_page_load_timeout(10)
    time.sleep(1)
    html=driver.page_source
    return html
def dangjian(html3):
    #解析目录页
    soup_links=BeautifulSoup(html3,'lxml').find('div',class_='nav-list')
    time.sleep(1)
    for link in soup_links.ol.children:
        if link !='\n':
            t2=link.a.get('href')
            t1=link.text
            print(t1+'部分'+'  '+'地址为：'+t2)
            # html=gethtml(t2)
            # soup=BeautifulSoup(html,'lxml').select('div ul li a')
            # for L in soup:
            #     #循环各个元素
            #     T55=L.get('href')
            #     if T55.startswith('./'):
            #         print(L.text+'   '+'\n'+'地址为：'+t2+T55)
            #     else:
            #         print(L.text+'   '+'\n'+'地址为：'+T55)

            # #对后续网页进行翻页
            # for page in range(1,num):
            #     try:
            #         url11=gethtml(t2+'index_'+'{0}'.format(page)+'.shtml')
            #         soup_links1 = BeautifulSoup(url11,'lxml').select('div ul li a')
            #         for link1 in soup_links1:
            #             #循环各个元素
            #             t22=link1.get('href')
            #             if t22.startswith("./"):
            #                 #标题查找
            #                 # if check in link1.text:
            #                 print(link1.text+'   '+'\n'+'地址为：'+t2+t22)
            #             else:
            #                 print(link1.text+'   '+'\n'+'地址为：'+t22)
            #     except Exception as e:
            #         pass


#主控函数
if __name__ == '__main__':

    #使用多代理
    User_Agent = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
        'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19']
    #随即选用UA代理防止被封
    UA = random.choice(User_Agent)
    head = {'User-Agent': UA}
    #随即选用IP代理防止被封
    IP=['219.138.58.167:3128',
        '122.72.18.35:80',
        '122.72.18.61:80',
        '112.74.94.142:3128',
        '101.37.79.125:3128',
        '122.114.27.241:808',
        '119.122.41.222:9000',
        '124.152.32.140:53281']
    #使用ip代理方法
    IP=random.choice(IP)
    proxies={'proxies':IP}
    proxy={'https':proxies}
    proxy_support =request.ProxyHandler(proxy)
    opener =request.build_opener(proxy_support)
    request.install_opener(opener)
    #开始统计爬虫启动的时间
    starttime=time.clock()
    # num=int(input('请输入每个模块您要循环的页码数(即是每个模块对应网页的深度):\n'))
    #党建网信息地址
    url3='http://dangjian.com/djw2016sy/'
    #党建网信息爬虫入口
    html3=gethtml(url3)
    time.sleep(1)
    dangjian(html3)
    #输出爬虫耗时
    endtime=time.clock()
    print('所用时间为：')
    print(endtime-starttime)
    os.system('pause')

