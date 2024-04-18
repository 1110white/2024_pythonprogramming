def read_single_digit(n):
    if n == 0:
        return '영'
    elif n == 1:
        return '일'
    elif n == 2:
        return '이'
    elif n == 3:
        return '삼'
    elif n == 4:
        return '사'
    elif n == 5:
        return '오'
    elif n == 6:
        return '육'
    elif n == 7:
        return '칠'
    elif n == 8:
        return '팔'
    else:
        return '구'

def read_number(num):
    n100 = read_single_digit(num//100)
    num %= 100
    n10 = read_single_digit(num//10)
    num %= 10
    n = read_single_digit(num)
    return n100 + n10 + n
    
number = int(input("세 자리 정수 입력: "))
print(read_number(number))
