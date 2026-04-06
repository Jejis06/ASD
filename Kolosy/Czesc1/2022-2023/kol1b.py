from kol1testy import runtests
from queue import PriorityQueue

"""
Algorytm:
Zlozonosc:
"""

def ksum(T, k, p):

    n = len(T)
    min_heap = PriorityQueue() # (val, ind)
    max_heap = PriorityQueue() # (-val, ind)

    in_min = [False] * n

    def clean_min(i:int):
        nonlocal p
        val, ind = 0, 0
        while not min_heap.empty():
            val, ind = min_heap.get()
            if ind > i - p: break
        min_heap.put((val, ind))

    def clean_max(i:int):
        nonlocal p
        val, ind = 0, 0
        while not max_heap.empty():
            val, ind = max_heap.get()
            if ind > i - p: break
        max_heap.put((val, ind))

    # first batch
    for i in range(p):
        max_heap.put((-T[i], i))

    for i in range(k):
        val, ind = max_heap.get()
        min_heap.put((-val, ind))
        in_min[ind] = True

    min_size = k
    max_size = p - k

    ans, ind = min_heap.get()
    min_heap.put((ans, ind))

    for i in range(p, n):
        left_ind = i - p

        if in_min[left_ind]: min_size -= 1
        else: max_size -= 1

        el = T[i]
        clean_min(i)

        # nowy element w kopcach
        flag = True
        if not min_heap.empty():
            topv, topind = min_heap.get()
            min_heap.put((topv, topind))

            if el >= topv:
                flag = False
                min_heap.put((el, i))
                in_min[i] = True
                min_size += 1
        elif flag:
            max_heap.put((-el,i))
            in_min[i] = False
            max_size += 1

        if min_size > k:
            clean_min(i)
            pval, pind = min_heap.get()
            max_heap.put((-pval, pind))
            in_min[pind] = False
            min_size -= 1
            max_size += 1

        elif min_size < k:
            clean_max(i)
            pval, pind = max_heap.get()
            min_heap.put((-pval, pind))
            in_min[pind] = True
            min_size += 1
            max_size -= 1

        clean_min(i)
        topv, topind = min_heap.get()
        min_heap.put((topv, topind))

        ans += topv




    return ans


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ksum, all_tests=False )
