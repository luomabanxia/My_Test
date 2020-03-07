# -*- coding: utf-8 -*-
# @Time     : 2020/1/30 21:20
# @Author   : lemon_ml
# @Email    : 8768765@qq.com
# @File     : login_datas.py
# @Software : PyCharm

from TestDatas.Common_Data import success_url

"""
1、手机号不正确，密码正确
2、手机号为空，密码正确
3、手机号正确，密码为空
4、手机号正确，密码不正确

"""
success_data = {"title": "正常登陆", "phone": "15", "pwd": "ma", "excepted": success_url}

error_phone_data_01 = {"title": "手机号不正确，密码正确", "phone": "", "pwd": "ma", "excepted": "用户不存在"}

error_phone_data_02 = {"title": "手机号为空，密码正确", "phone": "", "pwd": "m", "excepted": "用户名不能为空"}
error_pwd_data = {"title": "手机号正确，密码为空", "phone": "1", "pwd": "", "excepted": "密码不能为空"}