
amho = "good"

while True:
    a = input('암호를 입려해주세요 : ')
    if len(amho) == len(a) and amho == a:
        print('맞췄습니다.')
        break
    else:
        print('암호가 틀렸습니다 다시 입력해주세요 : ')
