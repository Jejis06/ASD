"""
Zadanie 2. (domknięcie przechodnie) Proszę zaimplementować algorytm 
obliczający domknięcie przechodnie grafu reprezentowanego w postaci 
macierzowej (domknięcie przechodnie grafu G, to graf nad tym samym 
zbiorem wierzchołków, który dla każdych dwóch wierzchołków u i v ma 
krawędź z u do v wtedy i tylko wtedy, gdy w G istnieje ścieżka z u 
do v).
"""
from collections import deque

def enclosure(graph:list[list[int]]) -> list[list[int]]:
    n = len(graph)

    new_graph = [[0 for _ in range(n)] for _ in range(n)]

    vis = [0] * n
    def bfs(s:int, vis_key:int):
        q:deque[int] = deque()
        q.append(s)
        vis[s] = vis_key

        while q:
            u = q.popleft()
            if u != s:
                new_graph[s][u] = 1 


            for child in range(n):
                if graph[u][child] == 1 and vis[child] != vis_key:
                    vis[child] = vis_key
                    q.append(child)
    vis_key = 1
    for u in range(n):
        bfs(u, vis_key)
        vis_key += 1
    return new_graph




        



def solution():
    # TODO: Implement algorithm logic here
    pass

if __name__ == "__main__":
    solution()
