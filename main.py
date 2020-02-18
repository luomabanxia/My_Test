# -*- coding: utf-8 -*-
# @Time     : 2020/1/29 19:38
# @Author   : lemon_ml
# @Email    : 8768765@qq.com
# @File     : main.py
# @Software : PyCharm

import pytest


if __name__ == '__main__':
    pytest.main(["--reruns", "2", "--reruns-delay", "5",
                 "--html=Outputs/reports/result.html",
                 "--alluredir=Outputs/allure_report"])