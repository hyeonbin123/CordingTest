def min_coins(K, coins):
    count = 0
    
    for coin in coins:
        if K == 0: break
        if coin <= K:
            num_coins = K // coin
            count += num_coins
            K -= num_coins * coin
    
    return count

N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]

print(min_coins(K, sorted(coins,reverse=True)))