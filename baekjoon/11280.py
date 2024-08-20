import sys
sys.setrecursionlimit(10**6)  # 재귀 깊이 제한 증가
input = sys.stdin.readline

class TwoSAT:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(2*n+1)]
        self.reversed_graph = [[] for _ in range(2*n+1)]
        self.visited = [False] * (2*n+1)
        self.stack = []
        self.scc = []
        self.scc_found = False

    def add_clause(self, i, j):
        self.graph[-i].append(j)
        self.graph[-j].append(i)
        self.reversed_graph[j].append(-i)
        self.reversed_graph[i].append(-j)

    def dfs(self, v, graph, is_reverse=False):
        self.visited[v] = True
        for neighbor in graph[v]:
            if not self.visited[neighbor]:
                self.dfs(neighbor, graph, is_reverse)
        if not is_reverse:
            self.stack.append(v)
        else:
            self.scc.append(v)

    def kosaraju(self):
        for i in range(1, 2*self.n+1):
            if not self.visited[i]:
                self.dfs(i, self.graph)

        self.visited = [False] * (2*self.n+1)

        while self.stack and not self.scc_found:
            node = self.stack.pop()
            if not self.visited[node]:
                self.scc = []
                self.dfs(node, self.reversed_graph, True)
                if any(-v in self.scc for v in self.scc):
                    return False
                self.scc = []

        return True

    def solve(self):
        return self.kosaraju()

def main():
    n, m = map(int, input().split())
    two_sat = TwoSAT(n)

    for _ in range(m):
        i, j = map(int, input().split())
        two_sat.add_clause(i, j)

    result = two_sat.solve()
    print(1 if result else 0)

if __name__ == "__main__":
    main()