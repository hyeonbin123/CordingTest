def calculate_decomposition_sum(n):
    return n + sum(int(digit) for digit in str(n))

def find_smallest_constructor(N):
    for i in range(1, N):
        if calculate_decomposition_sum(i) == N:
            return i
    return 0

def main():
    N = int(input())
    result = find_smallest_constructor(N)
    print(result)

if __name__ == "__main__":
    main()