# -*- coding: utf-8 -*-
# @Time     : 2020/2/2 13:34
# @Author   : lemon_ml
# @Email    : 8768765@qq.com
# @File     : test_04_sixin.py
# @Software : PyCharm

import pytest

from TestDatas.sixin_datas import success_data, error_data, file_data


@pytest.mark.usefixtures("sixin_setUp")
class TestSx:

    def test_01_success(self, sixin_setUp):
        sixin_setUp[1].send_xiaoxi(success_data["sixin"])
        assert success_data["sixin"] == sixin_setUp[1].get_text_sixin()

    def test_02_error(self, sixin_setUp):
        sixin_setUp[1].send_xiaoxi(error_data["sixin"])
        assert error_data["excepted"] == sixin_setUp[1].get_error_xinxi()

    def test_03_file(self, sixin_setUp):
        sixin_setUp[1].sc_fujian(file_data["filePath"])
        assert file_data["excepted"] in sixin_setUp[1].get_text_sixin()


if __name__ == '__main__':
    pytest.main()
