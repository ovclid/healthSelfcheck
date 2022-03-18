#%% 모듈 가져오기
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import time

#%% webdriver 옵션 설정 : 화면 최대사이즈, 자동제어 메시지 나타나지 않게 설정
opt = Options()
opt.add_argument('--start-maximized')
opt.add_experimental_option("excludeSwitches", ["enable-automation"])
opt.add_experimental_option('useAutomationExtension', False)

#%% webdriver를 통한 크롬 구동
driver = webdriver.Chrome("C:\chromedriver\chromedriver.exe", options=opt)
time.sleep(3)
driver.get('http://sbasu.pythonanywhere.com/tastyFoodApp/')


#%% 홈페이지 요소를 찾는 다양한 방법

ele = driver.find_element_by_link_text("Create New Profile")
ele.click()
time.sleep(3)
driver.back()

ele = driver.find_element_by_partial_link_text("New")
ele.click()
time.sleep(3)
driver.back()

ele = driver.find_element_by_css_selector("a[href='/tastyFoodApp/create']")
ele.click()
time.sleep(3)
driver.back()

ele = driver.find_element_by_xpath('//*[@id="homePageLinks"]/ul/li/a')
ele.click()
time.sleep(3)
driver.back()

ele = driver.find_element_by_xpath('/html/body/div/div/ul/li/a')   # full xpath 
ele.click()
time.sleep(3)
driver.back()
