import re

def sitech():
    site_p = re.compile('^[a-z]+.[a-z]+.[a-z]+$')
    site_c = 0
    while not site_c:
        site = input('사이트 주소? : ')
        site_c = site_p.match(site)
        print("입력 된 사이트 : "+ site)
    # return print("정상적인 사이트 주소 : "+ site)
    return site

print(sitech())
