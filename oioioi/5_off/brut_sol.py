import sys

graph_nei_weighted = list[list[tuple[int,int]]]

inf = 1000000 + 5

from collections import deque


def check_path(graph:graph_nei_weighted, start:int, dest:int , low:int, d:int|float, vis:list[int], vis_key:int) -> bool:
    n = len(graph) 
    q:deque[int] = deque([start])
    vis[start] = vis_key 
    while  q:
        u = q.popleft()
        if u == dest: return True

        for child, w in graph[u]:
            if w < low: continue
            if w > d: break

            if vis[child] != vis_key:
                #if child == dest: return True
                vis[child] = vis_key
                q.append(child)
        




    return False



data = iter(sys.stdin.read().split())

n = int(next(data))
m = int(next(data))
q = int(next(data))
d = int(next(data))

vis = [0] * (n+1)

graph:graph_nei_weighted = [ [] for _ in range(n+1) ]
heights:set[int] =set()

for _ in range(m):
    a = int(next(data))
    b = int(next(data))
    c = int(next(data))

    graph[a].append((b, c))
    graph[b].append((a, c))

    heights.add(c)

for i in range(1, n+1):
    graph[i].sort(key = lambda x: x[1])

vis_key = 0

for _ in range(q):
    u = int(next(data))
    v = int(next(data))
    vis_key += 1

    if not check_path(graph, u, v, 0, float('inf'), vis, vis_key):
        print("NIE")
        continue

    ok = False
    for low in heights:
        vis_key += 1
        ok = check_path(graph, u, v, low, low + d, vis, vis_key)
        if ok == True: break


    if ok: print("TAK")
    else: print("NIE")

