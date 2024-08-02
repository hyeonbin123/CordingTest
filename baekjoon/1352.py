def solve(n):
    stack = [(1, 0, [])]
    while stack:
        i, sum_val, ans = stack.pop()
        
        if sum_val == n:
            result = [''] * n
            remain = []
            for idx, val in enumerate(ans):
                char = chr(ord('A') + idx)
                result[val - 1] = char
                remain.extend([char] * (val - 1))
            
            for i in range(n):
                if not result[i]:
                    result[i] = remain.pop(0)
            
            return ''.join(result)
        
        if sum_val > n or i > n:
            continue
        
        for j in range(n - sum_val, i - 1, -1):
            if j - 1 <= sum_val:
                new_ans = ans + [j]
                stack.append((j + 1, sum_val + j, new_ans))
        
        stack.append((i + 1, sum_val, ans))
    
    return -1

if __name__ == "__main__":
    n = int(input())
    print(solve(n))