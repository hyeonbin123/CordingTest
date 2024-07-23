import math
t=int(input())
for _ in range(t):
    h, w, n = map(int,input().strip().split())
    print('{}{:0>2}'.format(n%h if n%h != 0 else h,math.ceil(n/h)))