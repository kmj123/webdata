import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv 
import time

# selenium 크롬자동화 프로그램(=매크로)
# user-agent 변경
options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size= 1920X1080")
options.add_argument('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7')
browser = webdriver.Chrome(options=options)
url = "https://www.coupang.com/np/search?component=&q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user"
browser.get(url)
# 시간멈춤
time.sleep(2)

# 파싱
soup = BeautifulSoup(browser.page_source,"lxml")

with open("w0512/coupang1.html","w",encoding="utf-8") as f:
    f.write(soup.prettify())
    
print("프로그램 종료시 enter>>")

elem = browser.find_element(By.ID,"query")  # query선택
