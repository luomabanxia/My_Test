# -*- coding: utf-8 -*-
# @Time     : 2020/1/30 16:54
# @Author   : lemon_ml
# @Email    : 8768765@qq.com
# @File     : file_path.py
# @Software : PyCharm

import os


# 当前文件所在目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 日志所在目录
LOG_PATH = os.path.join(BASE_DIR, "OutPuts/logs")

# 截图所在目录
SHOT_PATH = os.path.join(BASE_DIR, "OutPuts/shot")

# 测报所在目录
REPORT_PATH = os.path.join(BASE_DIR, "OutPuts/reports")