# coding=utf-8
from urllib import request
from bs4 import BeautifulSoup
import datetime
import os
import random
def gethtml(url):
    #成功实现编码的转换
    try:
        html=request.urlopen(request.Request(url,headers=head)).read().decode('utf-8')
    except Exception as e:
        html=request.urlopen(request.Request(url,headers=head)).read().decode('GB2312')
    return html
def dangjian(html3):
    #解析目录页
    soup_links=BeautifulSoup(html3,'lxml').find('div',class_='nav-list')
    for link in soup_links.ol.children:
        if link !='\n':
            t2=link.a.get('href')
            # print(t1+'部分'+'  '+'地址为：'+t2)
            html=gethtml(t2)
            soup=BeautifulSoup(html,'lxml').select('div ul li a')
            for L in soup:
                #循环各个元素
                T55=L.get('href')
                if T55.startswith('./'):
                    #标题查找
                    # if check in L.text:
                    print(L.text+'   '+'\n'+'地址为：'+t2+T55)
                    f.write('\n'+L.text+'   '+'\n'+'地址为：'+t2+T55)
            #对后续网页进行翻页
            for page in range(1,num):
                try:
                    url11=gethtml(t2+'index_'+'{0}'.format(page)+'.shtml')
                    soup_links1 = BeautifulSoup(url11,'lxml').select('div ul li a')
                    for link1 in soup_links1:
                        #循环各个元素
                        t22=link1.get('href')
                        if t22.startswith("./"):
                            #标题查找
                            # if check in link1.text:
                            print(link1.text+'   '+'\n'+'地址为：'+t2+t22)
                            f.write('\n'+link1.text+'   '+'\n'+'地址为：'+t2+t22)
                except Exception as e:
                    pass
#清华大学党建信息
def qinghau(html1):
    #解析目录页
    #解析目录页
    link_qing=BeautifulSoup(html1,'lxml').select('div ul li p a')
    for link in link_qing:
        qing=link.get('href')
        if qing.startswith('/'):
            # if check in link.text:
            print('\n'+link.text+'\n'+'地址为:'+'http://www.dangjian.tsinghua.edu.cn'+qing)
            f.write('\n'+link.text+'\n'+'地址为：'+'http://www.dangjian.tsinghua.edu.cn'+qing)
    for page in range(2,num+1):
        try:
            qing1=gethtml('http://www.dangjian.tsinghua.edu.cn/publish/dangjian/98/'+'index_'+'{0}'.format(page)+'.html')
            soup_qing = BeautifulSoup(qing1,'lxml').select('div ul li p a')
            for link1 in soup_qing:
                #循环各个元素
                qing=link1.get('href')
                if qing.startswith('/'):

                    # if check in link1.text:
                    print('\n'+link1.text+'\n'+'地址为:'+'http://www.dangjian.tsinghua.edu.cn'+qing)
                    f.write('\n'+link1.text+'\n'+'地址为：'+'http://www.dangjian.tsinghua.edu.cn'+qing)
        except Exception as e:
            pass
#人民网党建信息
def renmin(html2):
    link_ren=BeautifulSoup(html2,'lxml').select('div font a')
    for link in link_ren:
        ren_min=link.get('href')
        #对于输入的内容进行搜索
        # if check in link.text:
        print(link.text+'\n'+ren_min)
        # f.write('\n'+link.text+'\n'+'地址为：'+ren_min)
        #解析目录页
        try:
            Ren=gethtml(ren_min)
            link_ren=BeautifulSoup(Ren,'lxml').select('ul li a')
            for link1 in link_ren:

                    ren1=link1.get('href')
                    if ren1.startswith('/'):
                        print('\n'+link1.text+'\n'+'地址为：'+'http://dangjian.people.com.cn'+ren1)
                        # f.write('\n'+link1.text+'\n'+'地址为：'+'http://dangjian.people.com.cn'+ren1)
                    else:
                        print('\n'+link1.text+'\n'+'地址为：'+ren1)
                        # f.write('\n'+link1.text+'\n'+'地址为：'+ren1)
        except Exception as e:
                pass

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
    starttime=datetime.datetime.now()
    # check=input('输入您要查询的内容(使用关键字进行查询)：\n')
    num=int(input('请输入每个模块您要循环的页码数(即是每个模块对应网页的深度):\n'))
    f= open('C:/Users/Administrator/Desktop/'+'您所查询的'+'信息'+'.text','w',encoding='utf-8')
    f.write('您所查到的'+'信息如下：')
    #清华大学党建信息爬虫入口
    for page1 in range(98,101):
        url1='http://www.dangjian.tsinghua.edu.cn/publish/dangjian/'+'{0}'.format(page1)+'/index.html'
        html1=gethtml(url1)
        qinghau(html1)
    #人民网信息地址
    url2='http://dangjian.people.com.cn/GB/136058/407542/'
    #人民网党建信息爬虫入口
    html2=gethtml(url2)
    renmin(html2)
    #党建网信息地址
    url3='http://dangjian.com/djw2016sy/'
    #党建网信息爬虫入口
    html3=gethtml(url3)
    dangjian(html3)
    #输出爬虫耗时
    endtime=datetime.datetime.now()
    print('所用时间为：')
    print(endtime-starttime)
    f.close()
    os.system('pause')

