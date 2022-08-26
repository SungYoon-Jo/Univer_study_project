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
            print(am,'원이 출금되었습니다.')
        else:
            print('잔액이 부족합니다.')
    def info(self):
        print('예금주 : ', self.name)
        print('계좌번호 : ', self.ac_n)
        print('잔고 : ', self.blan)
        
    def __str__(self):
        return '예금주: '+self.name+' 계좌번호: '+self.ac_n+' 잔고: '+str(self.blan)

ac_l = [] 
while True:
    m = input('1.계좌개설 2.입금 3.출금 4.입출금내역 5.총계좌수출력 6.종료 \n')
    if m == '1':
        name = input("name : ")
        blan = int(input("입력 금액 : "))
        a = ac(name,blan)
        ac_l.append(a)
        print(a)
        print("계좌가 개설되었습니다.")
    elif m == '2':
        ac_n = input("계좌번호를 입력해주세요 : ")
        check = 0
        for acc in ac_l:
            if acc.ac_n == ac_n:
                check = 1
                am = int(input('입금할 금액을 입력하세요 : '))
                acc.deposit(am)
                print(am,'원이 입금되었습니다.')
        if check == 0:
            print('계좌번호가 없습니다.')
    elif m == '3':
        ac_n = input("계좌번호를 입력해주세요 : ")
        check = 0
        for acc in ac_l:
            if acc.ac_n == ac_n:
                check = 1
                am = int(input('출금할 금액을 입력하세요 : '))
                acc.withdraw(am)
                print(am,'원이 입금되었습니다.')
        if check == 0:
            print('계좌번호가 없습니다.')
    elif m == '4':
        ac_n = input("계좌번호를 입력해주세요 : ")
        check = 0
        for acc in ac_l:
            if acc.ac_n == ac_n:
                check = 1
                for d in acc.to_l:
                    print(d[0],d[1])
        if check == 0:
            print('계좌번호가 없습니다.')
    elif m == '5':
        ac.g_ac_n()
    elif m == '6':
        print("exit!")
        break
    else:
        print("no menu")