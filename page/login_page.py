#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
import allure
from commonlib.base import Base
from conf import settings


class Login(Base):
    def __init__(self):
        super().__init__()

    def login(self, user, pwd):
        allure.attach(f"输入用户名{user}")
        self.send_data(settings.EL_USER, user)
        allure.attach(f"输入密码{pwd}")
        self.send_data(settings.EL_PWD, pwd)
        allure.attach("点击登录")
        self.click_element(settings.EL_SUBMIT)

    def get_loginfo(self):
        return self.find_element(settings.EL_LOGINFO).text

    def get_invalid_msg(self):
        return self.find_element(settings.EL_INVALID_MSG).text

    def get_not_match(self):
        return self.find_element(settings.EL_NOT_MATCH).text

    def click_link_pwd(self):
        allure.attach("点击忘记密码链接")
        self.click_element(settings.EL_LINK_PWD)

    def get_fp(self):
        return self.find_element(settings.EL_FP).text

    def logout(self):
        allure.attach("点击安全退出")
        self.click_element(settings.EL_LOGOUT)
