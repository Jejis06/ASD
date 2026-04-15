
# Zalozenie: Graf nieskierowany

# !!!! ABY CYKL EULERA WGL ISTNIAL dla kazdego v musi zachodzic deg(v) % 2 == 0 oraz graf spojny !!!!

# O(V^2 + E + V) -> O(V^2 + E)
# lista sasiedztwa
def euler_brut(Graph:list[list[int]]):
    n = len(Graph)
    deleted_verts = [[False for _ in range(n)] for _ in range(n)]

    cycle:list[int] = []

    def dfs(Graph:list[list[int]], vert:int):
        nonlocal deleted_verts, cycle

        for child in Graph[vert]:
            min_v = min(vert, child)
            max_v = max(vert, child)

            if not deleted_verts[min_v][max_v]:
                deleted_verts[min_v][max_v] = True
                dfs(Graph, child)
        cycle.append(vert)

    dfs(Graph, 0)
    return cycle # [::-1] w przypadku skierowanego albo gdy cykl ma byc w porzadku leksykograficznym


# O(V + E)
# lista sasiedztwa ale kazda taka podlista jest posortowana rosnaco
def euler_sorted_verts(Graph:list[list[int]]):
    n = len(Graph)

    idx:list[int] = [0] * n
    cycle:list[int] = []

    def dfs(vert:int):
        nonlocal Graph, cycle, idx
        while idx[vert] < len(Graph[vert]):
            child = Graph[vert][ idx[vert] ]
            idx[vert] += 1
            if idx[child] >= len(Graph[child]) or Graph[child][idx[child]] > vert:
                continue
            dfs(child)
        cycle.append(vert)
    dfs(0)
    return cycle # [::-1] w przypadku skierowanego albo gdy cykl ma byc w porzadku leksykograficznym



