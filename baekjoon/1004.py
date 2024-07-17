import math

def is_inside_circle(x, y, cx, cy, r):
    distance = math.sqrt((x - cx)**2 + (y - cy)**2)
    return distance < r

def solution(x1, y1, x2, y2, planet_systems):
    count = 0
    for cx, cy, r in planet_systems:
        start_inside = is_inside_circle(x1, y1, cx, cy, r)
        end_inside = is_inside_circle(x2, y2, cx, cy, r)
        if start_inside != end_inside:
            count += 1
    return count


def main():
    
    t=int(input())
    for _ in range(t):
        x1, y1, x2, y2 = map(int,input().strip().split())
        n=int(input())
        planet_systems = []
        for _ in range(n):
            cx, cy, r = map(int, input().split())
            planet_systems.append((cx, cy, r))
            
        # 최소 행성계 진입/이탈 횟수 계산   
        print(solution(x1, y1, x2, y2, planet_systems))
        
if __name__ == "__main__":
    main()

