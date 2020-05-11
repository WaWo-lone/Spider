# -*- author:caoyue -*-
from selenium import webdriver

chrome_path = r'E:\drivers\chromedriver'
driver = webdriver.Chrome(executable_path=chrome_path)

driver.get('http://www.4399.com/')

# 点击登陆按钮
driver.find_element_by_id('login_tologin').click()

# 切换到iframe
driver.switch_to.frame('popup_login_frame')

# 填写用户名
username = driver.find_element_by_id('username')
username.clear()
username.send_keys('17779288331')

# 填写密码
driver.find_element_by_id('j-password').send_keys('123456')

# 勾选自动登陆
driver.find_element_by_id('login_autoLogin').click()

# 点击登陆
driver.find_element_by_class_name('ptlogin_btn').click()

# 切回到最外层页面
driver.switch_to.default_content()

# 点击个人信息进入个人中心
driver.find_element_by_xpath('//div[@id="func"]/a[3]').click()

