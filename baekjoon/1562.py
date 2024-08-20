def count_stair_numbers(N):
    MOD = 1000000000
    
    dp = [[[0 for _ in range(1024)] for _ in range(10)] for _ in range(N+1)]
    
    for i in range(1, 10):
        dp[1][i][1 << i] = 1
    
    for i in range(2, N+1):
        for j in range(10):
            for k in range(1024):
                if j > 0:
                    dp[i][j][k | (1 << j)] = (dp[i][j][k | (1 << j)] + dp[i-1][j-1][k]) % MOD
                if j < 9:
                    dp[i][j][k | (1 << j)] = (dp[i][j][k | (1 << j)] + dp[i-1][j+1][k]) % MOD
    
    result = sum(dp[N][j][1023] for j in range(10)) % MOD
    return result

N = int(input())

print(count_stair_numbers(N))