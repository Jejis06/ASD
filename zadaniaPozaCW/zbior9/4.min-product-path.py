"""
Zadanie 4. (logarytmy) Mamy dany graf G=(V,E) z wagami w: E -> N-{0} 
(dodatnie liczby naturalne). Chcemy znalezc scieżkę z wierzchołka u 
do v tak, by iloczyn wag był minimalny. Omówic rozwiązanie 
(bez implementacji).
"""
from math import log
from queue import PriorityQueue

graph_nei = list[list[tuple[int, int|float]]]

def shortest_multiplication(graph:graph_nei, u:int, v:int):
    n = len(graph)
    for vert in range(n):
        m = len(graph[vert])
        for j in range(m):
            graph[vert][j] = (graph[vert][j][0], log(graph[vert][j][1]))

    pq:PriorityQueue[tuple[int | float ,int]]= PriorityQueue()

    dist = [float('inf')] * n
    parent = [-1] * n
    dist[u] = 0

    pq.put((0, u))

    while not pq.empty():
        cost, vert = pq.get()
        if cost > dist[vert]: continue

        if vert == v: break

        for child, child_cost in graph[vert]:
            if dist[child] > child_cost + cost:
                dist[child] = child_cost + cost
                parent[child] = vert
                pq.put((child_cost + cost, child))
    path = []
    while v != -1:
        path.append(v)
        v = parent[v]
    return path


    



def solution():
    # TODO: Implement algorithm logic here
    pass

if __name__ == "__main__":
    solution()
