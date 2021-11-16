# "cafe.txt"파일의 값을 초기값으로 받아 재고를 관리하는 class
class Menu:
    orderList = {  # 1메뉴번호, 2이름, 3가격, 4재고 /dictionary
        1: {
            'menuNo': 0,
            'menuName': 'name',
            'menuCost': 0,
            'menuStock': 0
        },
        2: {
            'menuNo': 0,
            'menuName': 'name',
            'menuCost': 0,
            'menuStock': 0
        },
        3: {
            'menuNo': 0,
            'menuName': 'name',
            'menuCost': 0,
            'menuStock': 0
        },
        4: {
            'menuNo': 0,
            'menuName': 'name',
            'menuCost': 0,
            'menuStock': 0
        },
        5: {
            'menuNo': 0,
            'menuName': 'name',
            'menuCost': 0,
            'menuStock': 0
        }

    }
    total = int(0)

    # cafe.txt를 입력받아 orderList에 주어진 값 추가하는 함수
    def addMenu(self, f):
        lines = f.readlines()
        i = 1
        for line in lines:
            result = line.strip().split(", ")
            Menu.orderList[i]['menuNo'] = int(result[0])
            Menu.orderList[i]['menuName'] = str(result[1])
            Menu.orderList[i]['menuCost'] = int(result[2])
            Menu.orderList[i]['menuStock'] = int(result[3])
            i += 1
        f.close()

    # 메뉴 이름과 가격 현재 재고 수량을 출력
    def printMenu(self):
        print()
        print("=" * 40)
        for i in Menu.orderList:
            print(str(Menu.orderList[i]['menuNo']) + ". " + Menu.orderList[i]['menuName'] +
                  "\t 금액: " + str(Menu.orderList[i]['menuCost']) + "원" +
                  "\t 재고: " + str(Menu.orderList[i]['menuStock']))

        print("end를 입력하시면 주문서로 돌아갑니다.")
        print("=" * 40)


# 커피 메뉴를 주문하는 Class
class Order:
    orderResult = [0, 0, 0, 0, 0]  # 전체 주문 수량을 저장하는 변수/  list

    # 커피를 주문하는 함수
    def orderMenu(self, menuNum):  # 메뉴 번호
        tempResult = [0, 0, 0, 0, 0]  # 이번 주문 수량을 저장하는 변수

        count = 0
        while True:
            Menu.printMenu(self)

            if count == 0:
                print("주문할 메뉴 번호를 입력해주세요")
            else:
                print("추가로 주문할 메뉴 번호를 입력해주세요")

            coffee = input("input: ")

            if coffee == "end":
                total_order = 0
                total_cost = 0
                i = 0
                while i < 5:
                    total_order += tempResult[i]
                    total_cost += int(tempResult[i]) * int(Menu.orderList[i + 1]['menuCost'])
                    i += 1

                print("\n주문내역")
                print("총 주문 수량: " + str(total_order) + "개, " +
                      "총 주문 금액: " + str(total_cost) + "원")
                print("주문서로 돌아갑니다\n")
                break

            while True:
                count += 1

                if 0 < int(coffee) < 6:
                    print("선택한 메뉴의 수량을 입력해주세요")
                    quantity = int(input("input: "))

                    if Menu.orderList[int(coffee)]['menuStock'] == 0:
                        print("품절되었습니다 다른 메뉴를 선택해주세요.")
                        break

                    if Menu.orderList[int(coffee)]['menuStock'] < quantity:
                        print("수량이 부족합니다 다른 수량을 선택해주세요.")
                        Menu.printMenu(self)
                        continue
                    else:
                        Order.orderResult[int(coffee) - 1] += quantity
                        tempResult[int(coffee) - 1] += quantity
                        Menu.orderList[int(coffee)]['menuStock'] -= quantity
                        # print("주문갯수: " + str(Order.orderResult))
                        # print("재고갯수: " + str(Menu.orderList[int(coffee)]['menuStock']))
                        break
                else:
                    print("존재하지 않는 메뉴입니다")
                    break


# 커피 재고를 입고 및 관리하는 Class
class Manage:
    ManageResult = [0, 0, 0, 0, 0]  # 입고 수량을 저장하는 변수 / list

    # 커피 재고를 입고하는 함수
    def Management(self, menuNum):  # 커피 재고를 입고하는 함수
        count = 0
        while True:
            Menu.printMenu(self)

            if count == 0:
                print("입고할 메뉴 번호를 입력해주세요")
            else:
                print("추가로 입고할 메뉴 번호를 입력해주세요")

            x = input("input: ")

            if x == "end":
                total_order = 0
                total_cost = 0
                i = 0
                while i < 5:
                    total_order += Manage.ManageResult[i]
                    total_cost += int(Manage.ManageResult[i]) * int(Menu.orderList[i + 1]['menuCost'])
                    i += 1

                print("\n주문내역")
                print("총 주문 수량: " + str(total_order) + "개, " +
                      "총 주문 금액: " + str(total_cost) + "원")
                print("주문서로 돌아갑니다\n")
                break

            while True:
                count += 1

                if 0 < int(x) < 6:
                    print("선택한 메뉴의 수량을 입력해주세요")
                    quantity = int(input("input: "))

                    Manage.ManageResult[int(x) - 1] += quantity
                    Menu.orderList[int(x)]['menuStock'] += quantity
                    break

                else:
                    print("존재하지 않는 메뉴입니다")
                    break





    def toSale(self):  # 총 매출을 출력하는 함수
        income = 0
        i = 0
        while i < 5:
            income += int(Order.orderResult[i]) * int(Menu.orderList[i + 1]['menuCost'])
            i += 1
        print("총 매출은 " + str(income) + "입니다.\n")


# ----------------------------------------------------------------

menu = Menu()
order = Order()
manage = Manage()

file = open("cafe.txt", "r", encoding="utf-8")
menu.addMenu(file)

while True:
    print("================")
    print("      주문서     ")
    print("================")
    print("1. 커피 주문하기")
    print("2. 커피 매출 확인")
    print("3. 커피 입고 하기")
    print("4. 종료하기")
    print("================" + "\n")

    print("원하시는 주문번호를 입력해주세요")
    o = int(input("input: "))

    if o == 1:  # 커피 주문하기
        order.orderMenu(o)

    elif o == 2:  # 커피 매출 확인
        manage.toSale()

    elif o == 3:  # 커피 입고하기
        manage.Management(o)
    elif o == 4:  # 종료하기
        exit()
