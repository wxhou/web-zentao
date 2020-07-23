#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from page.webpage import WebPage
from common.readelement import Element

login = Element('login')


class LoginPage(WebPage):
    """登录类"""

    def username(self, name):
        """用户名"""
        self.input_text(login['账号'], name)

    def password(self, pwd):
        """密码"""
        self.input_text(login['密码'], pwd)

    def submit(self):
        """登录"""
        self.is_click(login['登录'])

    def quit_login(self):
        """退出登录"""
        self.is_click(login['右上角名称'])
        self.is_click(login['退出登录'])

    def login_success(self):
        """验证登录"""
        return self.is_exists(login['我的地盘'])


