import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import csv
import time
import random

# 크롬옵션설정 - 셀레니움 접근 제한 : 보안접근 해제
options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")  # 자동화 티 안 나게
options.add_argument("start-maximized")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

# 브라우저 실행
browser = webdriver.Chrome(options=options)

#### 네이버 자동 로그인 메일 쓰기
url = "https://www.naver.com/"
browser.get(url)
time.sleep(2)   # 페이지 로딩 대기

# 네이버 메인 페이지
elem = browser.find_element(By.CLASS_NAME,"MyView-module__link_login___HpHMW")
elem.click()

# 네이버 로그인페이지 이동
time.sleep(random.uniform(2,4))
elem = browser.find_element(By.ID,"id")
## 자바스크립트 사용, 아이디/패스워드 입력
input_js = 'document.getElementById("id").value= "kkk990108";\
            document.getElementById("pw").value="Navkmj324675!@";'
time.sleep(random.uniform(2,4))
browser.execute_script(input_js)    # 자바스크립트 코드 실행
time.sleep(random.uniform(2,4))


# # 아이디 입력
# elem.send_keys("kkk990108")
# time.sleep(random.uniform(2,4))     # 랜덤으로 2-4초 사이를 대기함
# # 패스워드 입력
# elem = browser.find_element(By.ID,"pw")
# elem.send_keys("Navkmj324675!@")
# time.sleep(random.uniform(2,4))     # 랜덤으로 2-4초 사이를 대기함
# # 로그인 버트 클릭
# elem = browser.find_element(By.CLASS_NAME,"btn_login")
# elem.click()



# 페이지가 종료되지 않게 하기 위해
input("enter키 입력")