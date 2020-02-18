# -*- coding: utf-8 -*-
# @Time     : 2020/1/31 20:49
# @Author   : lemon_ml
# @Email    : 8768765@qq.com
# @File     : conftest.py
# @Software : PyCharm

import pytest
from selenium import webdriver
from time import sleep

from TestDatas.Common_Data import login_url, number, pwd
from PageLoc.login_page_loc import Login_Page_Loc as lp_loc
from PageObjct.login_page import LoginPage
from TestDatas.Common_Data import phone, pwd
from PageObjct.home_page import HomePage
from PageObjct.kech_page import Kech_Page
from PageObjct.sc_page import Sc_Page
from PageObjct.sixin_page import Sx_Page
from Common.basepage import Base_Page


@pytest.fixture()
def int_driver():
    driver = webdriver.Chrome()
    driver.get(login_url)
    driver.maximize_window()
    driver.find_element(*lp_loc.login_button).click()
    yield driver
    driver.quit()


@pytest.fixture()
def login_setUp(int_driver):
    lp = LoginPage(int_driver)
    yield int_driver, lp


@pytest.fixture()
def jiake_setUp(int_driver):
    LoginPage(int_driver).login(phone, pwd)
    hp = HomePage(int_driver)
    hp.click_close()
    yield int_driver, hp


@pytest.fixture()
def sc_setUp(int_driver):
    LoginPage(int_driver).login(phone, pwd)
    HomePage(int_driver).click_close()
    HomePage(int_driver).jiake(number)
    HomePage(int_driver).click_ke_title()
    kc = Kech_Page(int_driver)
    kc.click_zuoye_btn()
    sleep(2)
    sc = Sc_Page(int_driver)
    yield kc, sc, int_driver
    sc.fanhui()
    HomePage(int_driver).out_ke(pwd)


@pytest.fixture()
def sixin_setUp(int_driver):
    LoginPage(int_driver).login(phone, pwd)
    HomePage(int_driver).click_close()
    sx = Sx_Page(int_driver)
    sx.sx_button()
    sx.switch_to_windows("课程页面_切换私信窗口")
    yield int_driver, sx


# @pytest.fixture()
# def sixin_setUp(int_driver):
#     LoginPage(int_driver).login(phone, pwd)
#     HomePage(int_driver).click_close()
#     HomePage(int_driver).jiake(number)
#     HomePage(int_driver).click_ke_title()
#     kc = Kech_Page(int_driver)
#     sc = Sc_Page(int_driver)
#     kc.click_zuoye_btn()
#     bp = Base_Page(int_driver)
#     handle = bp.switch_to_win()
#     sx = Sx_Page(int_driver)
#     sx.sx_button()
#     sx.switch_to_windows("课程页面_切换私信窗口")
#     yield sx, handle, bp
#     sc.click_ke()
#     HomePage(int_driver).out_ke(pwd)
