while True:
    n=input().strip()
    if n=='0': break
    total=len(n)+1
    for i in n:
        if i=='0': total+=4
        elif i=='1': total+=2
        else: total+=3
    print(total)