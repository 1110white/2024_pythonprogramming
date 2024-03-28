def exchange(prise):
    print("500원 동전의 개수:", prise//500)
    prise %= 500
    print("100원 동전의 개수:", prise//100)
    prise %= 100
    print("50원 동전의 개수:", prise//50)
    prise %= 50
    print("10원 동전의 개수:", prise//10)

def get_integer(prompt):
    res = int(input(prompt))
    return res

prise = get_integer("동전으로 교환하고자 하는 금액은? ")
exchange(prise)
