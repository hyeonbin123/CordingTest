def ccw(x1, y1, x2, y2, x3, y3):
    return (x2-x1)*(y3-y1) - (y2-y1)*(x3-x1)

def intersect(x1, y1, x2, y2, x3, y3, x4, y4):
    # CCW 값 계산
    ccw1 = ccw(x1, y1, x2, y2, x3, y3)
    ccw2 = ccw(x1, y1, x2, y2, x4, y4)
    ccw3 = ccw(x3, y3, x4, y4, x1, y1)
    ccw4 = ccw(x3, y3, x4, y4, x2, y2)
    
    # 두 선분이 일직선 상에 있는 경우
    if ccw1 * ccw2 == 0 and ccw3 * ccw4 == 0:
        if min(x1, x2) <= max(x3, x4) and min(x3, x4) <= max(x1, x2) and \
           min(y1, y2) <= max(y3, y4) and min(y3, y4) <= max(y1, y2):
            return 1
        else:
            return 0
    
    # 두 선분이 교차하는 경우
    if ccw1 * ccw2 <= 0 and ccw3 * ccw4 <= 0:
        return 1
    
    return 0

# 입력 받기
x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

# 결과 출력
print(intersect(x1, y1, x2, y2, x3, y3, x4, y4))