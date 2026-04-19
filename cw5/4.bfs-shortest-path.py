"""
Zadanie 4. Proszę zaimplementować algorytm BFS tak, żeby znajdował najkrótsze
ścieżki w grafie i następnie, żeby dało się wypisać najkrótszą ścieżkę
z zadanego punktu startowego do wskazanego wierzchołka.
"""
from collections import deque

graph_neighbor = list[list[int]]

# O(V + E)
def BFS_shortest_path(G:graph_neighbor, start:int, end:int) -> list[int]:
    n = len(G)
    vis:list[bool] = [False for _ in range(n)]
    parent:list[int] = [-1] * n

    q:deque[int] = deque([start])
    vis[start] = True

    while q:
        vert = q.popleft()
        if vert == end:
            path:list[int] = [end]
            while end != start:
                end = parent[end]
                path.append(end)
            return path[::-1]

        for child in G[vert]:
            if not vis[child]:
                parent[child] = vert
                vis[child] = True
                q.append(child)
    return []
            






def solution():
    # TODO: Implement algorithm logic here
    pass

if __name__ == "__main__":
    solution()
