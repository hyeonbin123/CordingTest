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

    lis = []
    last = len(dp) - 1
    for i in range(n - 1, -1, -1):
        if pos[i] == last:
            lis.append(seq[i])
            last -= 1
        if last < 0:
            break

    return len(dp), lis[::-1]

n = int(input())
sequence = list(map(int, input().split()))

length, subsequence = lis_with_binary_search(sequence)

print(length)
print(*subsequence)