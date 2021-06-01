from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.jd.com")
driver.maximize_window()
time.sleep(3)

# 登录
driver.find_element_by_link_text("你好，请登录").click()
# 账户登录
driver.find_element_by_xpath("//*[@id='content']/div[2]/div[1]/div/div[3]/a").click()
# 手机号
driver.find_element_by_xpath("//*[@id='loginname']").send_keys("18134241374")
driver.find_element_by_xpath("//*[@id='nloginpwd']").send_keys("19980227gsj")
# 登录
driver.find_element_by_xpath("//*[@id='loginsubmit']").click()
time.sleep(5)
# 搜索
driver.find_element_by_xpath("//*[@id='key']").send_keys("矿泉水")
driver.find_element_by_xpath("//*[@id='search']/div/div[2]/button").click()
time.sleep(5)

# 点击
driver.find_element_by_xpath("//*[@id='J_goodsList']/ul/li[1]/div/div[1]/a/img").click()
time.sleep(5)
# 转换窗口
win = driver.window_handles
driver.switch_to.window(win[1])
driver.find_element_by_xpath("//*[@id='choose-attr-1']/div[2]/div[1]/a").click()
driver.find_element_by_xpath("//*[@id='choose-baitiao']/div[2]/div[1]/div[1]/a").click()
driver.find_element_by_xpath("//*[@id='InitCartUrl']").click()
time.sleep(5)

driver.quit()