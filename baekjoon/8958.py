t=int(input().strip())
for _ in range(t):
    ox=list(input().strip().replace('O','1').replace('X','0'))
    for i in range(1,len(ox)):
        if ox[i]=='1' and ox[i-1] != '0':
            ox[i]=str(int(ox[i-1])+1)
    print(sum(map(int,ox)))