
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

    # 出发日期-逻辑运算符and多元素定位
    driver.find_element_by_xpath("//input[@id='train_date' and @class='inp_selected']").click()
    calLeft = driver.find_elements_by_css_selector("div.cal-wrap>div.cal div.cal-cm>div")
    count, now = 0, 0
    for date in calLeft:
        count += 1
        if date.text == r"今天":
            now = count
            print(f"{date.text}是当月第{count}天，我将买明天的车票。")
        if count == now+1:
            date.click()
      
    # 日期选择用法2：通过切换日期列表，选择第二个日期tomorrow，自动搜索车票
    # tomorrow = driver.find_element_by_css_selector('#date_range li:nth-child(2)')


    # 出发时间：06：00-12：00
    driver.find_element_by_id("cc_start_time").click()
    sleep(1)
    driver.find_element_by_xpath("//select[@id='cc_start_time']/option[position()=3]").click()
    sleep(1)
    
    # 出发时间用法2：导入Select，通过下拉框选择出发时间的用法
    # timeSelect =  Select(driver.find_element_by_id('cc_start_time'))
    # timeSelect.select_by_visible_text('06:00--12:00')
    
    
    # 点击查询
    driver.find_element_by_id("query_ticket").click()
    sleep(3)

    # 关闭浏览器（上次忘掉这个，导致电脑卡到飞起）
    sleep(5)
    driver.close()
