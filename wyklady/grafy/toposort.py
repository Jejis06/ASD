
# Zalozenie: Graf skierowany i acykliczny (DAG)
# O(V + E)
# lista sasiedztwa 
def toposort(G:list[list[int]]) -> list[int]:
    n = len(G)
    final_order:list[int] = []

    vis = [False for _ in range(n)]
    def dfs(G:list[list[int]], vert:int):
        nonlocal final_order, vis
        vis[vert] = True
        for child in G[vert]:
            if not vis[child]:
                dfs(G, child)
        final_order.append(vert)

    for vert in range(n):
        if not vis[vert]:
            dfs(G, vert)
        

    return final_order[::-1]



