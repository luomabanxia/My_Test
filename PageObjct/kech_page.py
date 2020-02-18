# -*- coding: utf-8 -*-
# @Time     : 2020/1/31 12:27
# @Author   : lemon_ml
# @Email    : 8768765@qq.com
# @File     : kech_page.py
# @Software : PyCharm

from Common.basepage import Base_Page
from PageLoc.kech_page_loc import Kech_Page_Loc as kp_loc


class Kech_Page(Base_Page):

    def wait_chengji(self):
        """
        课程页面成绩元素可见
        :return:
        """
        try:
            self.wait_ele_visiball(kp_loc.chengji, "课程页面_成绩按钮")
        except:
            return False
        else:
            return True

    def click_zuoye_btn(self):
        """
        点击作业按钮
        :return:
        """
        self.click_element(kp_loc.work_button, "课程页面_作业按钮")

    def click_ytj(self):
        """
        点击已提交按钮
        :return:
        """
        self.click_element(kp_loc.ytj, "课程作业页面_已提交按钮")


