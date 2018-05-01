# demo8:selenium 新建窗口定位，定位下拉框，关闭窗口

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time
import requests
import json
# 处理selenium中的下拉框时需导入此类
from selenium.webdriver.support.select import Select

# 如果新建了一个窗口，想新窗口页面定位元素，需要把handle转到新的页面上
def switch_handles():
    # 获得当前窗口handle
    currentwins = browser.window_handles
    # 切换到最新窗口
    browser.switch_to.window(currentwins[1])

browser = webdriver.Chrome()

browser.get("https://www.appannie.com/comparator/landing/")
browser.find_element_by_xpath("//*[@name='username']").send_keys(webdriver.common.keys.Keys.SPACE)
browser.find_element_by_xpath("//*[@name='username']").send_keys("mren-ext@appannie.com")

browser.implicitly_wait(3000)

browser.find_element_by_xpath("//*[@name='password']").send_keys(webdriver.common.keys.Keys.SPACE)

browser.find_element_by_xpath("//*[@name='password']").clear()
browser.find_element_by_xpath("//*[@name='password']").send_keys("Weiaisj1314")
browser.find_element_by_xpath("//*[@id='submit']").click()
time.sleep(5)
# 打开一个新网址在新窗口
browser.execute_script("window.open('https://www.appannie.com/admin/projecta/','_blank');")
time.sleep(5)
browser.execute_script("window.open('https://dashboard.smart-sense.org/admin/main#/alarms','_blank');")
time.sleep(30)

response = requests.get('https://dashboard.smart-sense.org/admin/get_all_alarms?&type=Smartphone&country=US'
    )
rows=json.loads(response.text) # 将字符串转化为json（字典）
# print(rows)

for r in rows['rows'][3:5]:
    app_id=r['app_id']
    print(app_id)
    script="window.open('https://dashboard.smart-sense.org/admin/app_detail?tag=daily&id=%s','_blank');" %app_id
    browser.execute_script(script)
    # 想新窗口页面定位元素，需要把handle转到新的页面上
    switch_handles()
    browser.find_element_by_link_text('Alarm Detail').click()
    time.sleep(20)
    # browser.find_element_by_xpath("//*[@class='glyphicon glyphicon-check']").click()
    browser.find_element_by_xpath("//*[@id='alarmIphoneTable']/tbody/tr[1]/td[6]/a[@class='edit ml10']").click()
    time.sleep(3)
    # 下拉框选择
    sel=browser.find_element_by_xpath("//select[@id='status']")
    Select(sel).select_by_index(3)
    time.sleep(1)
    browser.find_element_by_xpath("//*[text()='Fluctuation']").click()
    time.sleep(1)
    browser.find_element_by_xpath("//*[@id='submitOne']").click()
    # 关闭当前页面
    browser.close()
    # browser.quit() 关闭所有页面
    switch_handles()
