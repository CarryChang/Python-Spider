# coding=utf-8
from selenium import webdriver
import selenium.webdriver.support.ui as ui
import  pymysql
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

#数据库操作
cnn = pymysql.connect(host="localhost",user="root",password="9527",db="test",charset="utf8")
cursor = cnn.cursor()
cursor.execute("DROP TABLE IF EXISTS maotou")
createTab = """CREATE TABLE maotou(
      编号 INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
      景点 TEXT NOT NULL,
      网址 TEXT NOT NULL,
      总网评论数 VARCHAR(20) NOT NULL,
      排名情况 VARCHAR(20) NOT NULL,
      猫途鹰总评分 VARCHAR(20) NOT NULL,
      非常好占比 VARCHAR(20) NOT NULL,
      很好占比 VARCHAR(20) NOT NULL,
      一般占比 VARCHAR(20) NOT NULL,
      差评占比 VARCHAR(20) NOT NULL,
      很糟占比 VARCHAR(20) NOT NULL,
      旅行者总评论数 VARCHAR(20) NOT NULL,
      非常好的评论数  VARCHAR(20) NOT NULL,
      很好的评论数 VARCHAR(20) NOT NULL,
      一般的评论数 VARCHAR(20) NOT NULL,
      差评的评论数 VARCHAR(20) NOT NULL,
      感觉很糟的评论数  VARCHAR(20) NOT NULL
    )"""
cursor.execute(createTab)
driver =webdriver.Chrome()
wait = ui.WebDriverWait(driver,10)
logurl='https://www.tripadvisor.cn/Attraction_Review-g60763-d105127-Reviews-or20-Central_Park-New_York_City_New_York.html'
driver.get(logurl)
time.sleep(2)
#店铺
data=driver.find_element_by_id('HEADING')
#点评数
data1=driver.find_element_by_xpath('html/body/div[3]/div[3]/div/div[1]/div[1]/span[1]/div/a/span')
#总店铺数
time.sleep(1)
data3=driver.find_element_by_xpath('html/body/div[3]/div[3]/div/div[1]/div[1]/span[2]/div/span')
print(data.text+'\n'+data1.text+'\n'+data3.text)
###满意度分析
time.sleep(1)
#猫途鹰评分
data5=driver.find_element_by_xpath('html/body/div[3]/div[6]/div/div/div[2]/div/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/span')
#非常好的占比
data6=driver.find_element_by_xpath('html/body/div[3]/div[6]/div/div/div[2]/div/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/ul/li[1]/span[3]')
#很好的占比
data7=driver.find_element_by_xpath('html/body/div[3]/div[6]/div/div/div[2]/div/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/ul/li[2]/span[3]')
#一般的占比
time.sleep(1)
data8=driver.find_element_by_xpath('html/body/div[3]/div[6]/div/div/div[2]/div/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/ul/li[3]/span[3]')
#差的占比
time.sleep(1)
data9=driver.find_element_by_xpath('html/body/div[3]/div[6]/div/div/div[2]/div/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/ul/li[4]/span[3]')
#很糟的占比
data4=driver.find_element_by_xpath('html/body/div[3]/div[6]/div/div/div[2]/div/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/ul/li[5]/span[3]')
print('猫途鹰总评分：'+data5.text+'\n'+'非常好的占比'+data6.text+'\n'+'很好的占比'+data7.text+'\n'+'一般的占比'+data8.text+'\n'+'差的占比'+data9.text+'\n'+'很糟的占比'+data4.text)
time.sleep(2)
#总点评数
data10=driver.find_element_by_xpath('html/body/div[3]/div[6]/div/div/div[2]/div/div[3]/div/div[1]/div/div/div[4]/div/p/b[3]')
print('总评论数：'+data10.text+'\n')
#非常好的评论数
time.sleep(2)
data11=driver.find_element_by_xpath('html/body/div[3]/div[6]/div/div/div[2]/div/div[3]/div/div[1]/div/div/div[2]/div[1]/form/div[1]/ul/li[1]/label/span[2]')
#很好的评论数
time.sleep(2)
data12=driver.find_element_by_xpath('html/body/div[3]/div[6]/div/div/div[2]/div/div[3]/div/div[1]/div/div/div[2]/div[1]/form/div[1]/ul/li[2]/label/span[2]')
#一般的评论数
data13=driver.find_element_by_xpath('html/body/div[3]/div[6]/div/div/div[2]/div/div[3]/div/div[1]/div/div/div[2]/div[1]/form/div[1]/ul/li[3]/label/span[2]')
#差的评论数
time.sleep(2)
data14=driver.find_element_by_xpath('html/body/div[3]/div[6]/div/div/div[2]/div/div[3]/div/div[1]/div/div/div[2]/div[1]/form/div[1]/ul/li[4]/label/span[2]')
#很糟的评论数
time.sleep(2)
data15=driver.find_element_by_xpath('html/body/div[3]/div[6]/div/div/div[2]/div/div[3]/div/div[1]/div/div/div[2]/div[1]/form/div[1]/ul/li[5]/label/span[2]')

