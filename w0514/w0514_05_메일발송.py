import smtplib
from email.mime.text import MIMEText


# 중요정보
recvEmail = "kkk990108@naver.com"
password = "R12G34FT6FTH"
title = "웹스크래핑 이메일 보내기"
text = f"""
    <html>
    <body>
        <h2>{title}</h2>
        <p>메일 html전송</p>
    </body>
    </html>
    """

msg = MIMEText(text,'html')
msg['Subject'] = title
## 네이버주소메일이 아니면 에러
msg['From'] = "onulee@naver.com"
msg['To'] = recvEmail

s = smtplib.SMTP("smtp.naver.com",587)
s.starttls()
s.login("onulee",password)
### 보내는 주소가 네이버메일이 아니면 에러처리 
s.sendmail("onulee@naver.com",recvEmail,msg.as_string())
s.quit()

print("메일발송 완료")