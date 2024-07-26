def sequence_sort(N, A):
    indexed_A = list(enumerate(A))
    indexed_A.sort(key=lambda x: (x[1], x[0]))
    P = [0] * N
    for new_index, (old_index, _) in enumerate(indexed_A):
        P[old_index] = new_index
    
    return P

N = int(input())
A = list(map(int, input().split()))

print(' '.join(map(str, sequence_sort(N, A))))