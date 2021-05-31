from selenium import webdriver
import time

driver=webdriver.Chrome()
driver.get(r"E:/python1/autom/day01/day01/资料/练习的html/练习的html/上传文件和下拉列表/autotest.html")
# 输入用户名
driver.find_element_by_xpath("//*[@id='accountID']").send_keys("gong")
# 输入密码
driver.find_element_by_xpath("//*[@id='passwordID']").send_keys("123456")
# 地区
driver.find_element_by_xpath("//*[@id='areaID']").send_keys("北京市")
# 性别
driver.find_element_by_xpath("//*[@id='sexID2']").click()
# 季节
driver.find_element_by_xpath("//*[@value='spring']").click()
driver.find_element_by_xpath("//*[@value='winter']").click()

# 上传文件
driver.find_element_by_xpath("//*[@name='file' and @type='file']").send_keys(r"C:\Users\gsj\Pictures\Saved Pictures\lay.jpg")

time.sleep(3)
driver.quit()
