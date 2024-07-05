
def solution(money):
    Q,money = divmod(money,25)
    D,money = divmod(money,10)
    N,money = divmod(money,5)
    P,money = divmod(money,1)

    answer = str(Q)+' '+str(D)+' '+str(N)+' '+str(P)
    return answer


n = int(input())
m = [int(input()) for i in range(n)]
for i in range(n):
    print(solution(m[i]))