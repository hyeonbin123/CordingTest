n=input().strip()[:-2]
f=int(input().strip())
for i in ['{:0>2}'.format(i) for i in range(100)]:
    if int(n+i) % f == 0:
        print(i)
        break