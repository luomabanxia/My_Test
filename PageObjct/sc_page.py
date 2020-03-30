# -*- coding: utf-8 -*-
# @Time     : 2020/1/31 13:07
# @Author   : lemon_ml
# @Email    : 8768765@qq.com
# @File     : sc_page.py
# @Software : PyCharm

from time import sleep

from Common.basepage import Base_Page
from PageLoc.sc_page_loc import Sc_Page_Loc as sp_loc
from PageObjct.home_page import HomePage


class Sc_Page(Base_Page):

    def clear_liuyan(self):
        self.clear_input(sp_loc.liuyan_input, "留言页面_清空输入框")

    def click_update_before(self):
        self.click_element(sp_loc.upd_button_before, "上传作业前_更新提交按钮")

    def click_update_after(self):
        self.click_element(sp_loc.upd_button_after, "上传作业后_更新提交按钮")

    def update_tijiao(self):
        """
        点击更新提交按钮后点击弹窗确定按钮
        :return:
        """
        self.click_update_before()
        self.click_element(sp_loc.determine_button, "更新提交确定弹窗_确定按钮")

    def liuyan(self, text):
        """
        输入留言内容并保存
        :param text:
        :return:
        """
        self.update_tijiao()
        self.click_element(sp_loc.liuyan_button, "上传作业页面_点击留言输入框")
        self.clear_liuyan()
        self.input_element(sp_loc.liuyan_input, text, "留言_输入框")
        self.click_element(sp_loc.save_button, "留言_保存按钮")
        self.click_update_after()
        self.click_know()
        sleep(2)

    def liuyan_text(self):
        """
        获得留言后的留言信息
        :return:
        """
        return self.get_text(sp_loc.liuyan_button, "上传作业留言页面_留言输入框")

    def file_upload(self, filePath):
        """
        上传文件
        :param filePath:
        :return:
        """
        self.click_element(sp_loc.add_button, "上传页面_点击添加文件按钮")
        sleep(2)
        self.upload_file(filePath)
        sleep(3)
        self.click_update_after()
        self.click_know()
        sleep(2)

    def get_cg_text(self):
        """
        已上传提示字段
        :return:
        """
        return self.get_text(sp_loc.sc_filename, "上传文件名称")

    def update_cg_text(self):
        """
        更新提交后，提示语
        :return:
        """
        return self.get_text(sp_loc.cg_window, "更新提交_成功提示")

    def click_know(self):
        self.click_element(sp_loc.know_button, "更新成功_知道了按钮")

    def fanhui(self):
        """
        上传文件后返回至加课页面
        :return:
        """
        self.click_element(sp_loc.fanhui_button, "上传页面_返回按钮")
        sleep(2)
        self.click_element(sp_loc.ke_button, "课程页面_课程按钮")
        sleep(3)

    def click_ke(self):
        self.click_element(sp_loc.ke_button, "课程页面_课程按钮")
