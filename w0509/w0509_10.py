import requests
from bs4 import BeautifulSoup
import csv  # csv파일 저장

with open("w0509/notice_list.html","r",encoding="utf8")as f:
    soup = BeautifulSoup(f,"lxml")

ff = open("w0509/list.csv","w",encoding="utf-8-sig", newline="")    
writer = csv.writer(ff)    # csv List 타입 저장

## 상단타이틀 내용부분
trs = soup.table.find_all("tr")
# print(len(trs)) # 11개 
for i,tr in enumerate (trs):
    fileName = []
    if i == 0: ## 상단타이틀
        ths = soup.table.find_all("th")
        for th in ths:
            print(th.get_text(), end="\t")
            fileName.append(th.get_text())
            
        writer.writerow(fileName)   # 상단타이틀 List 타입으로 저장
        print() 
        continue
    # 내용 부분
    tds = tr.find_all("td")
    for td in tds:
        print(td.get_text(),end='\t')
        fileName.append(td.get_text())
    print()
    writer.writerow(fileName)   # 내용부분 List 타입으로 저장
        
print("파일 저장 완료")
    
    