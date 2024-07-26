def solve():
    T = int(input())
    for _ in range(T):
        k = int(input())
        n = int(input())
        
        # DP 테이블 초기화
        dp = [[0 for _ in range(n+1)] for _ in range(k+1)]
        
        # 0층 초기화
        for i in range(1, n+1):
            dp[0][i] = i
        
        # DP 테이블 채우기
        for floor in range(1, k+1):
            for room in range(1, n+1):
                dp[floor][room] = dp[floor][room-1] + dp[floor-1][room]
        
        print(dp[k][n])

if __name__ == "__main__":
    solve()