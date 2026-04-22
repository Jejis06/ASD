class PQ:
    def __init__(self):
        self.min_heap:list[tuple[int, int]] = []

    def __left(self, x:int): return 2 * x + 1
    def __right(self, x:int): return 2 * x + 2
    def __parent(self, x:int): return (x - 1) // 2

    def __heapify(self, i:int, n:int):
        min_ind = i
        li = self.__left(i); ri = self.__right(i)

        if li < n and self.min_heap[li] < self.min_heap[min_ind]:
            min_ind = li
        if ri < n and self.min_heap[ri] < self.min_heap[min_ind]:
            min_ind = ri

        if min_ind != i:
            self.min_heap[min_ind], self.min_heap[i] = self.min_heap[i], self.min_heap[min_ind]
            self.__heapify(min_ind, n)

    def size(self): return len(self.min_heap)

    def __bool__(self):
        return self.size() > 0

    def pop(self) -> tuple[int,int]:
        if self.size() == 1:
            return self.min_heap.pop()

        ret = self.min_heap[0]
        self.min_heap[0] = self.min_heap.pop()

        self.__heapify(0, self.size())
        return ret

    def insert(self, el:tuple[int, int]):
        self.min_heap.append(el)
        curr_ind = self.size() - 1
        while curr_ind > 0:
            par = self.__parent(curr_ind)
            if self.min_heap[par] > self.min_heap[curr_ind]:
                self.min_heap[par], self.min_heap[curr_ind] =  self.min_heap[curr_ind], self.min_heap[par]
                curr_ind = par
            else: break




