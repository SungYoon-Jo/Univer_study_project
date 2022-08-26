a = ["a","b","c","d","e"]
a.insert(1, 'p')
print(a)
del a[0]
print(a)
a.sort()
print(a)
a.reverse()
print(a)
print(a.index("c"))
print(a.pop(2))
print(a.count("e"))
a.extend(["j","k","l"])
print(a)