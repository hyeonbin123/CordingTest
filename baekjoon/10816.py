from collections import Counter
def main():

    # 상근이가 가지고 있는 카드의 개수와 카드 번호 입력 받기
    n = int(input())
    cards = Counter(map(int, input().split()))

    # 확인해야 할 숫자의 개수와 숫자들 입력 받기
    m = int(input())
    numbers = list(map(int, input().split()))

    # 각 숫자의 개수 계산 및 출력
    result = [cards[num] for num in numbers]
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()