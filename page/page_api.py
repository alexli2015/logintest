#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
from page.login_page import Login


class PageAPI(object):
    def to_login(self):
        return Login()
