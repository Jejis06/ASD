"""
Zadanie 6. (szachuję) Algocja leży na wielkiej pustyni i składa 
się z miast oraz oaz połączonych drogami. Każde miasto jest 
otoczone murem i ma tylko dwie bramy północną i południową. 
Z każdej bramy prowadzi dokładnie jedna droga do jednej oazy 
(ale do danej oazy może dochodzić dowolnie wiele dróg: oazy mogą 
też być połączone drogami między sobą). Prawo Algocji wymaga, 
że jeśli ktoś wjechał do miasta jedną bramą, to musi go opuścić 
drugą. Szach Algocji postanowił wysłać gońca, który w każdym 
mieście kraju odczyta zakaz formułowania zadań "o szachownicy" 
(obraza majestatu). Szach chce, żeby goniec odwiedził każde 
miasto dokładnie raz (ale nie ma ograniczeń na to ile razy odwiedzi 
każdą z oaz). Goniec wyjeżdża ze stolicji Algocji, miasta z, 
i po odwiedzeniu wszystkich miast ma do niej wrócić. Proszę 
przedstawić algorytm, który stwierdza czy odpowiednia trasa gońca 
istnieje.
"""

class FindUnion:
    def __init__(self, size:int):
        self.parent:list[int] = list(range(size))
        self.rank:list[int] = [0] * size
    def find(self, a:int) -> int:
        if a != self.parent[a]:
            self.parent[a] = self.find(self.parent[a])
        return self.parent[a]
    def union(self, a:int, b:int):
        a = self.find(a)
        b = self.find(b)

        if a == b: return

        if self.rank[a] > self.rank[b]:
            self.parent[b] = a
        else:
            self.parent[a] = b
            if self.rank[a] == self.rank[b]:
                self.rank[b] += 1



def szach(cities:list[tuple[int,int]], oasis_edges:list[tuple[int,int]], num_oasis:int, x:int):

    fu = FindUnion(num_oasis)

    for oasis_a, oasis_b in oasis_edges:
        fu.union(oasis_a, oasis_b)

    oasis_super_graph:list[list[int]] = [[] for _ in range(num_oasis)]
    deg:list[int] = [0] * (num_oasis)

    for oasis_a, oasis_b in cities:
        u = fu.find(oasis_a)
        v = fu.find(oasis_b)

        deg[u] += 1; deg[v] += 1

        oasis_super_graph[u].append(v)
        oasis_super_graph[v].append(u)

    vis = [False] * (num_oasis)

    for i in range(num_oasis):
        if deg[i] % 2 != 0: return False

    def dfs(vert:int):
        vis[vert] = True
        for child in oasis_super_graph[vert]:
            if not vis[child]:
                dfs(child)

    start_oasis = cities[x][0]
    start_node = fu.find(start_oasis)

    dfs(start_node)

    for i in range(num_oasis):
        if deg[i] > 0 and not vis[i]:
            return False
    return True


def solution():
    # TODO: Implement algorithm logic here
    pass

if __name__ == "__main__":
    solution()
