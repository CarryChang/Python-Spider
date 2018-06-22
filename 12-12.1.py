# coding=utf-8
from urllib import request
from bs4 import BeautifulSoup
from selenium import webdriver
import pymysql
import time
import random
import datetime

def gethtml(url):
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
    html=request.urlopen(request.Request(url,headers=head)).read().decode('utf-8')
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
            html=gethtml(t2)
            soup=BeautifulSoup(html,'lxml').select('div ul li a')
            for L in soup:
                #循环各个元素
                try:
                    T55=L.get('href')
                    if T55.startswith('./'):
                        print(L.text+'   '+'\n'+'地址为：'+t2+T55)
                        time.sleep(1)
                        driver.get(t2+T55)
                        driver.set_page_load_timeout(5)
                        time.sleep(1)
                        WebElement2 = driver.find_element_by_class_name('ly')
                        WebElement3 = driver.find_element_by_id('tex')
                        WebElement4 = driver.find_element_by_class_name('bj')
                        sql = "INSERT INTO `big6`(标题,链接,文章信息,内容,编辑) VALUES(%s,%s,%s,%s,%s)"
                        cursor.execute(sql,(L.text,t2+T55,WebElement2.text,WebElement3.text,WebElement4.text))
                        cnn.commit()
                        print('success')
                except Exception as e:
                    pass

            #对后续网页进行翻页
            for page in range(1,num):
                try:
                    url11=gethtml(t2+'index_'+'{0}'.format(page)+'.shtml')
                    soup_links1 = BeautifulSoup(url11,'lxml').select('div ul li a')
                    for link1 in soup_links1:
                        #循环各个元素
                        t22=link1.get('href')
                        if t22.startswith("./"):
                            print(link1.text+'   '+'\n'+'地址为：'+t2+t22)
                            time.sleep(1)
                            driver.get(t2+t22)
                            driver.set_page_load_timeout(5)
                            time.sleep(1)
                            WebElement2 = driver.find_element_by_class_name('ly')
                            WebElement3 = driver.find_element_by_id('tex')
                            WebElement4 = driver.find_element_by_class_name('bj')
                            sql = "INSERT INTO `big6`(标题,链接,文章信息,内容,编辑) VALUES(%s,%s,%s,%s,%s)"
                            cursor.execute(sql,(Link1.text,t2+t22,WebElement2.text,WebElement3.text,WebElement4.text))
                            cnn.commit()
                            print('success')
                except Exception as e:
                    pass


#主控函数
if __name__ == '__main__':
    starttime=datetime.datetime.now()
    #数据库操作
    cnn = pymysql.connect(host="localhost",user="root",password="9527",db="test",charset="utf8")
    cursor = cnn.cursor()
    cursor.execute("DROP TABLE IF EXISTS big6")
    createTab = """CREATE TABLE big6(
        编号 INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        标题 VARCHAR(100) NOT NULL,
        链接 VARCHAR(500) NOT NULL,
        文章信息 VARCHAR(100) NOT NULL,
        内容 LONGTEXT NOT NULL,
        编辑  VARCHAR(50) NOT NULL
    )"""
    cursor.execute(createTab)

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
    url3='http://dangjian.com/djw2016sy/'
    driver =webdriver.PhantomJS()
    num=int(input('页码数：\n'))
    #党建网信息爬虫入口
    html3=gethtml(url3)
    time.sleep(1)
    dangjian(html3)
    #输出爬虫耗时
    endtime=datetime.datetime.now()
    print('所用时间为：')
    print(endtime-starttime)


