# coding=utf-8
from urllib import request
from bs4 import BeautifulSoup
import datetime
import random
import pymysql
def gethtml(url):
    #成功实现编码的转换
    html=request.urlopen(request.Request(url,headers=head)).read().decode('utf-8')
    return  html

def printhtml(html1):
    #解析目录页
    link_qing=BeautifulSoup(html1,'lxml').select('div ul li p a')
    for link in link_qing:
        qing=link.get('href')
        if qing.startswith('/'):
            print(link.text+'\n'+'http://www.dangjian.tsinghua.edu.cn'+qing)
            URL='http://www.dangjian.tsinghua.edu.cn'+qing
            html1=gethtml(URL)
            link_qing=BeautifulSoup(html1,'lxml').find('li',class_='cont_f_title01')
            link_qing1=BeautifulSoup(html1,'lxml').find('li',class_='ti24')
            try:
                sql = "INSERT INTO qinghua(TOPIC,LINK,INFO,CONTENT) VALUES(%s,%s,%s,%s)"
                cursor.execute(sql,(link.text,URL,link_qing.text,link_qing1.text))
                cnn.commit()
            except Exception as e:
                pass

    for page in range(2,num+1):
        try:
            url11='http://www.dangjian.tsinghua.edu.cn/publish/dangjian/'+'{0}'.format(page1)+'/index_'+'{0}'.format(page)+'.html'
            html1=gethtml(url11)
            soup_qing = BeautifulSoup(html1,'lxml').select('div ul li p a')
            for link1 in soup_qing:
                #循环各个元素
                qing=link1.get('href')
                if qing.startswith('/'):
                    print(link1.text+'\n'+'http://www.dangjian.tsinghua.edu.cn'+qing)
                    URL='http://www.dangjian.tsinghua.edu.cn'+qing
                    html1=gethtml(URL)
                    link_qing=BeautifulSoup(html1,'lxml').find('li',class_='cont_f_title01')
                    link_qing1=BeautifulSoup(html1,'lxml').find('li',class_='ti24')
                    sql = "INSERT INTO qinghua(TOPIC,LINK,INFO,CONTENT) VALUES(%s,%s,%s,%s)"
                    cursor.execute(sql,(link1.text,URL,link_qing.text,link_qing1.text))
                    cnn.commit()
        except Exception as e:
            pass




if __name__ == '__main__':
    #数据库操作
    #数据库操作
    try:
        cnn = pymysql.connect(host="localhost",user="root",password="9527",db="test",charset="utf8")
        cursor = cnn.cursor()
        cursor.execute("DROP TABLE IF EXISTS qinghua")
        createTab = """CREATE TABLE qinghua(
                ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                TOPIC VARCHAR(100) NULL,
                LINK VARCHAR(500) NULL,
                INFO VARCHAR(100) NULL,
                CONTENT LONGTEXT NULL
        )"""
        cursor.execute(createTab)
    except:
        print('\n错误：数据库连接失败')
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
    UA = random.choice(User_Agent)
    head = {'User-Agent': UA}
    IP=['219.138.58.167:3128',
        '122.72.18.35:80',
        '122.72.18.61:80',
        '112.74.94.142:3128',
        '101.37.79.125:3128',
        '122.114.27.241:808',
        '119.122.41.222:9000',
        '124.152.32.140:53281']
    IP=random.choice(IP)
    proxies={'proxies':IP}
    proxy={'https':proxies}
    proxy_support =request.ProxyHandler(proxy)
    opener =request.build_opener(proxy_support)
    request.install_opener(opener)
    starttime=datetime.datetime.now()
    num=int(input('请输入每个模块您要循环的页码数(即是每个模块对应网页的深度):\n'))
    #数据源
    for page1 in range(98,101):
        url1='http://www.dangjian.tsinghua.edu.cn/publish/dangjian/'+'{0}'.format(page1)+'/index.html'
        #伪装成浏览器访问网站
        # x=input('输入你想查询的内容：')
        html1=gethtml(url1)
        printhtml(html1)
    endtime=datetime.datetime.now()
    print('所用时间为：')
    print(endtime-starttime)
    cursor.close()
    cnn.close()
