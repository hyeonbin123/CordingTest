MAX_N = 11
dp = [0] * MAX_N
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, MAX_N):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

T = int(input())

for _ in range(T):
    n = int(input())
    print(dp[n])