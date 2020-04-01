# -*- coding: utf-8 -*-
# @Time     : 2020/2/1 14:35
# @Author   : lemon_ml
# @Email    : 8768765@qq.com
# @File     : jiake_datas.py
# @Software : PyCharm

# success_data = {"title": "正确加课码", "number": "P69UVV", "excepted": "加入课堂成功"}

jiake_data = [{"title": "正确加课码", "number": "P69UVV", "excepted": "加入课堂成功"},
              {"title": "空格加课码", "number": " ", "excepted": "加课验证码必须是6位字符"},
              {"title": "错误加课码", "number": "123456", "excepted": "该加课码不存在或者已经失效"},
              {"title": "重复加课码", "number": "P69UVV", "excepted": "你已经选过此课程"}]

tuike_data = [{"title": "退课密码错误", "pwd": "ma", "excepted": "密码错误"},
              {"title": "退课密码正确", "pwd": "ma15369155985", "excepted": "课程退课成功"}]

