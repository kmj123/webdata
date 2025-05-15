import pyautogui

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import csv
import time
import random
import pyautogui        # 마우스 제어

# 크롬 옵션 설정 - 셀레니움 접근 제한 : 보안접근 해제
options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")  # 자동화 티 안 나게
options.add_argument("start-maximized")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

## 메일관련 import
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

## 날짜관련 import
from datetime import datetime

# 브라우저 실행

browser = webdriver.Chrome(options=options)
browser.maximize_window() # 창 최대화

### 1. 네이버 접속
url = "https://flight.naver.com/"
browser.get(url)
time.sleep(3)
# 팝업
elem = browser.find_element(By.XPATH,'//*[@id="layer"]/button[2]').click()
time.sleep(2)
# 출발지
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[1]/button[1]').click()
time.sleep(2)
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[8]/div[2]/div/div/ul[1]/li[3]/button').click()
time.sleep(2)
# 도착지
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[1]/button[2]').click()
time.sleep(2)
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[8]/div[2]/div[2]/div[2]/ul[1]/li[1]/button').click()
time.sleep(2)
# 날짜
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[8]/div[2]/div[1]/div[2]/div/div/div[2]/table/tbody/tr[5]/td[7]/button').click()
time.sleep(1)
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[8]/div[2]/div[1]/div[2]/div/div/div[3]/table/tbody/tr[1]/td[1]/button').click()
time.sleep(2)
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[9]/div[2]/div[1]/div[2]/div/div/div[3]/table/tbody/tr[1]/td[1]/button/b').click()
time.sleep(2)
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/button/span').click()



# #### 네이버 항공권
# 김포, 제주 5/31 6/1 ->
# 금액 90000원 이상 제외
# 김포출발시간 17:00 이상 제외

soup = BeautifulSoup(browser.page_source,"lxml")

data = soup.find("div",{"class":"domestic_results__gp5WB"})
rows = data.find_all("div",{"class":"domestic_inner__8geIy"})

rows_list = []
for row in rows:   
    # 가격
    price = row.find("i",{"class":"domestic_num__ShOub"}).get_text().strip().replace(",","")
    price = int(price)
    

    # 출발, 도착 시간
    schedule = row.find_all("b",{"class":"route_time__xWu7a"})
    ETD = schedule[0].get_text().strip()
    ETA = schedule[1].get_text().strip()
    
    # # 김포 출발시간 17:00 이상 제외
    # ## 출발시간 "17:00" > "06:15"
    # start_Time = schedule[0].strptime(2025,5,31,17,00,00)
    # endTime = schedule.strptime(2025,5,31,17,00,00)
    # if start_Time <= endTime : continue


    # 기준시간
    standard_time = datetime(2025,5,31,17,00,00)

    # 검색된 시간 - "06:15"
    ETD = "06:15"
    d_time = ETD.split(":")
    search_time = datetime(2025,5,31,int(d_time[0]),int(d_time[1]),00)

    # 금액 130000원 보다 크거나, 시간이 17:00보다 크면 제외대상
    # 기준시간보다 검색된 시간이 더 크면 제외
    if price > 140000 or (standard_time<search_time) : continue

    # 항공사
    airline = row.find("b",{"class":"airline_name__0Tw5w"}).get_text().strip()
    print(airline)
    
    
    # 출발, 도착 시간
    print("ETD: ",ETD)
    print("ETA: ",ETA)
    # 가격
    print(price)

    
    print("-"*30)
    
input("엔터시 종료")

