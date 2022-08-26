

def one(a):

    if "fuun" in a:
        print("fuun")
    elif "python" in a and "is" not in a:
        print("python")
    elif "love" not in a:
        print("python love")
    elif "fun" in a:
        print("fun")
    else:
        print("name")

def two(b):
    
    if  b == "yes":
        print("파이썬 쉬워요")
    else:
        print("파이썬 싫어요")

a = "Python is fun"
one(a)

b = input("파인썬 기초를 수강 했나요 yes or no를 입력해주세요 : ")
two(b)