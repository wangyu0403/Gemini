#!/usr/bin/python
# _*_coding:utf-8 _*_
"""
@File    : Login_in.py
@Time    : 2021/12/7 4:44 下午
@Author  : wangyu   
@Email   : wangyu03@smartdot.com
@Software: PyCharm
"""

from selenium import

# driver = webdriver.chrome()
# driver.get("http://weoffice.smartdot.com:28080/")


driver =
driver.get("http://www.baidu.com")

driver.find_element_by_id("kw").send_keys("Selenium2")
driver.find_element_by_id("su").click()

driver.quit()
