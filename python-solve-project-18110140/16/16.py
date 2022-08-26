import functionM as fm
word = ['cat','dog','fox','monkey','mouse','panda','frog','snake','wolf']
rank = {}

rank = fm.rankLoad()
print(rank)

while True:
    prompt = '1.문제추가 2.문제저장 3.문제읽기 4.타자게임 5.등수리스트 6.종료 \n'
    menu = input(prompt)
    if menu == '1':
        word = fm.wordAppend(word)
    elif menu == '2':
        fm.wordSavePik(word)
    elif menu == '3':
        word = fm.wordLoadPik()
    elif menu == '4':
        rank = fm.game(word,rank)
    elif menu == '5':
        fm.rankList(rank)
    elif menu == '6':
        fm.enfGame(rank)
        break
    else:
        print("메뉴 선택을 잘못하셨습니다.")

    