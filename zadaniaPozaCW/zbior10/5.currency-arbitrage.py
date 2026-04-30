"""
Zadanie 5. (wymiana walut) Dana jest tabela kursów walut. Dla 
każdych dwóch walut z oraz y wpis K[x][y] oznacza ile trzeba 
zapłacić waluty z żeby otrzymać jednostkę waluty y. Proszę 
zaproponować algorytm, który sprawdza czy istnieje taka waluta z, 
że za jednostkę z można uzyskać więcej niż jednostkę z przez 
serię wymian walut.
"""
from math import log

def arbitrage(K:list[list[int]]):
    n = len(K)
    graph:list[list[tuple[int,float]]] = [[] for _ in range(n)]

    for v in range(n):
        for u in range(n):
            if v == u: continue
            graph[v].append((u, log(K[v][u])))

    # zaczynamy z kazdej waluty
    dist:list[float] = [0] * n

    for _ in range(n-1):
        changed = False
        for v in range(n):
            for child, cost in graph[v]:
                if dist[child] > dist[v] + cost:
                    dist[child] = dist[v] + cost
                    changed = True 
        if not changed: break

    for v in range(n):
        for child, cost in graph[v]:
            if dist[child] > dist[v] + cost:
                return True
    return False

def solution():
    # TODO: Implement algorithm logic here
    pass

if __name__ == "__main__":
    solution()
