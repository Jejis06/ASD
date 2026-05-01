from kol2_test import runtests
from heapq import heappop as pq_pop, heappush as pq_push

def change(mosty:list[tuple[int,int,str]], poczty:list[int], s:int):
    n = 0
    for u, v, _ in mosty:
        n = max(u, v, n)
    n += 1

    graph = [[] for _ in range(n)]

    for u, v, c in mosty:
        c = 0 if c == 'F' else 1
        graph[u].append((v, c))
        graph[v].append((u, c))

    post_office = [False] * n

    for poczta in poczty: post_office[poczta] = True

    dist = [[float('inf') for _ in range(2)] for _ in range(n)]
    # 1 - kapelusz, 0 - czapka
    pq = [(0, s, 0), (0, s, 1)]

    dist[s][0] = 0
    dist[s][1] = 0

    while pq:
        curr_cost, vert, state = pq_pop(pq)

        if dist[vert][state] < curr_cost: continue

        if post_office[vert]:
            return curr_cost

        for child, needed_cap in graph[vert]:
            if needed_cap == state:
                if dist[child][needed_cap] > curr_cost:
                    dist[child][needed_cap] = curr_cost
                    pq_push(pq, (curr_cost, child, needed_cap))
            else:
                if dist[child][needed_cap] > curr_cost + 1:
                    dist[child][needed_cap] = curr_cost + 1
                    pq_push(pq, (curr_cost + 1, child, needed_cap))




    return -1

runtests(change, all_tests = True)
