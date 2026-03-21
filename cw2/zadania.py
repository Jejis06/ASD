'''
1 
a) scalanie 2 list jednokierunkowych
b) merge sort na seriach naturalnych

'''
# zad 1 a
class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None

def scal(head1, head2):
    head = Node(0)
    tail = head
    while head1 is not None and head2 is not None:
        if head1.val < head2.val:
            tail.next = head1
            head1 = head1.next
        else:
            tail.next = head2
            head2 = head2.next
        tail = tail.next

    if head1 is not None: tail.next = head1
    if head2 is not None: tail.next = head2

    return head.next

# zad 1 b
def ciecie(head):
    if head is None: return (None, None)
    curr = head
    while curr.next is not None and curr.val < curr.next.val:
        curr = curr.next

    curr1 = curr.next
    curr.next = None
    return (head, curr1)

def mergesort(head):

    while True:
        cntr = 0
        res = Node(0)
        curr = res
        
        while head is not None:
            a, head = ciecie(head)
            l, head = ciecie(head)

            d = scal(a, l)
            curr.next = d

            while curr.next is not None:
                curr = d.next
            cntr += 1
        if cntr == 1:
            break
        head = res.next
    return res.next


'''
2 - done
wstawianie do kopca binarnego -- trza zrobic
'''

def parent(x): return (x-1) // 2
def left(x): return 2*x+1
def right(x): return 2*x+2

# insert min heap
def insert(heap, el):
    heap.append(el)
    curr_ind = len(heap) - 1

    while curr_ind > 0:
        par_ind = parent(curr_ind)
        if heap[curr_ind] < heap[par_ind]:
            heap[curr_ind], heap[par_ind] = heap[par_ind], heap[curr_ind]
            curr_ind = par_ind
        else: break


'''
3 - done 
posortuj tablice k - chaotyczna
T[i] -> T_sorted[j].
j nal do {i-k, i+k}
'''

def heapify(A, n, i):
    min_ind = i
    if left(i) < n and A[left(i)] < A[min_ind]:
        min_ind = left(i)
    if right(i) < n and A[right(i)] < A[min_ind]:
        min_ind = right(i)
    if min_ind != i:
        A[i], A[min_ind] = A[min_ind], A[i]
        heapify(A, n, min_ind)

def extract_min(heap):
    n = len(heap)
    if n == 0: return None
    if n == 1: return heap.pop()

    root = heap[0]
    heap[0] = heap.pop()

    heapify(heap, len(heap), 0)
    return root


def sort_chaotic(T, k):
    n = len(T)
    heap = []
    size = min(k+1, n)
    for i in range(size):
        insert(heap, T[i])

    target = 0
    for i in range(k+1, n):
        T[target] = extract_min(heap)
        target += 1
        insert(heap, T[i])

    while len(heap) > 0:
        T[target] = extract_min(heap)
        target += 1





'''
4 - done
sorted tablce A[n]
i liczba x znajdz i, j takie, ze
a) A[i] - A[j] = x ----- gasienica
b) A[i] + A[j]= x
'''

# zad 4 a
def find_diff(A, x):
    n = len(A)
    i = 0; j = 1
    while i < n:
        diff = A[j] - A[i]
        if diff == x: return (i, j)
        elif diff > x: i += 1
        else: j += 1

    return (None, None)
# zad 4 b
def find_sum(A, x):
    i = 0
    j = n-1

    while i < j:
        su = A[i] + A[j]
        if su == x: return (i, j)
        if su > x: j-= 1
        else: i += 1
    return (None, None)


'''
5 struktura (CIEKAWOSTKA)
insert
rem min
rem max
(2 kopce)
'''

'''
6 struktura  (CIEKAWOSTKA)
inster
remove mediana
'''

'''
7 zliczyc inwersje w talblicy
i < j, A[i] > A[j] (merge sort)
'''

def scal(A, B, p, q, r):
    inv = 0
    i = p; j = q; k = p
    while i < q and j < r:
        if A[i] <= A[j]:
            B[k] = A[i]
            i += 1
        else:
            B[k] = A[j]
            j += 1
            inv += (q - i) 
        k += 1

    while i < q:
        B[k] = A[i]
        k += 1
        i += 1

    while j < r:
        B[k] = A[j]
        k += 1
        j += 1

    for t in range(p, r):
        A[t] = B[t]
    return inv

def helper(A, B, p, r):
    inv = 0
    if r - p > 1:
        q = (p + r) // 2
        inv += helper(A, B, p, q)
        inv += helper(A, B, q, r)
        inv += scal(A, B, p, q, r)
    return inv

def calc(A):
    global res
    n = len(A)
    B = [0] * n

    return helper(A, B, 0, n)



'''
8 scalic k posortowanych list jednokierunkowych
o laczie n elementach w O(n log k)
'''

def par(x): return (x - 1) // 2 
def le(x): return 2 * x + 1 
def ri(x): return 2 * x + 2

def heapify_ll(A, i, n):
    min_ind = i; l = le(i); r = ri(i)

    if l < n and A[l].val < A[min_ind].val: min_ind = l
    if r < n and A[r].val < A[min_ind].val: min_ind = r

    if min_ind != i:
        A[i], A[min_ind] = A[min_ind], A[i]
        heapify_ll(A, min_ind, n)



def merge_lists(L):
    k = len(L)
    heap = L
    for i in range(par(k - 1), -1, -1):
        heapify_ll(L, i, k)


    head = Node(0)
    curr = head
    while k > 0:
        curr.next = heap[0]
        heap[0] = heap[0].next

        if heap[0] is None:
            heap[0], heap[k-1] = heap[k-1], heap[0]
            k -= 1

        heapify_ll(L, 0, k)
        curr = curr.next

    return head.next

def build_list(l):
    head = Node(0)
    curr = head
    for i in l:
        curr.next = Node(i)
        curr = curr.next
    return head.next

def print_list(head):
    while head is not None:
        print(head.val, end=' ')
        head = head.next
    print()
        

L = [ build_list([8,9,100]), build_list([1,2,3,4]),build_list([32,48,199])]
for li in L:
    print_list(li)
res = merge_lists(L)
print_list(res)
