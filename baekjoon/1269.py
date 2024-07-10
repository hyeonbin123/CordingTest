def main():

    n,m=map(int,input().split())
    A = set(input().strip().split())
    B = set(input().strip().split())
    print(len(A-B)+len(B-A))
if __name__ == "__main__":
    main()