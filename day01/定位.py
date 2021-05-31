from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get(r"E:\python1\autom\day01\day01\资料\练习的html\练习的html\main.html")
# 切换到id=frame框架页里
driver.switch_to.frame("frame")

driver.find_element_by_id("input1").send_keys("123")
time.sleep(2)
# 清空
driver.find_element_by_id("input1").clear()

time.sleep(3)
driver.quit()