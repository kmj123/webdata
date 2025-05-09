import requests
from bs4 import BeautifulSoup
import csv

with open("w0509/게시판3.html","r",encoding="utf8")as f:
    soup = BeautifulSoup(f,"lxml")
    
    
# # html 태그 출력 soup.title
# print(soup.title)
# print(soup.title.get_text())    # 없는걸 출력하려고 하는 경우 에러발생함
# # 속성 출력 soup.a['href']
# print(soup.a['href'])
# # find(), find_all()
# print(soup.find("thead"))

data = soup.find("thead")
ths = data.find_all("th")
print("th개수: ",len(ths))
# for th in ths:
#     print(th)
    
# for i in range (len(ths)-1):
#     print(ths[i])

## 파일저장
fileName = "board.csv"
ff = open("w0509/"+fileName,"w",encoding="utf-8-sig",newline="")
# with open("w0509/"+fileName,"w",encoding="utf-8-sig",newline="")
writer = csv.writer(ff)

txt = "번호,제목,작성자,작성일,조회수\n"; 

## 1. 상단
# 상단제목 파일에 저장
topTitle = []
for i,th in enumerate (ths):
    if i<5:
        print(th.get_text(),end="\t")
        topTitle.append(th.get_text())
writer.writerow(topTitle)   # 리스트 타입만 가능
print()



## 2. 하단
data2 = soup.find("tbody")
trs = data2.find_all("tr")
# print("tr개수: ",len(trs))
#리스트가 넘어오면 for문
for tr in trs:  
    tds = tr.find_all("td")
    if len(tds)<=1: continue
    bodyData = []   # 게시글 부분 데이터저장
    for i,td in enumerate (tds):
        if i<5: 
            print(td.get_text(),end="\t")
            bodyData.append(td.get_text())
    writer.writerow(bodyData)   # 파일에 게시글 1개를 저장
    print()




# data = soup.find("tbody",{"id":"tbody"})
# tbs = data.find_all("tr")
# print(len(tbs))

# for tb in tbs:
#     tbs = tb.find_all("td")
   
#     # if len(tbs) > 1: ## 사이공간 제외
#     #     for i in range(len(tbs)-1): ## 수정, 삭제 제외
#     #         print(tbs[i].get_text(),end="\t")   ## 텍스트만 가져오기
#     #     print()
    
#     if len(tbs)>1:
#         for i in range(len(tbs)-1):
#             print(tbs[i].get_text(),end="\t")
#         print()

ff.close()
print("파일 저장완료!!")   