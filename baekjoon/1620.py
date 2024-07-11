import sys
def main():


    input = sys.stdin.readline
    N, M = map(int, input().split())

    # 포켓몬 이름을 저장할 리스트 (번호 -> 이름)
    pokemon_names = [""] * (N + 1)  # 0번 인덱스는 비워둠

    # 포켓몬 번호를 저장할 딕셔너리 (이름 -> 번호)
    pokemon_numbers = {}

    # N개의 포켓몬 정보 입력 받기
    for i in range(1, N + 1):
        name = input().strip()
        pokemon_names[i] = name
        pokemon_numbers[name] = i

    # M개의 문제 처리
    for _ in range(M):
        query = input().strip()
        if query.isdigit():
            print(pokemon_names[int(query)])
        else:
            print(pokemon_numbers[query])

if __name__ == "__main__":
    main()