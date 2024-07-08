def solution(first, second):
    if second % first == 0:
        return "factor"
    elif first % second == 0:
        return "multiple"
    else:
        return "neither"

while True:
    first,second=map(int,input().split())
    if first==0 and second==0: break
    print(solution(first,second))