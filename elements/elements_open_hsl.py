from selenium.webdriver.common.by import By



class ElementsOpenHsl:

    open_hsl_to_not_agree_rules_id = (By.ID, "com.hsl.stock:id/txt_cancel")
    open_hsl_to_agree_rules_id = (By.ID, "com.hsl.stock:id/txt_buy")
    hsl_rules_id = (By.ID, "com.hsl.stock:id/tvContent")
    hsl_back_button_id = (By.ID, "com.hsl.stock:id/imageBack")
    confuse_hsl_rules_button_xpath = (By.XPATH, "//*[contains(@text, '暂不')]")
    go_agree_button_xpath = (By.XPATH, "//*[contains(@text, '去同意')]")
    login_for_agree_system_power_id = (By.ID, "android:id/button1")
    hsl_rules_text_id = (By.ID, "com.hsl.stock:id/tvContent")
    toast_xpath = (By.XPATH, "//*[@class='android.widget.Toast']")



class ElementsHomePage:
    open_first_page_level_power_xpath = (By.XPATH, "//*[contains(@text, '涨停强度')]")
    get_first_assert_text_xpath = (By.XPATH, "//*[contains(@text, '涨停成功率')]")
    go_to_mine_page_xpath = (By.XPATH, "//*[contains(@bounds, '[864,2016][1080,2030]')]")
    close_learn_some_id = (By.ID, "com.hsl.stock:id/tv_cancel")
    open_login_to_hsl_id = (By.ID, "com.hsl.stock:id/linearPayDetail")
    input_id_for_login_button_id = (By.ID, "com.hsl.stock:id/edit_phone_num")
    input_password_for_login_button_id = (By.ID, "com.hsl.stock:id/eidt_password")
    login_button_id = (By.ID, "com.hsl.stock:id/btn_login")
    get_username_id = (By.ID, "com.hsl.stock:id/tv_user_name")
    get_level2_button_home_id = (By.ID, "com.hsl.stock:id/tv_shangzheng")


