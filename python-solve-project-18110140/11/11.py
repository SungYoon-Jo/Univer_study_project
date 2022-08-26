a = input("도서명 : ")
b = input("저자 : ")
c = input("출판사 : ")

f = open("./save.txt", 'w')
f.write(a+','+b+','+c+'\n')
f.close()


f1 = open("./save.txt", "r")
for line in f1.readlines():
    line = line.replace('\n','')
    data = line.split(',')
    print(line[0],line[1],line[2])
    print('도서명 : {},저자 : {},출판사 : {}'.format(data[0],data[1],data[2]))
    

