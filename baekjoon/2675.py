n=int(input().strip())
for i in range(n):
    r,s=map(str,input().strip().split())
    p=''
    for j in s:
        p+=j*int(r)
    print(p)