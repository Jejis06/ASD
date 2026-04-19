"""
Zadanie 1. Proszę zaimplementować następujące algorytmy:
a) Sprawdzanie czy graf jest dwudzielny
b) Policzyć liczbę spójnych składowych w grafie
Podzadania powinny zostać zaimplementowane z użyciem BSF i DFS (do wyboru co
gdzie "zużyć") oraz reprezentacji macierzowej i list sąsiedztwa
"""


# A) lista sasiedztwa + BFS
from collections import deque

def dwudzielny(G:list[list[int]]) -> bool:
    n = len(G)

    q:deque[int] = deque()
    color = [-1] * n

    color[0] = 0
    q.append(0)

    while q:
        vert = q.popleft()
        next_col = (color[vert] + 1) % 2
        for child in G[vert]:
            if color[child] == -1:
                color[child] = next_col
                q.append(child)
            elif color[child] == color[vert]:
                return False
    return True

# B) - repr macierzowa + dfs
def num_spojne(G:list[list[int]]) -> int:
    n = len(G)
    vis:list[bool] = [False for _ in range(n)]
    
    def dfs(G:list[list[int]], vert:int):
        vis[vert] = True
        for child in range(n):
            if G[vert][child] == 1 and not vis[child]:
                    dfs(G, child)

    res = 0
    for i in range(n):
        if not vis[i]:
            dfs(G, i)
            res += 1

    return res




def solution():
    pass

if __name__ == "__main__":
    solution()
