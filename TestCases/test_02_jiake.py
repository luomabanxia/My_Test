# -*- coding: utf-8 -*-
# @Time     : 2020/2/1 14:24
# @Author   : lemon_ml
# @Email    : 8768765@qq.com
# @File     : test_02_jiake.py
# @Software : PyCharm

import pytest

from TestDatas.jiake_datas import jiake_data, tuike_data


@pytest.mark.usefixtures("jiake_setUp")
class TestJiake:

    @pytest.mark.parametrize("cases", jiake_data)
    def test_01_jiake(self, cases, jiake_setUp):
        jiake_setUp[1].jiake(cases["number"])
        assert cases["excepted"] == jiake_setUp[1].get_jiake_text()

    @pytest.mark.parametrize("case", tuike_data)
    def test_02_tuike(self, case, jiake_setUp):
        jiake_setUp[1].out_ke(case["pwd"])
        assert case["excepted"] == jiake_setUp[1].get_jiake_text()


if __name__ == '__main__':
    pytest.main()