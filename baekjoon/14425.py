def main():
    n,m=map(int,input().split())
    search_set = set(input().strip() for _ in range(n))
    count = sum(1 for _ in range(m) if input().strip() in search_set)

    print(count)


if __name__ == "__main__":
    main()