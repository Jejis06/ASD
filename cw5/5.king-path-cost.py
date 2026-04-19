"""
Zadanie 5. Dana jest szachownica o wymiarach n x n. Każde pole (i,j) ma koszt
(liczbę ze zbioru {1, ..., 5}) umieszczony w tablicy A (w polu A[j][i]).
W lewym górnym rogu szachownicy stoi król, którego zadaniem jest przejść do
prawego dolnego rogu, przechodząc po polach o minimalnym sumarycznym koszcie.
Prosze zaimplementować funkcję kings_path(A), która oblicza koszt ścieżki króla.
Funkcja powinna być możliwie jak najszybsza.
"""
from collections import deque
graph_neighbor = list[list[int]]


# O((V + E) * 5) -> O(V + E)
# BFS division of verticies
def kings_path(G:graph_neighbor) -> int:
    n = len(G)
    cost = [[0 for _ in range(n)] for _ in range(n)]
    vis = [[False for _ in range(n)] for _ in range(n)]
    q:deque[tuple[int,int,int, int]]= deque([(0,0,0,0)])

    while q:
        i, j, curr_cost , delay = q.popleft()
        if delay > 0:
            q.append((i, j, curr_cost+1, delay -1))
            continue
        if vis[j][i] == True: continue

        vis[j][i] = True
        cost[j][i] = curr_cost
        if i == n-1 and j == n-1: return curr_cost


        dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1),  (0, 1), (1, -1), (1, 0), (1, 1)]
        for d_i, d_j in dirs:
            ch_j = j + d_j
            ch_i = i + d_i
            if 0 <= ch_i < n and 0 <= ch_j < n:
                if not vis[ch_j][ch_i]:
                    q.append((ch_i, ch_j, curr_cost+1, G[ch_j][ch_i]-1))
    return cost[n-1][n-1]


# O (V + E) dijkstra ale bez kolejki priorytetowej tylko kubelki
def kings_path_kindaDijkstra(G:graph_neighbor) -> int:

    n = len(G)

    cost_buckets:list[deque[tuple[int,int]]] = [deque() for _ in range(6)] # kubelki odpowiednio dla kazdej z wartosci
    dist: list[list[int]] = [[float('inf') for _ in range(n)] for _ in range(n)]
    dist[0][0] = 0
    curr_dist = dist[0][0]
    processed = 0

    dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1),  (0, 1), (1, -1), (1, 0), (1, 1)]

    while processed < n * n:
        while not cost_buckets[curr_dist % 6]:
            curr_dist += 1

        i, j = cost_buckets[curr_dist % 6].popleft()

        if i == n-1 and j == n-1: return curr_dist
        if curr_dist > dist[j][i]: continue

        processed += 1
        for di, dj in dirs:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < n:
                cost = G[nj][ni]
                if dist[j][i] + cost < dist[nj][ni]:
                    dist[nj][ni] = dist[j][i] + cost
                    cost_buckets[dist[nj][ni] % 6].append((ni, nj))

    return dist[n-1][n-1]



def solution():
    # TODO: Implement algorithm logic here
    pass

if __name__ == "__main__":
    solution()
