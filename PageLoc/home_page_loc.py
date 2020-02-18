# -*- coding: utf-8 -*-
# @Time     : 2020/1/29 20:48
# @Author   : lemon_ml
# @Email    : 8768765@qq.com
# @File     : home_page_loc.py
# @Software : PyCharm

from selenium.webdriver.common.by import By


class Home_Page_Loc:

    # 进入首页后弹窗关闭按钮
    close_button = (By.XPATH, '//a[@class="close"]')
    # 页面中间的加课程
    icon_kecheng = (By.XPATH, '//i[@class="iconfont iconchuangjiankecheng"]')
    # 加课码输入框
    input_jiakema = (By.XPATH, '//div[@class="chuangjiankc"]//input[@type="text"]')
    # 加课弹窗取消按钮
    remove_button = (By.XPATH, '//a[@class="btn btn-defalut"]')
    # 输入错误加课码错误提示弹窗和加入成功后弹窗
    input_error = (By.XPATH, '//div[@class="gTips"]')
    # 加课程弹窗确定按钮
    determine_button = (By.XPATH, '//li[@class="cjli2"]')
    # 课程标题
    kecheng_title = (By.XPATH, '//dt[@class="bgclass1"]//a[@title]')
    # 更多按钮
    more_button = (By.XPATH, '//div[@id="viewer-container-toplists"]//a[@class="kdmore"]')
    # 退课按钮
    tuike_button = (By.XPATH, '//dt[@class="bgclass1"]//a[text()="退课"]')
    # 退课确认弹窗输入框
    tuike_input = (By.XPATH, '//input[@type="password"]')
    # 退课弹窗确定按钮
    tuike_determine_button = (By.XPATH, '//div[@class="deletekt"]//a[@class="btn btn-positive"]')

