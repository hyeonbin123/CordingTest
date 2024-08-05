def longest_bitonic_subsequence(N, A):
    lis = [1] * N
    for i in range(1, N):
        for j in range(i):
            if A[i] > A[j]:
                lis[i] = max(lis[i], lis[j] + 1)
    
    lds = [1] * N
    for i in range(N-2, -1, -1):
        for j in range(N-1, i, -1):
            if A[i] > A[j]:
                lds[i] = max(lds[i], lds[j] + 1)
    
    max_length = 0
    for i in range(N):
        max_length = max(max_length, lis[i] + lds[i] - 1)
    
    return max_length

def main():
    N = int(input())
    A = list(map(int, input().split()))
    
    result = longest_bitonic_subsequence(N, A)
    print(result)

if __name__ == "__main__":
    main()