def solution(N):
    factor = [i for i in range(1,N) if N%i==0]
    return factor


while True:
    n=int(input())
    if n == -1: break
    result = solution(n)
    if sum(result) == n:
        print(f'{n} = {" + ".join(map(str, result))}')
    else:
        print(f"{n} is NOT perfect.")