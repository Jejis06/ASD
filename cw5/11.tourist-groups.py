"""
Zadanie 11. (problem przewodnika turystycznego) Przewodnik chce przewieźć
grupę K turystów z miasta A do miasta B. Po drodze jest jednak wiele innych
miast i między różnymi miastami jeżdżą autobusy o różnej pojemności. Mamy
daną listę trójek postaci (x, y, c), gdzie x i y to miasta między którymi
bezpośrednio jeździ autobus o pojemności c pasażerów. Przewodnik musi
wyznaczyć wspólną trasę dla wszystkich turystów i musi ich podzielić na
grupki tak, żeby każda grupka mogła przebyć trasę bez rozdzielania się.
Proszę podać algorytm, który oblicza na ile (najmniej) grupek przewodnik
musi podzielić turystów (i jaką trasą powinni się poruszać), żeby wszyscy
dostali się z A do B.
"""
from heapq import heappush as pq_push, heappop as pq_pop

graph_neighbor = list[list[tuple[int,int]]]
weighted_edges = list[tuple[int,int,int]]

def group_path(edges:weighted_edges, a:int, b:int, k:int) -> tuple[int, list[int]]:

    n = max(max(u, v) for u, v, _ in edges) + 1

    graph:graph_neighbor = [[] for _ in range(n)]
    for x, y, c in edges:
        graph[x].append((y, c))
        graph[y].append((x, c))

    dist:list[int | float]= [ -1 for _ in range(n)]
    parent:list[int] = [-1] * n

    dist[a] = k+1 
    pq:list[tuple[int | float, int]]= [(-(k+1), a)]


    while pq:
        curr_cost, vert = pq_pop(pq)
        curr_cost *= -1

        if curr_cost < dist[vert]: continue

        for child, child_cost in graph[vert]:

            new_cost = min(child_cost, curr_cost)

            if dist[child] < new_cost:
                dist[child] = new_cost 
                parent[child] = vert
                
                pq_push(pq, (-new_cost, child))

    final_cost = dist[b] - 1
    if final_cost <= 0: return (-1, [])

    num_peaople:int = int( (k + final_cost - 1) // final_cost )
    path:list[int] = []
    while b != -1:
        path.append(b)
        b = parent[b]

    return (num_peaople, path[::-1])





def solution():
    # TODO: Implement algorithm logic here
    pass

if __name__ == "__main__":
    solution()
