import datetime as dt


j = input("주민등록번호를 입력해주세요 ex) yy-mm-dd-1,2,3,4 : ")

y = j[:2]
m = j[2:4]
d = j[4:6]
b = j[6]
a = j[:]

yy = "20" if y[6:7]=="3" or y[6:7]=="4" else "19"
yy += y[:2]

n = dt.datetime.now()
age = n.year - int(yy)

print(age)

