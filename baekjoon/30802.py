n=int(input().strip())
size=list(map(int,input().strip().split()))
t,p=map(int,input().strip().split())
print(sum([i//t if i%t==0 else i//t+1 for i in size]))
print(n//p,n%p)