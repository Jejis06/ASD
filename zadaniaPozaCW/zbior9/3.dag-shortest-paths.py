"""
Zadanie 3. (najkrósze ścieżki w DAGu) Jak znaleźć najkrótsze ścieżki 
z wierzchołka s do wszystkich innych w acyklicznym grafie skierowanym?
"""

graph_nei = list[list[tuple[int,int]]]

def shortest_path_in_dag(graph:graph_nei, start:int) -> tuple[list[int], list[float]]:

    n = len(graph)
    dist = [float('inf')] * n
    post_order:list[int] = []
    vis:list[bool] = [False] * n

    def find_post(vert:int):
        vis[vert] = True
        for child, _ in graph[vert]:
            if not vis[child]:
                find_post(child)
        post_order.append(vert)

    find_post(start)
    m = len(post_order)

    parent = [-1] * n
    dist[start] = 0

    for i in range(m-1, -1, -1):
        vert = post_order[i]
        for child, cost in graph[vert]:
            if dist[child] > cost + dist[vert]:
                dist[child] = cost + dist[vert]
                parent[child] = vert
    return parent, dist


def solution():
    # TODO: Implement algorithm logic here
    pass

if __name__ == "__main__":
    solution()
