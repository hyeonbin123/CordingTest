while True:
    try:
        s = input().strip()
        print(s)
    except EOFError:
        # 입력이 끝나면 프로그램 종료
        break