def main():

    N, M = map(int, input().split())

    # 포켓몬 이름을 저장할 리스트
    pokemon_names = [""]  # 0번 인덱스는 비워둠

    # 포켓몬 이름을 저장할 집합
    pokemon_set = set()

    # N개의 포켓몬 정보 입력 받기
    for _ in range(N):
        name = input().strip()
        pokemon_names.append(name)
        pokemon_set.add(name)
    
    # M개의 문제 처리
    querys=[input().strip() for i in range(M)]
    print("*"*50)
    for query in querys:
        if query.isdigit():
            print(pokemon_names[int(query)])
        else:
            print(pokemon_names.index(query))

if __name__ == "__main__":
    main()