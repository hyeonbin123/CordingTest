def convert_to_decimal(N, B):
    # N: B진법으로 표현된 수 (문자열)
    # B: 진법 (정수)
    
    # 36진법에서 사용되는 문자와 그에 해당하는 값을 딕셔너리로 정의합니다.
    digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digit_map = {digit: index for index, digit in enumerate(digits)}
    
    # 10진법으로 변환한 값을 저장할 변수
    decimal_value = 0
    
    # N의 각 자리를 순회하면서 10진법으로 변환합니다.
    for i, digit in enumerate(reversed(N)):
        decimal_value += digit_map[digit] * (B ** i)
    
    return decimal_value

# 입력을 받습니다.
N, B = input().split()
B = int(B)

# 결과를 출력합니다.
print(convert_to_decimal(N, B))
