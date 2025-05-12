import requests
from bs4 import BeautifulSoup
import csv

url = "https://finance.naver.com/sise/sise_market_sum.naver?&page=1"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()  # 에러시 종료
soup = BeautifulSoup(res.text,"lxml")



# ## 상단 타이틀
# print(soup.thead)
# ff = open('w0509/stock.csv',"w",encoding="utf-8-sig",newline="")
# writer = csv.writer(ff)
# ths = soup.thead.find_all("th")
# fileName = []
# for th in ths:
#     print(th.get_text(),end="\t")
#     fileName.append(th.get_text().strip())
# writer.writerow(fileName)


### 내용부분 5개 -> 50개
# print(soup.tbody)
trs = soup.tbody.find_all("tr")
print("trs개수: ",len(trs))
count = 0
for i,tr in enumerate (trs):
    if count > 5 : break
    tds = tr.find_all("td")
    if len(tds) <= 1: continue
    print(tds)
    count += 1



## 완료
# ff.close()
# print("파일저장완료")