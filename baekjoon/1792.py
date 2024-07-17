def solution(a,b,d):
    count = 0
    for i in range(1, a//d + 1):
        for j in range(1, b//d + 1):
            if i == 1 or j == 1:
                count += 1
    return count


def main():
    n=int(input())
    for _ in range(n):
        a,b,d=map(int,input().strip().split())
        print(solution(a,b,d))

if __name__ == "__main__":
    main()

