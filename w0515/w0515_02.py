import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import time
import random
# 크롬 옵션 설정 - 셀레니움 접근 제한 : 보안접근 해제
options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")  # 자동화 티 안 나게
options.add_argument("start-maximized")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
# 브라우저 실행
browser = webdriver.Chrome(options=options)
browser.maximize_window() # 창 최대화

## 메일관련 import
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

#### 임시패스워드 : aaa1111
### 자신에게 보내기
#### onulee@naver.com

smtpName = "smtp.naver.com"
smtpPort = 587

# 중요정보
recvMails = "kkk990108@naver.com"  # 받는사람 주소
password = "R12G34FT6FTH"       ### 네이버 로그인 비밀번호를 입력해도 되지만, 파일이 노출되는 경우 개인정보 침해 우려 ###

### 파일첨부 부분 ###
## MIME 객체화
msg = MIMEMultipart('alternative')
# 내용부분
text = """

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="ko" xml:lang="ko">
<head>
<meta http-equiv="Content-Type" content="application/xhtml+xml; charset=utf-8" />
<meta http-equiv="X-UA-Compatible" content="IE=edge" />
<title> 비밀번호 발송 </title>


</head>
<body bgcolor="#FFFFFF" leftmargin="0" topmargin="0" marginwidth="0" marginheight="0" style="margin:0; padding:0; font:normal 12px/1.5 돋움;">


<table width="700" cellpadding="0" cellspacing="0" align="center">
<tr>
	<td style="width:700px;height:175px;padding:0;margin:0;vertical-align:top;font-size:0;line-height:0;">
		<img src='https://mail.naver.com/read/image/original/?mimeSN=1747273030.254651.348.22272&offset=9529455&size=4808542&u=kkk990108&cid=e1b4f3145d215f4ced22991380fe69c3@cweb007.nm&contentType=image/jpeg&filename=1747273011309.jpeg&org=1'>					
	</td>
</tr>
<tr>
	<td style="width:700px;height:78px;padding:0;margin:0;vertical-align:top;">
		<p style="width:620px;margin:50px 0 40px 38px;text-align:center;font-size:0;line-height:0;"><img src='https://mail.naver.com/read/image/original/?mimeSN=1747273060.306033.151.14080&offset=1758&size=4805124&u=kkk990108&cid=979d41262c4af33ca3b9fcda4a9c3327@cweb012.nm&contentType=image/jpeg&filename=1747273057958.jpeg&org=1'>
</p>
	</td>
</tr>
<tr>
	<td style="width:700px;height:196px;padding:0;margin:0;vertical-align:top;">
		<table width="618" height="194" cellpadding="0" cellspacing="0" align="center" style="margin:0 0 0 40px;border:1px #d9d9d9 solid;">
		<tr>
			<td style="width:618px;height:194px;padding:0;margin:0;vertical-align:top;font-size:0;line-height:0;background:#f9f9f9;">
				<p style="width:620px;margin:30px 0 0 0;padding:0;text-align:center;"><img src='https://mail.naver.com/read/image/original/?mimeSN=1747273060.306033.151.14080&offset=4807178&size=4766834&u=kkk990108&cid=114b48b7a66dd4a7ceeab199bf74955@cweb015.nm&contentType=image/jpeg&filename=1747273058387.jpeg&org=1'></p>
				<p style="width:620px;margin:10px 0 0 0;padding:0;text-align:center;color:#888888;font-size:12px;line-height:1;">아래의 PASSWORD는 임시 PASSWORD이므로 홈페이지 로그인 후 다시 수정해 주십시오.</p>
				<p style="width:620px;margin:28px 0 0 0;padding:0;text-align:center;color:#666666;font-size:12px;line-height:1;"><strong>임시 패스워드 : <span style="color:#f7703c;line-height:1;">aaa1111</span></strong></p>
				<p style="width:620px;margin:30px 0 0 0;padding:0;text-align:center;color:#888888;font-size:12px;line-height:1.4;">쟈뎅샵에서는 고객님께 보다 나은 서비스를 제공하기 위해 항상 노력하고 있습니다.<br/>앞으로 많은 관심 부탁드립니다.</p>
			</td>
		</tr>
		</table>	
	</td>
</tr>
<tr>
	<td style="width:700px;height:120px;padding:0;margin:0;vertical-align:top;">
		<p style="width:700px;margin:30px 0 50px 0;text-align:center;"><a href="#"><img src='https://mail.naver.com/read/image/original/?mimeSN=1747273030.254651.348.22272&offset=1925&size=4769776&u=kkk990108&cid=47e02b28374bf996779cd4a2ed689e@cweb010.nm&contentType=image/jpeg&filename=1747273010452.jpeg&org=1'></a></p>
	</td>
</tr>
<tr>
	<td style="width:700px;height:50px;padding:0;vertical-align:top;font-size:0;line-height:0;text-align:center;">
		<img src='https://mail.naver.com/read/image/original/?mimeSN=1747273504.944167.152.5888&offset=1590&size=4757162&u=kkk990108&cid=d834d384232e996f78d1010ad7c78@cweb011.nm&contentType=image/jpeg&filename=1747273503370.jpeg&org=1'>
	</td>
</tr>
<tr>
	<td style="width:700px;height:140px;padding:0;margin:0;vertical-align:top;background-color:#5a524c;">
		<p style="width:620px;margin:20px 0 0 40px;padding:0;text-align:center;line-height:1.5;color:#b2aeac;">메일수신을 원치 않으시는 분은 로그인 후. <span style="color:#ffffff">메일 수신 여부</span>를 변경해주시기 바랍니다.<br/>IF YOU DO NOT WISH TO RECEIVE EMAILS FROM US, PLEASE LOG-IN AND UPDATE<br/> YOUR MEMBERSHIP INFORMATION.</p>

		<p style="width:620px;margin:15px 0 0 40px;padding:0;text-align:center;line-height:1.5;color:#b2aeac;"><span style="color:#ffffff">본 메일에 관한 문의사항은 사이트 내 고객센터를 이용해주시기 바랍니다.</span><br/>COPYRIGHT ©  2014 JARDIN ALL RIGHTS RESERVED.</p>
	</td>
</tr>
</table>



</div>
</body>
</html>
"""
part2 = MIMEText(text,"html")
msg.attach(part2)
msg['From'] = "kkk990108@naver.com"
msg['To'] = recvMails
msg['Subject'] = "임시비밀번호 발급"

## 메일발송부분   
s = smtplib.SMTP("smtp.naver.com",587)
s.starttls()
s.login("kkk990108",password)
### 보내는 주소가 네이버메일이 아니면 에러처리 
recvMails = {'kkk990108@naver.com','onulee@naver.com'}
for recvmail in recvMails:
    s.sendmail("kkk990108@naver.com",recvmail,msg.as_string())
s.quit() 

print("메일발송완료")