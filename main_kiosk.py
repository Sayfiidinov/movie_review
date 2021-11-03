#########################################################################
# 키오스크 프로그램 Main 저석부(console programming)
# 개발자 :촬철웅
# 2021.10.31
##############################################################################

# view => Console
# controller =>Python
# Model(데이터베이으스)=>LIST,DICT

import choice_menu

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
########################################
### 메인 메뉴 선택 ##
#######################################

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
########################################
###2.세부메뉴 선택##
#######################################

if menu_num == 1:
    # 햄버거 세부 메뉴 선택하는 함수
    choice_num = choice_menu.choice_burger()
    mane_save['burger'] = burger_name[choice_num]  # 사용자가 선택한 버거매뉴 기록
    price_save['burger'] = burger_price[choice_num]  # 사용자가 선택한 버거매뉴의 기록
    #사으드 세부 메뉴 선택하는 함수
    choice_num2 = choice_menu.choice_saide()
    mane_save['side'] = side_name[choice_num2]
    price_save['side'] = side_price[choice_num2]
    # 음료 단품 세부 메뉴 선택
    choice_num3 = choice_menu.choice_drink()
    mane_save['drink'] = drink_name[choice_num3]
    price_save['dirnk'] = drink_price[choice_num3]
    # 메뉴
elif menu_num == 2:
    choice_num = choice_menu.choice_burger()
    mane_save['burger'] = burger_name[choice_num]  # 사용자가 선택한 버거매뉴 기록
    price_save['burger'] = burger_price[choice_num]  # 사용자가 선택한 버거매뉴의 기록
elif menu_num == 3:
    # 사으드 세부 메뉴 선택하는 함수
    choice_num2 = choice_menu.choice_saide()
    mane_save['side'] = side_name[choice_num2]
    price_save['side'] = side_price[choice_num2]


elif menu_num == 4:
    choice_num3 = choice_menu.choice_drink()
    mane_save['drink'] = drink_name[choice_num3]
    price_save['dirnk'] = drink_price[choice_num3]


print(mane_save)
print(price_save)

####################################################
## 3.주문 메뉴와 금액 선택
####################################################

# Total 주문 김액 계산

total_price = 0

for price in price_save.values():
    total_price += price

print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
print('■■ 고객님이 주문하신 메뉴는')
for i , menu in enumerate(  mane_save.values()):
    print('■■{}. {}'.format(i+1,menu))
print('■■ 으로 총 주문금액은 {} 원 입니다' .format(total_price))
print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
print('■■ 이용해주셔서 감사합니다 :)')
print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')












