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

# 크롬 옵션 설정 - 셀레니움 접근 제한 : 보안접근 해제 /# 자동화 티 안 나게
options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")  
options.add_argument("start-maximized")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

# 브라우저 실행 
browser = webdriver.Chrome(options=options)
browser.maximize_window()   # 창 최대화

soup = BeautifulSoup(browser.page_source,"lxml")

url = "https://nol.yanolja.com/"
browser.get(url)
time.sleep(2)

# 1. 호텔/리조트 클릭
elem = browser.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div/div[2]/button")
elem.click()
time.sleep(1)

elem = browser.find_element(By.XPATH,"/html/body/div[9]/div/div/aside/div/div[1]/div[2]/div[1]/button[1]")
elem.click()


# 2. 지역선택 > 제주> 서귀포/모슬포 입력 enter
# 지역 선택
elem = browser.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div/div[1]/div/div[1]/button')
elem.click()

# 제주 선택
elem = browser.find_element(By.XPATH,'//*[@id="_MODAL_DIM_"]/div/section/div[2]/div[1]/button[3]')
elem.click()

# 서귀포/모슬포 선택
elem = browser.find_element(By.XPATH,'//*[@id="_MODAL_DIM_"]/div/section/div[2]/div[1]/button[3]')
elem.click()


# 3. 날짜 6/7-6/8 적용 후 확인 버튼 클릭
elem = browser.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/header/div[2]/div/button[1]')
elem.click()
time.sleep(1)
# 가는날
elem = browser.find_element(By.XPATH,'//*[@id="day-picker-2025-06"]/div[2]/div[1]/div[7]/button/span')
elem.click()
time.sleep(1)
# 오는날
elem = browser.find_element(By.XPATH,'//*[@id="day-picker-2025-06"]/div[2]/div[2]/div[1]/button/span')
elem.click()
time.sleep(1)
# 적용하기
elem = browser.find_element(By.XPATH,'//*[@id="pc-dialog-sheet"]/div/div/div[3]/button')
elem.click()
time.sleep(1)

### 스크롤 내리기
# 현재 사이트 높이를 가져오는 자바스크립트
prev_height = browser.execute_script("return document.body.scrollHeight")

# 반복 실행
while True:
    # 현재 브라우저에서 0에서 현재 높이까지 스크롤 내리기
    # 자바스크립트 실행
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(2)
    # 변동된 현재 문서 높이을 가져오기
    curr_height = browser.execute_script("return document.body.scrollHeight")
    # 스크롤 높이가 변동이 없을시
    if curr_height == prev_height: break 
    prev_height = curr_height # 현재 높이를 다시 입력해서 스크롤 내리기 재실행

print("스크롤 내리기 종료")

# 5. 호텔/ 호텔이름/ 평점(없으면 없음으로)/ 후기개수/ 가격 가져오기
datas = soup.find("div",{"class":"mb-[calc(76px+env(safe-area-inset-bottom))]"})
print(datas)



input("엔터시 종료")
