"""
Zadanie 10. Dany jest graf nieskierowany G oraz dwa jego wierzchołki, s i t.
Proszę zaproponować algorytm, który sprawdza czy istnieje taka krawędź, po
usunięciu której długość najkrótszej ścieżki z s do t wzrośnie (lub taka
ścieżka przestaje istnieć).
"""
from collections import deque

graph_neighbor = list[list[int]]

def edge_breaker(G:graph_neighbor, s:int, t:int) -> bool:
    n = len(G)
    vis = [False] * n

    dist_s = [-1 for _ in range(n)]
    dist_t = [-1 for _ in range(n)]
    layers = [0] * n

    def bfs(vert:int, true_key:bool = True, max_dist:int=0):
        q:deque[int] = deque()

        q.append(vert)
        vis[vert] = true_key

        if true_key: dist_s[vert] = 0
        else: dist_t[vert] = 0

        while q:
            next_vert = q.popleft()
            for child in G[next_vert]:
                if vis[child] != true_key:
                    vis[child] = true_key

                    if true_key:
                        dist_s[child] = dist_s[next_vert] + 1
                    else:
                        dist_t[child] = dist_t[next_vert] + 1
                        if dist_s[child] + dist_t[child] == max_dist:
                            layers[ dist_s[child] ] += 1

                    q.append(child)
    bfs(s)
    bfs(t, False, dist_s[t])

    if dist_s[t] == -1: return False

    layers[dist_s[t]] = 1

    for i in range(0, dist_s[t]):
        if layers[i] == 1 and layers[i+1] == 1:
            return True
    return False

def solution():
    # TODO: Implement algorithm logic here
    pass

if __name__ == "__main__":
    solution()
