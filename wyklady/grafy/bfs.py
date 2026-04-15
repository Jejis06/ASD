from collections import deque

# lista sasiedztwa

# O(V + E)

def bfs(Graph:list[list[int]], v:int):

    n = len(Graph)
    queue: deque[int] = deque()

    dist = [-1 for _ in range(n)]
    vis = [False for _ in range(n)]
    parent = [-1 for _ in range(n)]

    dist[v] = 0
    vis[v] = True

    queue.append(v)

    while len(queue) > 0:
        u = queue.popleft()

        for child in Graph[u]:
            if not vis[child]:
                vis[child] = True
                dist[child] = dist[u] + 1
                parent[child] = u

                queue.append(child)

    return dist, vis, parent


    

