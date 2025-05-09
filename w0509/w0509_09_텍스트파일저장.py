f= open("w0509/a1.txt","a",encoding="utf8")
txt = "번호,제목,작성자,작성일,조회수\n"; 
f.write(txt)

txt1 = "1,이벤트신청,홍길동,2025-04-20,1\n";
f.write(txt1)
txt2 = "2,강의신청2,유관순,2025-04-21,10\n";
f.write(txt2)

f.close()

print("프로그램 종료")

