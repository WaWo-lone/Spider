# -*- author:caoyue -*-
from selenium import webdriver

chrome_path = r'E:\drivers\chromedriver'

# 创建一个options选项
options = webdriver.ChromeOptions()

# 添加参数，代理ip
options.add_argument('--proxy-server=http://117.69.185.46:4286')

driver = webdriver.Chrome(executable_path=chrome_path, chrome_options=options)

driver.get('http://httpbin.org/ip')

