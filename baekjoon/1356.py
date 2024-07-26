def is_eugene_number(digits):
    
    for i in range(1, len(digits)):
        
        left_product = 1
        for digit in digits[:i]:
            left_product *= int(digit)
        
        right_product = 1
        for digit in digits[i:]:
            right_product *= int(digit)
        
        if left_product == right_product:
            return True
    
    return False

def main():
    n = input().strip()
    print("YES" if is_eugene_number(n) else "NO")

if __name__ == "__main__":
    main()