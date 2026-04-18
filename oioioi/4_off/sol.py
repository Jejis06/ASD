from sys import stdin
import sys
from math import log

from collections import deque

from heapq import heappush as pq_push
from heapq import heappop as pq_pop

# wgl bez tego nie dziala mnozenie w 4a
sys.set_int_max_str_digits(0)

def dijkstra(graph:list[list[tuple[int,float, int]]], start:int):
    pq:list[tuple[float,int, int]]= []
    n = len(graph)

    dist:list[float] = [float('inf') for _ in range(n)]
    village_count:list[int] = [0] * n
    parent:list[int] = [-1] * n
    parent_weight:list[int] = [1] * n

    dist[start] = 0
    village_count[start] = 1
    pq = [(0, 1, start)]

    err = 1e-9

    while pq:
        cost, villages, vert = pq_pop(pq)
        if cost > dist[vert] + err:
            continue

        for child, child_cost_log, child_cost_real in graph[vert]:
            new_cost = child_cost_log + cost
            num_villages = villages + 1

            if new_cost < dist[child] - err:
                dist[child] = new_cost

                village_count[child] = num_villages

                parent[child] = vert
                parent_weight[child] = child_cost_real
                pq_push(pq, (new_cost, num_villages, child))

            elif abs(new_cost - dist[child]) <= err:
                if num_villages < village_count[child]:
                    dist[child] = new_cost

                    village_count[child] = num_villages

                    parent[child] = vert
                    parent_weight[child] = child_cost_real
                    pq_push(pq, (new_cost, num_villages, child))


    return parent, parent_weight 

def solve():
    x = iter(stdin.read().split())

    n = int(next(x))
    m = int(next(x))
    k = int(next(x))

    graph_log:list[list[tuple[int, float, int]]]= [[] for _ in range(n+1)] 

    for _ in range(m):
        a, b, c = int(next(x)), int(next(x)), int(next(x))

        graph_log[a].append((b, log(c), c))
        graph_log[b].append((a, log(c), c))


    queries:list[int] = []
    for _ in range(k):
        q = int(next(x))
        queries.append(q)

    parent, parent_weight = dijkstra(graph_log, 1)

    for q in queries:

        path:list[int] = [q]
        costs:list[int] = []

        while q != 1:
            path.append(parent[q])
            costs.append(parent_weight[q])
            q = parent[q]

        # przyspieszenie mnozania najpierw male potem duze
        if not costs: path_cost = 1
        else:
            queue_costs = deque(costs)
            while len(queue_costs) > 1:
                a = queue_costs.popleft()
                b = queue_costs.popleft()
                queue_costs.append(a * b)
            path_cost = queue_costs[0]


        print(len(path) , end = ' ')
        for i in range(len(path) - 1, -1, -1):
            print(path[i], end=' ')
        print(path_cost)
    pass

solve()
