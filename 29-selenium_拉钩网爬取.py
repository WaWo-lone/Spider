# -*- author:caoyue -*-
import json
import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

chrome_path = r'E:\drivers\chromedriver'
driver = webdriver.Chrome(executable_path=chrome_path)

driver.get('https://www.lagou.com/')

# 添加cookie模拟登录
cookies = 'user_trace_token=20200510114121-04635af7-56f9-4120-8982-1667d63fc975; LGUID=20200510114121-3db532ff-56ed-4d32-9b50-88fc6ab0a157; _ga=GA1.2.80652907.1589081959; _gid=GA1.2.1367849157.1589081959; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=30; privacyPolicyPopup=false; LG_HAS_LOGIN=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22171fcae069710d-0c4daa7cd5d713-d373666-1327104-171fcae069926b%22%2C%22%24device_id%22%3A%22171fcae069710d-0c4daa7cd5d713-d373666-1327104-171fcae069926b%22%7D; index_location_city=%E5%85%A8%E5%9B%BD; gate_login_token=e6cf9af026924debf53738845f30ed1c86ed6f896e1adcd0f5f905400813b012; LG_LOGIN_USER_ID=2d8a346ce8d83205c5bcf71578c0aca48e7bba1c6930698a00e68eed5f74d8cf; _putrc=D5EE438BA884DAD6123F89F2B170EADC; JSESSIONID=ABAAABAABEIABCI43C511F8C30260645AB54C73A8032384; login=true; unick=%E6%9B%B9%E8%B6%8A; WEBTJ-ID=20200510225030-171ff10eab4351-020f01cd0b56e5-d373666-1327104-171ff10eab5328; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1589109585,1589109645,1589122223,1589172358; _gat=1; LGSID=20200511124802-156a07f4-830a-4939-9313-1474e6eb93dc; PRE_UTM=m_cf_cpt_baidu_pcbt; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Fother.php%3Fsc.0f0000azYzyN6C4BTuUnK6QuotEPQI%5FNbmIkOjIdc9061o6dLi1vBsiCKLj5vUZ-IDsgWzGiy07mtAgUJU7%5FG3qDWxtKEwZsq4IeQXzDjLo6c0S8UYwoFjFw2aLSve4A-ALztiap0nFzBjOhtC5rJ8hrYD5R8Xtu9ROOVIfQLpEkW4tEZjcwGOrqdpwgWY5cVvPky3gidfyRmptVOgaK%5FbuKPRiu.7Y%5FNR2Ar5Od663rj6tJQrGvKD77h24SU5WudF6ksswGuh9J4qt7jHzk8sHfGmYt%5FrE-9kYryqM764TTPqKi%5FnYQZHuukL0.TLFWgv-b5HDkrfK1ThPGujYknHb0THY0IAYqUA7MULR0IgP-T-qYXgK-5H00mywxIZ-suHY10ZIEThfqUA7MULR0ThPv5HD0IgF%5Fgv-b5HDdnHT3P1mYrjR0UgNxpyfqnHD3njRznH60UNqGujYknjmknHTYn6KVIZK%5Fgv-b5HDkPHnY0ZKvgv-b5H00mLFW5HD4nHD4%26ck%3D3784.3.89.224.148.317.187.495%26dt%3D1589172480%26wd%3D%26tpl%3Dtpl%5F11534%5F22213%5F17382%26l%3D1517876485%26us%3DlinkName%253D%2525E6%2525A0%252587%2525E5%252587%252586%2525E5%2525A4%2525B4%2525E9%252583%2525A8-%2525E4%2525B8%2525BB%2525E6%2525A0%252587%2525E9%2525A2%252598%2526linkText%253D%2525E3%252580%252590%2525E6%25258B%252589%2525E5%25258B%2525BE%2525E6%25258B%25259B%2525E8%252581%252598%2525E3%252580%252591%2525E5%2525AE%252598%2525E6%252596%2525B9%2525E7%2525BD%252591%2525E7%2525AB%252599%252520-%252520%2525E4%2525BA%252592%2525E8%252581%252594%2525E7%2525BD%252591%2525E9%2525AB%252598%2525E8%252596%2525AA%2525E5%2525A5%2525BD%2525E5%2525B7%2525A5%2525E4%2525BD%25259C%2525EF%2525BC%25258C%2525E4%2525B8%25258A%2525E6%25258B%252589%2525E5%25258B%2525BE%21%2526linkType%253D; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Flanding-page%2Fpc%2Fsearch.html%3Futm%5Fsource%3Dm%5Fcf%5Fcpt%5Fbaidu%5Fpcbt; X_HTTP_TOKEN=2f14169fd0b8ac838842719851faba842cacdcfdc4; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1589172364; LGRID=20200511124808-1ccc5e1d-fdf7-48d8-a905-b39a89e89b91'
cookie_list = cookies.split(';')

for cookie in cookie_list:
    data = cookie.split('=')
    driver.add_cookie({'name': data[0].strip(), 'value': data[1].strip()})


driver.get('https://www.lagou.com/jobs/list_python/p-city_0?&cl=false&fromSearch=true&labelWords=&suginput=')

# 关闭弹窗
driver.find_element_by_class_name('body-btn').click()

# print(len(links))

data = []
while True:
    try:
        # 获取所有职位的链接
        links = driver.find_elements_by_xpath('//div[@id="s_position_list"]//li//div[@class="p_top"]/a')
        for link in links:
            href = link.get_attribute('href')

            # 打开一个新的页面

            driver.execute_script("window.open('" + href + "')")
            # 切换到新页面
            driver.switch_to.window(driver.window_handles[1])


            # 获取数据
            company = driver.find_element_by_xpath('//h4[@class="company"]').text
            position = driver.find_element_by_xpath('//h1[@class="name"]').text
            salary = driver.find_element_by_xpath('//span[@class="salary"]').text
            requirement_list = driver.find_elements_by_xpath('//dd[@class="job_request"]/h3/span')

            requirements = []

            for requirement in requirement_list:
                requirements.append(requirement.text)
            data.append({
                'company': company,
                'position': position,
                'salary': salary,
                'requirements': requirements
            })
            # 关闭新的页面
            driver.close()

            # 切换回第一页
            driver.switch_to.window(driver.window_handles[0])

            # 等待按钮显示出来
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//span[@action="next"]'))
            )

            # 下一页
            next_page = driver.find_element_by_xpath('//span[@action="next"]')

            if next_page.get_attribute('class') == 'pager_next pager_next_disabled':
                break

            next_page.click()
            time.sleep(2)
    except:
        continue


for d in data:
    # ensure_ascii=False 不会将中文转为16进制格式
    da = json.dumps(d, ensure_ascii=False) + '\n'
    with open('./lagou.txt', 'a') as f:
        f.write(da)




