# -*- coding: utf-8 -*-
# @Time     : 2020/1/29 20:04
# @Author   : lemon_ml
# @Email    : 8768765@qq.com
# @File     : login_page_loc.py
# @Software : PyCharm

from selenium.webdriver.common.by import By


class Login_Page_Loc:

    # 顶部登录按钮
    login_button = (By.XPATH, '//a[@class="login"]')
    # 账号输入框
    input_phone = (By.XPATH, '//input[@name="account"]')
    # 密码输入框
    input_pwd = (By.XPATH, '//input[@name="pass"]')
    # 输入账号密码后登录按钮
    button_login = (By.XPATH, '//div[@class="padding-cont pt-login"]//a[@class="btn-btn"]')
    # 账号错误提示语
    error_phone = (By.XPATH, '//div[@class="input"]//p[@class="error-tips"]')
    # 错误密码提示语
    error_pwd = (By.XPATH, '//div[@class="input errtips"]//p[@class="error-tips"]')


