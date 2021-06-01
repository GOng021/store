from  selenium import webdriver
from  selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://www.qcc.com")
driver.maximize_window()

# 弹出框
driver.find_element_by_xpath("//*[@id='addfavorModal']/div/div/div[1]/img[1]").click()
# 登录
driver.find_element_by_link_text("登录 | 注册").click()

time.sleep(5)
# 获取模块
ele = driver.find_element_by_xpath("//*[@id='nc_1_n1z']")

# actionchain
ac = ActionChains(driver)
ac.click_and_hold(ele).move_by_offset(348,0).perform()
time.sleep(3)
driver.quit()