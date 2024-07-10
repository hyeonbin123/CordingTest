def main():

    # 상근이가 가지고 있는 카드의 개수와 카드 번호 입력 받기
    n = int(input())
    cards = set(map(int, input().split()))

    # 확인해야 할 숫자의 개수와 숫자들 입력 받기
    m = int(input())
    numbers = list(map(int, input().split()))

    # 결과 출력
    print(' '.join(['1' if num in cards else '0' for num in numbers]))

if __name__ == "__main__":
    main()