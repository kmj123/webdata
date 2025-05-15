import requests
from bs4 import BeautifulSoup

### fly1.html 을 불러오기
### 항공사, 출발시간, 도착시간, 편도 금액 출력

with open("w0513/fly1.html","r",encoding="utf-8") as f:
    soup = BeautifulSoup(f,"lxml")

rows = soup.find_all("div",{"class":"domestic_Flight__8bR_b"})
datas_list = [] # List 정렬

for row in rows:
    print("-"*30)
    # 항공사
    airline = row.find("b",{"class":"airline_name__0Tw5w"}).get_text().strip()
    print(airline)

    # 출발, 도착 시간
    schedule = row.find_all("b",{"class":"route_time__xWu7a"})
    startTime = schedule[0].get_text().strip()
    departTime = schedule[1].get_text().strip()
    print(startTime)
    print(departTime)
    
    # 편도금액
    price = row.find("i",{"class":"domestic_num__ShOub"})
    price = price.get_text().strip().replace(",","")
    price = int(price)
    print(price)
    print("-"*30)
    
    datas_list.append([airline,startTime,departTime,price])
    
### 최저가 LISt 정렬
dd_list = sorted(datas_list,key=lambda x:x[3])  # 순차정렬
# dd_list = sorted(datas_list,key=lambda x:x[3], reverse=True)  # 역순정렬
# datas_list를 가져와서 안에들어있는 내용을 람다식으로 3번째 있는 데이터로 정렬
print(dd_list)


input("엔터시 종료")