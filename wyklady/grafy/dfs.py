
# lista sasiedztwa
# O(V + E)
def dfs(Graph:list[list[int]]):
    n = len(Graph)

    vis_time_in = [-1 for _ in range(n)]
    vis_time_out = [-1 for _ in range(n)]
    parent = [-1 for _ in range(n)]
    vis = [False for _ in range(n)]

    vis_time = 0

    def dfs_visit(Graph:list[list[int]], vert:int):
        nonlocal vis_time, vis_time_in, vis_time_out, vis

        vis_time_in[vert] = vis_time
        vis[vert] = True
        vis_time += 1

        for child in Graph[vert]:
            if not vis[child]:
                parent[child] = vert
                vis[child] = True

                dfs_visit(Graph, child)

        vis_time_out[vert] = vis_time
        vis_time += 1

    for vert in range(n):
        if not vis[vert]:
            dfs_visit(Graph, vert)

    return vis_time_in, vis_time_out, vis, parent



