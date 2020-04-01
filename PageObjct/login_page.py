# -*- coding: utf-8 -*-
# @Time     : 2020/1/30 15:59
# @Author   : lemon_ml
# @Email    : 8768765@qq.com
# @File     : login_page.py
# @Software : PyCharm

from PageLoc.login_page_loc import Login_Page_Loc as lp_loc
from Common.basepage import Base_Page


class LoginPage(Base_Page):

    def login(self, phone, pwd):
        """
        登录
        :param phone:
        :param pwd:
        :return:
        """
        self.input_element(lp_loc.input_phone, phone, "登录页面_手机号输入框")
        self.input_element(lp_loc.input_pwd, pwd, "登录页面_密码输入框")
        self.click_element(lp_loc.button_login, "登录页面_登录按钮")

    def get_error_phone_text(self):
        """
        输入错误的账号返回提示语
        :return:
        """
        return self.get_text(lp_loc.error_phone, "登录页面_账号错误提示语")

    def get_error_pwd_text(self):
        """
        输入错误的密码返回提示语
        :return:
        """
        return self.get_text(lp_loc.error_pwd, "登录页面_密码错误提示语")

    def clear_input_phone(self):
        """
        清空手机号
        :return:
        """
        self.get_element(lp_loc.input_phone, "清空手机号").clear()

    def clear_input_pwd(self):
        """
        清空手机号
        :return:
        """
        self.get_element(lp_loc.input_pwd, "清空密码").clear()