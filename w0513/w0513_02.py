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
url = "https://www.gmarket.co.kr/n/best"
browser.get(url)
time.sleep(2)   # 페이지 로딩 대기

# print(browser.page_source)    # 전체 소스
soup = BeautifulSoup(browser.page_source,"lxml")

data = soup.find("div",{"id":"container"})  
ul = data.find("ul",{"class":"list__best"})
lis = ul.find_all("li")

sum = 0
for li in lis[:10]:
    print(li.find("span",{"class":"box__label-rank"}).get_text())   # 순위
    print(li.find("p",{"class":"box__item-title"}).get_text())      # 제목
    price = li.find("span",{"class":"text__value"}).get_text()
    print(price)  # 가격
    price = int(price.replace(",","") ) 
    ### 총합계 가격 출력
    sum += price
    
print("-"*30)
print(f"총합계: {sum:,d}")



# 파일 저장 후 저장된 파일을 가지고 웹스크래핑해도됨. requests 사용 가능
input("프로그램 종료(엔터키 입력)")

# import requests
# from bs4 import BeautifulSoup
# import csv
# import time

# url = "https://www.gmarket.co.kr/n/best"

# # 옵션설정
# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"}

# # 페이지 접속
# res = requests.get(url,headers=headers)
# res.raise_for_status()  # 에러시 종료


# print(res.text) # 소스출력
# soup = BeautifulSoup(res.text,"lxml")   # html 파싱
