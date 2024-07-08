import re

def solution(dartResult):
    scores = []
    pattern = re.compile(r'(\d+)([SDT])([*#]?)')
    power = {'S': 1, 'D': 2, 'T': 3}
    
    for score, area, option in pattern.findall(dartResult):
        current_score = int(score) ** power[area]
        if option == '*':
            current_score *= 2
            if scores:
                scores[-1] *= 2
        elif option == '#':
            current_score *= -1
        
        scores.append(current_score)
    return sum(scores)



print(solution("1S2D*3T"))
print(solution("1D2S#10S"))
print(solution("1D2S0T"))
print(solution("1S*2T*3S"))
print(solution("1D#2S*3S"))
print(solution("1T2D3D#"))
print(solution("1D2S3T*"))