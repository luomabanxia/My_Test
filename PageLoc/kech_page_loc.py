# -*- coding: utf-8 -*-
# @Time     : 2020/1/30 12:01
# @Author   : lemon_ml
# @Email    : 8768765@qq.com
# @File     : kech_page_loc.py
# @Software : PyCharm

from selenium.webdriver.common.by import By


class Kech_Page_Loc:

    # 成绩按钮
    chengji = (By.XPATH, '//li[@class="li6"]')
    # 作业按钮
    work_button = (By.XPATH, '//div[@id="third-nav"]//a[text()="作业"]')
    # 上传作业按钮
    sc_button = (By.XPATH, '//div[@class="homework-list clearfix"]//a[text()="上传作业"]')
    # 提交后状态
    ytj = (By.XPATH, '//div[@class="work-new-r fl "]')




