"""
4. najkrotsza droga z s do pozostalych wierzcholkow w dagu skierowanym
"""

graph_wei = list[list[tuple[int,int]]]

# O (V + E)

def dag_shortest_path(graph:graph_wei, start:int):
    n = len(graph)
    post_order:list[int]= []
    vis = [False] * n

    def dfs(ver:int):
        vis[ver] = True

        for child, _ in  graph[ver]:
            if not vis[child]:
                dfs(child)
        post_order.append(ver)
    

    dist = [float('inf')] * n
    dfs(start)

    dist[start] = 0

    for i in range(len(post_order)-1, -1,-1):
        vert = post_order[i]
        for child, cost in graph[vert]:
            if dist[child] > cost + dist[vert]:
                dist[child] = cost + dist[vert]
    return dist






def solution():
    # TODO: Implement algorithm logic here
    pass

if __name__ == "__main__":
    solution()
