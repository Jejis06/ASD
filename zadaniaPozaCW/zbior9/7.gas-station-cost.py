"""
Zadanie 7. (problem stacji benzynowych na grafie) Pewien podróżnik chce 
przebyć trasę z punktu A do punktu B. Niestety jego samochód spala 
dokładnie jeden litr paliwa na jeden kilometr trasy. W baku mieści się 
dokładnie D litrów paliwa. Trasa jest reprezentowana jako graf, gdzie 
wierzchołki to miasta a krawędzie to łączące je drogi. Każda krawędź 
ma długość w kilometrach (przedstawioną jako licza naturalna). W każdym 
wierzchołku jest stacja benzynowa, z daną ceną za litr paliwa. Proszę 
podać algorytm znajdujący trasę z punktu A do punktu B o najmniejszym 
koszcie. Proszę uzasadnić poprawność algorytmu.
"""
from queue import PriorityQueue

graph_nei = list[list[tuple[int,int]]]

# capacity -> D
# len(graph) -> V
# O(D* E * log(D * V)) -> O(E log V) [jezeli D to jakas stosunkowo mala liczba albo stala]

def cheapest_path(graph:graph_nei, prices:list[int|float], capacity:int, a:int, b:int):
    n = len(graph)

    dist:list[list[float]] = [[float('inf') for _ in range(capacity + 1)] for _ in range(n)] 
    parent:list[list[tuple[int,int]]] = [[(-1, -1) for _ in range(capacity + 1)] for _ in range(n)] 


    pq:PriorityQueue[tuple[int,int,int]] = PriorityQueue()


    # start z pustym bakiem
    pq.put((0, a, 0))
    dist[a][0] = 0

    fuel_state = -1
    while not pq.empty():
        curr_cost, vert, fuel= pq.get()
        if dist[vert][fuel] < curr_cost: continue

        if vert == b:
            # TODO: LOGIC
            fuel_state = fuel
            break

        # tankowanie
        if fuel < capacity and prices[vert] != float('inf'):
            price_per_liter = int(prices[vert])
            if dist[vert][fuel + 1] > price_per_liter + curr_cost:
                dist[vert][fuel + 1] = price_per_liter + curr_cost
                parent[vert][fuel + 1] = (vert, fuel)
                pq.put((curr_cost + price_per_liter, vert, fuel + 1))


        # jazda dalej
        for child, needed_fuel in graph[vert]:
            if fuel >= needed_fuel:
                if dist[child][fuel - needed_fuel] > curr_cost:
                    dist[child][fuel - needed_fuel] = curr_cost
                    parent[child][fuel - needed_fuel] = (vert, fuel)
                    pq.put((curr_cost, child, fuel - needed_fuel))

    if fuel_state == -1: return []
    path = []
    curr_state = fuel_state
    curr_vert = b

    while curr_vert != -1:
        if not path or curr_vert != path[-1]:
            path.append(curr_vert)
        
        par, prev_state = parent[curr_vert][curr_state]

        if par == -1: break

        curr_vert = par
        curr_state = prev_state
    return path[::-1]

            


def solution():
    # TODO: Implement algorithm logic here
    pass

if __name__ == "__main__":
    solution()
