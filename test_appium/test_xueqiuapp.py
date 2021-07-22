""""


"""
from time import sleep

import allure
from appium import webdriver
import pytest
from appium.webdriver.common.touch_action import TouchAction


@allure.feature("雪球app测试实战")
@allure.title("雪球app测试实战")
class TestXueQiu:
    def setup(self):
        desired_caps = {
            "platformName": "Android",
            "deviceName": "emulator-5554",
            "appPackage": "com.xueqiu.android",
            "appActivity": ".view.WelcomeActivityAlias",
            "noReset": True,  # 对上次操作不做重置（比如点掉更新软件，则会记住这个操作，下次再启动软件则不会跳出更新软件提示）
            # "dontStopAppOnReset": True,  # 不关闭app,继续操作
            "skipDeviceInitialization": True,  # 跳过设备初始化
            "unicodeKeyBoard": True,        # 允许中文输入
            "resetKeyBoard": True
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)  # 隐式等待

    def teardown(self):
        # self.driver.back()
        # self.driver.back()
        # self.driver.back()  # 回到首页（模拟手工测试，返回三次之后才能回到桌面）
        self.driver.quit()

    @allure.story("雪球阿里巴巴股价查询")
    @allure.title("雪球阿里巴巴股价查询")
    def test_search(self):
        """"
        1、打开雪球
        2、点击搜索框
        3、填入”阿里巴巴“
        4、在搜索结果里选择”阿里巴巴“，然后进行点击
        5、获取这只上 阿里巴巴的股价，并判断这只股价的价格>200
        """
        with allure.step("步骤一：打开雪球"):
            el1 = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
            el1.click()
        with allure.step("步骤二：找到输入框"):
            el2 = self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
        with allure.step("步骤三：输入'阿里巴巴'"):
            el2.send_keys("阿里巴巴")
        with allure.step("步骤四：在结果中选择‘阿里巴巴’并点击"):
            el3 = self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']")
            el3.click()
        with allure.step("步骤五：获取阿里巴巴股价信息并断言其大于200"):
            current_price = float(self.driver.find_element_by_id("com.xueqiu.android:id/current_price").text)
            assert current_price > 200

    @allure.story("获取属性值测试")
    @allure.title("获取属性值测试")
    def test_attribute(self):
        """"
        1、打开雪球应用首页
        2、定位首页的搜索框
        3、判断搜索框的是否可用，并查看搜索框name属性值
        4、打印搜索框这个元素的左上角坐标和它的宽高
        5、向搜索框输入：alibaba
        6、判断【阿里巴巴】是否可见
        7、如果可见，打印”搜索成功“点击，如果不可见，打印”搜索失败“
        """
        with allure.step("步骤一：打开雪球应用首页"):
            self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        with allure.step("步骤二：定位首页的搜索框"):
            el1 = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        with allure.step("步骤三：判断搜索框是否可用，并查看搜索框name属性值"):
            el1_enabled = el1.is_enabled()
            # print(el1.text)     # 下面这句代码同样可行
            print(el1.get_attribute("name"))
            if el1_enabled:
                print("搜索框可用")
            else:
                print("搜索框不可用")
        with allure.step("步骤四：打印搜索框这个元素的左上角坐标和它的宽高"):
            print(el1.location)
            print(el1.size)
        with allure.step("步骤五：向搜索框输入：alibaba"):
            el1.click()
            el2 = self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
            el2.send_keys("alibaba")
        with allure.step("步骤六：判断【阿里巴巴】是否可见"):
            el3 = self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']")
            is_diaplayed_ornot = el3.get_attribute("displayed")
        with allure.step("步骤七：如果可见，打印”搜索成功“点击，如果不可见，打印”搜索失败“"):
            if is_diaplayed_ornot == 'true':
                print("搜索成功")
            else:
                print("搜索失败")

    @allure.story("xpath高级定位测试")
    @allure.title("xpath高级定位测试")
    def test_xpathexpracise(self):
        """"
        1、打开雪球
        2、点击搜索框
        3、填入”阿里巴巴“
        4、在搜索结果里选择”阿里巴巴“，然后进行点击
        5、获取这只上香港 阿里巴巴的股价，并判断这只股价的价格<200
        """
        with allure.step("步骤一：打开雪球"):
            el1 = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
            el1.click()
        with allure.step("步骤二：找到输入框"):
            el2 = self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
        with allure.step("步骤三：输入'阿里巴巴'"):
            el2.send_keys("阿里巴巴")
        with allure.step("步骤四：在结果中选择‘阿里巴巴’并点击"):
            el3 = self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']")
            el3.click()
        with allure.step("步骤五：获取这只上香港 阿里巴巴的股价，并判断这只股价的价格<200"):
            current_price = float(self.driver.find_element_by_xpath(
                "//*[@text='09988']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']").text)
            assert current_price > 200

    @allure.feature("雪球app我的选项-uiautomator")
    @allure.title("雪球app我的选项-uiautomator")
    def test_myinfo(self):
        """"
        1、点击我的，进入到个人信息页面
        2、点击登录，进入到登录页面
        3、输入用户名，输入密码
        4、点击登录


        """
        with allure.step("点击我的，进入到个人信息页面"):
            self.driver.find_element_by_android_uiautomator('new UiSelector().text("我的")').click()
        with allure.step("点击登录，进入到登录页面"):
            self.driver.find_element_by_android_uiautomator('new UiSelector().text("登录雪球")').click()  # 下句代码有问题
            # self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("账号密码")').click()
        with allure.step("输入用户名，输入密码"):
            self.driver.find_element_by_android_uiautomator(
                'new UiSelector().resourceId("com.xueqiu.android:id/login_account")').send_keys("17826829606")
            self.driver.find_element_by_android_uiautomator(
                'new UiSelector().resourceId("com.xueqiu.android:id/login_password")').send_keys("120811dongjian")
            sleep(3)
        with allure.step("点击登录"):
            self.driver.find_element_by_android_uiautomator(
                'new UiSelector().resourceId("com.xueqiu.android:id/button_next")').click()

    @allure.feature("滑动定位")
    @allure.title("滑动定位")
    def test_scrollintoview(self):
        with allure.step("点击关注"):
            self.driver.find_element_by_android_uiautomator('new UiSelector().text("关注")').click()
        with allure.step("查找'雪球访谈'"):
            self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().scrollable('
                                                            'true).instance(0)).scrollIntoView(new UiSelector().text('
                                                            '"雪球访谈").instance(0));').click()
        sleep(5)

    @allure.story("触屏操作自动化")
    @allure.title("触屏操作自动化")
    def test_touch_action(self):
        with allure.step("垂直滑动一定距离:固定坐标"):
            action = TouchAction(self.driver)
            sleep(5)
            action.press(x=400, y=1000).wait(200).move_to(x=400, y=250).release().perform()
        with allure.step("垂直滑动一定距离：相对坐标"):
            action = TouchAction(self.driver)
            sleep(4)
            # print(self.driver.get_window_rect())
            window_rect = self.driver.get_window_rect()
            width = self.driver.get_window_rect()['width']
            height = self.driver.get_window_rect()['height']
            x1 = int(width / 2)
            y_start = int(height * 4 / 5)
            y_end = int(height / 5)
            action.press(x=x1, y=y_start).wait(200).move_to(x=x1, y=y_end).release().perform()


@allure.feature("手势操作模块")
@allure.title("手势操作模块")
class TestTouchActionGestures:
    def setup(self):
        desired_caps = {
            "platformName": "Android",
            "deviceName": "emulator-5554",
            "appPackage": "cn.kmob.screenfingermovelock",
            "appActivity": "com.samsung.ui.MainActivity",
            "noReset": True,  # 对上次操作不做重置（比如点掉更新软件，则会记住这个操作，下次再启动软件则不会跳出更新软件提示）
            # "dontStopAppOnReset": True,  # 不关闭app,继续操作
            "skipDeviceInitialization": True,  # 跳过设备初始化
            "unicodeKeyBoard": True,  # 允许中文输入
            "resetKeyBoard": True
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)  # 隐式等待

    def teardown(self):
        self.driver.quit()

    @allure.story("手势操作")
    @allure.title("手势操作")
    def test_gestures(self):
        with allure.step("解锁手势密码"):
            action = TouchAction(self.driver)
            action.press(x=117, y=174).wait(100).move_to(x=358, y=174).wait(100).move_to(x=600, y=174).wait(100).move_to(x=600, y=416).wait(100).move_to(x=600, y=657).release().perform()


if __name__ == '__main__':
    pytest.main()
