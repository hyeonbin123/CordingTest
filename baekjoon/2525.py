h,m=map(int,input().strip().split())
add_m=int(input().strip())
m+=add_m%60
h+=add_m//60+m//60
m%=60
h%=24
print(f'{h} {m}')
