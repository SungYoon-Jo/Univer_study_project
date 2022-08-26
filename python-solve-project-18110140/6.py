import random as r

ri = r.randint(1, 100)

print(ri)
c = 1
while True:
    s = int(input("1~100사이 숫자를 입력하세요 : "))
    if ri == s:
        print("정답입니다. %d번만에 맞추셨습니다."% c)
        break
    elif ri < s:
        print("%d 번째 시도 : 더 작은수를 입력하세요"% c) 
    elif ri > s:
        print("%d 번째 시도 : 더 큰수를 입력하세요"% c)   
    else:
        c += 1