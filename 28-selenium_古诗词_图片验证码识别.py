# -*- author:caoyue -*-
from selenium import webdriver
import time

from ocr import getcode

chrome_path = r'E:\drivers\chromedriver'
driver = webdriver.Chrome(executable_path=chrome_path)

driver.get('https://so.gushiwen.org/user/login.aspx?from=')

# 填写用户名
driver.find_element_by_id('email').send_keys('702100479@qq.com')
time.sleep(1)

# 填写密码
driver.find_element_by_id('pwd').send_keys('123456')
time.sleep(1)

# 图片验证码截图
driver.find_element_by_id('imgCode').screenshot('./code.jpg')
time.sleep(1)

# 根据接口识别并获取验证码
code = getcode()

# 填写验证码
driver.find_element_by_id('code').send_keys(code)
time.sleep(1)

# 点击登录
driver.find_element_by_id('denglu').click()
