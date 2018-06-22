# coding=utf-8
from selenium import webdriver
import selenium.webdriver.support.ui as ui
import  pymysql
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

# #数据库操作
# cnn = pymysql.connect(host="localhost",user="root",password="9527",db="test",charset="utf8")
# cursor = cnn.cursor()
# cursor.execute("DROP TABLE IF EXISTS comment2")
# createTab = """CREATE TABLE comment2(
#       id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
#       评论 TEXT NOT NULL
#     )"""
# cursor.execute(createTab)

driver =webdriver.Chrome()
#设定加载时间
# f= open('C:/Users/Administrator/Desktop/'+'您所查询的信息'+'.text','w',encoding='utf-8')
wait = ui.WebDriverWait(driver,10)
logurl='https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F'
driver.get(logurl)
time.sleep(1)
driver.find_element_by_id('loginName').send_keys('630117639@qq.com')
time.sleep(1)
driver.find_element_by_id('loginPassword').send_keys('Zhang1017')
time.sleep(1)
try:
    driver.find_element_by_id('loginAction').click()
    print('click success!')
except:
    print('click error!')
try:
    time.sleep(1)
    driver.find_element_by_xpath('html/body/div[1]/div[1]/div[1]/div[1]/a[4]').click()
    time.sleep(1)
    driver.find_element_by_xpath('html/body/div/article/header/a[2]').click()
    time.sleep(1)
    driver.find_element_by_xpath('html/body/div/article/form/div/div/input').send_keys('胡歌')
    time.sleep(1)
    driver.find_element_by_xpath('html/body/div/article/form/div/div/input').send_keys(Keys.ENTER)
    time.sleep(2)
    ###点胡歌本人微博
    driver.find_element_by_xpath('html/body/div/div[1]/div[1]/div[2]/div/div[1]/div/div/div/div[2]/div').click()
    time.sleep(2)
    #点击微博
    driver.find_element_by_xpath('html/body/div/div[1]/div[1]/div[2]/nav/div/div/div/ul/li[2]/span').click()
    time.sleep(1)
    #点击文章
    driver.find_element_by_xpath('html/body/div/div[1]/div[1]/div[3]/div/div/article/div/div[1]').click()
    time.sleep(1)
    data=driver.find_element_by_xpath('html/body/div/div[1]/div/div[2]/div/div/article/div/div[1]')
    print(data.text+'\n')
####抓取本篇微博的数据
    data1=driver.find_element_by_xpath('html/body/div/div[1]/div/div[2]/div/div/footer/div[1]')
    time.sleep(1)
    data2=driver.find_element_by_xpath('html/body/div/div[1]/div/div[2]/div/div/footer/div[2]')
    time.sleep(1)
    data3=driver.find_element_by_xpath('html/body/div/div[1]/div/div[2]/div/div/footer/div[3]')
    # time.sleep(1)
    print('转发量：'+data1.text+'评论数：'+data2.text+'微博点赞数：'+data3.text)
    print('first success')
except Exception as e:
    pass
    #点击评论
# driver.find_element_by_xpath('html/body/div/div[1]/div/div[3]/div[1]/ul/li[2]').click()
# time.sleep(2)
# driver.find_element_by_xpath('html/body/div/div[1]/div/div[3]/div[2]/div[1]/div[11]/a').click()
# time.sleep(2)
 #点击更多评论
    #提取评论id
    # ids=driver.find_elements_by_class_name('comment-user-name')
    # time.sleep(1)
    # for id in ids:
    #     print('用户id：'+id.text)
    #开始翻页

##############################################################################################################评论f翻页获取成功
# i=0
# while i < 100:
#     comments=BeautifulSoup(driver.page_source,'lxml').find_all('div',class_='item-minor txt-l mct-b')
#     time.sleep(1)
#     for comment in comments:
#         f.write(comment.text+'\n')
#         try:
#             sql = "INSERT INTO `comment2`(评论) VALUES(%s)"
#             cursor.execute(sql,(comment.text))
#             cnn.commit()
#         except Exception as e:
#             pass
#     time.sleep(1)
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
#     time.sleep(2)
#     print('second success')
#     i+=1

# f.close()
# cursor.close()
# cnn.close()



