"""
Zadanie 12. Proszę wskazać algorytm, który mając na wejściu graf nieskierowany
G = (V, E) stwierdza, czy jego zbiór wierzchołków można podzielić na dwa
rozłączne zbiory V1 i V2 takie, że V = V1 suma V2 oraz zarówno wierzchołki
z V1 jak i wierzchołki z V2 tworzą kliki.
"""
from collections import deque

graph_neighbor = list[list[int]]

def clique_partition(G:graph_neighbor) -> bool:
    n = len(G) # zakladam ze wierzch. sa od 0 do n-1


    G_dop:list[list[int]]= [[] for _ in range(n)]

    for v in range(n):
        mask = [False] * n
        for child in G[v]:
            mask[child] = True
        for i in range(n):
            if not mask[i] and i != v:
                G_dop[v].append(i)

    col = [-1] * n
    def check_parity(Graph:graph_neighbor, start:int):
        q:deque[int] = deque()
        col[start] = 1

        q.append(start)
        while q:
            u = q.popleft()
            for child in Graph[u]:
                if col[child] == -1:
                    col[child] = col[u] ^ 1
                    q.append(child)
                elif col[child] == col[u]: return False
        return True

    for v in range(n):
        if col[v] == -1:
            if not check_parity(G_dop, v):
                return False
    return True

def solution():
    # TODO: Implement algorithm logic here
    pass

if __name__ == "__main__":
    solution()
