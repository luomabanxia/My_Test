# -*- coding: utf-8 -*-
# @Time     : 2020/1/30 16:59
# @Author   : lemon_ml
# @Email    : 8768765@qq.com
# @File     : handle_log.py
# @Software : PyCharm

import logging
import os

from datetime import datetime
from Common.file_path import LOG_PATH


class HandleLog:

    @classmethod
    def handle_log(cls):
        mylog = logging.getLogger("my_log")
        mylog.setLevel("DEBUG")
        # 设置日志输出格式
        formate = logging.Formatter("%(asctime)s - [%(filename)s-->line:%(lineno)d] - %(levelname)s:%(message)s")
        # 创建控制台输出渠道
        sh = logging.StreamHandler()
        # 创建文件输出渠道
        filename = os.path.join(LOG_PATH, "mylog") + "_" + \
                   datetime.strftime(datetime.now(), '%Y%m%d_%H%M%S') + ".log"
        fh = logging.FileHandler(filename=filename, encoding="utf8")
        # 设置收集等级
        sh.setLevel("INFO")
        fh.setLevel("INFO")
        # 设置输出格式
        sh.setFormatter(formate)
        fh.setFormatter(formate)
        # 添加到收集器
        mylog.addHandler(sh)
        mylog.addHandler(fh)

        return mylog


do_log = HandleLog.handle_log()