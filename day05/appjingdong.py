from appium import webdriver
import time
server = r"http://localhost:4723/wd/hub"
desired_capabilities = {
    "platformName":"Android",
    "deviceName":"127.0.0.1:62001",
    "platformVersion":"7.1.2",
    "appPackage":"com.jingdong.app.mall",
   "appActivity":"com.jingdong.app.mall.main.MainActivity"
}
driver = webdriver.Remote(server,desired_capabilities)

el1 = driver.find_element_by_id("com.jingdong.app.mall:id/bqd")
el1.click()
time.sleep(10)
el2 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[3]/android.widget.ViewFlipper")
el2.click()
time.sleep(10)
el5 = driver.find_element_by_id("com.jd.lib.search.feature:id/zw")
el5.send_keys("冰激凌")
el5.click()
time.sleep(10)
el4 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.LinearLayout")
el4.click()
time.sleep(10)
el6 = driver.find_element_by_xpath("(//android.widget.ImageButton[@content-desc=\"加入购物车\"])[1]")
el6.click()
driver.quit()
