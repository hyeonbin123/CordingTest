import sys
import bisect
input = sys.stdin.readline

def lis_with_binary_search(seq):
    if not seq:
        return 0, []

    n = len(seq)
    dp = [seq[0]]
    pos = [0] * n

    for i in range(1, n):
        if seq[i] > dp[-1]:
            dp.append(seq[i])
            pos[i] = len(dp) - 1
        else:
            j = bisect.bisect_left(dp, seq[i])
            dp[j] = seq[i]
            pos[i] = j

    return len(dp)

n = int(input())
sequence = list(map(int, input().split()))

print(lis_with_binary_search(sequence))