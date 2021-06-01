from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://www.suning.com/")
driver.maximize_window()
time.sleep(3)
# 搜索
driver.find_element_by_xpath("//*[@id='searchKeywords']").send_keys("扫地机器人")
driver.find_element_by_xpath("//*[@id='searchSubmit']").click()
time.sleep(5)
# 选中
driver.find_element_by_xpath("//*[@id='0000000000-12258769702']/div/div/div[1]/div/a/i/img").click()
time.sleep(5)
# 切换窗口
win = driver.window_handles
driver.switch_to.window(win[1])
# 选型号
driver.find_element_by_xpath("//*[@id='colorItemList']/dd/ul/li[1]/a/span").click()
driver.find_element_by_xpath("//*[@id='yanbao']/dd/ul/li[1]/a/span").click()
driver.find_element_by_xpath("//*[@id='addCart']").click()
time.sleep(5)


driver.quit()
