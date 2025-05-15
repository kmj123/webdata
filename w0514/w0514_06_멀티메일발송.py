import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase 
from email import encoders

## 중요부분
recvEmail = "kkk990108@naver.com"
password = "R12G34FT6FTH"


### 파일첨부 부분 ###
## MIME 객체화
msg = MIMEMultipart('alternative')
# 내용부분
text = "이메일 글자 발송"
part2 = MIMEText(text)
msg.attach(part2)
msg['From'] = "onulee@naver.com"
msg['To'] = recvEmail
msg['Subject'] = "시가총액 250개 주식정보를 보냅니다."

## 파일첨부
part = MIMEBase('application',"octet-stream")
## 파일읽어오기
with open('w0514/stock.csv',"rb") as f:
    #part담기
    part.set_payload(f.read())

#파일첨부할수 있는 형태로 인코딩
encoders.encode_base64(part) 
## header 정보
part.add_header('Content-Disposition','attachment',filename='stock.csv')
msg.attach(part)

## 메일발송부분   
s = smtplib.SMTP("smtp.naver.com",587)
s.starttls()
s.login("onulee",password)
### 보내는 주소가 네이버메일이 아니면 에러처리 
recvMails = ['onlee@naver.com','onulee74@gmail.com']
for recvMail in recvMails:
    s.sendmail("onulee@naver.com",recvEmail,msg.as_string())
s.quit() 

print("메일발송 완료")