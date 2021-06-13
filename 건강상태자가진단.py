from selenium import webdriver
from bs4 import BeautifulSoup as bs
import time
import os, sys
import pandas as pd
import openpyxl
import random
import re
import requests
import pyperclip

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup as bs
from selenium.webdriver.support.ui import Select


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from selenium.common.exceptions import NoSuchElementException

from selenium.common.exceptions import TimeoutException, NoSuchElementException, NoAlertPresentException,\
     UnexpectedAlertPresentException

from webdriver_manager.chrome import ChromeDriverManager


def log_in(driver):                      
    #url = 'https://blog.naver.com/bizinfo1357'
    url = 'https://hcs.eduro.go.kr/#/loginHome'

    driver.implicitly_wait(1)
    
    driver.get(url)
    driver.implicitly_wait(1)
 
    return driver

def save_html (driver, filename):
    soup_html = bs(driver.page_source, 'html.parser')

    with open(filename, "w", encoding='utf-8') as file:
        file.write(str(soup_html))


    
                           
    
if __name__ ==  "__main__" :
    
    driver = webdriver.Chrome(ChromeDriverManager().install())
    print("try to login...")
    
    driver.get('https://hcs.eduro.go.kr/#/loginHome')
    time.sleep(1)


    # 로그인 버튼을 찾고 클릭합니다
    
    btn = driver.find_element_by_id('btnConfirm2')
    btn.click()
    time.sleep(3)


    btn =  driver.find_element_by_id('schul_name_input')
    btn.click()
    time.sleep(1)

    obj1 = Select(driver.find_element_by_id("sidolabel"))
    obj1.select_by_index(8)
    time.sleep(1)

    obj1 = Select(driver.find_element_by_id("crseScCode"))
    obj1.select_by_index(2)
    btn =  driver.find_element_by_id('orgname')
    btn.send_keys("늘봄초")

    xpath = '//*[@id="softBoardListLayer"]/div[2]/div[1]/table/tbody/tr[3]/td[2]/button'
    btn =  driver.find_element_by_xpath(xpath)
    btn.click()
    time.sleep(1)


    xpath = '//*[@id="softBoardListLayer"]/div[2]/div[1]/ul/li/a/p/a'
    btn =  driver.find_element_by_xpath(xpath)
    btn.click()
    time.sleep(1)
    
    xpath = '//*[@id="softBoardListLayer"]/div[2]/div[2]/input'
    btn =  driver.find_element_by_xpath(xpath)
    btn.click()

    btn =  driver.find_element_by_id('user_name_input')
    btn.send_keys("하지훈")

    btn =  driver.find_element_by_id('birthday_input')
    btn.send_keys("111117")
    btn =  driver.find_element_by_id('btnConfirm')
    btn.click()
    time.sleep(2)
    
    xpath = '//*[@id="WriteInfoForm"]/table/tbody/tr/td/input'
    btn =  driver.find_element_by_xpath(xpath)
    btn.send_keys('8080')
    
    btn =  driver.find_element_by_id('btnConfirm')
    btn.click()
    

    
    
    """
    
    print("td, pw 입력할 곳을 찾습니다...")
    # id, pw 입력할 곳을 찾습니다.
    tag_id = driver.find_element_by_name('id')
    tag_pw = driver.find_element_by_name('pw')
    tag_id.clear()
    time.sleep(1)

    # id 입력
    tag_id.click()
    pyperclip.copy('cbmss1357')
    tag_id.send_keys(Keys.CONTROL, 'v')
    time.sleep(1)

    # pw 입력
    tag_pw.click()
    pyperclip.copy('cbmss1357!')
    tag_pw.send_keys(Keys.CONTROL, 'v')
    time.sleep(1)

    # 로그인 버튼을 클릭합니다
    login_btn = driver.find_element_by_id('log.login')
    login_btn.click()

    time.sleep(1)
    

    driver.get('https://nid.naver.com/nidlogin.login')
    driver.find_element_by_name('id').send_keys('ovclid')
    driver.find_element_by_name('pw').send_keys('*sang716901')
    driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
 
    
    driver = log_in(driver)

    soup_html = bs(driver.page_source, 'html.parser')

    subs = soup_html.findAll(class_="p_photo_d")
    
    for i in range(5):  #len(subs)
        
        sub_url = subs[i].find("a")["href"]
        driver.get(sub_url)

        driver.find_element_by_class_name('_spi_blog').click()  # spi_btn_blog
        time.sleep(0.5)

        handles = driver.window_handles
        driver.switch_to.window(handles[1])
        
        driver.find_element_by_id('_submit').click()  # spi_btn_blog
        time.sleep(0.5)
        driver.switch_to.window(handles[0])
         
        #driver.find_element_by_class_name('pop_btn')
        
    save_html(driver, f"blog.html")
        

    try:
        handles = driver.window_handles
        driver.switch_to.window(handles[0])

        search = '//*[@id="contents"]/div[2]/section/div[2]/div[3]/span/a/img'
        driver.find_element_by_xpath(search).click()
        driver.implicitly_wait(5)

        handles = driver.window_handles
        bizInfoListPopupHandleIndex= len(handles) - 1 # PopUP 창이 뜨지 않을 경우 1로 변경해야
        driver.switch_to.window(handles[bizInfoListPopupHandleIndex])
        
        result_cominfo = '//*[@id="mySheet"]/tbody/tr[3]/td/div/div[1]/table/tbody/tr[2]/td[5]'
        v
        driver.find_element_by_xpath(result_cominfo).click()            
        


        #first_filename = input("!!!! 1차 파업 저장 파일 이름: ")
        #save_html(driver, f"{first_filename}.html")
    
        soup_html = bs(driver.page_source, 'html.parser')

        save_html(driver, f"blog.html")
        
        
        handles = driver.window_handles
        driver.switch_to.window(handles[bizInfoListPopupHandleIndex]) 
                                                   
        src = driver.find_element_by_name("hidden_frame").get_attribute("src")

        
        driver.get(src)         
        soup_html = bs(driver.page_source, 'html.parser')

    except TimeoutException:
        print("Timeout")
        continue
    
    except NoSuchElementException:
        print("No duplicate order detected")
        continue
    
    except NoAlertPresentException:
        print("No Alert Present")
        continue
    
    except AttributeError:
        print("AttributeError Present")
        continue
     
    except UnexpectedAlertPresentException:
        alert = driver.switch_to_alert()
        alert.accept()
        print("Unexpected alert, yo!") 
        continue
    """
