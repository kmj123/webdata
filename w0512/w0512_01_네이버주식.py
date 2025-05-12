import requests
from bs4 import BeautifulSoup   ## 파싱할 때 사용
import csv

sum = 0     # 총합계
# 파일 저장
ff = open("w0512/stock.csv","a",encoding = "utf-8-sig",newline="")
writer = csv.writer(ff)

for j in range(1,6):
    url = f"https://finance.naver.com/sise/sise_market_sum.naver?&page={j}"
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"}
    res = requests.get(url,headers=headers)
    res.raise_for_status()  # 에러시 종료

    # 파싱
    soup = BeautifulSoup(res.text,"lxml")   
    data = soup.find("tbody")
    trs = data.find_all("tr")

    ### 상단 타이틀 저장 부분
    if j == 1:
        title = []
        tdata = soup.find("thead")
        ths = tdata.find_all("th")
        for th in ths:
            title.append(th.get_text().strip())
    
        # 파일저장 
        writer.writerow(title)

    
    for tr in trs[:-1]:
        tds = tr.find_all("td")
        contents = []

        # 빈 공백 줄 제거
        if len(tds) <= 1: 
            continue
        # 여러개이면 for문을 사용
        for i,td in enumerate (tds):
            if i ==12: break
            # 1. sum 변수
            # 2. , 천단위 표시 제거 (replace)
            # 3. str -> int 타입 변환
            # 4. 더하기 -> sum
            if i == 2:
                number = td.get_text().strip()
                contents.append(number)
                price = number.replace(",","") # 천단위 표시제거
                sum += int(price)  # 타입변환
                print(price)
                continue
                
            # 상승 500	의 공백 제거 및 출력
            if i == 3: 
                em1 = td.find("em").get_text().strip()
                span1 = td.find("span",{"class":"tah"}).get_text().strip()
                contents.append(em1+span1)
                print(em1+span1)
                continue
            tcontent = td.get_text().strip()
            contents.append(tcontent)
            print(td.get_text().strip())
            
        writer.writerow(contents)   #내용 파일 저장
        print("-"*50)    
    
        
print(f"총합계: {sum:,d}")
ff.close()
print("프로그램을 종료합니다.")   


# # td 여러개
# tds = trs[1].find_all("td")
# # 여러개이면 for문을 사용
# for td in tds:
#     print(td.get_text().strip())
# print("-"*50)
# tds = trs[2].find_all("td")

# # 여러개이면 for문을 사용
# for td in tds:
#     print(td.get_text().strip())


# data = soup.find("thead")
# print(data)

# # 데이터 찾는 방법
# th1 = data.find("th")       # 한개/ 없으면 NONE
# print(th1)
# print("-"*50)
# ths = data.find_all("th")   # 여러개
# print(ths)
# print("-"*50)
# tr1 = data.find("th",{"class":"tr"})   # class이름이 tr인 데이터들   
# print(tr1.get_text())   # 텍스트만 출력