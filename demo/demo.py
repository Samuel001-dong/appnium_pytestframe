""""


"""
from appium import webdriver
desired_caps={}
desired_caps['platformName']='Android'
desired_caps['platformVersion']='6.0'
desired_caps['deviceName']='emulator-5554'
# com.android.settings/com.android.settings.Settings
desired_caps['appPackage']='com.android.settings'
desired_caps['appActivity']='com.android.settings.Settings'

driver=webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
print("启动【设置】应用")
driver.quit()
