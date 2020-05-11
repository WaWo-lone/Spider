# -*- author:caoyue -*-
from selenium import webdriver
import time

driver_path = r'E:\drivers\chromedriver'

driver = webdriver.Chrome(executable_path=driver_path)

driver.get('https://www.baidu.com/')

# 获取页面源代码
# print(driver.page_source)

# time.sleep(2)
# 关闭当前页面
# driver.close()

# 关闭浏览器
# driver.quit()

# 使用element定位的元素都是第一个，使用elements定位的元素则是全部，返回一个列表
# 根据id定位元素
element = driver.find_element_by_id('su')
# 获取元素属性
value = element.get_attribute('value')
print(value)

# 根据class_name(类名)定位元素
element = driver.find_element_by_class_name('bri')
# 获取元素内容
text = element.text
print(text)

# 根据tag_name(标签名)定位元素
element = driver.find_element_by_tag_name('img')
print(element.get_attribute('class'))

# 根据xpath定位元素,只能定位到元素
element = driver.find_element_by_xpath('//div[@id="u1"]/a[3]')
print(element.text)

# 根据selector定位元素
element = driver.find_element_by_css_selector('#su')
print(element.get_attribute('value'))

# 截图
driver.save_screenshot('./images/bd.png')
driver.close()






