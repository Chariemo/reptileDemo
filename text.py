# -*- coding: utf-8 -*-

# @author: chenjianlin
# @create: 2018-03-08 14:06
import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
# print(browser.page_source)
# lis = browser.find_element_by_css_selector('ul.service-bd')
# print(lis.text)
input = browser.find_element_by_id('q')
input.send_keys('华为')
input.clear()
time.sleep(1)
input.clear()
input.send_keys('一加')
button = browser.find_element_by_css_selector('button.btn-search.tb-bg')
button.click()
browser.close()