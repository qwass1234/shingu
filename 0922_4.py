print "당신이 태어난 년도를 입력하세요."
x=int(raw_input())
y=(2015-x)+1
if 26>= y >=20:
    print "대학생"
elif 20> y >=17:
    print "고딩"
elif 17> y >=14:
    print "중딩"
elif 14> y >=8:
    print "초딩"
else:
    print "학생이 아닙니다."
