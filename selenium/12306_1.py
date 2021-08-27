
# selenium 查询12306余票信息

# 测试能否打开网页

from selenium import webdriver
from time import sleep

import selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

if __name__ == "__main__":
  
  # 实例化浏览器驱动
  driver = webdriver.Chrome()
  driver.get("https://kyfw.12306.cn/otn/leftTicket/init")
  driver.implicitly_wait(2)
  sleep(3)


  # 关闭浏览器
  driver.close()