#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from page.webpage import WebPage, sleep
from common.readelement import Element

product = Element('product')


class ProductPage(WebPage):
    """产品类"""

    def click_product(self):
        """点击产品"""
        self.is_click(product['产品按钮'])

    def add_product(self):
        """添加产品"""
        self.is_click(product['添加产品'])

    def add_product_content(self, name, code):
        """添加产品内容"""
        self.input_text(product['产品名称'], name)
        self.input_text(product['产品代号'], code)

    def save_product(self):
        """保存产品"""
        self.focus()
        self.is_click(product['保存产品'])

    def product_list(self):
        """产品列表"""
        return [i.get_attribute('title') for i in self.find_elements(product['产品列表'])]


if __name__ == '__main__':
    a = product['产品列表'][1] + "[1]"
    print(a)
