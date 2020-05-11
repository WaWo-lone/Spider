# -*- author:caoyue -*-
import os

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

chrome_path = r'E:\drivers\chromedriver'
driver = webdriver.Chrome(executable_path=chrome_path)

driver.get('https://movie.douban.com/typerank?type_name=%E5%89%A7%E6%83%85&type=11&interval_id=100:90&action=')

# 隐式等待
# driver.implicitly_wait(10)
# print(driver.find_element_by_class_name('movie-content'))

# 显示等待
element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'movie-content'))
)

con = driver.page_source

os.chdir(r'C:\Users\Administrator\Desktop\spider\htmls')
with open('douban_movie.html', 'w', encoding='utf-8') as f:
    f.write(con)