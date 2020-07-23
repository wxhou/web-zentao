#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import allure
import pytest
from tools.times import sleep
from page_object.loginpage import LoginPage


@allure.feature("测试禅道登录功能")
class TestLogin:
    """测试登录"""

    @pytest.mark.parametrize("name,pwd", [('admin', 'Admin123'), ('test', 'test123')])
    def test_001(self, drivers, name, pwd):
        login = LoginPage(drivers)
        login.username(name)
        login.password(pwd)
        login.submit()
        sleep(3)
        res = login.alert_exists()
        if res:
            assert res == "登录失败，请检查您的用户名或密码是否填写正确。"
        elif login.login_success():
            login.quit_login()
