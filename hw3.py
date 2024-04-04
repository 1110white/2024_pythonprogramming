def get_fixed_price(per, price):
    return int(price*(100/(100-per)))

per = int(input("할인율은? "))
a = int(input("A상품의 할인된 가격은? "))
b = int(input("B상품의 할인된 가격은? "))

at = get_fixed_price(per, a)
print("A상품의 정가는",at,"원")
bt = get_fixed_price(per, b)
print("B상품의 정가는",bt,"원")
