import sys
input = sys.stdin.readline
t=int(input().strip())
for i in range(t):
    a,b=map(int,input().strip().split())
    print(a+b)