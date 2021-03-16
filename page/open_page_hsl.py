from time import sleep

from base.base import Base
from elements.elements_open_hsl import ElementsHomePage, ElementsOpenHsl



class OpenInHsl(Base):

    def __init__(self, driver):
        Base.__init__(self, driver)

    def open_rules_click_agrees(self):
        self.click_element(ElementsOpenHsl.open_hsl_to_agree_rules_id)
        self.click_element(ElementsOpenHsl.login_for_agree_system_power_id)
        self.click_element(ElementsOpenHsl.login_for_agree_system_power_id)
        # self.click_element(ElementsHSL.open_first_page_level_power_xpath)
        self.click_element(ElementsHomePage.go_to_mine_page_xpath)
        self.click_element(ElementsHomePage.close_learn_some_id)
        self.click_element(ElementsHomePage.open_login_to_hsl_id)
        self.click_element(ElementsHomePage.input_id_for_login_button_id)
        self.send_element(ElementsHomePage.input_id_for_login_button_id, "13120683383")
        self.click_element(ElementsHomePage.input_password_for_login_button_id)
        self.send_element(ElementsHomePage.input_password_for_login_button_id, "123456")
        self.click_element(ElementsHomePage.login_button_id)


    def get_result(self):
        # res = self.get_element(ElementsHSL.get_first_assert_text_xpath).text
        res = self.get_element(ElementsHomePage.get_username_id).text
        return res

    def open_not_agree_rules(self):
        self.click_element(ElementsOpenHsl.open_hsl_to_not_agree_rules_id)
        self.click_element(ElementsOpenHsl.confuse_hsl_rules_button_xpath)


    def get_hsl_rules_result(self):
        re = self.get_element(ElementsOpenHsl.hsl_rules_text_id).text
        return re

    def open_agree_rules(self):
        self.click_element(ElementsOpenHsl.open_hsl_to_agree_rules_id)
        self.click_element(ElementsOpenHsl.login_for_agree_system_power_id)
        self.click_element(ElementsOpenHsl.login_for_agree_system_power_id)
        re = self.get_element(ElementsHomePage.get_level2_button_home_id).text
        self.screen_page()

        assert re == "免费Level-2"




    def login_hsl_warning_password(self):
        self.click_element(ElementsHomePage.go_to_mine_page_xpath)
        self.click_element(ElementsHomePage.close_learn_some_id)
        self.click_element(ElementsHomePage.open_login_to_hsl_id)
        self.click_element(ElementsHomePage.input_id_for_login_button_id)
        self.send_element(ElementsHomePage.input_id_for_login_button_id, "13120683383")
        self.click_element(ElementsHomePage.login_button_id)
        re = self.get_element(ElementsOpenHsl.toast_xpath).text
        assert "请输入" in re


    def open_hsl_rules(self):
        print(self.driver.page_source)


    def swipe_test(self):
        self.swip_window_right_to_left()
        sleep(2)

    def screen_press_in_rules(self):
        sleep(20)
        self.sccren_in()
        sleep(5)
