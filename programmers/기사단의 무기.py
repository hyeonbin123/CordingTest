def solution(number, limit, power):
    factors=[]
    for i in range(1,number+1):
        temp=[]
        for j in range(1,int(i**0.5)+1):
            if i%j==0:
                temp.append(j)
                if((j**2)!=i):
                    temp.append(i//j)
        factors.append(len(temp) if len(temp)<=limit else power)
    return sum(factors)


print(solution(5,3,2))
print(solution(10,3,2))