# -*- coding: utf-8 -*-
# @Time     : 2020/1/30 16:00
# @Author   : lemon_ml
# @Email    : 8768765@qq.com
# @File     : baspage.py
# @Software : PyCharm

import os
from datetime import datetime
from time import sleep

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver

from Common.file_path import SHOT_PATH
from Common.handle_log import do_log
from Common.upload_files import upload


class Base_Page:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def save_page_shot(self, img_doc):
        """
        保存截图封装
        :param img_doc:
        :return:
        """
        shot_name = os.path.join(SHOT_PATH, img_doc) + "_" + \
                    datetime.strftime(datetime.now(), '%Y%m%d%H%M%S') + ".png"
        try:
            self.driver.save_screenshot(shot_name)
        except AssertionError as e:
            do_log.error("保存截图失败{}".format(e))
        else:
            do_log.info("保存截图成功")

    def wait_ele_visiball(self, loc, img_doc, timeout=20, poll_frequency=0.5):
        """
        等待元素封装
        :param loc:
        :param img_doc:
        :param timeout:
        :param poll_frequency:
        :return:
        """
        do_log.info("等待{}可见".format(img_doc))
        star_time = datetime.now()
        try:
            WebDriverWait(self.driver, timeout, poll_frequency).until(EC.visibility_of_element_located(loc))
        except:
            self.save_page_shot(img_doc)
            do_log.error("等待{}失败，保存截图".format(img_doc))
            raise
        else:
            end_time = datetime.now()
            do_log.info("等待{}可见成功，共等待{}".format(img_doc, (end_time - star_time)))

    def get_element(self, loc, img_doc):
        """
        查找元素
        :param loc:
        :param img_doc:
        :return:
        """
        do_log.info("查找{}可见".format(img_doc))
        try:
            ele = self.driver.find_element(*loc)
        except:
            self.save_page_shot(img_doc)
            do_log.error("查找{}失败，保存截图".format(img_doc))
            raise
        else:
            return ele

    def click_element(self, loc, img_doc, timeout=20, poll_frequency=0.5):
        """
        点击元素
        :param loc:
        :param img_doc:
        :param timeout:
        :param poll_frequency:
        :return:
        """
        self.wait_ele_visiball(loc, img_doc, timeout, poll_frequency)
        ele = self.get_element(loc, img_doc)
        do_log.info("点击{}元素".format(img_doc))
        try:
            ele.click()
        except:
            self.save_page_shot(img_doc)
            do_log.info("点击{}失败，保存截图".format(img_doc))
            raise

    def input_element(self, loc, text, img_doc, timeout=20, poll_frequency=0.5):
        """
        输入框输入内容
        :param loc:
        :param text:
        :param img_doc:
        :param timeout:
        :param poll_frequency:
        :return:
        """
        self.wait_ele_visiball(loc, img_doc, timeout, poll_frequency)
        ele = self.get_element(loc, img_doc)
        try:
            ele.send_keys(text)
        except:
            self.save_page_shot(img_doc)
            do_log.info("{}输入失败，保存截图".format(img_doc))
            raise
        else:
            do_log.info("{}输入内容成功".format(img_doc))

    def get_text(self, loc, img_doc, timeout=20, poll_frequency=0.5):
        """
        获取文本内容
        :param loc:
        :param img_doc:
        :param timeout:
        :param poll_frequency:
        :return:
        """
        self.wait_ele_visiball(loc, img_doc, timeout, poll_frequency)
        ele = self.get_element(loc, img_doc)
        do_log.info("获取{}文本内容".format(img_doc))
        try:
            text = ele.text
        except:
            self.save_page_shot(img_doc)
            do_log.info("{}获取文本失败，保存截图".format(img_doc))
            raise
        else:
            do_log.info("{}获取文本成功".format(img_doc))
            return text

    def get_attr_element(self, loc, attr_name, img_doc, timeout=20, poll_frequency=0.5):
        """
        获取元素属性
        :param loc:
        :param attr_name:
        :param img_doc:
        :param timeout:
        :param poll_frequency:
        :return:
        """
        self.wait_ele_visiball(loc, img_doc, timeout, poll_frequency)
        ele = self.get_element(loc, img_doc)
        try:
            do_log.info("获取{}元素属性".format(img_doc))
            attr = ele.get_attribute(attr_name)
        except:
            self.save_page_shot(img_doc)
            do_log.info("获取{}元素属性失败，保存截图".format(img_doc))
            raise
        else:
            do_log.info("获取{}属性成功".format(attr_name))
            return attr

    def switch_to_iframe(self, iframe_loc, img_doc, timeout=20):
        """
        切换iframe窗口
        :param iframe_loc:
        :param img_doc:
        :param timeout:
        :return:
        """
        try:
            WebDriverWait(self.driver, timeout).until(EC.frame_to_be_available_and_switch_to_it(iframe_loc))
        except:
            do_log.info("切换{}iframe窗口失败".format(img_doc))
            self.save_page_shot(img_doc)
            raise
        else:
            sleep(2)
            do_log.info("切换{}iframe窗口成功".format(img_doc))

    def switch_to_windows(self, img_doc):
        """
        切换窗口
        :param img_doc:
        :return:
        """
        wins = self.driver.window_handles
        try:
            self.driver.switch_to.window(wins[-1])
        except:
            do_log.info("切换{}窗口失败".format(img_doc))
            self.save_page_shot(img_doc)
            raise
        else:
            do_log.info("切换{}窗口成功".format(img_doc))

    def switch_to_win(self):
        """
        获取当前窗口句柄
        :return:
        """
        return self.driver.current_window_handle

    def switch_to_yuan_window(self, handle):
        """
        切换回原窗口
        :return:
        """
        self.driver.switch_to.window(handle)

    def upload_file(self, filePath):
        """
        上传文件
        :param filePath:
        :return:
        """
        do_log.info("开始上传文件")
        try:
            upload(filePath)
        except:
            do_log.info("上传文件失败")
            raise
        else:
            do_log.info("上传文件成功")

    def clear_input(self, loc, img_loc):
        ele = self.get_element(loc, img_loc)
        try:
            ele.clear()
        except:
            do_log.info("清空失败")
            self.save_page_shot(img_loc)
            raise
        else:
            do_log.info("清空成功")

    def close_windows(self):
        self.driver.close()
