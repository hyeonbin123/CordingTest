def plus_cycle(n):
    check=n
    count=1
    while True:
        sum_digits = (n//10)+(n%10)
        n=(n%10)*10+(sum_digits%10)
        if n==check: return count
        else: count+=1

n=int(input())
print(plus_cycle(n))