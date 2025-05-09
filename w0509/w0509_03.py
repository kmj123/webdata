import requests

# url = "https://finance.naver.com/sise/sise_market_sum.naver"
url = "https://n.news.naver.com/article/011/0004483132?ntype=RANKING"
header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"}

res = requests.get(url,headers=header)
res.raise_for_status()  # 에러시 종료
print(res.text)
with open("w0509/test3.html","w",encoding="utf8")as f:  # 한글로 파일저장
    f.write(res.text)
    print("[ 프로그램 종료 ]")