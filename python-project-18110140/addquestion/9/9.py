f= open('./sample.txt','r')
lines = f.read().splitlines() #한줄씩 문자열 읽기 
data = []
sum=0

for line in lines:
    data.append(line)

for i in range(0,len(data)):
    sum += int(data[i])

avg = sum/len(data)

print(avg)
print(sum)


f.close()