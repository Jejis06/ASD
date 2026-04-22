multitype = int | str | bool | list[int] # itd ...

# wszystkie operacje w  zamortyzowanym koszcie O(log*n) - logarytm iterowany

# Reprezentacja Nodeowa
class Node:
    def __init__(self, val:multitype):
        self.parent:Node     = self
        self.rank:int        = 0
        self.value:multitype = val

def find_set(a:Node) -> Node:
    if a != a.parent:
        a.parent = find_set(a.parent)
    return a.parent

def union(a:Node, b:Node):
    a = find_set(a)
    b = find_set(b)

    if a == b: return
    if a.rank > b.rank:
        b.parent = a
    else:
        a.parent = b
        if a.rank == b.rank:
            b.rank += 1


# Reprezentacja tablicowa
class FindUnion:
    def __init__(self, n:int):
        self.parent:list[int] = list( range(n) )
        self.rank:list[int] = [0] * n

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




