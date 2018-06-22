# coding=utf-8
import datetime
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import re
import pymysql
import datetime

def url1(url):
    driver =webdriver.PhantomJS()
    driver.get(url)
    time.sleep(1)
    WebElements = BeautifulSoup(driver.page_source,'lxml').select('ul li p a')
    for element in WebElements:
        print(element.text+'\n'+element.get('href'))
        URL= re.compile(r'(.+?.cn)').match(element.get('href'))
        driver.get(element.get('href'))
        i=0
        for i in range(int(num)):
            WebElements1 = BeautifulSoup(driver.page_source,'lxml').select('ul li a')
            for element1 in WebElements1:
                try:
                    if element1.get('href').startswith('http'):
                        print(element1.text+'\n'+element1.get('href'))
                        U=element1.get('href')
                        time.sleep(1)
                        driver.get(U)
                        driver.set_page_load_timeout(5)
                        WebElement2 = driver.find_element_by_class_name('sou')
                        WebElement3 = driver.find_element_by_class_name('show_text')
                        sql = "INSERT INTO renmin(TOPIC,LINK,INFO,CONTENT) VALUES(%s,%s,%s,%s)"
                        cursor.execute(sql,(element1.text,U,WebElement2.text,WebElement3.text))
                        cnn.commit()
                        print('success')
                    else:
                        print(element1.text+'\n'+URL.group()+element1.get('href'))
                        U=URL.group()+element1.get('href')
                        time.sleep(1)
                        driver.get(U)
                        driver.set_page_load_timeout(5)
                        WebElement2 = driver.find_element_by_class_name('sou')
                        WebElement3 = driver.find_element_by_class_name('show_text')
                        sql = "INSERT INTO renmin(TOPIC,LINK,INFO,CONTENT) VALUES(%s,%s,%s,%s)"
                        cursor.execute(sql,(element1.text,U,WebElement2.text,WebElement3.text))
                        cnn.commit()
                        print('success')
                except Exception as e:
                    pass
            try:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
                time.sleep(1)
                if i < 1 or i > 2:
                    driver.find_element_by_xpath('html/body/div[5]/div[1]/div/a[8]').click()
                else:
                    driver.find_element_by_xpath('html/body/div[5]/div[1]/div/a[9]').click()
                driver.set_page_load_timeout(5)
                print('###############################################')
                i+=1
            except Exception as e:
                pass
    driver.close()
if __name__ == '__main__':
    starttime=datetime.datetime.now()
    #数据库操作
    try:
        cnn = pymysql.connect(host="localhost",user="root",password="9527",db="test",charset="utf8")
        cursor = cnn.cursor()
        cursor.execute("DROP TABLE IF EXISTS renmin")
        createTab = """CREATE TABLE renmin(
                ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                TOPIC VARCHAR(100) NOT NULL,
                LINK VARCHAR(500) NOT NULL,
                INFO VARCHAR(100) NOT NULL,
                CONTENT LONGTEXT NOT NULL
        )"""
        cursor.execute(createTab)
    except:
        print('\n错误：数据库连接失败')
    url='http://cpc.people.com.cn/'
    num=input('输入你要翻页的次数：\n')
    url1(url)
    endtime=datetime.datetime.now()
    print('所用时间为：')
    print(endtime-starttime)
    cursor.close()
    cnn.close()

