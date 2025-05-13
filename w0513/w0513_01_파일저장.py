import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import csv
import time

# 크롬옵션설정 - 셀레니움 접근 제한 : 보안접근 해제
options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")  # 자동화 티 안 나게
options.add_argument("start-maximized")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

# 브라우저 실행
browser = webdriver.Chrome(options=options)

# 페이지 접속
url = "https://edu1032.shiningcorp.com/index.php?device=pc&designkits=1"
browser.get(url)
time.sleep(2)   # 페이지 로딩 대기

print(browser.page_source)
soup = BeautifulSoup(browser.page_source,"lxml")

# 파일저장
with open("w0513/temple1.html","w",encoding="utf-8")as f:
    f.write(soup.prettify())
    
# 프로그램 종료
input("프로그램 종료(엔터키입력)")