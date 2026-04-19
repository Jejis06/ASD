"""
Zadanie 6. Dany jest graf G = (V, E), gdzie każda krawędź ma wagę ze zbioru
{1, ..., |E|} (wagi krawędzi są parami różne). Proszę zaproponować algorytm,
który dla danych wierzchołków x i y sprawdza, czy istnieje ścieżka z x do y,
w której przechodzimy po krawędziach o coraz mniejszych wagach.
"""

graph_neighbor = list[list[tuple[int,int]]]


# O( E^2 ) -> O(V * E)
def deacreasing_path(G:graph_neighbor, x:int, y:int) -> bool:
    n = len(G)
    vis:list[float] = [0 for _ in range(n)]

    def dfs(G:graph_neighbor, vert:int, end:int, val:float):
        if vert == end: return
        for child, weight in G[vert]:
            if weight < val and weight > vis[child]:
                vis[child] = weight
                dfs(G, child, end, weight)


    vis[x] = float('inf')
    dfs(G, x, y, float('inf'))
    return vis[y] != 0


# O(V + E)
def decreasing_path_sorted(edges:list[tuple[int,int,int]], x:int, y:int) -> bool:
    max_edge = max(edges, key = lambda edge: max(edge[0], edge[1]) )  # O(E)
    n = max(max_edge[0], max_edge[1])

    sorted_edges = sorted(edges, key = lambda edge: edge[2], reverse=True) # tutaj mozna zrobic pp counting sort i wtedy O(E)
    reachable = [False] * n # O(V)

    reachable[x] = True
    for u, v, _ in sorted_edges: # O(E)
        if reachable[u] or reachable[v]:
            reachable[u] = True
            reachable[v] = True
    return reachable[y]


def solution():
    G = [
        (0, 1, 7),
        (0, 3, 6),
        (1, 2, 5),
        (3, 2, 4),
        (1, 4, 3),
        (2, 5, 2),
        (4, 5, 1)
    ]
    graph:graph_neighbor = [[] for _ in range(6)]
    for a, b, c in G:
        graph[a].append((b, c))
        graph[b].append((a, c))
    print(deacreasing_path(graph, 3, 1))
    print(deacreasing_path(graph, 3, 4))

    pass

if __name__ == "__main__":
    solution()
