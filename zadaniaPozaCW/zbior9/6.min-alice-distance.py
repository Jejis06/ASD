"""
Zadanie 6. (dwóch kierowców) Dana jest mapa kraju w postaci grafu G=(V,E), 
gdzie wierzchołki to miasta a krawędzie to drogi łączące miasta. Dla 
każdej drogi znana jest jej długość (wyrażona w kilometrach jako liczba 
naturalna). Alicja i Bob prowadzą (na zmianę) autobus z miasta x w V 
do miasta y w V, zamieniając się za kierownicą w każdym kolejnym mieście. 
Alicja wybiera trasę oraz decyduje, kto prowadzi pierwszy. Proszę zapropnować 
algorytm, który wskazuje taką trasę (oraz osobę, która ma prowadzić 
pierwsza), żeby Alicja przejechała jak najmniej kilometrów. Algorytm 
powinien być jak najszybszy (ale przede wszystkim poprawny).
"""
from queue import PriorityQueue

graph_nei = list[list[tuple[int,int]]]

def find_route_and_apoint_driver(G:graph_nei, x:int, y:int) -> tuple[list[int], str]:
    n = len(G)

    dist:list[list[int | float]] = [[float('inf')] * 2 for _ in range(n)]
    parent:list[list[int]] = [[-1] * 2 for _ in range(n)]

    pq: PriorityQueue[tuple[int,int, int]] = PriorityQueue()
    pq.put((0, x, 0))
    pq.put((0, x, 1))

    dist[x][0] = 0
    dist[x][1] = 0

    # 0 ten jedzie pierwszy
    # 1 ten jedzie drugi
    
    best_end_state = -1
    while not pq.empty():
        curr_cost, vert, driver = pq.get()

        if dist[vert][driver] < curr_cost : continue
        if vert == y:
            best_end_state = driver
            break

        for child, child_cost in G[vert]:
            if driver == 0: new_dist = child_cost + curr_cost
            else: new_dist = curr_cost

            if dist[child][1 - driver] > new_dist:
                dist[child][1 - driver] = new_dist
                parent[child][1 - driver] = vert

                pq.put((new_dist, child, 1-driver))
    if best_end_state == -1:
        return [], "Brak trasy"

    path = []
    curr_v = y
    curr_state = best_end_state
    start_driver = -1

    while curr_v != -1:
        path.append(curr_v)
        p = parent[curr_v][curr_state]

        if p == -1: break

        curr_v = p
        curr_state = 1 - curr_state

    if curr_state == 0:
        return path[::-1], "Alicja"
    else:
        return path[::-1], "Bob"



def solution():
    # TODO: Implement algorithm logic here
    pass

if __name__ == "__main__":
    solution()
