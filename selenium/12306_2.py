
# selenium 查询12306余票信息

# 输入始发站和终点站

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

    # 关闭确认框
    driver.find_element_by_id("qd_closeDefaultWarningWindowDialog_id").click()
    sleep(1)

    # 出发站
    driver.find_element_by_id("fromStationText").click()
    driver.find_element_by_id("fromStationText").send_keys("武汉")
    # 模拟键盘操作：回车键
    driver.find_element_by_id("fromStationText").send_keys(Keys.ENTER)

    # 终点站
    driver.find_element_by_id("toStationText").click()
    driver.find_element_by_id("toStationText").send_keys("深圳")
    driver.find_element_by_id("toStationText").send_keys(Keys.ENTER)


    # 关闭浏览器（上次忘掉这个，导致电脑卡到飞起）
    sleep(5)
    driver.close()
