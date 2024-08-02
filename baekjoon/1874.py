def generate_stack_sequence(sequence):
    stack = []
    result = []
    current = 1

    for num in sequence:
        while current <= num:
            stack.append(current)
            result.append('+')
            current += 1
        
        if stack[-1] == num:
            stack.pop()
            result.append('-')
        else:
            return "NO"
    
    return '\n'.join(result)

n = int(input())
sequence = [int(input()) for _ in range(n)]

print(generate_stack_sequence(sequence))