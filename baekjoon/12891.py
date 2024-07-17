def solution(p,dna,a,c,g,t):
    count=0
    for i in range(len(dna)-p+1):
        pwd = dna[i:i+p]
        if pwd.count('A')>=a and pwd.count('C')>=c and pwd.count('G')>=g and pwd.count('T')>=t:
            count+=1
    return count


def main():
    S, P = map(int, input().strip().split())
    DNA=input().strip()
    A,C,G,T=map(int,input().strip().split())
    print(solution(P,DNA,A,C,G,T))

if __name__ == "__main__":
    main()

