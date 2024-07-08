def star_score(star,answer):
    if star:
        if len(answer)>=2:
            if star =="*":
                answer[-1],answer[-2]=answer[-1]*2,answer[-2]*2
            if star =="#":
                answer[-1]=answer[-1]*-1
        else:
            if star =="*":
                answer[-1]=answer[-1]*2
            if star =="#":
                answer[-1]=answer[-1]*-1
    return answer

def solution(dartResult):
    answer=[]
    while dartResult:
        star=None
        score,square,dartResult = dartResult[0],dartResult[1],dartResult[2:]
        if square =='0':
            score,square,dartResult = score+'0',dartResult[0],dartResult[1:]
        if dartResult:
            if dartResult[0]=="*" or dartResult[0]=="#":
                star,dartResult = dartResult[0],dartResult[1:]
        if square=="S":
            answer.append(int(score)**1)
            answer = star_score(star,answer)
        if square=="D":
            answer.append(int(score)**2)
            answer = star_score(star,answer)
        if square=="T":
            answer.append(int(score)**3)
            answer = star_score(star,answer)
    return sum(answer)



print(solution("1S2D*3T"))
print(solution("1D2S#10S"))
print(solution("1D2S0T"))
print(solution("1S*2T*3S"))
print(solution("1D#2S*3S"))
print(solution("1T2D3D#"))
print(solution("1D2S3T*"))