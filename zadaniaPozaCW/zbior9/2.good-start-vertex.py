"""
Zadanie 2. (dobry początek) Wierzchołek v w grafie skierowanym nazywamy 
dobrym początkiem jeśli każdy inny wierzchołek można osiągnąć scieżką 
skierowaną wychodzącą z v. Proszę podać algorytm, który stwierdza czy 
dany graf zawiera dobry początek.
"""

graph_nei= list[list[int]]

def good_start(graph:graph_nei):
    n = len(graph)
    post_ortder:list[int] = []
    vis:list[bool] = [False] * n

    def dfs(vert:int):
        vis[vert] = True
        for child in graph[vert]:
            if not vis[child]:
                dfs(child)
        post_ortder.append(vert)

    enc_verts = 0
    def dfs_validate(vert:int):
        nonlocal enc_verts
        vis[vert] = False
        enc_verts += 1
        for child in graph[vert]:
            if vis[child]:
                dfs_validate(child)

    for vert in range(n):
        if not vis[vert]:
            dfs(vert)


    candidate = post_ortder[n-1]
    dfs_validate(candidate)

    return enc_verts == n





def solution():
    # TODO: Implement algorithm logic here
    pass

if __name__ == "__main__":
    solution()
