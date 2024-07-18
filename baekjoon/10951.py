while True:
    try:
        # 두 정수를 입력받음
        a, b = map(int, input().split())
        
        # 두 정수의 합을 출력
        print(a + b)
    except EOFError:
        # 입력이 끝나면 프로그램 종료
        break