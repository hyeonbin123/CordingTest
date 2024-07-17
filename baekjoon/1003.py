def solution(n):
    # 기본 케이스: n이 0이거나 1일 때
    if n == 0:
        return 1, 0
    elif n == 1:
        return 0, 1
    
    # DP 테이블 초기화
    dp = [[0, 0] for _ in range(n+1)]
    dp[0] = [1, 0]  # fibonacci(0)은 0을 1번 출력
    dp[1] = [0, 1]  # fibonacci(1)은 1을 1번 출력
    
    # 상향식(bottom-up) DP
    for i in range(2, n+1):
        dp[i][0] = dp[i-1][0] + dp[i-2][0]  # 0 출력 횟수
        dp[i][1] = dp[i-1][1] + dp[i-2][1]  # 1 출력 횟수
    
    return dp[n][0], dp[n][1]


def main():
    n=int(input())
    for _ in range(n):
        zero, one = solution(int(input()))
        print(zero, one)

if __name__ == "__main__":
    main()

