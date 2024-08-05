def lexicographical_lcs(A, B):
    result = []
    i, j = 0, 0
    
    while i < len(A) and j < len(B):
        max_element = 0
        next_i, next_j = i, j
        
        for x in range(i, len(A)):
            for y in range(j, len(B)):
                if A[x] == B[y] and A[x] > max_element:
                    max_element = A[x]
                    next_i, next_j = x, y
        
        if max_element == 0:
            break
        
        result.append(max_element)
        i, j = next_i + 1, next_j + 1
    
    return result

N = int(input())
A = list(map(int, input().split()))

M = int(input())
B = list(map(int, input().split()))

result = lexicographical_lcs(A, B)

print(len(result))
if result:
    print(' '.join(map(str, result)))