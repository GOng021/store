from appium import webdriver

import time
server = r"http://localhost:4723/wd/hub"
desired_capabilities = {
    "platformName":"Android",
    "deviceName":"127.0.0.1:62001",
    "platformVersion":"7.1.2",
    "appPackage":"com.ss.android.ugc.aweme",
   "appActivity":"com.ss.android.ugc.aweme.splash.SplashActivity"
}
driver = webdriver.Remote(server,desired_capabilities)
time.sleep(5)
el1 = driver.find_element_by_id("com.ss.android.ugc.aweme:id/bdb")
el1.click()
# for i in range(0,20):
while True:
    driver.swipe(336, 937, 398, 303, 500)
    time.sleep(10)
# driver.quit()


