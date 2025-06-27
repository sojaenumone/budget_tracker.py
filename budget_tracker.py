# budget_tracker.py
def display_menu():
    """메뉴를 출력합니다."""
    print("\n--- 간단 가계부 ---")
    print("1. 수입 추가")
    print("2. 지출 추가")
    print("3. 현재 잔액 확인")
    print("4. 기록된 거래 내역 보기")
    print("5. 종료")
    print("-------------------")

def main():
    balance = 0 # 초기 잔액
    transactions = [] # 거래 내역을 저장할 리스트 (날짜, 유형, 금액, 메모)

    print("--- 간단 가계부 프로그램 시작! ---")

    while True:
        display_menu()
        choice = input("원하는 작업을 선택하세요: ")

        if choice == '1': # 수입 추가
            try:
                amount = float(input("수입 금액을 입력하세요: "))
                if amount <= 0:
                    print("수입 금액은 0보다 커야 합니다.")
                    continue
                memo = input("수입에 대한 간단한 메모를 입력하세요 (선택 사항): ")
                balance += amount
                transactions.append({"type": "수입", "amount": amount, "memo": memo})
                print(f"{amount}원 수입이 기록되었습니다. 현재 잔액: {balance}원")
            except ValueError:
                print("유효한 숫자를 입력해주세요.")
        elif choice == '2': # 지출 추가
            try:
                amount = float(input("지출 금액을 입력하세요: "))
                if amount <= 0:
                    print("지출 금액은 0보다 커야 합니다.")
                    continue
                memo = input("지출에 대한 간단한 메모를 입력하세요 (선택 사항): ")
                balance -= amount
                transactions.append({"type": "지출", "amount": amount, "memo": memo})
                print(f"{amount}원 지출이 기록되었습니다. 현재 잔액: {balance}원")
            except ValueError:
                print("유효한 숫자를 입력해주세요.")
        elif choice == '3': # 현재 잔액 확인
            print(f"\n현재 잔액: {balance}원")
        elif choice == '4': # 기록된 거래 내역 보기
            if not transactions:
                print("\n기록된 거래 내역이 없습니다.")
            else:
                print("\n--- 거래 내역 ---")
                for i, t in enumerate(transactions):
                    print(f"{i+1}. [{t['type']}] 금액: {t['amount']}원, 메모: {t['memo']}")
                print("-------------------")
        elif choice == '5': # 종료
            print("가계부 프로그램을 종료합니다. 감사합니다!")
            break
        else:
            print("유효하지 않은 선택입니다. 다시 시도해주세요.")

if __name__ == "__main__":
    main()
