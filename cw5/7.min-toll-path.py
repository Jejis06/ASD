"""
Zadanie 7. Dana jest mapa kraju w postaci grafu G = (V, E). Kierowca chce
przejechać z miasta (wierzchołka) s do miasta t. Niestety niektóre drogi
(krawędzie) są płatne. Każda droga ma taką samą jednostkową opłatę. Proszę
podać algorytm, który znajduje trasę wymagającą jak najmniejszej liczby opłat.
W ogólności graf G jest skierowany, ale można najpierw wskazać algorytm dla
grafu nieskierowanego.
"""

from collections import deque

graph_neighbor = list[list[tuple[int,int]]]

# wagi (0,1)

def find_cheapes_path(G:graph_neighbor, s:int, t:int) -> list[int]:
    n = len(G)
    parent:list[int] = [-1 for _ in range(n)]
    dist:list[int]   = [ -1 for _ in range(n)]


    q: deque[int] = deque([s])





def solution():
    # TODO: Implement algorithm logic here

    pass

if __name__ == "__main__":
    solution()
