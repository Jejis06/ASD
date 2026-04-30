"""
Zadanie 8. (najlepszy korzeń) Dany jest acykliczny, spójny 
nieskierowany, ważony graf T (czyli T jest tak naprawdę ważonym 
drzewem). Proszę wskazać algorytm, który znajduje taki 
wierzchołek T, z którego odległość do najdalszego wierzchołka 
jest minimalna.
"""

def min_V(graph:list[list[tuple[int,int]]]):
    n = len(graph)
    dist1 = [0] * n

    max_dist = 0
    max_v =-1 

    def dfs1(vert:int, parent:int):
        nonlocal max_dist, max_v
        for child, cost in graph[vert]:
            if child != parent:
                dist1[child] = dist1[vert] + cost
                if dist1[child] > max_dist:
                    max_dist = dist1[child]
                    max_v = child 
                dfs1(child, vert)
    dfs1(0, -1)

    dist2 = [0] * n
    parent = [-1] * n
    max_dist = 0
    max_u = -1 

    def dfs2(vert:int, par:int):
        nonlocal max_dist, max_u
        for child, cost in graph[vert]:
            if child != par:
                dist2[child] = dist2[vert] + cost
                parent[child] = vert
                if dist2[child] > max_dist:
                    max_dist = dist2[child]
                    max_u = child
                dfs2(child, vert)
    dfs2(max_v, -1)

    min_v = 0

    min_dist = max_dist 
    curr_v = max_u

    while curr_v != -1:
        curr_dist = max(dist2[curr_v], max_dist - dist2[curr_v])
        if curr_dist < min_dist:
            min_dist = curr_dist
            min_v = curr_v

        curr_v = parent[curr_v]
    return min_v
            





def solution():
    # TODO: Implement algorithm logic here
    pass

if __name__ == "__main__":
    solution()
