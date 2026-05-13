'''
Bitoniczny problem komiwojazera:
 - miasta to punkty w R^2
 - trasa tylko raz zmienia kierunek
 - kazdy punkt ma inna wspolrzedna
 - x1, ... , xn - kolejne miasta posortowane wzgl x

[ O(n^2) ]

'''
from math import sqrt

def bitonic_tsp(cities:list[tuple[int,int]]) -> float:

    n = len(cities)

    # if n <= 1: return 0.0                               |
    # cities = sorted(cities, key = lambda x: x[0])       |_----> zabezpieczenia


    dist:list[list[float]] = [[0 for _ in range(n) ] for _ in range(n)]

    for i in range(n):
        for j in range(i+1, n):
            x1, y1 = cities[i]
            x2, y2 = cities[j]

            dist[i][j] = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    
    dp_mem = [[float('inf') for _ in range(n)] for _ in range(n)]

    dp_mem[0][1] = dist[0][1]

    def dp(i:int, j:int) -> float:
        if dp_mem[i][j] != float('inf'): return dp_mem[i][j]

        if i < j - 1:
            dp_mem[i][j] = dp(i, j-1) + dist[j-1][j]
        else:
            for k in range(j-1):
                dp_mem[i][j] = min(dp_mem[i][j], dp(k, j-1) + dist[k][j])
        return dp_mem[i][j]
    
    min_path = float('inf')
    for i in range(n-1):
        min_path = min(min_path, dp(i, n-1) + dist[i][n-1])

    return min_path


        


