def exchange(money):
    a = float(input("오늘의 환율은(100엔)? "))
    n100 = int(money//(a*100))
    m = money%(a*100)
    n50 = int(m//(a*50))
    m = m%(a*50)
    n10 = int(m//(a*10))
    ex = int(((m%(a*10))//10)*10)
    
    print(f'10000엔의 개수: {n100}')
    print(f'5000엔의 개수: {n50}')
    print(f'1000엔의 개수: {n10}')
    print(f'잔돈: {ex}원')



n = int(input("엔화지폐로 교환하고자 하는 금액은? "))
exchange(n)
