def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes(m, n):
    primes = [num for num in range(m, n+1) if is_prime(num)]
    return primes

def main():
    m = int(input())
    n = int(input())
    
    primes = find_primes(m, n)
    
    if not primes:
        print(-1)
    else:
        print(sum(primes))
        print(min(primes))

if __name__ == "__main__":
    main()