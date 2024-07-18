total_cash=int(input().strip())
n=int(input().strip())
total=0
for i in range(n):
    cash,su=map(int,input().strip().split())
    total+=cash*su
print('Yes' if total_cash == total else 'No')