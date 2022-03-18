from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import time

###############################################################
########## 페이지(1) : webdriver 구동 및 홈페이지 접속 #########
###############################################################

student = {'school' : '늘봄초', 'name' : '', 'sinNum' : '', 'secNum' : '8080'}

# webdriver 옵션 설정 : 화면 최대사이즈, 자동제어 메시지 나타나지 않게 설정
opt = Options()
opt.add_argument('--start-maximized')
opt.add_experimental_option("excludeSwitches", ["enable-automation"])
opt.add_experimental_option('useAutomationExtension', False)

# webdriver를 통한 크롬 구동
driver = webdriver.Chrome("C:\chromedriver\chromedriver.exe", options=opt)
driver.get('https://hcs.eduro.go.kr/#/loginHome')
time.sleep(3)

# '자가진단참여하기' 자동 선택(기본으로 초중고 선택되어 있음)
ele = driver.find_element_by_id('btnConfirm2')
ele.click()
time.sleep(3)

###############################################################
####### 페이지(2) : 학교 정보 입력 ############################ 
###############################################################

# 학교 검색
ele =  driver.find_element_by_id('schul_name_input')  
ele.click()
time.sleep(2)

# 시/도 선택 :: 'Select'를 활용한 드롭다운 메뉴 선택 
ele = Select(driver.find_element_by_id("sidolabel"))   
ele.select_by_index(8)

# 학교명 검색 :: 'Select'를 활용한 드롭다운 메뉴 선택 
ele = Select(driver.find_element_by_id("crseScCode"))
ele.select_by_index(2)

# 학교명 입력
ele = driver.find_element_by_id('orgname')
ele.send_keys(student["school"])

ele = driver.find_element_by_class_name("searchBtn")
ele.click()
time.sleep(1)

# 학교명 선택(처음에는 나타나지 않음)
ele = driver.find_element_by_tag_name("em")
ele.click()
time.sleep(1)

# 학교선택 정보 최종 제출
ele = driver.find_element_by_class_name("layerFullBtn")
ele.click()
time.sleep(2)


###############################################################
############# 페이지(2) : 학생 정보 입력 ######################
###############################################################

ele = driver.find_element_by_id('user_name_input')
ele.send_keys(student["name"])

ele = driver.find_element_by_id('birthday_input')
ele.send_keys(student["sinNum"])

ele = driver.find_element_by_id('btnConfirm')
ele.click()
time.sleep(1)


###############################################################
############## 페이지(2) : 비밀번호 자동 클릭 설정 #############
###############################################################

# 비밀번호 입력 버튼 클릭
ele = driver.find_element_by_class_name("keyboard-img")
ele.click()
time.sleep(2)

# a 태그들 중 'aria-label' 속성값이 비밀번호랑 일치하는 것을 찾아 클릭
"""
numPadEles = driver.find_elements_by_tag_name("a")
for i in range(len(student["secNum"])):
    for j in range(len(numPadEles)):
        if student["secNum"][i] == numPadEles[j].get_attribute("aria-label"):
            numPadEles[j].click()            
            time.sleep(0.5)
"""

for i in range(len(student["secNum"])):
    secNum = student['secNum'][i]
    numPadEle = driver.find_element_by_css_selector(f"a[aria-label='{secNum}']")
    numPadEle.click()
    time.sleep(0.5)
                      
ele =  driver.find_element_by_id('btnConfirm')
ele.click()
time.sleep(2)

# 설문조사 버튼 클릭
ele = driver.find_element_by_class_name("survey-button.active")  # class name space => . 
ele.click()
time.sleep(2)


###############################################################
############### 페이지(3): 설문조사 기본 응답 후 제출 ##########
###############################################################

self_test_id = ['survey_q1a1', 'survey_q2a3', 'survey_q3a1', 'btnConfirm']

for i in range(len(self_test_id)):
    if i == len(self_test_id) -1 :
        last = input("마지막 단계 진행 할까요? (y/n)")
        if last == 'n' or last == 'N':
            break

    ele = driver.find_element_by_id(self_test_id[i])
    ele.click()
    time.sleep(1)

driver.close()
