# -*- coding: utf-8 -*-
# @Time     : 2020/1/30 15:00
# @Author   : lemon_ml
# @Email    : 8768765@qq.com
# @File     : sixin_page_loc.py
# @Software : PyCharm

from selenium.webdriver.common.by import By


class Sx_Page_Loc:

    # 私信按钮
    sixin_button = (By.XPATH, '//div[@class="privateLetter"]//a[@target="_blank"]')
    # 输入框
    sx_input = (By.XPATH, '//textarea[@class="ps-container"]')
    # 私信页面上传附件按钮
    append_button = (By.XPATH, '//a[@id="upload"]')
    # 发送按钮
    send_button = (By.XPATH, '//a[contains(@class, "btn-positive")]')
    # # 发送成功后信息
    # xinxi = (By.XPATH, '//div[@class="self"]//div[text()="mary测试"]')
    # 发送文件成功后验证
    # file_cg_text = (By.XPATH, '//div[@class="self"]//div[@class="file"]//a[@data-name]')
    # 发送空私信提示语
    error_xinxi = (By.XPATH, '//div[@id="error-tip"]')
    # 获取最后一条文本信息
    one_text_xinxi = (By.XPATH, '//*[@id="chat"]/div[3]/div[2]/ul/li[last()]/div/div[1]')
    # 获取最后一条文件消息文件名
    # one_file_xinxi = (By.XPATH, '//*[@id="chat"]/div[3]/div[2]/ul/li[last()]/div/div[1]/div[2]/h3/a')
    one_file_xinxi = (By.XPATH, '//*[@id="chat"]/div[3]/div[2]/ul/li[last()]/div/div[1]/div[2]/h3[@class="file-name"]')




