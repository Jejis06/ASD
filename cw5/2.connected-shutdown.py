"""
Zadanie 2. Znany operator telefonii komórkowej Pause postanowił zakończyć
działalność w Polsce. Jednym z głównych elementów całej procedury jest
wyłączenie wszystkich stacji nadawczych (które tworzą spójny graf połączeń).
Ze względów technologicznych urządzenia należy wyłączać pojedynczo, a operatorowi
dodatkowo zależy na tym, by podczas całego procesu wszyscy abonenci znajdujący
się w zasięgu działających stacji mogli się ze sobą łączyć (czyli by graf
pozostał spójny). Proszę zaproponować algorytm podający kolejność wyłączania
stacji.
"""


# Nalezy usuwac tylko liscie w drzewie DFS poniewaz jako najglebsze wierzcholki nie rozspojniaja grafu
# lista sasiedztwa

# O(V + E)

def shutdown_ordering(G:list[list[int]]):
    n = len(G)
    vis:list[bool] = [False for _ in range(n)]
    post_order:list[int] = []

    def dfs(G:list[list[int]], vert:int):
        vis[vert] = True
        for child in G[vert]:
            if not vis[child]:
                dfs(G, child)

        post_order.append(vert)

    # zadanie sprowadza sie do zwrocenia tablicy post order
    return post_order



def solution():
    pass


if __name__ == "__main__":
    solution()
