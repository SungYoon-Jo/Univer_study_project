a = 10000

b = int(input("구매한 물건 가격 : "))
c = int(input("지불 가격 : "))
d = 0
d = c - b

lis = [0 for i in range(8)]
while d != 0 : 
    if d >= 50000:
        lis[0] += 1
        d = d - 50000
    elif d >= 10000 : 
        lis[1] += 1 
        d = d - 10000         
    elif d >= 5000 : 
        lis[2] += 1 
        d = d - 5000 
    elif d >= 1000 : 
        lis[3] += 1 
        d = d - 1000 
    elif d >= 500 : 
        lis[4] += 1 
        d = d - 500 
    elif d >= 100 : 
        lis[5] += 1 
        d = d - 100 
    elif d >= 50 : 
        lis[6] += 1 
        d = d - 50 
    elif d >= 10 : 
        lis[7] += 1 
        d = d - 10

print("50000원 : ",list[0],"개")
print("10000원 : ",list[1],"개")
print("5000원 : ",list[2],"개") 
print("1000원 : ",list[3],"개")
print("500원 : ",list[4],"개")
print("100원 : ",list[5],"개")
print("50원 : ",list[6],"개") 
print("10원 : ",list[7],"개")