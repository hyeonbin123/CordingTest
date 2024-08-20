import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

class TwoSAT:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(2*n+1)]
        self.reversed_graph = [[] for _ in range(2*n+1)]
        self.visited = [False] * (2*n+1)
        self.stack = []
        self.scc_id = [0] * (2*n+1)
        self.scc_counter = 0
        self.result = [False] * (n+1)

    def add_clause(self, i, j):
        self.graph[-i].append(j)
        self.graph[-j].append(i)
        self.reversed_graph[j].append(-i)
        self.reversed_graph[i].append(-j)

    def dfs(self, v, graph, scc=None):
        self.visited[v] = True
        for neighbor in graph[v]:
            if not self.visited[neighbor]:
                self.dfs(neighbor, graph, scc)
        if scc is not None:
            scc.append(v)
        else:
            self.stack.append(v)

    def kosaraju(self):
        # 첫 번째 DFS
        for i in range(1, 2*self.n+1):
            if not self.visited[i]:
                self.dfs(i, self.graph)

        self.visited = [False] * (2*self.n+1)

        # 두 번째 DFS
        while self.stack:
            node = self.stack.pop()
            if not self.visited[node]:
                scc = []
                self.dfs(node, self.reversed_graph, scc)
                self.scc_counter += 1
                for v in scc:
                    self.scc_id[v] = self.scc_counter
                    if self.scc_id[v] == self.scc_id[-v]:
                        return False  # 모순 발견

        # 변수 할당
        for i in range(1, self.n+1):
            if self.scc_id[i] > self.scc_id[-i]:
                self.result[i] = True
            else:
                self.result[i] = False

        return True

    def solve(self):
        return self.kosaraju(), self.result[1:]

def main():
    n, m = map(int, input().split())
    two_sat = TwoSAT(n)

    for _ in range(m):
        i, j = map(int, input().split())
        two_sat.add_clause(i, j)

    solvable, assignment = two_sat.solve()
    print(1 if solvable else 0)
    if solvable:
        print(' '.join('1' if x else '0' for x in assignment))

if __name__ == "__main__":
    main()