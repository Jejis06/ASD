from zad2testy import runtests

class Node:
  def __init__(self):
    self.val = None     
    self.next = None 

def printheap(heap:list[Node]):
    print("Printing heap")
    for x in heap:
        print(x.val, end = ' ')
    print()

def left(x:int): return 2*x + 1
def right(x:int): return 2*x + 2
def parent(x:int): return (x - 1) // 2

def heapify(heap:list[Node], ind:int, bound:int):

    min_ind=ind; li = left(ind); ri = right(ind)


    if li < bound and heap[li].val < heap[min_ind].val:
        min_ind = li
    if ri < bound and heap[ri].val < heap[min_ind].val:
        min_ind = ri

    if min_ind != ind:
        heap[ind], heap[min_ind] = heap[min_ind], heap[ind]
        heapify(heap, min_ind, bound)

def heap_insert(heap:list[Node], node:Node):
    heap.append(node)
    curr_ind = len(heap) - 1

    while curr_ind > 0:
        par = parent(curr_ind)
        if heap[curr_ind].val < heap[par].val:
            heap[curr_ind], heap[par] = heap[par], heap[curr_ind]
            curr_ind = par
        else: break

def heap_pop(heap:list[Node]):
    if len(heap) == 1: 
        return heap.pop()

    head = heap[0]
    heap[0] = heap.pop()

    heapify(heap, 0, len(heap))
    return head


# O(n log k)
def SortH(p:Node|None,k:int):
    # tu prosze wpisac wlasna implementacje
    heap = []

    k = k+1
    
    res = Node() 
    curr = res

    if p is None: return None
    
    while p is not None:
        heap_insert(heap, p)
        p = p.next
        if len(heap) == k:
            curr.next = heap_pop(heap)
            curr = curr.next

    while len(heap) > 0:
        curr.next = heap_pop(heap)
        curr = curr.next

    curr.next = None

    return res.next


runtests( SortH ) 
