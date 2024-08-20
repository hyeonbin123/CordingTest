def min_palindrome_cut(s):
    n = len(s)
    
    # is_palindrome[i][j]: s[i:j+1]이 팰린드롬인지 여부
    is_palindrome = [[False] * n for _ in range(n)]
    
    # 길이 1인 부분 문자열은 모두 팰린드롬
    for i in range(n):
        is_palindrome[i][i] = True
    
    # 길이 2 이상인 부분 문자열에 대해 팰린드롬 여부 계산
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if length == 2:
                is_palindrome[i][j] = (s[i] == s[j])
            else:
                is_palindrome[i][j] = (s[i] == s[j] and is_palindrome[i+1][j-1])
    
    # dp[i]: s[0:i+1]의 최소 팰린드롬 분할 횟수
    dp = [float('inf')] * n
    
    for i in range(n):
        if is_palindrome[0][i]:
            dp[i] = 0
        else:
            for j in range(i):
                if is_palindrome[j+1][i]:
                    dp[i] = min(dp[i], dp[j] + 1)
    
    return dp[n-1] + 1  # 분할 횟수는 (최소 컷 수 + 1)

# 입력 받기
s = input().strip()

# 결과 출력
print(min_palindrome_cut(s))