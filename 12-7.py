# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains #引入ActionChains鼠标操作类
from selenium.webdriver.common.keys import Keys #引入keys类操作
from bs4 import BeautifulSoup
import time
#使用搜狗
driver =webdriver.Chrome()
url='http://sogou.com'
driver.get(url)
X=input('Enter Ur need:')
driver.find_element_by_id('query').send_keys(X)
time.sleep(1)
driver.find_element_by_id('stb').click()
time.sleep(1)
num=input('输入要翻页数目：\n')
#循环导入地址
html1=driver.page_source
link_qing=BeautifulSoup(html1,'lxml').select('h3 a')
for link in link_qing:
    if link.get('href').startswith('http'):
        print(link.text+'\n'+link.get('href'))
#点击翻页
i=1
while i <int(num):
    i+=1
    driver.find_element_by_id('sogou_next').click()
    time.sleep(1)
    html2=driver.page_source
    link_qing=BeautifulSoup(html2,'lxml').select('h3 a')
    for link in link_qing:
        if link.get('href').startswith('http'):
            print(link.text+'\n'+link.get('href'))
#########################################################################百度搜索
url2='https://www.baidu.com'
driver.get(url2)
driver.find_element_by_id('kw').send_keys(X)
time.sleep(1)
driver.find_element_by_id('su').click()
time.sleep(1)
# num=input('输入要翻页数目：\n')
#循环导入地址
html1=driver.page_source
link_qing=BeautifulSoup(html1,'lxml').select('h3 a')
for link in link_qing:
    if link.get('href').startswith('http'):
        print(link.text+'\n'+link.get('href'))
i=1
while i <int(num):
    i+=1
    driver.find_element_by_class_name("n").click()
    time.sleep(1)
    html2=driver.page_source
    link_qing=BeautifulSoup(html2,'lxml').select('h3 a')
    for link in link_qing:
        if link.get('href').startswith('http'):
            print(link.text+'\n'+link.get('href'))
#########################################################################360搜索
url3='https://www.so.com/'
driver.get(url3)
driver.find_element_by_id('input').send_keys(X)
time.sleep(1)
driver.find_element_by_id('search-button').click()
time.sleep(1)
# num=input('输入要翻页数目：\n')
#循环导入地址
html1=driver.page_source
link_qing=BeautifulSoup(html1,'lxml').select('h3 a')
for link in link_qing:
    if link.get('href').startswith('http'):
        print(link.text+'\n'+link.get('href'))
i=1
while i <int(num):
    i+=1
    driver.find_element_by_id("snext").click()
    time.sleep(1)
    html2=driver.page_source
    link_qing=BeautifulSoup(html2,'lxml').select('h3 a')
    for link in link_qing:
        if link.get('href').startswith('http'):
            print(link.text+'\n'+link.get('href'))
#########################################################################必应国内版
url4='http://cn.bing.com/'
driver.get(url4)
time.sleep(1)
driver.find_element_by_id('est_cn').click()
time.sleep(1)
driver.find_element_by_id('sb_form_q').send_keys(X)
time.sleep(1)
driver.find_element_by_id('sb_form_go').click()
time.sleep(1)
# num=input('输入要翻页数目：\n')
#循环导入地址
html1=driver.page_source
link_qing=BeautifulSoup(html1,'lxml').select('h2 a')
for link in link_qing:
    if link.get('href').startswith('http'):
        print(link.text+'\n'+link.get('href'))
i=1
while i <int(num):
    try:
        i+=1
        driver.find_element_by_class_name("sb_pagN").click()
        time.sleep(1)
        html2=driver.page_source
        link_qing=BeautifulSoup(html2,'lxml').select('h2 a')
        for link in link_qing:
            if link.get('href').startswith('http'):
                print(link.text+'\n'+link.get('href'))
    except Exception as e:
        pass
#####################################################################必应国外版
driver.get(url4)
time.sleep(1)
driver.find_element_by_id('est_en').click()
time.sleep(1)
driver.find_element_by_id('sb_form_q').send_keys(X)
time.sleep(1)
driver.find_element_by_id('sb_form_go').click()
time.sleep(1)
#循环导入地址
html1=driver.page_source
link_qing=BeautifulSoup(html1,'lxml').select('h2 a')
for link in link_qing:
    if link.get('href').startswith('http'):
        print(link.text+'\n'+link.get('href'))
i=1
while i <int(num):
    try:
        i+=1
        driver.find_element_by_class_name("sb_pagN").click()
        time.sleep(1)
        html2=driver.page_source
        link_qing=BeautifulSoup(html2,'lxml').select('h2 a')
        for link in link_qing:
            if link.get('href').startswith('http'):
                print(link.text+'\n'+link.get('href'))
    except Exception as e:
        pass
driver.close()