from kol2testy import runtests
from collections import deque

def bfs(G, v):
    n = len(G)
    vis = [False] * n
    q = deque([v])
    vis[v] = True

    visited = 1
    while q:
        u = q.popleft()
        for child in G[u]:
            if not vis[child]:
                visited += 1
                vis[child] = True
                q.append(child)
    return visited



def beautree(G:list[list[tuple[int,int]]]):

    edges:list[tuple[int,int,int]] = []
    n = len(G)
    for vert in range(n):
        for child, cost in G[vert]:
            if vert > child:
                edges.append((child, vert, cost))

    edges.sort(key = lambda x: x[2])
    m = len(edges)
    for start_edge in range(m - n + 2):
        mst_cost = 0

        temp_g = [ [] for _ in range(n)]

        for i in range(n-1):
            u, v, w = edges[start_edge + i]
            temp_g[u].append(v)
            temp_g[v].append(u)
            mst_cost += w
        
        if bfs(temp_g, 0) == n:
            return mst_cost
    



    return None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( beautree, all_tests = True)
