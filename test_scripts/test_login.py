#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
import pytest
import allure
import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from page.page_api import PageAPI
from commonlib.read_data import read_yaml


def get_param(key):
    dic = read_yaml("login_data").get(key)
    return [(dic[k]["user"], dic[k]["pwd"], dic[k]["exp"]) for k in dic]


class TestLogin(object):
    def setup_class(self):
        self.url = "http://iwebshop.itcast.com/index.php?controller=simple&action=login"
        self.login_obj = PageAPI().to_login()
        self.login_obj.open(self.url)

    def teardown_class(self):
        self.login_obj.quit()

    @allure.step(title="登录成功测试用例")
    @pytest.mark.parametrize("user,pwd,exp", get_param("login_pass"))
    def test_login_pass(self, user, pwd, exp):
        self.login_obj.login(user, pwd)
        assert exp in self.login_obj.get_loginfo()
        self.login_obj.logout()

    @allure.step(title="用户名和密码不匹配测试用例")
    @pytest.mark.parametrize("user,pwd,exp", get_param("login_error"))
    def test_login_error(self, user, pwd, exp):
        self.login_obj.login(user, pwd)
        assert exp in self.login_obj.get_not_match()

    @allure.step(title="用户名或密码输入无效测试用例")
    @pytest.mark.parametrize("user,pwd,exp", get_param("login_part"))
    def test_login_part(self, user, pwd, exp):
        self.login_obj.login(user, pwd)
        assert exp in self.login_obj.get_invalid_msg()

    def test_link_pwd(self):
        self.login_obj.click_link_pwd()
        assert '忘记密码' in self.login_obj.get_fp()
