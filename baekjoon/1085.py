x,y,w,h=map(int,input().strip().split())
print(min(x,y,w-x,h-y))