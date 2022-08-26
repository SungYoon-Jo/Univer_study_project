import re

custlist=[
    {'name':'jsy','number':'18110140','math':'100','korea':'80','english':'30','sum':'210','li':'3'},
    {'name':'jje','number':'18110141','math':'90','korea':'90','english':'25','sum':'205','li':'4'},
    {'name':'ptt','number':'18110142','math':'80','korea':'100','english':'40','sum':'220','li':'2'},
    {'name':'jsy','number':'18110143','math':'100','korea':'80','english':'100','sum':'280','li':'1'}
]

page = 0

def exe(choice,page):
    if choice == 'I':
        page = insertData(page)
        print(page)
    elif choice == 'C':
        curSearch(page)
        print(page)
    elif choice == 'P':
        page = preSearch(page)
    elif choice == 'N':
        page = nextSearch(page)
    elif choice == 'U':
        updateData(page)
    elif choice == 'D':
        page = deletSearch(page)
    elif choice == 'S':
        page = allSearch()
    elif choice == 'L':
        page = listSearch(page)
        print(page)
    elif choice == 'Q':
        quit()
    return page

def insertData(page):
    print('학생 정보 입력')
    customer={'name':'','number':'','math':'','korea':'','english':'','sum':''}
    customer['name'] = input("name 입력하세요 : ")

    while True:
        customer['number'] = input("number 입력하세요 : ")
        check = 0
        for i in custlist:
            if i['number'] == customer['number']:
                check = 1
        if check == 1:
            print('중복되는 학번이 있습니다.')
        elif check == 0:
            break
    
    while True:
        customer['math'] = input("math 입력하세요 : ")
        customer['korea'] = input("korea 입력하세요 : ")
        customer['english'] = input("english 입력하세요 : ")
        
        customer['sum'] = int(customer['math']) + int(customer['korea']) + int(customer['english'])


        if custlist.append(customer):
            print("저장 되었습니다.")
        page += 1
        print(custlist[page])
        return page
         
         
def curSearch(page):
    print('현재 학생 정보 조회')
    if page >= 0:
        print('현재 페이지는 {}쪽 입니다.'.format(page+1))
        print(custlist[page])
    else:
        print('입력된 정보가 없습니다.')
        
def preSearch(page):
    print('이전 고객 정보 조회')
    if page <= 0:
        print("첫번째 페이지이므로 이전 페이지로 이동이 불가능 합니다.")
        print(custlist[page])
    else:
        page -= 1
        print('현재 페이지는 {}쪽 입니다.'.format(page+1))
        print(custlist[page])
    return page
    
def nextSearch(page):
    print('다음 고객 정보 조회')
    if page >= len(custlist) - 1:
        print('마지막 페이지이므로 다음 페이지로 이동이 불가능 합니다.')
        print(custlist[page])
    else:
        page += 1
        print("현재페이지는 {}쪽 입니다.".format(page + 1))
        print(custlist[page])
    return page

def updateData(page):
    print('고객 정보 수정')
    while True:
        choice1 = input('수정하려는 학생정보의 학번를 입력하세요 : ')
        page = -1
        for i in range(0,len(custlist)):
            if custlist[i]['number'] == choice1:
                page = i
                break
        if page == -1:
            print('등록되지 않은 이메일 입니다.')
            break

        print(custlist[page])
        choice2 = input('수정하실 정보를 선택하세요(name,number,math,korea,english) 종료:q : ')
        
        if choice2 in ('name','number','math','korea','english'):
            custlist[page][choice2] = input('수정할 {}을 입력하세요 종료:q : '.format(choice2))
        elif choice2 == 'q':
            break
        else:
            print('존재하지 않는 정보입니다.')
            break

    print(custlist[page])
    
def deletSearch():
    choice1 = input('삭제하려는 학생정보의 학번을 입력하세요 : ')
    delok = 0
    for i in range(0,len(custlist)):
        if custlist[i]['math'] == choice1:
            print('{} 고객님의 정보가 삭제되었습니다.'.format(custlist[i]['name']))
            del custlist[i]
            delok = 1
            break
    if delok == 0:
        print('등록되지 않은 고객 정보입니다.')
    print(custlist)

def allSearch():
    choice1 = input('찾으려는 학생 이름을 입력하세요 : ')
    asear = 0
    i = 0

    while True:
        if custlist[i]['name'] == choice1:
            print(custlist[i])
            asear = 1
        
        if i == len(custlist)-1:
            break
        i += 1

    if asear == 0:
        print('등록되지 않은 고객 정보입니다.')

def listSearch(page):
    b = []
    page += 1
    if page == len(custlist):
        page -= 1

    for i in range(0,len(custlist)):
        b.append(custlist[i]['sum'])
        b.sort(reverse=True)

    for i in range(len(b)):
        for j in range(len(custlist)):
            if b[i] == custlist[j]['sum']:
                # print(custlist[j])
                # print(b[i])
                custlist[j]['li'] = i+1
                break

    return page

# 0 - 0123
# 1 - 0123
# 2 - 0123
# 3 - 0123


def quit():
    print('bye~ bye~')
    exit()
    
    
while True:
    choice = input('''
다음 중에서 하실 작업을 골라주세요 : 
I - 학생 정보 입력
C - 현재 학생 정보 조회
P - 이전 학생 정보 조회
N - 다음 학생 정보 조회
U - 학생 정보 수정
D - 학생정보 삭제
S - 학생 이름 조회
L - 학생 성적 등수 조회
Q - 프로그램 종료
''').upper()
    page = exe(choice,page)