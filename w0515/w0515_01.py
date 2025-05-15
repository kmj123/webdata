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
# 크롬 옵션 설정 - 셀레니움 접근 제한 : 보안접근 해제
options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")  # 자동화 티 안 나게
options.add_argument("start-maximized")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
# 브라우저 실행
browser = webdriver.Chrome(options=options)
browser.maximize_window() # 창 최대화

## 메일관련 import
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

smtpName = "smtp.naver.com"
smtpPort = 587

# 중요정보
recvEmail = "kkk990108@naver.com"  # 받는사람 주소
password = "R12G34FT6FTH"       ### 네이버 로그인 비밀번호를 입력해도 되지만, 파일이 노출되는 경우 개인정보 침해 우려 ###

### 파일첨부 부분 ###
## MIME 객체화
msg = MIMEMultipart('alternative')
# 내용부분
text = """<h2> 랭킹뉴스 기사모음</h2>
<img src='https://mail.naver.com/read/image/original/?mimeSN=1747271993.181274.172.46848&offset=1588&size=4808542&u=kkk990108&cid=7577d4c71e5c52f91a7cbbc4eea2a32@cweb011.nm&contentType=image/jpeg&filename=1747271991065.jpeg&org=1'>
"""
part2 = MIMEText(text,"html")
msg.attach(part2)
msg['From'] = "kkk990108@naver.com"
msg['To'] = recvEmail
msg['Subject'] = "언론사별 랭킹뉴스를 보냅니다."

## 파일첨부
part = MIMEBase('application',"octet-stream")
## 파일읽어오기
with open('w0514/news.csv',"rb") as f:
    #part담기
    part.set_payload(f.read())

#파일첨부할수 있는 형태로 인코딩
encoders.encode_base64(part) 
## header 정보
part.add_header('Content-Disposition','attachment',filename='news.csv')
msg.attach(part)

## 메일발송부분   
s = smtplib.SMTP("smtp.naver.com",587)
s.starttls()
s.login("kkk990108",password)
### 보내는 주소가 네이버메일이 아니면 에러처리 
recvMails = 'kkk990108@naver.com'
s.sendmail("kkk990108@naver.com",recvEmail,msg.as_string())
s.quit() 


## csv 파일 생성
f = open("w0515/news.csv","w",encoding="utf-8-sig",newline="")
writer = csv.writer(f)


title = ['언론사','기사제목']
writer.writerow(title)      ## csv 리스트 저장

### 1. 네이버 접속
url = "https://news.naver.com/main/ranking/popularDay.naver"
browser.get(url)

## html 파싱
soup = BeautifulSoup(browser.page_source,"lxml")

## 언론사별 랭킹 뉴스 전체
data = soup.find("div",{"class":"rankingnews_box_wrap"})
## 랭킹뉴스 리스트  - 12개
rNews = data.find_all("div",{"class":"rankingnews_box"})


for r in rNews:
    ## 언론사 이름
    newsName = r.find("strong",{"class":"rankingnews_name"}).get_text().strip()
    print(newsName)
    newscontent = r.find("a",{"class":"list_title"}).get_text().strip()
    print(newscontent)
    
    ## news_list = [] 
    # 리스트를 안만들고 바로 적어도됨
    writer.writerow([newsName,newscontent])

# 파일생성완료
f.close()

# 파일 생성하는 동안 잠시 대기
time.sleep(2)

print("메일발송완료")

input("엔터시 종료")

