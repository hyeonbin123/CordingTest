def main():

    n,m=map(int,input().split())
    names_set=sorted(set(input().strip() for _ in range(n))&set(input().strip() for _ in range(m)))
    print(len(names_set))
    for name in names_set:
        print(name)
if __name__ == "__main__":
    main()