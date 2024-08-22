import sys

input = sys.stdin.readline
print = sys.stdout.write

class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.weight = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            root = x
            weight = 0
            while self.parent[root] != root:
                weight += self.weight[root]
                root = self.parent[root]
            
            while x != root:
                old_parent = self.parent[x]
                old_weight = self.weight[x]
                self.parent[x] = root
                self.weight[x] = weight
                weight -= old_weight
                x = old_parent
        
        return self.parent[x]

    def union(self, x, y, w):
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            self.parent[root_y] = root_x
            self.weight[root_y] = self.weight[x] - self.weight[y] + w

    def diff(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            return None
        return self.weight[y] - self.weight[x]

def solve():
    while True:
        n, m = map(int, input().split())
        if n == 0 and m == 0:
            return

        ds = DisjointSet(n + 1)
        
        for _ in range(m):
            query = input().split()
            if query[0] == '!':
                a, b, w = map(int, query[1:])
                ds.union(a, b, w)
            else:
                a, b = map(int, query[1:])
                result = ds.diff(a, b)
                if result is None:
                    print("UNKNOWN\n")
                else:
                    print(f"{result}\n")

if __name__ == "__main__":
    solve()