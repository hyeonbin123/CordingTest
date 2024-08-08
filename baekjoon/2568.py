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
            lis.append(i)
            last -= 1
        if last < 0:
            break

    return n - len(dp), sorted(set(range(n)) - set(lis))

n = int(input())
wires = [tuple(map(int, input().split())) for _ in range(n)]
wires.sort(key=lambda x: x[0])

sequence = [wire[1] for wire in wires]

remove_count, to_remove = lis_with_binary_search(sequence)

print(remove_count)
for idx in to_remove:
    print(wires[idx][0])