# -*- author:caoyue -*-
from selenium import webdriver
chrome_path = r'E:\drivers\chromedriver'
driver = webdriver.Chrome(executable_path=chrome_path)

driver.get('https://www.baidu.com/')

# 用js语法打开一个新的页面
driver.execute_script('window.open("https://www.chinaz.com/")')

# 当前页面路径
# url = driver.current_url
# print(url)  # https://www.baidu.com/

# 切换页面
driver.switch_to.window(driver.window_handles[1])

print(driver.current_url)  # https://www.chinaz.com/