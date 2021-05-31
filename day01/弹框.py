from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get(r"E:\python1\autom\day01\day01\资料\练习的html\练习的html\弹框的验证/dialogs.html")
driver.find_element_by_id("alert").click()
time.sleep(3)
# 点击弹框的确定取消按钮     dismiss 取消
driver.switch_to.alert.accept()
time.sleep(3)
driver.quit()