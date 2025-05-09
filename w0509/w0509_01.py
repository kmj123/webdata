import requests

# 사이트에 접속해서 html 소스를 가져옴/
#res = requests.get("https://www.google.com/")  # 접근가능

# 파이썬에서 웹스크래핑 -> 406-> 웹 접근 제한을 진행
# 접근을 할 수 없음
res = requests.get("https://www.melon.com/")    #  접근제한 됨
res = requests.get("https://www.naver.com/")
if res.status_code ==200:
    print("정상적인 프로그램 진행")
    print(res)
    # 응답코드: 200: 정상, 400~404: 페이지 없음,접근제한, 500: 프로그램 에러
    print("응답코드: ", res.status_code)    # 코드 상태 출력
    res.raise_for_status()  # 에러가 났을 시 종료
    print(res.text) # html 소스를 출력해줌/ text 글자타입으로 출력
else: 
    pass

