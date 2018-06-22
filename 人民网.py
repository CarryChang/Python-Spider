
from urllib import request
from bs4 import BeautifulSoup
import datetime
import random



def gethtml(url):

    try:
        html=request.urlopen(request.Request(url,headers=head)).read().decode('utf-8')
    except Exception as e:
        html=request.urlopen(request.Request(url,headers=head)).read().decode('GB2312')
    return html
#人民网党建信息
def renmin(html2):
    link_ren=BeautifulSoup(html2,'lxml').select('div font a')
    for link in link_ren:
        ren_min=link.get('href')
        #对于输入的内容进行搜索
        # if check in link.text:
        print(link.text+'\n'+ren_min)
        # f.write('\n'+link.text+'\n'+'地址为：'+ren_min)
        # #解析目录页
        # try:
        #     Ren=gethtml(ren_min)
        #     link_ren=BeautifulSoup(Ren,'lxml').select('ul li a')
        #     for link1 in link_ren:
        #             ren1=link1.get('href')
        #             if ren1.startswith('/'):
        #                 print('\n'+link1.text+'\n'+'地址为：'+'http://dangjian.people.com.cn'+ren1)
        #                 # f.write('\n'+link1.text+'\n'+'地址为：'+'http://dangjian.people.com.cn'+ren1)
        #             else:
        #                 print('\n'+link1.text+'\n'+'地址为：'+ren1)
        #                 # f.write('\n'+link1.text+'\n'+'地址为：'+ren1)
        # except Exception as e:
        #         pass
if __name__ == '__main__':
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
    #人民网信息地址
    url2='http://dangjian.people.com.cn/GB/136058/407542/'
    #人民网党建信息爬虫入口
    html2=gethtml(url2)
    renmin(html2)
    # check=input('输入您要查询的内容(使用关键字进行查询)：\n')
    endtime=datetime.datetime.now()
    print('所用时间为：')
    print(endtime-starttime)
