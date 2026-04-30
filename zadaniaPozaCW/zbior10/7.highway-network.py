"""
Zadanie 7. (autostrady) W pewnym państwie, w którym znajduje się 
N miast, postanowiono połączyć wszystkie miasta siecią autostrad, 
tak aby możliwe było dotarcie autostradą do każdego miasta. 
Ponieważ kontynent, na którym leży państwo jest płaski położenie 
każdego z miast opisują dwie liczby x, y, a odległość w linii 
prostej pomiędzy miastami liczona w kilometrach wyraża się wzorem 
len=sqrt{(x_{1}-x_{2})^{2}+(y_{1}-y_{2})^{2}}. Z uwagi na oszczędności 
materiałów autostrada łączy dwa miasta w linii prostej. 
Ponieważ zbliżają się wybory prezydenta, wszystkie autostrady 
zaczęto budować równocześnie i jako cel postanowiono zminimalizować 
czas pomiędzy otwarciem pierwszej i ostatniej autostrady. 
Czas budowy autostrady wyrażony w dniach wynosi [len] (sufit z 
długości autostrady wyrażonej w km). Proszę zaproponować 
algorytm wyznaczający minimalną liczbę dni dzielącą otwarcie 
pierwszej i ostatniej autostrady.
"""
from math import ceil, sqrt
from collections import deque
class FindUnion:
    def __init__(self, size:int):
        self.parent:list[int] = list(range(size))
        self.rank:list[int] = [0] * size
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

def min_diff(cities:list[tuple[int,int]]) -> int:
    edges:list[tuple[int,int,int]] = []
    num_cities = len(cities)
    for i in range(num_cities):
        for j in range(i + 1, num_cities):
            x1 = cities[i][0]
            y1 = cities[i][1]

            x2 = cities[j][0]
            y2 = cities[j][1]

            cost = ceil(sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2)))
            edges.append((i, j, cost))

    edges.sort(key = lambda x : x[2])

    adj:list[list[tuple[int,int]]] = [[] for _ in range(num_cities)]
    edges_count = 0
    res = float('inf')

    for u, v, w in edges:
        q = deque([u])
        parent:list[int] = [-1] * num_cities
        parent_weight:list[int] = [-1] * num_cities
        vis = [False] * num_cities

        vis[u] = True
        found_cycle = False

        while q:
            curr = q.popleft()
            if curr == v:
                found_cycle = True
                break
            for child, weight in adj[curr]:
                if not vis[child]:
                    vis[child] = True
                    parent[child] = curr
                    parent_weight[child] = weight
                    q.append(child)

        if found_cycle:
            curr = v
            min_edge_val = float('inf')
            minu, minv = -1, -1

            while curr != u:
                prev = parent[curr]
                weight = parent_weight[curr]

                if weight <  min_edge_val:
                    min_edge_val = weight
                    minu, minv = prev, curr
                curr = prev

            for i in range(len(adj[minu])):
                if adj[minu][i][0] == minv:
                    _ = adj[minu].pop(i)
                    break
            for i in range(len(adj[minv])):
                if adj[minv][i][0] == minu:
                    _ = adj[minv].pop(i)
                    break

            edges_count -= 1

        adj[u].append((v, w))
        adj[v].append((u, w))
        edges_count += 1

        if edges_count == num_cities - 1:
            curr_min = float('inf')
            for i in range(num_cities):
                for child, weight in adj[i]:
                    if weight < curr_min:
                        curr_min = weight
            res = min(res, w - curr_min)

    return int(res)




def solution():
    # TODO: Implement algorithm logic here
    pass

if __name__ == "__main__":
    solution()
