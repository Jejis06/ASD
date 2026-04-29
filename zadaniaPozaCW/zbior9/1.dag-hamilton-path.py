"""
Zadanie 1. (ścieżka Hamiltona w DAGu) Ścieżka Hamiltona to ścieżka 
przechodząca przez wszystkie wierzchołki w grafie, przez każdy dokładnie raz. 
W ogólnym grafie znalezienie ścieżki Hamiltona jest problemem NP-trudnym. 
Proszę podać algorytm, który stwierdzi czy istnieje ścieżka Hamiltona 
w acyklicznym grafie skierowanym.
"""


graph_nei = list[list[int]]

def existshamilton(graph:graph_nei) -> bool:

    n = len(graph)
    post_order:list[int] = []
    vis:list[bool] = [False] * n

    def dfs(vert:int):
        vis[vert] = True
        for child in graph[vert]:
            if not vis[child]:
                dfs(child)
        post_order.append(vert)

    for i in range(n):
        if not vis[i]:
            dfs(i)

    if len(post_order) != n: return False
    for i in range(n-1, 0, -1):
        if post_order[i-1] not in graph[post_order[i]]:
            return False
    return True


def solution():
    # TODO: Implement algorithm logic here
    pass

if __name__ == "__main__":
    solution()
