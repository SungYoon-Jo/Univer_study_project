coffee = {"카푸치노": 2500,"카페라떼": 3500,
"아메리카노": 1500,"레몬에이드": 3000,
"자몽에이드": 3300,"오곡라떼": 4000,
"믹스커피": 500,"감자커피": 6000}

print("mune",coffee.keys())

s = input("음료선택 : ")

print("price : ",coffee[s])
