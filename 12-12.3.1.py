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
    driver =webdriver.PhantomJS()
    for link in soup_links.ol.children:
        if link !='\n':
            t2=link.a.get('href')
            t1=link.text
            print(t1+'部分'+'  '+'地址为：'+t2)
            i=0
            time.sleep(1)
            driver.get(t2)
            while i<int(num):
                try:
                    driver.set_page_load_timeout(5)
                    soup_links1 = BeautifulSoup(driver.page_source,'lxml').select('div ul li a')
                    for link1 in soup_links1:
                        #循环各个元素

                        t22=link1.get('href')
                        if t22.startswith("./"):
                            starttime1=time.clock()
                            page=gethtml(t2+t22)
                            WebElement1=BeautifulSoup(page,'lxml').find('div',class_='context-tit')
                            WebElement2=BeautifulSoup(page,'lxml').find('div',class_='ly')
                            WebElement3=BeautifulSoup(page,'lxml').find('div',id='tex')
                            sql = "INSERT INTO `big7`(标题,链接,文章信息,内容) VALUES(%s,%s,%s,%s)"
                            cursor.execute(sql,(WebElement1.text,t2+t22,WebElement2.text,WebElement3.text))
                            cnn.commit()
                            endtime1=time.clock()
                            speed=1/(endtime1-starttime1)
                            print('当前速度为：%s篇文章每秒'%speed)
                    print('################################################翻页')
                    i+=1
                    driver.find_element_by_xpath('html/body/div[3]/div/div[2]/div[2]/span[4]/a').click()
                except Exception as e:
                    pass
#主控函数
if __name__ == '__main__':
    starttime=datetime.datetime.now()
    #数据库操作
    try:
        cnn = pymysql.connect(host="localhost",user="root",password="9527",db="test",charset="utf8")
        cursor = cnn.cursor()
        cursor.execute("DROP TABLE IF EXISTS big7")
        createTab = """CREATE TABLE big7(
            编号 INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
            标题 VARCHAR(100) NOT NULL,
            链接 VARCHAR(500) NOT NULL,
            文章信息 VARCHAR(100) NOT NULL,
            内容 LONGTEXT NOT NULL
        )"""
        cursor.execute(createTab)
    except:
        print('\n错误：数据库连接失败')
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
    num=input('页码数：\n')
    url3='http://dangjian.com/djw2016sy'
    #党建网信息爬虫入口
    html3=gethtml(url3)
    time.sleep(1)
    dangjian(html3)
    #输出爬虫耗时
    endtime=datetime.datetime.now()
    print('所用时间为：')
    print(endtime-starttime)


