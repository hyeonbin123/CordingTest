MOD = 1000000007

def power(base, exponent, modulus):
    result = 1
    while exponent > 0:
        if exponent & 1:
            result = (result * base) % modulus
        exponent = exponent >> 1
        base = (base * base) % modulus
    return result

def mod_inverse(n):
    return power(n, MOD - 2, MOD)

def add_fractions(fractions):
    numerator_sum = sum(fraction for fraction in fractions)
    return numerator_sum % MOD

def main():
    M = int(input())
    fractions = []
    
    for _ in range(M):
        N, S = map(int, input().split())
        numerator = (S * mod_inverse(N)) % MOD
        fractions.append(numerator)
    
    result = add_fractions(fractions)
    print(result)

if __name__ == "__main__":
    main()