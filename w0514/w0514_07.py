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
browser = webdriver.Chrome(options=options) # 다른위치에 있는경우 위치점 찍어야 실행가능 "c:/down/chromedriver"
browser.maximize_window() # 창 최대화

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

smtpName = "smtp.naver.com"
smtpPort = 587

# 중요정보
recvEmail = "onulee@naver.com"
password = "R12G34FT6FTH"
### 네이버 로그인 비밀번호를 입력해도 되지만, 파일이 노출되는 경우 개인정보 침해 우려 ###

## MIME 객체화
msg = MIMEMultipart('alternative')
# 내용부분
text = "네이버 랭킹뉴스보냄"
part2 = MIMEText(text)
msg.attach(part2)
msg['From'] = "kkk990108@naver.com"
msg['To'] = recvEmail
msg['Subject'] = "네이버 12개 랭킹 1위 뉴스를 보내드립ㄴ디ㅏ."

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
recvMails = ['kkk990108@naver.com','onulee@naver.com']
for recvMail in recvMails:
    s.sendmail("kkk990108@naver.com",recvEmail,msg.as_string())
s.quit() 

browser = webdriver.Chrome(options=options)

url = "https://news.naver.com/main/ranking/popularDay.naver"
browser.get(url)

soup = BeautifulSoup(browser.page_source,"lxml")
data = soup.find("div", {"class":"_officeCard _officeCard0"})
data2 = data.find_all("div", {"class":"rankingnews_box"})

ff= open("w0514/news.csv","w",encoding="utf-8-sig",newline="")
writer = csv.writer(ff)

for news in data2:
    list = []
    # 신문사
    paper = news.find("strong",{"class":"rankingnews_name"}).get_text().strip()
    list.append(paper)
    # 제목
    title = news.find("a",{"class":"list_title nclicks('RBP.rnknws')"}).get_text().strip()
    list.append(title)

    writer.writerow(list)
print(list)




### 퀴즈 ###
# news.csv
# # 신문사 기사
# 뉴시스,'전원일기 일용이' 박은수 수천만원 사기 혐의로 피소
# 한국경제,'지금 계약해도
# 파일첨부 메일로 발송
# 제목 : 네이버 랭킹뉴스 보냄.
# 내용 : 네이버 12개 랭킹 1위 뉴스를 보내드립니다.
# 보내는 주소 : onulee@naver.com

ff.close()
input("종료시 엔터")