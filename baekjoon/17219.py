import sys
input = sys.stdin.readline

n,m=map(int,input().split())
save_pwd={}
for _ in range(n):
    a,b=input().split()
    save_pwd[a]=b
for _ in range(m):
    a = input().strip()
    print(save_pwd[a])