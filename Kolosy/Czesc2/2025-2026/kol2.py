from kol2testy import runtests
from queue import PriorityQueue

'''

wiemy z kolejki priorytetowej wychodzi nam najszybsza aktualna sciezka a jezeli sa dwie takie same to ta o mniejszym wierzcholku koncowym z mniejszym indeksem, jezeli taki wierzcholek to jeden
z tych ktorych szukamy to od razu wiemy ze jest to pierwszy ktory powinien odwiedzic bajtek podczas swojej podrozy. Jednoczesnie wiemy ze kazda kolejna wycieczka nie moze przez taki wierzcholek
przechodzic wiec ustawiamy go jako niemozliwego do zdobycia i ponadto nie kontunuujemy z niego drogi dalej

zlozonosc O(ElogV)


'''



# resorts -> destinations
# flights -> edges
# start_city -> start_vert
def lets_roll(start_city:int, flights:list[tuple[int,int,int]], resorts:list[int]) -> int:
    n = 0
    for u, v, _ in flights: n = max(n, u, v) # O(E)
    n += 1


    graph:list[list[tuple[int,int]]] = [[] for _ in range(n)]

    for u, v, cost in flights: # O(E)
        graph[u].append((v, cost))
        graph[v].append((u, cost))

    vis:list[int] = [False] * n # O(V)
    lookup:list[bool] = [False] * n # O(V)

    for resort in resorts: lookup[resort] = True # O(R)



    pq:PriorityQueue[tuple[int,int]] = PriorityQueue()

    res = 0
    dist:list[float] = [float('inf')] * n 
    pq:PriorityQueue[tuple[int,int]] = PriorityQueue()


    pq.put((0, start_city))
    vis[start_city] = False

    while not pq.empty():
        curr_cost, vert = pq.get()
        if vis[vert]: continue
        if curr_cost > dist[vert]: continue

        if lookup[vert]:
            vis[vert] = True
            res += 2 * dist[vert]
            continue

        for child, child_cost in graph[vert]:
            if vis[child]: continue
            if dist[child] > child_cost + curr_cost:
                dist[child] = child_cost + curr_cost
                pq.put((child_cost + curr_cost, child))



    return res

runtests(lets_roll, all_tests = True)
