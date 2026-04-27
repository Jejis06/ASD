import sys

def find(x:int, parent:list[int]) -> int:
    if x != parent[x]:
        parent[x] = find(parent[x], parent)
    return parent[x]

def onion(x:int, y:int, parent:list[int], rank:list[int]):
    x = find(x, parent)
    y = find(y, parent)

    if x == y: return
    if rank[x] > rank[y]:
        parent[y] = x
    else:
        parent[x] = y
        if rank[x] == rank[y]:
            rank[y] += 1


    


data = iter(sys.stdin.read().split())

n = int(next(data))
m = int(next(data))
q = int(next(data))
d = int(next(data))

edges:list[tuple[int,int,int]] = []
queries:list[tuple[int,int]]= []
active_queries:set[int] = set( range(q) )



for _ in range(m):
    a = int(next(data))
    b = int(next(data))
    c = int(next(data))

    edges.append((c, a, b))

for i in range(q):
    u = int(next(data))
    v = int(next(data))

    queries.append((u, v))

edges.sort()

parent = list(range(n+1))
rank = [0] * (n+1)

res = [False] * q
for c, u, v in edges:
    onion(u, v, parent, rank)


# INITIAL CLEANUP
to_remove:list[int] = []
for q_ind in active_queries:
    qu, qv = queries[q_ind]
    if find(qu, parent) != find(qv, parent):
        to_remove.append(q_ind)
for q_ind in to_remove:
    active_queries.remove(q_ind)

# sliding window
for l in range(m):
    if not active_queries: break

    parent = list(range(n+1))
    rank = [0] * (n+1)

    for r in range(l, m):
        w, u, v = edges[r]

        if w - edges[l][0] > d: break
        onion(u, v, parent, rank)

        to_remove = []
        for q_ind in active_queries:
            qu, qv = queries[q_ind]
            if find(qu, parent) == find(qv, parent):
                to_remove.append(q_ind)
                res[q_ind] = True

        for q_ind in to_remove:
            active_queries.remove(q_ind)
for t in res:
    if t == True: print("TAK")
    else: print("NIE")








