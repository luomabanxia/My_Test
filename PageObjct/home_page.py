# -*- coding: utf-8 -*-
# @Time     : 2020/1/31 11:03
# @Author   : lemon_ml
# @Email    : 8768765@qq.com
# @File     : home_page.py
# @Software : PyCharm

from Common.basepage import Base_Page
from PageLoc.home_page_loc import Home_Page_Loc as hp_loc


class HomePage(Base_Page):

    def wait_close_button(self):
        """
        等待首次进入加课页弹窗出现
        :return:
        """
        try:
            self.wait_ele_visiball(hp_loc.close_button, "加课页_首次弹窗关闭按钮")
        except:
            return False
        else:
            return True

    def wait_quxiao_btn(self):
        """
        加课弹窗取消按钮
        :return:
        """
        try:
            self.wait_ele_visiball(hp_loc.remove_button, "加课页_加课弹窗取消按钮")
        except:
            return False
        else:
            return True

    def jiake(self, text):
        """
        加课弹窗输入加课码点击确定按钮
        :param text:
        :return:
        """
        self.click_element(hp_loc.icon_kecheng, "加课页_加课按钮")
        self.input_element(hp_loc.input_jiakema, text, "加课弹窗_输入加课码")
        self.click_element(hp_loc.determine_button, "加课弹窗_确定按钮")

    def click_title(self):
        """
        点击加课页课程标题
        :return:
        """
        self.click_element(hp_loc.kecheng_title, "加课页_课程标题")

    def out_ke(self, text):
        """
        点击退课按钮
        :return:
        """
        self.click_element(hp_loc.more_button, "加课页面_更多按钮")
        self.click_element(hp_loc.tuike_button, "加课页面_退课按钮")
        self.input_element(hp_loc.tuike_input, text, "退课弹窗_密码输入框")
        self.click_element(hp_loc.tuike_determine_button, "退课弹窗_确定按钮")

    def get_jiake_text(self):
        """
        加课成功或失败提示语
        :return:
        """
        return self.get_text(hp_loc.input_error, "加课成功/失败_提示语")

    def click_ke_title(self):
        """
        点击课程标题
        :return:
        """
        self.click_element(hp_loc.kecheng_title, "加课页面_课程标题")

    def click_close(self):
        self.click_element(hp_loc.close_button, "登录成功后_弹窗关闭按钮")


