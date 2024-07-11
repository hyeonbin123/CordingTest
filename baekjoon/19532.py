def solve_system(a, b, c, d, e, f):
    # 행렬식 계산
    determinant = a * e - b * d
    
    # x와 y 계산
    x = (c * e - b * f) / determinant
    y = (a * f - c * d) / determinant
    
    return round(x), round(y)

def main():
    # 입력 받기
    a, b, c, d, e, f = map(int, input().split())
    
    # 연립방정식 풀기
    x, y = solve_system(a, b, c, d, e, f)
    
    print(x, y)

if __name__ == "__main__":
    main()