import requests
from bs4 import BeautifulSoup   ## 파싱할 때 사용
import csv

url = "https://search.daum.net/search?w=tot&q=2024%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()  # 에러시 종료
# print(res.text)

# 파싱
soup = BeautifulSoup(res.text,"lxml")   

## 파일 저장
# with open("w0512/screen.html","w",encoding="utf8")as f:
#     f.write(soup.prettify())

with open("w05112/screen.html","r",encoding="utf-8") as f:
    soup = BeautifulSoup(f,"lxml")

data = soup.find("div",{"id":"morColl"})
# print(data)
data2 = data.find("c-flicking")
# print(data2)

### 영화 30개 가져오기
data3 = data2.find_all("c-doc")
print(len(data3))
print(data3[0].find("c-title"))
print(data3[0].find("c-contents-desc"))
print(data3[0].find("c-contents-desc-sub"))

# 제목, 누적, 날짜 출력
title = data3[0].find("c-title")
contents = data3[0].find("c-contents-desc")
date = data3[0].find("c-contents-desc-sub")
