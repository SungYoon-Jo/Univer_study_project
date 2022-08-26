import random,time,pickle,os

dir = os.path.dirname(__file__)

word = ['cat','dog','fox','monkey','mouse','panda','frog','snake','wolf']
rank = {}

with open(dir+'/rank.pkl','rb') as f:
    rank = pickle.load(f)

while True:
    prompt = '1.문제추가 2.문제저장 3.문제읽기 4.타자게임 5.등수리스트 6.종료 \n'
    menu = input(prompt)
    if menu == '1':
        quiz = 1
        while quiz:
            quiz = input("추가할 단어를 입력하세요(종료:0) : ")
            if quiz == '0':
                print('입력을 종료합니다.')
                break
            word.append(quiz)
        print(word)
    elif menu == '2':
        with open(dir+'/word.pkl','wb') as f:
            pickle.dump(word,f)
        print(word)
    elif menu == '3':
        with open(dir+'/word.pkl','rb') as f:
            word = pickle.load(f)
    elif menu == '4':
        n = 1
        q = random.choice(word)
        input('start!!')
        start = time.time()
        while n <= 5:
            print('--{}번--'.format(n))
            print(q)
            x = input()
            if q == x:
                print('good!')
                n+=1
                q=random.choice(word)
            else:
                print("replay!")
        end = time.time()
        print('걸린 시간 : {:.0f}초'.format(end-start))
        name = input("이름을 입력하세요 : ")
        rank[name]=end-start
        print(rank)
    elif menu == '5':
        ranklist = sorted(rank.items(),key=(lambda x:x[1]))
        print(ranklist)
        cnt = 1
        for k,v in ranklist:
            print('{}등 {} 시간:{:.2f}'.format(cnt,k,v))
            cnt += 1
    elif menu == '6':
        with open (dir+'/rank.pkl','wb') as f:
            pickle.dump(rank,f)
        print("bye~ bye~")
        break
    else:
        print('다시 선택해주세요')
        