from time import sleep
import allure

from base.get_driver import get_phone_driver
from base.page import Page

@allure.feature("首次打开app")
class TestHslOpen:

    def setup_class(self):
        self.driver = get_phone_driver("com.hsl.stock", ".module.main.StartV2Activity")
        self.page = Page(self.driver)

    def teardown_class(self):
        self.driver.quit()


    # def teardown(self):
    #     for i in range(4):
    #         self.driver.back()

    # def test_01(self):
    #     self.page.open_hsl().open_rules_click_agrees()
    #     ass = self.page.open_hsl().get_result()
    #     assert ass == "兔子人"

    @allure.step("打开app")
    @allure.step("然后不同意条约")
    @allure.step("再次打开app")
    @allure.story("首次打开app不同意用户协议")
    @allure.issue("https://www.bugclose.com/bug.html?id=51588&projectId=38335")
    @allure.testcase("https://www.bugclose.com/testCase.html?id=2065&projectId=38335")
    def test_open_hsl_refuse_rules(self):
        '''
        用例描述:首次打开app不同意用户协议和隐私政策会退出app,下次启动时仍然弹出条约弹窗
        setup: 打开app
        step1: 不同意条约
        step2: 确定以及肯定不同意
        step3: 重新热启动打开app
        step4: 仍然首先弹出条约弹窗
        assert:断言弹窗是否存在
        '''
        self.page.open_hsl().open_not_agree_rules()
        self.driver = get_phone_driver("com.hsl.stock", ".module.main.StartV2Activity")
        assert "具体要求点击上方红色" in self.page.open_hsl().get_hsl_rules_result()

    @allure.testcase("pass")
    def test_open_rules_right(self):
        allure.attach("这是一个文本信息", attachment_type=allure.attachment_type.TEXT)


    @allure.testcase("首次打开app同意用户协议")
    def test_open_hsl_agree_rules(self):
        self.page.open_hsl().open_agree_rules()
        # filename = "./images/tt.png"
        # self.driver.save_screenshot("./images/tt.png")
        # allure.attach.file(r"./images/tt.png", attachment_type=allure.attachment_type.PNG)


    @allure.testcase("登陆时不输入密码")
    def test_not_input_pwd_login(self):
        self.page.open_hsl().login_hsl_warning_password()

    @allure.testcase("滑动")
    def test_swipe(self):
        self.page.open_hsl().swipe_test()
        allure.attach('''
        <div class="col-sm-12 bugTestTaskInfoDescription">前提条件：处于非活动期间<br>测试步骤：用户A打赏给操盘手B&nbsp;91元，获得10天<br>预期结果：无法获得额外天数<br>实际结果：无法获得额外天数</div>''', attachment_type=allure.attachment_type.HTML)

    @allure.testcase("测试图片视频上传allure测试报告")
    def test_imp_MP4(self):
        allure.attach.file(r"C:\Users\86131\Desktop\图片\_{~~S[10I$(UQ8V9_]QG`)J.png",
                           attachment_type=allure.attachment_type.JPG, name="Aileen")
        allure.attach.file(r"C:\Users\86131\Desktop\RPReplay_Final1599210159.MP4",
                           attachment_type=allure.attachment_type.MP4, name="选股复现")



    def test_click_rules_screen_size(self):
        self.page.open_hsl().screen_press_in_rules()

