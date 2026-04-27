"""
6. mamy graf reprezentujacy kraj i ten graf jest wazony i wierzcholki s, t, wagi to odleglosci w kilometrach, chcemy i mamy dwoch zmieniajacych sie kierowcow
i chcemy zrobic taka sciezke ze pierwszy kierowca jedzie minimalna droge a drugi obojetnie dodatkowo w kazdym miescie kierowcy sie zmieniaja
"""

from heapq import heappop as pq_pop, heappush as pq_push

graph_wei = list[list[tuple[int,int]]]


# wierzcholki maja numery {0......n-1}
def find_path_for_driver(graph_in:graph_wei, s:int, t:int) -> tuple[list[int], int]:
    n = len(graph_in)

    graph:graph_wei = [ [] for _ in range(2 * n + 1) ]


    for vert in range(n):
        virt_vert = vert + 1 + n
        new_vert = vert + 1

        for child, w in graph_in[vert]:
            new_child = child + 1
            virt_child = child + 1 + n

            graph[new_vert].append((virt_child, w))

            graph[virt_vert].append((new_child, 0))

    real_s = s + 1
    virt_s = s + 1 + n
    real_t = t + 1
    virt_t = t + n + 1

    graph[0].append((real_s, 0))
    graph[0].append((virt_s, 0))


    parent = [-1] * (2 * n + 1) 
    dist = [float('inf')] * (2 * n + 1)
    pq:list[tuple[int, int]] = [(0, 0)]

    dist[0] = 0

    while pq:
        cost, vert = pq_pop(pq)
        if cost > dist[vert]: continue
        for child, child_cost in graph[vert]:
            if dist[child] > child_cost + cost:
                dist[child] = child_cost + cost
                parent[child] = vert
                pq_push(pq, (child_cost + cost, child))

    path:list[int]= []
    if dist[virt_t] > dist[real_t]:
        virt_t = real_t

    if dist[virt_t] == float('inf'): return [], -1

    player = 0
    while virt_t != 0:
        vert = virt_t if virt_t < n else virt_t - n
        path.append(vert - 1)

        if parent[virt_t] == 0:
            player = 1 if virt_t < n else 2
        virt_t = parent[virt_t]

    return path[::-1], player 



def solution():
    # TODO: Implement algorithm logic here
    pass

if __name__ == "__main__":
    solution()
