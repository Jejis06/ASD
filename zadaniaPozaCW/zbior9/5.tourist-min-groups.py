"""
Zadanie 5. (problem przewodnika turystycznego) Przewodnik chce przewieźć 
grupę K turystów z miasta A do miasta B. Po drodze jest jednak wiele innych 
miast i między różnymi miastami jeżdzą autobusy o różnej pojemności. 
Mamy daną listę trójek postaci (x,y,c), gdzie x i y to miasta między 
którymi bezpośrednio jeździ autobus o pojemności c pasażerów. Przewodnik 
musi wyznaczyć wspólną trasę dla wszystkich tursytów i musi ich podzielić 
na grupki tak, żeby każda grupka mogła przebyć trasę bez rodzielania się. 
Proszę podać algorytm, który oblicza na ile (najmniej) grupek przewodnik 
musi podzielić turystów (i jaką trasą powinni się poruszać), żeby wszyscy 
dostali się z A do B.
"""
from queue import PriorityQueue
from math import ceil

def find_path(edges:list[tuple[int,int,int]], k:int, a:int, b:int) -> tuple[list[int], int]:

    n = 0
    for u, v, c in edges:
        n = max(n, u, v)
    n += 1

    graph:list[list[tuple[int,int]]] = [[] for _ in range(n)]
    for u, v, c in edges:
        graph[u].append((v, c))
        graph[v].append((u, c))



    pq:PriorityQueue[tuple[int,int]] = PriorityQueue()
    dist:list[int] = [0] * n
    parent:list[int] = [-1] * n

    dist[a] = k + 1
    pq.put((-dist[a], a))
    
    while not pq.empty():
        neg_cost, vert = pq.get()
        curr_cost = -neg_cost

        if curr_cost < dist[vert]: continue
        if vert == b: break

        for child, cost in graph[vert]:
            new_cost = min(cost, curr_cost)
            if dist[child] < new_cost:
                dist[child] = new_cost
                parent[child] = vert
                pq.put((-new_cost, child))
    
    if dist[b] == 0: return ([], 0)

    groups = ceil( k / (dist[b] - 1) )
    path = []
    while b != -1:
        path.append(b)
        b = parent[b]
    return (path[::-1], groups)


        




def solution():
    # TODO: Implement algorithm logic here
    pass

if __name__ == "__main__":
    solution()
