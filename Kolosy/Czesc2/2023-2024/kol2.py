from kol2testy import runtests

from collections import deque


# O(16 * (V + E) )

def warrior( G:list[tuple[int,int,int]], s:int, t:int) -> int:
    n = 0
    for u, v, _ in G:
        n = max(n, u, v)
    n += 1

    graph:list[list[tuple[int,int]]] = [ [] for _ in range(n) ]
    dist: list[list[int]] = [[-1 for _ in range(17)] for _ in range(n) ]

    for u, v, c in G:
        graph[u].append((v, c))
        graph[v].append((u, c))


    q:deque[tuple[int, int, int, int]] = deque([(s,0, 0, 0)])

    while len(q) > 0:
        vert, delay, curr_dist, strength_left = q.popleft()
        
        if delay > 0:
            q.append((vert, delay-1, curr_dist+1, strength_left))
            continue

        if dist[vert][strength_left] != -1: continue

        dist[vert][strength_left] = curr_dist 
        if vert == t:
            return dist[t][strength_left]

        for child, child_cost in graph[vert]:
            if strength_left + child_cost > 16:
                q.append((child, child_cost - 1 + 8, curr_dist + 1, child_cost))
            else:
                q.append((child, child_cost-1, curr_dist + 1, child_cost + strength_left))



    min_val =float('inf') 
    print(dist[t])
    for d in dist[t]:
        if d != -1:
            min_val = min(min_val, d)
    return min_val

    

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( warrior, all_tests = True)
