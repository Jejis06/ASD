import sys

graph_nei_weighted = list[list[tuple[int,int]]]

inf = 1000000 + 5
vis = []

# jak zwraca true to dobrze jak nie zwraca to nie zawsze dobrze 
def check_dist_possibility(graph:graph_nei_weighted, curr_vert:int, dest_vert:int, minval_path:int, maxval_path:int) -> bool:
    global d
    n = len(graph)
    vis = [False] * (n+1)

    if curr_vert == dest_vert: return True
    vis[curr_vert] = True 

    ok = False
    for child, w in graph[curr_vert]:
        if not vis[child] :
            curr_maxval_path = max(maxval_path, w)
            curr_minval_path = min(minval_path, w)

            if curr_maxval_path - curr_minval_path <= d:
                ok = ok or check_dist_possibility(graph, child, dest_vert, curr_minval_path, curr_maxval_path)
    return ok

def check_dist_possibiliti_2(graph:graph_nei_weighted):



data = iter(sys.stdin.read().split())

n = int(next(data))
m = int(next(data))
q = int(next(data))
d = int(next(data))


graph:graph_nei_weighted = [ [] for _ in range(n+1) ]
vis = [False] * (n+1)

for _ in range(m):
    a = int(next(data))
    b = int(next(data))
    c = int(next(data))

    graph[a].append((b, c))
    graph[b].append((a, c))

for _ in range(q):
    u = int(next(data))
    v = int(next(data))

    ok = check_dist_possibility(graph, u, v, inf, 0 )

    if ok: print("TAK")
    else: print("NIE")

