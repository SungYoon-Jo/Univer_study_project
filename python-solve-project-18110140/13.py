class ac:
    ac_c = 0
    
    @classmethod
    def g_ac_n(cls):
        print("num : ", cls.ac_c)
        
    def __init__(self,name,blan):
        ac.ac_c += 1
        self.de_c = 0
        self.to_l = []
        self.name = name
        self.blan = blan
        self.ac_n = str(ac.ac_c)
        
    def de(self,am):
        if am >= 1:
            self.to_l.append(('입금',am))
            self.blan += am
            self.de_c += 1
            if self.de_c % 5 ==0:
                ins = int(self.blan * 0.01)
                self.blan += ins
                self.to_l.append(('이자지급',ins))
                print(ins, '원의 이자가 지금되었습니다.')
    def wi(self,am):
        if self.blan > am:
            self.to_l.append(('출금', am))
            self.blan -= am
        else:
            print('잔액이 부족합니다.')
    def info(self):
        print('예금주 : ', self.name)
        print('계좌번호 : ', self.ac_n)
        print('잔고 : ', self.blan)
        
    def __str__(self):
        return '예금주: '+self.name+' 계좌번호: '+self.ac_n+' 잔고: '+str(self.blan)
    
a = ac('jo', 20000)
b = ac('sung', 30000)
a.info()
print(b)

a.de(2000)
a.de(100)
a.de(787)
a.wi(30000)
a.de(3429)
a.de(787878)
a.de(3434)

print(a.to_l)
print(b.to_l)

ac.g_ac_n()
