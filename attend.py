# attend.py - 스터디 출석부 프로그램
# 외부 라이브러리 없이 파이썬 기본 기능만 사용합니다.

# 출석 기록을 담아둘 보관함 (리스트)
records = []


def add_record():
    """출석 한 건을 추가하는 기능"""
    date = input("날짜를 입력하세요 (예: 2025-07-10): ").strip()
    name = input("이름을 입력하세요: ").strip()

    # 빈 칸 입력 방지
    if not date or not name:
        print("⚠️  날짜와 이름을 모두 입력해야 합니다.\n")
        return

    # 보관함에 딕셔너리로 한 줄 추가
    records.append({"date": date, "name": name})
    print(f"✅  {date} / {name} 출석 완료!\n")


def show_records():
    """지금까지 쌓인 출석 목록을 보여주는 기능"""
    if not records:
        print("아직 출석 기록이 없습니다.\n")
        return

    print("\n📋  출석 목록")
    print("-" * 30)
    for i, r in enumerate(records, start=1):
        print(f"{i}. {r['date']}  |  {r['name']}")
    print("-" * 30)
    print(f"총 {len(records)}건\n")


def main():
    """메뉴를 보여주고 사용자의 선택을 받는 본체"""
    print("=== 스터디 출석부 ===\n")

    while True:
        print("1. 출석 추가")
        print("2. 목록 보기")
        print("3. 종료")
        choice = input("번호를 선택하세요: ").strip()

        if choice == "1":
            add_record()
        elif choice == "2":
            show_records()
        elif choice == "3":
            print("프로그램을 종료합니다. 👋")
            break
        else:
            print("⚠️  1, 2, 3 중에서 선택해 주세요.\n")


if __name__ == "__main__":
    main()
