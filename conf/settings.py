#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
import os
from selenium.webdriver.common.by import By

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(BASE_DIR)

# 用户名输入框
EL_USER = (By.XPATH, '//*[@name="login_info"]')
# 密码输入框
EL_PWD = (By.XPATH, '//*[@name="password"]')
# 登录按钮
EL_SUBMIT = (By.XPATH, '//*[@class="submit_login"]')
# 填写用户名或邮箱/填写密码
EL_INVALID_MSG = (By.XPATH, '//*[@class="invalid-msg"]')
# 用户名和密码不匹配
EL_NOT_MATCH = (By.XPATH, '//*[@class="prompt"]')
# 忘记密码链接
EL_LINK_PWD = (By.XPATH, '//*[@class="link pwd"]')
# 忘记密码标题
EL_FP = (By.XPATH, "//*[@id='fp_form']/h3")
# 登录成功后欢迎信息
EL_LOGINFO = (By.XPATH, '//*[@class="loginfo"]')
# 安全退出
EL_LOGOUT = (By.XPATH, '//*[@class="loginfo"]/a')