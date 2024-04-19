def display_triangle(height):
    for i in range (1, height + 1):
        display_nums(i)
        print()

def display_nums(n):
    for i in range(1, n + 1):
        print(i, end='')
        

# 이중 for문을 활용한 경우 아래 함수 하나로 가능
# def display_triangle(height):
    # for i in range (1, height + 1):
        # for j in range (1, i + 1):
            # print(j, end='')
        # print()


h = int(input('높이? '))
display_triangle(h)
