h,m=map(int,input().strip().split())
print(f"{h} {m-45}" if m>=45 else f"{h-1} {m+15}" if h!=0 else f"{23} {m+15}")