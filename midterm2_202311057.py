
def shift0p(a, n, isLeftDirection):
    c = a*(2**n)
    d = a//(2**n)
    if isLeftDirection == True:
        print(f'{a}<<{n} = {c:d} (0b{c:b})')
    if isLeftDirection == False:
        print(f'{a}>>{n} = {d:d} (0b{d:b})')
    

a = int(input("a를 입력하세요: "))
n = int(input("b를 입력하세요: "))
shift0p(a, n, True)
shift0p(a, n, False)


