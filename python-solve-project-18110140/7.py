import random as r

c = 0
o = ['+','-','*','/']

for x in range (5):
    a = r.randint(1,50)
    b = r.randint(1,50)
    p = r.choice(o)
    q = str(a)+p+str(b)
    print(q, '=')
    r = int(input('정답 = '))
    if int(eval(q)) == r:
        print('정답!')
        c += 1
    else:
        print('오답!')
print('{}개 맞음'.format(c))

