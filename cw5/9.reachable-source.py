"""
Zadanie 9. Wierzchołek v w grafie skierowanym nazywamy dobrym początkiem jeśli
każdy inny wierzchołek można osiągnąć ścieżką skierowaną wychodzącą z v.
Proszę podać algorytm, który stwierdza czy dany graf zawiera dobry początek.
"""

graph_nei = list[list[int]]

def good_start(G:graph_nei) -> bool:

    n = len(G)
    vis = [False] * n
    post_order:list[int] = []

    def dfs(G:graph_nei, vert:int):
        vis[vert] = True
        for child in G[vert]:
            if not vis[child]:
                dfs(G, child)
        post_order.append(vert)

    for i in range(n):
        if not vis[i]:
            dfs(G, i)

    num_met = len(post_order)
    def dfs2(G:graph_nei, vert:int):
        nonlocal num_met
        vis[vert] = False
        num_met -= 1
        for child in G[vert]:
            if vis[child]:
                dfs2(G, child)

    post_order = post_order[::-1]
    dfs2(G, post_order[0])
    if num_met > 0: return False
    return True




