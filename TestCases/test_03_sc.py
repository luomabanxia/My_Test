# -*- coding: utf-8 -*-
# @Time     : 2020/2/1 17:37
# @Author   : lemon_ml
# @Email    : 8768765@qq.com
# @File     : test_03_sc.py
# @Software : PyCharm

import pytest

from time import sleep
from TestDatas.scfile_datas import filePath, liuyan_data


@pytest.mark.usefixtures("sc_setUp")
class TestScFile:

    def test_01_sc_file(self, sc_setUp):
        """
        1、点击作业按钮
        2、点击已提交
        3、点击更新提交
        4、上传文件
        5、点击更新提交
        6、断言
        :param sc_setUp:
        :return:
        """
        sc_setUp[0].click_ytj()
        sc_setUp[1].update_tijiao()
        sleep(2)
        sc_setUp[1].file_upload(filePath)
        assert "软件测试知识梳理.png" == sc_setUp[1].get_cg_text()

    def test_02_liuyan(self, sc_setUp):
        """
        3、留言
        4、断言
        :param sc_setUp:
        :return:
        """
        sc_setUp[0].click_ytj()
        sc_setUp[1].liuyan(liuyan_data["liuyan"])
        assert liuyan_data["liuyan"] == sc_setUp[1].liuyan_text()


if __name__ == '__main__':
    pytest.main()

