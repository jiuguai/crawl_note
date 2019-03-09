from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import time
driver_path = r"E:\Python\driver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path)
url = "https://v.qq.com/x/cover/hzgtnf6tbvfekfv/g0014r3khdw.html"

driver.get(url)


# more_ele = driver.find_element_by_css_selector(more_css)


def click_show_more():
    more_css = '.item_more .icon_xs.arrow_down_xs'
    more_ele = WebDriverWait(driver,5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR,more_css))
    )
    more_ele.click()
    time.sleep(0.05)
    return more_ele



pagetab_css = ".mod_episode_filter .item"
pagetab_eles = driver.find_elements_by_css_selector(pagetab_css)


item_css = ".mod_episode .item_detail_half a"
pagetab_len = len(pagetab_eles)
l = []

for i in range(pagetab_len):
    click_show_more()
    pagetab_eles = driver.find_elements_by_css_selector(pagetab_css)
    pagetab_eles[i].click()
    item_eles = driver.find_elements_by_css_selector(item_css)
    for item_ele in item_eles:
        # print(item_ele.get_attribute('title'))
        l.append(item_ele.get_attribute('title'))

print(len(l))
print(l)
time.sleep(3)
# 关闭当前页面
driver.close()

# 退出整个浏览
driver.quit()

