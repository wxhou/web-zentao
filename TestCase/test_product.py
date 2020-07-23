#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import pytest
import allure
from random import randint
from tools.times import sleep
from page_object.loginpage import LoginPage
from page_object.productpage import ProductPage


@allure.feature("测试禅道产品模块")
class TestProduct:

    @pytest.fixture(scope='class', autouse=True)
    def is_login(self, request, drivers):
        login = LoginPage(drivers)
        login.username('admin')
        login.password('Admin123')
        login.submit()
        sleep(3)

        def logout():
            login.quit_login()

        request.addfinalizer(logout)

    @allure.story("测试在禅道中添加一个产品")
    def test_001(self, drivers):
        """搜索"""
        product = ProductPage(drivers)
        product.click_product()
        product.add_product()
        name, code = randint(100, 999), randint(100, 999)
        product.add_product_content(name, code)
        product.save_product()
        sleep(3)
        product.click_product()
        assert str(name) in product.product_list()


if __name__ == '__main__':
    pytest.main(['TestCase/test_product.py'])
