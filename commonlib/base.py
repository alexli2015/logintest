#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver


class Base(object):
    def __init__(self):
        self.driver = webdriver.Chrome()

    def open(self, url):
        self.driver.get(url)

    def quit(self):
        self.driver.quit()

    def find_element(self, loc, timeout=5, interval=0.5):
        """
        定位单个元素
        :param loc: 元组形式，比如（By.ID，value）
        :param timeout: 超时等待时间
        :param interval: 查找元素时间间隔
        :return: 查找的元素
        """
        return WebDriverWait(self.driver, timeout, interval).until(lambda x: x.find_element(*loc))
    
    def find_elements(self, loc, timeout=5, interval=0.5):
        """
        定位一组元素
        :param loc: 元组形式，比如（By.ID，value）
        :param timeout: 超时等待时间
        :param interval: 查找元素时间间隔
        :return: 查找的元素列表
        """
        return WebDriverWait(self.driver, timeout, interval).until(lambda x: x.find_elements(*loc))
    
    def click_element(self, loc):
        """
        点击元素
        :param loc: 元组形式，比如(By.ID，value)/(By.CLASS_NAME，value)/(By.XPATH，value)
        :return: None
        """
        self.find_element(loc).click()

    def send_data(self, loc, data):
        """
        先清空输入框，然后往输入框输入内容
        :param loc: 元组形式，比如（By.ID，value）
        :param data: 输入的内容
        :return: None
        """
        elem = self.find_element(loc)
        elem.clear()
        elem.send_keys(data)

    def is_disp(self, loc):
        """
        判断元素是否出现
        :param loc: 元组形式，比如（By.ID，value）
        :return:
        """
        try:
            self.find_element(loc, timeout=10)
            return True
        except Exception as e:
            print(e)
            return False
