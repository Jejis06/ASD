"""
2. Bellman-Ford - napisac
"""

graph_wei = list[list[tuple[int, int]]]
def bell_ford(graph:graph_wei, start:int):
    n = len(graph)
    dist = [float('inf') for _ in range(n)]

    dist[start] = 0

    for _ in range(n-1):
        changed = False
        for vert in range(n):
            if dist[vert] == float('inf'):
                continue
            for child, cost in graph[vert]:
                if dist[child] > cost + dist[vert]:
                    dist[child] = cost + dist[vert]
                    changed = True
        if not changed: break

    # weryfikacja
    for vert in range(n):
        for child, cost in graph[vert]:
            if dist[child] > cost + dist[vert]:
                return []
    return dist



def solution():
    # TODO: Implement algorithm logic here
    pass

if __name__ == "__main__":
    solution()
