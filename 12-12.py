# coding=utf-8
import datetime
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import re
import pymysql
import datetime

def url1(url):
    driver =webdriver.Chrome()
    driver.get(url)
    time.sleep(1)
    WebElements = BeautifulSoup(driver.page_source,'lxml').select('ul li a')
    for element in WebElements:
        print(element.text+'\n'+element.get('href'))
        URL= re.compile(r'(.+?.cn)').match(element.get('href'))
        driver.get(element.get('href'))
        i=0
        for i in range(int(num)):
            time.sleep(1)
            WebElements1 = BeautifulSoup(driver.page_source,'lxml').select('ul li p a')
            for element1 in WebElements1:
                print(element1.text+'\n'+URL.group()+element1.get('href'))
                # U=URL.group()+element1.get('href')
                # time.sleep(1)
                # driver.get(U)
                # driver.set_page_load_timeout(20)
                # WebElement2 = driver.find_element_by_class_name('sou')
                # WebElement3 = driver.find_element_by_class_name('show_text')
                # WebElement4 = driver.find_element_by_class_name('edit')
                # sql = "INSERT INTO `big3`(标题,链接,文章信息,内容,编辑) VALUES(%s,%s,%s,%s,%s)"
                # cursor.execute(sql,(element1.text,U,WebElement2.text,WebElement3.text,WebElement4.text))
                # cnn.commit()
                # print('success')
            try:
                time.sleep(1)
                driver.find_element_by_xpath('html/body/div[5]/div[1]/div/a[8]').click()
                driver.set_page_load_timeout(20)
                time.sleep(1)
                print('###############################################')
                i+=1
            except :
                pass

    driver.close()
if __name__ == '__main__':
    # starttime=datetime.datetime.now()
    # #数据库操作
    # cnn = pymysql.connect(host="localhost",user="root",password="9527",db="test",charset="utf8")
    # cursor = cnn.cursor()
    # cursor.execute("DROP TABLE IF EXISTS big3")
    # createTab = """CREATE TABLE big3(
    #     编号 INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    #     标题 VARCHAR(100) NOT NULL,
    #     链接 VARCHAR(500) NOT NULL,
    #     文章信息 VARCHAR(100) NOT NULL,
    #     内容 TEXT NOT NULL,
    #     编辑  VARCHAR(50) NOT NULL
    # )"""
    # cursor.execute(createTab)
    starttime=datetime.datetime.now()
    url='http://cpc.people.com.cn/'
    num=input('输入你要翻页的次数：\n')
    url1(url)
    cursor.close()
    cnn.close()
    endtime=datetime.datetime.now()
    print('所用时间为：')
    print(endtime-starttime)

