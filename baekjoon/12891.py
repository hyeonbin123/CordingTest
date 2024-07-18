def solution(p,dna,a,c,g,t):
    count=0
    counts={'A':0,'C':0,'G':0,'T':0}
    for i in range(p):
        counts[dna[i]] += 1

    if counts['A'] >= a and counts['C'] >= c and counts['G'] >= g and counts['T'] >= t:
        count += 1
        
    for i in range(p, len(dna)):
        counts[dna[i-p]] -= 1
        counts[dna[i]] += 1
        
        if counts['A'] >= a and counts['C'] >= c and counts['G'] >= g and counts['T'] >= t:
            count += 1
    return count


def main():
    S, P = map(int, input().strip().split())
    DNA=input().strip()
    A,C,G,T=map(int,input().strip().split())
    print(solution(P,DNA,A,C,G,T))

if __name__ == "__main__":
    main()

