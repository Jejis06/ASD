"""
Zadanie 1. (malejące krawędzie, c.d.) Dany jest graf G=(V,E), gdzie 
każda krawędź ma wagę ze zbioru {1,... E} (wagi krawędzi są parami 
różne). Proszę zaproponować algorytm, który dla danych 
wierzchołków z i y oblicza ścieżkę o najmniejszej sumie wag, która 
prowadzi z z do y po krawędziach o malejących wagach (jeśli ścieżki 
nie ma to zwracamy ∞).
"""

graph_nei = list[list[tuple[int,int]]]
def shortest_path(graph:graph_nei, z:int, y:int):
    n = len(graph)
    m = 0

    for vert in range(n):
        for child, _ in graph[vert]:
            if child > vert:
                m += 1
    edges:list[tuple[int,int,int]] = [(-1,-1,-1)] * m
                
    for vert in range(n):
        for child, cost in graph[vert]:
            if child > vert:
                edges[m-cost] = (vert, child, cost)
    
    dist = [float('inf')] * n
    dist[z] = 0


    for u, v, cost in edges:
        if dist[v] > dist[u] + cost:
            dist[v] = dist[u] + cost

        if dist[u] > dist[v] + cost:
            dist[u] = dist[v] + cost

    return dist[y]


def solution():
    # TODO: Implement algorithm logic here
    pass

if __name__ == "__main__":
    solution()
