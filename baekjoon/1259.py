while True:
    su=input().strip()
    if su=='0':break
    print('yes' if su==su[::-1] else 'no')
        