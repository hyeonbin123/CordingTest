import sys

def set_operations():
    S = 0
    M = int(sys.stdin.readline())
    
    for _ in range(M):
        operation = sys.stdin.readline().strip().split()
        
        if operation[0] == 'add':
            S |= (1 << int(operation[1]))
        elif operation[0] == 'remove':
            S &= ~(1 << int(operation[1]))
        elif operation[0] == 'check':
            print(1 if S & (1 << int(operation[1])) else 0)
        elif operation[0] == 'toggle':
            S ^= (1 << int(operation[1]))
        elif operation[0] == 'all':
            S = (1 << 21) - 1
        elif operation[0] == 'empty':
            S = 0

set_operations()