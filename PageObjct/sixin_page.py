# -*- coding: utf-8 -*-
# @Time     : 2020/1/31 19:12
# @Author   : lemon_ml
# @Email    : 8768765@qq.com
# @File     : sixin_page.py
# @Software : PyCharm

from time import sleep

from Common.basepage import Base_Page
from PageLoc.sixin_page_loc import Sx_Page_Loc as sx_loc


class Sx_Page(Base_Page):

    def sx_button(self):
        """
        点击私信按钮
        :return:
        """
        self.click_element(sx_loc.sixin_button, "课程页面_私信按钮")

    def sc_fujian(self, filePath):
        """
        上传附件
        :param filePath:
        :return:
        """
        self.click_element(sx_loc.append_button, "私信页面_附件按钮")
        sleep(2)
        self.upload_file(filePath)
        sleep(3)

    def send_xiaoxi(self, text):
        """
        发送私信信息
        :param text:
        :return:
        """
        self.input_element(sx_loc.sx_input, text, "私信页面_输入信息")
        self.click_element(sx_loc.send_button, "私信页面_发送按钮")

    def get_error_xinxi(self):
        """
        获取发送空消息后提示语
        :return:
        """
        return self.get_text(sx_loc.error_xinxi, "私信页面_发空消息")

    def close_sixin_win(self):
        self.close_windows()

    def get_text_sixin(self):
        """
        获取文本消息最新一条文本消息内容
        :return:
        """
        try:
            self.wait_ele_visiball(sx_loc.one_text_xinxi, "文本元素")
        except:
            return self.get_text(sx_loc.one_file_xinxi, "文件名字")
        else:
            return self.get_text(sx_loc.one_text_xinxi, "私信页面_第一条私信")