#!/usr/bin/python
# _*_coding:utf-8 _*_
"""
@File    : Login_in.py
@Time    : 2021/12/7 4:44 下午
@Author  : wangyu
@Email   : wangyu03@smartdot.com
@Software: PyCharm
"""
import time
from selenium import webdriver

driver = webdriver.Chrome()
# driver.get("http://www.baidu.com")
driver.get("http://weoffice.smartdot.com:28080/")
driver.find_element_by_id("horizontal_login_userName").send_keys("yujie")
driver.find_element_by_id("horizontal_login_password").send_keys("123456&")
# //*[@id="sd-body"]/div/div[2]/div[1]/form/div[3]/div/div/span/button
driver.find_element_by_xpath('//*[@id="sd-body"]/div/div[2]/div[1]/form/div[3]/div/div/span/button').submit()
time.sleep(1)


print(driver.find_element_by_css_selector("html > body > section > header > div > ul > li.ant-menu-item.ant-menu-item-selected"))
time.sleep(3)
# driver.find_element_by_css_selector("#sd-body > section > header > div.right_sd-header_common > ul > li.ant-menu-item.ant-menu-item-selected").click()
# driver.find_element_by_css_selector("html > body > section > header > div > ul > li ").click()
# driver.find_elements_by_xpath('//*[@id="sd-body"]/section/header/div[2]/ul/li[4]').click()

# full Xpath
# driver.find_element_by_xpath('/html/body/section/header/div[2]/ul/li[4]').submit()
time.sleep(1)
# driver.find_element_by_xpath('//*[@id="sd-body"]/section/section/aside/div/div/ul/li[1]')
# time.sleep(1)
# driver.find_element_by_xpath('//*[@id="0"]/div[2]/div/span')



driver.quit()