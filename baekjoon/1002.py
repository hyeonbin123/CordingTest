import math

def solution(x1, y1, r1, x2, y2, r2):
    # 두 원의 중심 사이의 거리 계산
    d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
    # 두 원이 완전히 겹치는 경우
    if d == 0 and r1 == r2:
        return -1
    
    # 한 원이 다른 원을 완전히 포함하는 경우
    if d < abs(r1 - r2):
        return 0
    
    # 두 원이 외접하거나 내접하는 경우
    if d == r1 + r2 or d == abs(r1 - r2):
        return 1
    
    # 두 원이 두 점에서 만나는 경우
    if abs(r1 - r2) < d < r1 + r2:
        return 2
    
    # 그 외의 경우 (두 원이 만나지 않음)
    return 0


def main():
    n = int(input())
    for _ in range(n):
        x1, y1, r1, x2, y2, r2 = map(int,input().strip().split())
        print(solution(x1, y1, r1, x2, y2, r2))

if __name__ == "__main__":
    main()

