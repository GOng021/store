from selenium import webdriver
from selenium.webdriver import ActionChains
import  time
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.maximize_window()
ac = ActionChains(driver)
driver.find_element_by_id("kw")
time.sleep(5)
ac.key_down("a").key_up("a").key_down("b").key_up("b").perform()
