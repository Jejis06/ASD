"""
Zadanie 3. (SAT-2CNF) Dana jest formuła logiczna w postaci 2CNF. 
To znaczy, że formuła jest koniunkcją klauzuli, gdzie każda klauzula 
to alternatywa dwóch literałów, a każdy literał to zmienna lub jej 
negacja. Przykładem formuły w postaci 2CNF nad zmiennymi 
x,y,z jest: 
(Ivy) (Vz) (V). 
Proszę podać algorytm, który w czasie wielomianowym stwierdza, czy 
istnieje wartościowanie spełniające formulę.
"""

# przyjmujemy ze formuly podawane sa nastepujaco
# dla takiej (a v  b) ^ (~a v c) ^ (~c v ~b)
# a - 1  ~a - 3 + 1 = 4
# b - 2  ~b - 3 + 2 = 5
# c - 3  ~c - 3 + 3 = 6
# otrzymyjemy [(1, 2), (4, 3), (6, 5)]

# jezeli formula jest spelnialna to nie ma sprzecznosci
def exists_completenes(formula:list[tuple[int,int]], num_vars:int) -> bool:
    n = 2 * (num_vars +1)
    graph:list[list[int]] = [[] for _ in range(n)]
    graph_t:list[list[int]] = [[] for _ in range(n)]

    def get_neg(x:int)->int:
        if x > num_vars:
            return x - num_vars
        return x + num_vars

    for u, v in formula:
        neg_u = get_neg(u)
        neg_v = get_neg(v)

        graph[neg_u].append(v)
        graph[neg_v].append(u)

        graph_t[v].append(neg_u)
        graph_t[u].append(neg_v)

    vis = [False] * n
    post_order:list[int]=  []

    def dfs_normal(vert:int):
        vis[vert] = True
        for child in graph[vert]:
            if not vis[child]:
                dfs_normal(child)
        post_order.append(vert)

    for vert in range(1, n):
        if not vis[vert]:
            dfs_normal(vert)

    scc_id = [0] * n

    def dfs_latter(vert:int, curr_id:int):
        vis[vert]= False
        for child in graph_t[vert]:
            if vis[child]:
                dfs_latter(child, curr_id)
        scc_id[vert] = curr_id
    
    curr_id = 1
    for i in range(len(post_order)-1, -1, -1):
        vert = post_order[i]
        if vis[vert]:
            dfs_latter(vert, curr_id)
            curr_id += 1

    for i in range(1, num_vars+1):
        if scc_id[i] == scc_id[i + num_vars]:
            return False



    return True



def solution():
    # TODO: Implement algorithm logic here
    pass

if __name__ == "__main__":
    solution()
