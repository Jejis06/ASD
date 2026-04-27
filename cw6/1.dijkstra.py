"""
1. Dijkstra - napisac
"""

from heapq import heappop as pq_pop, heappush as pq_push

graph_wei = list[list[tuple[int, int]]]

def dijkstra(graph:graph_wei, start:int):

    n = len(graph)
    dist = [float('inf')] * n

    pq = [(0, start)]
    dist[start] = 0

    while pq:
        curr_cost, vert = pq_pop(pq)

        if curr_cost > dist[vert]: continue

        for child, child_cost in graph[vert]:
            new_cost = child_cost + curr_cost
            if dist[child] > new_cost:
                dist[child] = new_cost
                pq_push(pq, (new_cost, child))
    return dist


def solution():
    # TODO: Implement algorithm logic here
    pass

if __name__ == "__main__":
    solution()
