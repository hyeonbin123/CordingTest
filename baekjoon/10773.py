
def main():
    k=int(input())
    solution=[]
    for _ in range(k):
        n=int(input())
        if n != 0:
            solution.append(n)
        else:
            solution.pop()
    print(sum(solution))
if __name__ == "__main__":
    main()

