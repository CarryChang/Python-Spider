# coding=utf-8
from selenium import webdriver
import selenium.webdriver.support.ui as ui
import  pymysql
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup


driver =webdriver.Chrome()
wait = ui.WebDriverWait(driver,3)
logurl='https://www.tripadvisor.cn/Attractions'
time.sleep(5)
driver.get(logurl)
driver.find_element_by_class_name('typeahead_input').send_keys(input('请输入地区名字，我为你找当地的旅游景点：'))
time.sleep(5)
driver.find_element_by_id('SUBMIT_THINGS_TO_DO').click()
time.sleep(5)
data=driver.find_elements_by_class_name('poiTitle')
for i in data:
    print(i.get_attribute('href')+i.text)