"""
Zadanie 7. Dana jest mapa kraju w postaci grafu G = (V, E). Kierowca chce
przejechać z miasta (wierzchołka) s do miasta t. Niestety niektóre drogi
(krawędzie) są płatne. Każda droga ma taką samą jednostkową opłatę. Proszę
podać algorytm, który znajduje trasę wymagającą jak najmniejszej liczby opłat.
W ogólności graf G jest skierowany, ale można najpierw wskazać algorytm dla
grafu nieskierowanego.
"""

from collections import deque

graph_neighbor = list[list[tuple[int,int]]]

# wagi (0,1)

# O (V + E)
def find_cheapes_path(G:graph_neighbor, s:int, t:int) -> list[int]:
    n = len(G)
    parent:list[int] = [-1 for _ in range(n)]
    dist:list[int]   = [ float('inf') for _ in range(n)]


    q: deque[int] = deque([s])
    dist[s] = 0

    while q:
        vert = q.popleft()
        if vert == t: break

        for child, w in G[vert]:
            if dist[vert] + w < dist[child]:
                dist[child] = dist[vert] + w
                parent[child] = vert

                if w == 0: q.appendleft(child)
                else: q.append(child)

    if dist[t] == float('inf'):
        return []
    path = [t]
    while t != s:
        t = parent[t]
        path.append(t)
    return path[::-1]

def solution():
    # TODO: Implement algorithm logic here

    pass

if __name__ == "__main__":
    solution()
