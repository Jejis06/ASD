
# najkrotsza droga w grafie wazonym z ujemnymi wagami oraz graf jest skierowany
# lista sasiedztwa
# O(V * E)

def bell_ford(G:list[list[tuple[int,int]]], start:int) -> tuple[bool, list[float], list[int]]:
    n = len(G)
    dist = [float('inf') for _ in range(n)]
    parent = [-1 for _ in range(n)]

    dist[start] = 0

    for _ in range(n-1):
        changed = False

        for vert in range(n):
            if dist[vert] == float('inf'): 
                continue

            for child, w in G[vert]:
                if dist[vert] + w < dist[child]:
                    dist[child] = dist[vert] + w
                    parent[child] = vert
                    changed = True
        if not changed: 
            break

    # weryfikacja
    for vert in range(n):
        if dist[vert] == float('inf'): 
            continue
        for child, w in G[vert]:
            if dist[child] > dist[vert] + w:
                print("negative cycle")
                return False, [], []

    return True, dist, parent