print('非常好的评论数'+data11.text+'\n'+'很好的评论数'+data12.text+'\n'+'一般的评论数'+data13.text+'\n'+'差的评论数'+data14.text+'\n'+'很糟的评论数'+data15.text)

sql = "INSERT INTO `maotou`(景点,网址,总网评论数,排名情况,猫途鹰总评分,非常好占比,很好占比,一般占比,差评占比,很糟占比,旅行者总评论数,非常好的评论数,很好的评论数,一般的评论数,差评的评论数,感觉很糟的评论数) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
cursor.execute(sql,(data.text,logurl,data1.text,data3.text,data5.text,data6.text,data7.text,data8.text,data9.text,data4.text,data10.text,data11.text,data12.text,data13.text,data14.text,data15.text))
cnn.commit()
cursor.close()

driver.close()

# try:
#     time.sleep(1)
#     driver.find_element_by_xpath('html/body/div[1]/div[1]/div[1]/div[1]/a[4]').click()
#     time.sleep(1)
#     driver.find_element_by_xpath('html/body/div/article/header/a[2]').click()
#     time.sleep(1)
#     driver.find_element_by_xpath('html/body/div/article/form/div/div/input').send_keys('胡歌')
#     time.sleep(1)
#     driver.find_element_by_xpath('html/body/div/article/form/div/div/input').send_keys(Keys.ENTER)
#     time.sleep(2)
#     ###点胡歌本人微博
#     driver.find_element_by_xpath('html/body/div/div[1]/div[1]/div[2]/div/div[1]/div/div/div/div[2]/div').click()
#     time.sleep(2)
#     #点击微博
#     driver.find_element_by_xpath('html/body/div/div[1]/div[1]/div[2]/nav/div/div/div/ul/li[2]/span').click()
#     time.sleep(1)
#     #点击文章
#     driver.find_element_by_xpath('html/body/div/div[1]/div[1]/div[3]/div/div/article/div/div[1]').click()
#     time.sleep(1)
#     data=driver.find_element_by_xpath('html/body/div/div[1]/div/div[2]/div/div/article/div/div[1]')
#     print(data.text+'\n')
# ####抓取本篇微博的数据
#     data1=driver.find_element_by_xpath('html/body/div/div[1]/div/div[2]/div/div/footer/div[1]')
#     time.sleep(1)
#     data2=driver.find_element_by_xpath('html/body/div/div[1]/div/div[2]/div/div/footer/div[2]')
#     time.sleep(1)
#     data3=driver.find_element_by_xpath('html/body/div/div[1]/div/div[2]/div/div/footer/div[3]')
#     # time.sleep(1)
#     print('转发量：'+data1.text+'评论数：'+data2.text+'微博点赞数：'+data3.text)
#     print('first success')
# except Exception as e:
#     pass
#     #点击评论
# # driver.find_element_by_xpath('html/body/div/div[1]/div/div[3]/div[1]/ul/li[2]').click()
# # time.sleep(2)
# # driver.find_element_by_xpath('html/body/div/div[1]/div/div[3]/div[2]/div[1]/div[11]/a').click()
# # time.sleep(2)
#  #点击更多评论
#     #提取评论id
#     # ids=driver.find_elements_by_class_name('comment-user-name')
#     # time.sleep(1)
#     # for id in ids:
#     #     print('用户id：'+id.text)
#     #开始翻页
#
# ##############################################################################################################评论f翻页获取成功
# # i=0
# # while i < 100:
# #     comments=BeautifulSoup(driver.page_source,'lxml').find_all('div',class_='item-minor txt-l mct-b')
# #     time.sleep(1)
# #     for comment in comments:
# #         f.write(comment.text+'\n')
# #         try:
# #             sql = "INSERT INTO `comment2`(评论) VALUES(%s)"
# #             cursor.execute(sql,(comment.text))
# #             cnn.commit()
# #         except Exception as e:
# #             pass
# #     time.sleep(1)
# #     driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
# #     time.sleep(2)
# #     print('second success')
# #     i+=1
#
# # f.close()
# # cursor.close()
# # cnn.close()
#
#
#
