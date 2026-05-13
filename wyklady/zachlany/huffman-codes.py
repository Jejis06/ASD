
'''
generator kodow huffmana

[ O(nlogn)]
'''


class Node:
    def __init__(self, symbol:str|None, prop:int, ind:int):
        self.prop: int = prop
        self.symbol: str | None = symbol
        self.ind:int = ind

        self.parent: Node | None = None
        self.left: Node | None = None
        self.right: Node | None = None

class NodePQ:
    def __init__(self):
        self.min_heap:list[Node] = []

    def size(self): return len(self.min_heap)

    def __bool__(self):
        return self.size() > 0

    def __left(self, x:int): return 2*x + 1
    def __right(self, x:int): return 2*x + 2
    def __parent(self, x:int): return (x - 1) // 2

    def __heapify(self, i:int, n:int):
        min_ind = i
        li = self.__left(i) ; ri = self.__right(i)

        if li < n and self.min_heap[li].prop < self.min_heap[min_ind].prop:
            min_ind = li
        if ri < n and self.min_heap[ri].prop < self.min_heap[min_ind].prop:
            min_ind = ri

        if min_ind != i:
            self.min_heap[min_ind], self.min_heap[i] = self.min_heap[i], self.min_heap[min_ind]
            self.__heapify(min_ind, n)

    def pop(self) -> Node:
        if self.size() == 1:
            return self.min_heap.pop()
        ret = self.min_heap[0]

        self.min_heap[0] = self.min_heap.pop()
        self.__heapify(0, self.size())

        return ret

    def insert(self, node:Node):
        self.min_heap.append(node)
        curr_ind = self.size() - 1

        while curr_ind > 0:
            par = self.__parent(curr_ind)
            if self.min_heap[par].prop > self.min_heap[curr_ind].prop:
                self.min_heap[par], self.min_heap[curr_ind] = self.min_heap[curr_ind], self.min_heap[par]
                curr_ind = par
            else: break

def generate_huffman_coding(symbols:list[tuple[str, int]]):

    n = len(symbols)

    pq = NodePQ()

    ind = 0
    for (symbol, prop) in symbols:
        node = Node(symbol, prop, ind)
        ind += 1
        pq.insert(node)

    while pq.size() != 1:
        node1 = pq.pop()
        node2 = pq.pop()

        joint_node = Node(None, node1.prop + node2.prop, -1)

        node1.parent = joint_node
        node2.parent = joint_node

        joint_node.left = node1
        joint_node.right = node2

        pq.insert(joint_node)

    head = pq.pop()
    encodings:list[str] = ["" for _ in range(n)]   # encodings saved in the same order as symbols

    def retrieve_codes(curr:Node, path:str):
        if curr.symbol is not None and curr.ind != -1:
            encodings[curr.ind] = path
            return

        if curr.left != None:
            retrieve_codes(curr.left, path + '0')
        if curr.right != None:
            retrieve_codes(curr.right, path + '1')
    
    retrieve_codes(head, "")
    print(symbols)
    print(encodings)


    
    

A = [ ('a', 500), ('b', 5), ('c', 20), ('d', 300), ('e', 700), ('f', 67) ]
generate_huffman_coding(A)











