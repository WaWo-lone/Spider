# -*- author:caoyue -*-
import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver_path = r'E:\drivers\chromedriver'
driver = webdriver.Chrome(executable_path=driver_path)

'''操作输入框input
driver.get('https://www.baidu.com/')
input = driver.find_element_by_id('kw')
input.send_keys('python')  # 填充数据
time.sleep(3)
input.clear()  # 清除数据
'''

'''操作复选框checkbox
driver.get('http://cn.hoyoyo.com/member~login.html')
checkbox = driver.find_element_by_name('remember_login')
checkbox.click()
'''

'''操作按钮button
driver.get('https://www.baidu.com/')
input = driver.find_element_by_id('kw')
input.send_keys('python')
btn = driver.find_element_by_id('su')
btn.click()
'''

'''操作选择栏select
from selenium.webdriver.support.ui import Select

driver.get('http://tieba.baidu.com/f/search/adv?red_tag=y2157203949')
sel = driver.find_element_by_name('sm')
selectTag = Select(sel)
# 根据索引选中
# selectTag.select_by_index(1)

# 根据值选中
# selectTag.select_by_value('2')

# 根据可视化文本选中
selectTag.select_by_visible_text('按相关性排序')
'''

'''行为链
'''
driver.get('https://www.baidu.com/')
input = driver.find_element_by_id('kw')
btn = driver.find_element_by_id('su')
actions = ActionChains(driver)
actions.move_to_element(input)  # 移动到input元素
actions.send_keys_to_element(input, 'python')  # 给input元素填充信息
actions.move_to_element(btn)  # 移动到btn元素
actions.click(btn)  # 点击btn元素
actions.perform()  # 执行所有行为


