a = {1: 'filled ',2: 'everyone ', 3: 'happy ', 4: 'days '}
b = {5: 'hope ',6: "is ",7: 'i ',8: 'you ',9: 'good '}
c = {10: "it's ", 11: 'everyday ', 12: 'with ' }
print(a.keys(),b.keys())

t = []
t.append(b[7]+b[5]+a[2]+b[6]+a[3])
t.append(b[7]+b[5]+c[10]+a[1]+c[12]+b[9]+a[4])

print(t)
