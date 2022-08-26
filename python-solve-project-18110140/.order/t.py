import re

custlist=[
    {'name':'jsy','number':'18110140','math':'100','korea':'80','english':'30','sum':'210'},
    {'name':'jje','number':'18110141','math':'90','korea':'90','english':'25','sum':'205'},
    {'name':'ptt','number':'18110142','math':'80','korea':'100','english':'40','sum':'220'},
    {'name':'jsy','number':'18110143','math':'100','korea':'80','english':'100','sum':'280'}
]

page = 0

def exe(choice,page):
    if choice == 'I':
        page = insertData(page)
        print(page)
    elif choice == 'C':
        curSearch(page)
    elif choice == 'P':
        page = preSearch(page)
    elif choice == 'N':
        page = nextSearch(page)
    elif choice == 'U':
        updateData(page)
    elif choice == 'D':
        page = deletSearch(page)
    elif choice == 'S':
        page = allSearch(page)
        # allSearch(page)
    elif choice == 'Q':
        quit()
    return page

b = []

def allSearch(page):
    # asear = 0
    # i = 0

    # while True:
    #     if custlist[i]['name'] == choice1:
    #         print(custlist[i])
    #         asear = 1
        
    #     if i == len(custlist)-1:
    #         break
    #     i += 1
    customer={'sum':''}
    
    for i in range(0,len(custlist)):
        b.append(custlist[i]['sum'])

    b.sort(reverse=True)

    # for i in range(0,len(custlist)):
        # customer[i]['sum'] = b[i]
        # print(customer[i]['sum'])
        # print(b[i])

    customer['sum'] = b

    


    # if asear == 0:
    #     print('등록되지 않은 고객 정보입니다.')

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
Q - 프로그램 종료
''').upper()
    page = exe(choice,page)