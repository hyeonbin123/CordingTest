def min_sugar_bags(n):
    for i in range(n//5,-1,-1):
        remainder = n - (5 * i)
        if remainder % 3 == 0:
            return i + (remainder // 3)
    return -1

def main():
    n = int(input())
    result = min_sugar_bags(n)
    print(result)

if __name__ == "__main__":
    main()