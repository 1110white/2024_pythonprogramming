def buy(dict):
    print('[구입]')
    item = input('상품명? ')
    if item == '' :
        return False
    amount = int(input('수량은? '))
    if amount <= 0 :
        print('잘못된 수량을 입력하셨습니다.')
        return False
    shopping_bag[item] = amount
    print(f'장바구니에 {item} {shopping_bag[item]}개가 담겼습니다.\n')

def show(dict):
    print(f'\n>>> 장바구니 보기: {shopping_bag}\n')

def find(dict):
    print('[검색]')
    item = input('장바구니에서 확인하고자 하는 상품은? ')
    if item in shopping_bag :
        print(f'{item}은(는) {shopping_bag[item]}개 담겨 있습니다.')
    else :
        print(f'{item}은(는) 장바구니에 없습니다.')


shopping_bag = {}
while True:
    if buy(shopping_bag) == False:
        break
show(shopping_bag)
find(shopping_bag)
