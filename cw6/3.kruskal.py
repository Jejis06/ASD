"""
3. Kruskal - napisac
"""

class FindUnion:
    def __init__(self, size:int):
        self.parent: list[int] = list(range(size))
        self.rank: list[int] = [0] * size

    def find(self, a:int) -> int:
        if a != self.parent[a]:
            self.parent[a] = self.find(self.parent[a])
        return self.parent[a]

    def union(self, a:int, b:int):
        a = self.find(a)
        b = self.find(b)

        if a == b: return
        if self.rank[a] > self.rank[b]:
            self.parent[b] = a
        else:
            self.parent[a] = b
            if self.rank[a] == self.rank[b]:
                self.rank[b] += 1

def mst_kruskal(edges:list[tuple[int,int,int]], n:int):

    edges.sort(key = lambda x: x[2])
    mst:list[tuple[int,int]] = []
    fu = FindUnion(n)
    for u, v, _ in edges:
        if fu.find(u) != fu.find(v):
            fu.union(u, v)
            mst.append((u, v))
    return mst



