def convert_from_decimal(N, B):
    # N: 10진법으로 표현된 수 (정수)
    # B: 변환할 진법 (정수)
    
    # 36진법에서 사용되는 문자와 그에 해당하는 값을 정의합니다.
    digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    # 변환된 결과를 저장할 리스트
    result = []
    
    # N이 0이 될 때까지 나누기와 나머지 연산을 반복합니다.
    while N > 0:
        remainder = N % B
        result.append(digits[remainder])
        N //= B
    
    # 리스트에 저장된 결과를 역순으로 결합하여 문자열로 만듭니다.
    result.reverse()
    return ''.join(result)

# 입력을 받습니다.
N, B = map(int, input().split())

# 결과를 출력합니다.
print(convert_from_decimal(N, B))
