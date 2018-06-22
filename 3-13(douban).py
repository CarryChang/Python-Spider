
# coding=utf-8
import random
from lxml import etree
import pymysql
import datetime
import time
import requests
def get(x):
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
    time.sleep(5)
    # html=request.urlopen(request.Request(url,headers=head)).read().decode('utf-8')
    f=open(r'C:/Users/63011/Desktop/cookie.txt','r')#打开所保存的cookies内容文件
    cookies={}#初始化cookies字典变量
    for line in f.read().split(';'):   #按照字符：进行划分读取
        #其设置为1就会把字符串拆分成2份
        name,value=line.strip().split('=',1)
        cookies[name]=value  #为字典cookies添加内容
    html=requests.get(x,cookies=cookies)
    time.sleep(5)
    sel= etree.HTML(html.content)
    time.sleep(4)
    now = datetime.datetime.now()
    for msg in sel.xpath('//*[@class="comment-item"]'):
        user_name= msg.xpath('div/a/@title')
        # user_link= msg.xpath('div/a/@href')
        comment= msg.xpath('div/p/text()')[0].strip().replace(u'\n',u'')
        #########haiwnag
        # comment_time= msg.xpath('div/h3/span/span[3]/@title')
        comment_time= msg.xpath('div/h3/span[2]/span[2]/@title')
        vote= msg.xpath('div/h3/span[1]/span[1]/text()')
        link = x
        print(user_name,comment,comment_time,vote,link)
        try:
            sql = ("""
                            INSERT INTO haiwang_comment(crawl_datetime,user_name,comment_time,comment,vote)
                            VALUES (%s,%s,%s,%s,%s,%s)
                            """)
            cursor.execute(sql,(now,user_name,comment_time,comment,vote,link))
            conn.commit()
        except Exception as e:
            pass


if __name__ == '__main__':
    conn = pymysql.connect(
        user='root', passwd='9527',
        db='db', host='120.77.203.115', charset="utf8", use_unicode=True
    )
    cursor = conn.cursor()
    createTab = """CREATE TABLE IF NOT EXISTS haiwang_comment(
            id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
            crawl_datetime VARCHAR(30) NULL,
            user_name TEXT NULL,
            comment_time TEXT NULL,
            comment TEXT NULL,
            vote TEXT NULL,
            link TEXT NULL
            )"""
    cursor.execute(createTab)

    url =(
        'https://movie.douban.com/subject/3878007/comments?start={}&limit=20&sort=new_score&status=F&percent_type='
    )
    for i in range(1):
        x= url.format(str(i * 20))
        print(x)
        get(x)
        i+=1



