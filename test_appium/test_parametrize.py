import allure
import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from hamcrest import *


@allure.feature("测试用例参数化")
@allure.title("测试用例参数化")
class TestParameterize:
    def setup(self):
        desired_caps = {
            "platformName": "Android",
            "deviceName": "emulator-5554",
            "appPackage": "com.xueqiu.android",
            "appActivity": ".view.WelcomeActivityAlias",
            "noReset": True,  # 对上次操作不做重置（比如点掉更新软件，则会记住这个操作，下次再启动软件则不会跳出更新软件提示）
            # "dontStopAppOnReset": True,  # 不关闭app,继续操作
            "skipDeviceInitialization": True,  # 跳过设备初始化
            # "skipServerInstallation": True,
            "unicodeKeyBoard": True,        # 允许中文输入
            "resetKeyBoard": True
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)  # 隐式等待

    def teardown(self):
        # pass
        self.driver.quit()

    @allure.story("参数化用例1")
    @allure.title("参数化用例1")
    @pytest.mark.parametrize('sendKeys, textName, expected_price', [('alibaba', 'BABA', 210), ('xiaomi', '01810',
                                                                                                 26.55)])
    def test_para1(self, sendKeys, textName, expected_price):
        """
        1、打开雪球 应用
        2、点击 搜索框
        3、输入 搜索词 'alibaba' or 'xiaomi'...
        4、点击 第一个搜索结果
        5、判断股票价格
        """
        with allure.step("步骤一：打开雪球应用"):
            print("已打开雪球应用")
        with allure.step("步骤二：点击搜索框"):
            self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/tv_search").click()
            # self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        with allure.step("步骤三：输入搜索词：alibaba"):
            self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/search_input_text").send_keys(sendKeys)
        with allure.step("步骤四：点击第一个搜索结果"):
            self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/name").click()
        with allure.step("步骤五：判断股票价格"):
            current_price = float(self.driver.find_element(MobileBy.XPATH, f"//*[@text='{textName}']/../../..//*[@resource-id="
                                                                    "'com.xueqiu.android:id/current_price']").text)
            print(f"{current_price}")
            assert_that(current_price, close_to(expected_price, expected_price*0.1))


if __name__ == '__main__':
    pytest.main()
