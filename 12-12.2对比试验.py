# coding=utf-8
import datetime
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import re
import pymysql
import datetime
##########################################################################################
# def url1(url):
#     driver =webdriver.PhantomJS()
#     time.sleep(1)
#     driver.get(url)
#     driver.set_page_load_timeout(10)
#     time.sleep(1)
#     element1 = BeautifulSoup(driver.page_source,'lxml').find('div',class_='context-tit')
#     WebElement2 = BeautifulSoup(driver.page_source,'lxml').find('div',class_='ly')
#     WebElement3 = BeautifulSoup(driver.page_source,'lxml').find('div',id='tex')
#     WebElement4 = BeautifulSoup(driver.page_source,'lxml').find('div',class_='bj')
#     sql = "INSERT INTO `big5`(标题,链接,文章信息,内容,编辑) VALUES(%s,%s,%s,%s,%s)"
#     cursor.execute(sql,(element1.text,url,WebElement2.text,WebElement3.text,WebElement4.text))
#     cnn.commit()
#     print('success')
#     driver.close()
##########################################################################################
def url11(url):
    driver =webdriver.Chrome()
    time.sleep(1)
    driver.get(url)
    time.sleep(1)
    element1=driver.find_element_by_class_name('context-tit')
    WebElement2 = driver.find_element_by_class_name('ly')
    WebElement3 = driver.find_element_by_id('tex')
    WebElement4 = driver.find_element_by_class_name('bj')
    sql = "INSERT INTO `big6`(标题,链接,文章信息,内容,编辑) VALUES(%s,%s,%s,%s,%s)"
    cursor.execute(sql,(element1.text,url,WebElement2.text,WebElement3,WebElement4.text))
    cnn.commit()
    print('success')
    driver.close()




##########################################################################################
if __name__ == '__main__':
    # starttime=time.clock()
    # #数据库操作
    # cnn = pymysql.connect(host="localhost",user="root",password="9527",db="test",charset="utf8")
    # cursor = cnn.cursor()
    # cursor.execute("DROP TABLE IF EXISTS big5")
    # createTab = """CREATE TABLE big5(
    #     编号 INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    #     标题 VARCHAR(100) NOT NULL,
    #     链接 VARCHAR(500) NOT NULL,
    #     文章信息 VARCHAR(100) NOT NULL,
    #     内容 TEXT NOT NULL,
    #     编辑  VARCHAR(50) NOT NULL
    # )"""
    # cursor.execute(createTab)
    # starttime=time.clock()
    # url='http://dangjian.com/djw2016sy/djw2016wkztl/wkztl2016xihy/201711/t20171113_4485736.shtml'
    # url1(url)
    # cursor.close()
    # cnn.close()
    # endtime=time.clock()
    # print('所用时间为：')
    # print(endtime-starttime)



    starttime=time.clock()
    #数据库操作
    cnn = pymysql.connect(host="localhost",user="root",password="9527",db="test",charset="utf8")
    cursor = cnn.cursor()
    cursor.execute("DROP TABLE IF EXISTS big6")
    createTab = """CREATE TABLE big6(
        编号 INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        标题 VARCHAR(100) NOT NULL,
        链接 VARCHAR(500) NOT NULL,
        文章信息 VARCHAR(100) NOT NULL,
        内容  LONGTEXT NOT NULL,
        编辑  VARCHAR(50) NOT NULL
    )"""
    cursor.execute(createTab)
    starttime=time.clock()
    # url='http://dangjian.com/djw2016sy/djw2016wkztl/wkztl2016xihy/201711/t20171113_4485736.shtml'
    url='http://dangjian.com/djw2016sy/djw2016syyw/201712/t20171212_4521689.shtml'
    url11(url)
    cursor.close()
    cnn.close()
    endtime=time.clock()
    print('所用时间为：')
    print(endtime-starttime)


    #######实验证明beautifulsoup没有find by element速度快，性能稳定，并且格式好，所以在以后尽量用find by element