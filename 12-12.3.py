# coding=utf-8
from urllib import request
from bs4 import BeautifulSoup
from selenium import webdriver
import pymysql
import time
import random
import datetime
from lxml import etree

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
    try:
        html=request.urlopen(request.Request(url,headers=head)).read().decode('utf-8')
    except:
         html=request.urlopen(request.Request(url,headers=head)).read().decode('GB2312')
    return html
# #人民网党建信息
# def renmin(html3):
#     link_ren=BeautifulSoup(html3,'lxml').find_all('a')
#     for link in link_ren:
#         if link.get('href').startswith('http'):
#             print(link.get('href')+link.text)
#             html=gethtml()
        # i=1
        # driver.get(t2)
        # while i<int(num):
        #     # # try:
        #     # driver.set_page_load_timeout(3)
        #     # time.sleep(1)
        #     #
        #
        #     print('################################################翻页')
        #     # i+=1
        #     driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        #     time.sleep(1)
        #     driver.find_element_by_xpath('/html/body/div[5]/div[1]/div/a[8]').click()
            # time.sleep(1)
            # # except Exception as e:
            # #     pass

#主控函数
if __name__ == '__main__':
    starttime=datetime.datetime.now()

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
    # num=int(input('页码数：\n'))
    url3='http://cpc.people.com.cn/GB/64093/64094/index1.html'
    driver =webdriver.Chrome()
    #人民网信息爬虫入口
    # html3=gethtml(url3)
    # time.sleep(1)
    # renmin(html3)
    driver.get(url3)
    time.sleep(1)

    for i in driver.find_elements_by_xpath('html/body/div[2]/div/div[2]/a'):
        print(i.get_attribute('href')+i.text)
        new_url=i.get_attribute('href')
        html=gethtml(new_url)
        selector = etree.HTML(html)
        page=selector.xpath('//ul/li')
        for a in page:
            title=a.xpath('a/text()')
            time=a.xpath('i/text()')
            link=a.xpath('a/@href')
            print(title+time+'http://cpc.people.com.cn'+link)









    #输出爬虫耗时
    endtime=datetime.datetime.now()
    print('所用时间为：')
    print(endtime-starttime)
