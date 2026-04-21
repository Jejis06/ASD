"""
Zadanie 8. Ścieżka Hamiltona to ścieżka przechodząca przez wszystkie wierzchołki
w grafie, przez każdy dokładnie raz. W ogólnym grafie znalezienie ścieżki
Hamiltona jest problemem NP-trudnym. Proszę podać algorytm, który stwierdzi
czy istnieje ścieżka Hamiltona w acyklicznym grafie skierowanym.
"""


graph_nei = list[list[int]]

def hamilton_path(G:graph_nei):

    n = len(G)
    vis = [False] * n
    post_order:list[int] = []

    def dfs(G:graph_nei, vert:int):
        vis[vert] = True
        for child in G[vert]:
            if not vis[child]:
                dfs(G, child)
        post_order.append(vert)

    for i in range(n-1, 0, -1):
        if post_order[i-1] not in G[post_order[i]]:
            return False
    return True




def solution():
    # TODO: Implement algorithm logic here
    pass

if __name__ == "__main__":
    solution()
