# -*- coding: utf-8 -*-
# @Time     : 2020/1/31 20:09
# @Author   : lemon_ml
# @Email    : 8768765@qq.com
# @File     : test_01_login.py
# @Software : PyCharm

import pytest

from TestDatas.login_datas import success_data, error_phone_data_01, error_phone_data_02, error_pwd_data
from Common.handle_log import do_log


@pytest.mark.usefixtures("login_setUp")
class TestLogin:

    def test_01_login_success(self, login_setUp):
        login_setUp[1].login(success_data["phone"], success_data["pwd"])
        assert success_data["excepted"] == login_setUp[0].current_url
        do_log.info("{}案例通过".format(success_data["title"]))

    def test_02_phone_error(self, login_setUp):
        login_setUp[1].login(error_phone_data_01["phone"], error_phone_data_01["pwd"])
        assert error_phone_data_01["excepted"] == login_setUp[1].get_error_phone_text()
        do_log.info("{}案例通过".format(error_phone_data_01["title"]))

    def test_03_phone_error(self, login_setUp):
        login_setUp[1].login(error_phone_data_01["phone"], error_phone_data_01["pwd"])
        login_setUp[1].clear_input_phone()
        login_setUp[1].clear_input_pwd()
        login_setUp[1].login(error_phone_data_02["phone"], error_phone_data_02["pwd"])
        assert error_phone_data_02["excepted"] == login_setUp[1].get_error_phone_text()
        do_log.info("{}案例通过".format(error_phone_data_02["title"]))

    def test_04_pwd_error(self, login_setUp):
        login_setUp[1].login(error_phone_data_01["phone"], error_phone_data_01["pwd"])
        login_setUp[1].clear_input_phone()
        login_setUp[1].clear_input_pwd()
        login_setUp[1].login(error_pwd_data["phone"], error_pwd_data["pwd"])
        assert error_pwd_data["excepted"] == login_setUp[1].get_error_phone_text()
        do_log.info("{}案例通过".format(error_pwd_data["title"]))


if __name__ == '__main__':
    pytest.main()
