#demo4:
#some knowledge about selenium

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time

browser = webdriver.Chrome()

# selenium键盘操作：
# from selenium.webdriver.common.keys import Keys ---- send_keys(Keys.SPACE)
# 亦可不import，直接webdriver.common.keys.Keys.SPACE
# 全选：send_keys(Keys.CONTROL,'a'),复制粘贴等类似

browser.get("https://www.appannie.com/comparator/landing/")
browser.find_element_by_xpath("//*[@name='username']").send_keys(webdriver.common.keys.Keys.SPACE)
browser.find_element_by_xpath("//*[@name='username']").send_keys("mren-ext@appannie.com")

# time.sleep(秒)强制停止休眠n秒
# implicitly_wait(秒)隐式等待n秒，设置一段时间，在这个时间段内如果一找到该元素，就执行下一步
# 隐形等待是设置了一个最长等待时间，如果在规定时间内网页加载完成，则执行下一步，否则一直等到时间截止，
# 然后执行下一步。注意这里有一个弊端，那就是程序会一直等待整个页面加载完成，
# 也就是一般情况下你看到浏览器标签栏那个小圈不再转，才会执行下一步，
# 但有时候页面想要的元素早就在加载完成了，但是因为个别js之类的东西特别慢，我仍得等到页面全部完成才能执行下一步
# !!!!!（隐性等待对整个driver的周期都起作用，所以只要设置一次即可）
# 页面想要的元素在加载完前出现了，此时可以用WebDriverWait(driver, 超时时长, 调用频率, 忽略异常).until(可执行方法, 超时时返回的信息)
browser.implicitly_wait(3000)
browser.find_element_by_xpath("//*[@name='password']").send_keys(webdriver.common.keys.Keys.SPACE)

browser.find_element_by_xpath("//*[@name='password']").clear()
browser.find_element_by_xpath("//*[@name='password']").send_keys("Weiaisj1314")
browser.find_element_by_xpath("//*[@id='submit']").click()

# 打开一个新网址在新窗口
browser.execute_script("window.open('https://www.appannie.com/admin/projecta/','_blank');")
time.sleep(10)
browser.execute_script("window.open('https://dashboard.smart-sense.org/admin/app_detail?id=915056765','_blank');")
