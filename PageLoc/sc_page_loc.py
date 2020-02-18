# -*- coding: utf-8 -*-
# @Time     : 2020/1/30 13:10
# @Author   : lemon_ml
# @Email    : 8768765@qq.com
# @File     : sc_page_loc.py
# @Software : PyCharm

from selenium.webdriver.common.by import By


class Sc_Page_Loc:

    # 留言输入按钮
    liuyan_button = (By.XPATH, '//span[@class="s2"]')
    # 留言输入框
    liuyan_input = (By.XPATH, '//textarea[@id="comment"]')
    # 留言保存按钮
    save_button = (By.XPATH, '//a[text()="保存"]')
    # 添加作业按钮
    add_button = (By.XPATH, '//div[@class="shangchuan"]//a[contains(@class, "sc-btn")]')
    # 提交按钮
    tj_button = (By.XPATH, '//a[text()="提交"]')
    # 上传成功后文件名
    sc_filename = (By.XPATH, '//div[@class="file-cont fl"]//a[contains(@title, "软件测试")]')
    # 作业提交成功弹窗提示语
    cg_window = (By.XPATH, '//div[text()="作业提交成功"]')
    # 作业提交成功弹窗知道了按钮
    know_button = (By.XPATH, '//a[text()="知道了"]')
    # 更新提交按钮
    upd_button_before = (By.XPATH, '//a[@class="new-tj1"]')
    upd_button_after = (By.XPATH, '//a[contains(@class, "new-tj2 active")]')
    # 点击更新后弹窗取消按钮
    cancel_button = (By.XPATH, '//div[@id="update-pop"]//a[@class="cancel"]')
    # 点击更新后弹窗确定按钮
    determine_button = (By.XPATH, '//div[@id="update-pop"]//a[@class="sure active"]')
    # 上传作业页面返回按钮
    fanhui_button = (By.XPATH, '//i[@class="iconfont iconfanhui"]')
    # 课堂按钮
    ke_button = (By.XPATH, '//ul[@class="nav-menu-left"]/li[3]//a')



