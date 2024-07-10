def main():

    # 로그 기록 수 입력
    n = int(input())

    # 현재 회사에 있는 사람들을 추적하기 위한 집합
    in_company = set()

    # 로그 처리
    for _ in range(n):
        name, action = input().split()
        if action == "enter":
            in_company.add(name)
        elif action == "leave":
            in_company.remove(name)

    # 결과를 사전 순의 역순으로 정렬하여 출력
    for name in sorted(in_company, reverse=True):
        print(name)

if __name__ == "__main__":
    main()