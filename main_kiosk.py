#########################################################################
# 키오스크 프로그램 Main 저석부(console programming)
# 개발자 :촬철웅
# 2021.10.31
##############################################################################

# view => Console
# controller =>Python
# Model(데이터베이으스)=>LIST,DICT

# 조건
# 사용자는 최대로 버거 1개 사으드 1개 음료 1개 주문할 있습니다

# 매뉴와 가격표

burger_name = {1: '치즈버거', 2: '불고기버거', 3: '새우버거'}
side_name = {1: '프렌치프라으', 2: '치킨너겟'}
drink_name = {1: '코카콜라', 2: '커피', 3: '주스'}

burger_price = {1: 3500, 2: 3000, 3: 2500}
side_price = {1: 1500, 2: 2000}
drink_price = {1: 1000, 2: 1200, 3: 1500}

# 고객 주문 기록 저장
mane_save = {}
price_save = {}

# >> VIEW :메뉴 선택(최소)


print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
print('■■ == CNU 버거(ver.01) ==')
print('■■ CNU 버거에 방문해주셔서 감사합니다.')
print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
print('□■ 메뉴')
print('□■ 1.햄버거 세트')
print('□■ 2.햄버거 단품')
print('□■ 3.사이드 메뉴')
print('□■ 4.음료')
print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')

while True:

    print('■■ 원하시는 메뉴의 번호를 입력해주세요.')
    menu_num = int(input('>> 번호:'))

    if 1 <= menu_num <= 4:
        break
    else:
        print('# Msg: 1~4의 번호만 입력해주세요)')

        # 사용자의값은 1~4

if menu_num == 1:
    print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
    print('□■ BURGER MENU')
    print('□■ 1.치즈버거:3,500원')
    print('□■ 2.불고기버거:3,000원')
    print('□■ 3.새우버거:2,500원')
    print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
    print('■■ 원하시는 메뉴의 번호를 입력해주세요.')

    while True:
        choice_num = int(input('>> 번호:'))
        if choice_num >= 1 and choice_num <= 3:
            mane_save['burger'] = burger_name[choice_num] # 사용자가 선택한 버거매뉴 기록
            price_save['burger'] = burger_price[choice_num]  # 사용자가 선택한 버거매뉴의 기록
            break
        else:
            print('#MSG:1~3의 번호만 입력해주세요')
    print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
    print('□■ SIDE MENU')
    print("□■ 1.프렌치프라으:1,500원")
    print('□■ 2.치킨너겟:2,000원')
    print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
    print('■■ 원하시는 메뉴의 번호를 입력해주세요.')

    while True:
        choice_num2 = int(input('>>번호:'))
        if choice_num2 >= 1 and choice_num2 <= 2:
            mane_save['side'] = side_name[choice_num2]
            price_save['side'] = side_price[choice_num2]
            break
        else:
            print('#MSG:1~2의 번호만 입력해주세요')
    print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
    print('□■ Drink MENU')
    print("□■ 1.코카콜라:1,000원")
    print('□■ 2.커피:1,200원')
    print('□■ 3.주스:1,500원')
    print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
    print('■■ 원하시는 메뉴의 번호를 입력해주세요.')
    while True:
        choice_num3 = int(input('>>번호:'))
        if choice_num3 >= 1 and choice_num3 <= 3:
            mane_save['drink'] = drink_name[choice_num3]
            price_save['dirnk'] = drink_price[choice_num3]
            break
        else:
            print('#MSG:1~3의 번호만 입력해주세요')

    print(mane_save)
    print(price_save)
