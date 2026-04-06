from kol1testy import runtests

"""
Algorytm: 
    Program rozwiazuje zadanie z wykorzystaniem 2 kopcow (min, max) w kopcu min przechowywane jest zawsze k najwiekszych elementow z rozwazanego przedzialu, natomiast w max pozostale p-k
    elementow. Zastosowanie 2 kopcow umozliwia nam w czasie logarytmicznym balansowac min kopiec (tj w przypadku kiedy kolejne okno nie zawiera jakiegos elementu ktory poprzednio znajdowal
    sie w min kopcu). Liczba z_i dla danego przedzialu i poprawnie zbalansowanego min_kopca znajduje sie w min_kopiec[0][0] ( bo jest to wlasnie w zasadzie k-ta co do wielkosci liczba z danego okna).
    Aby nie trzeba bylo tworzyc nowego min_kopca dla kazdego kolejnego okna skoro wiemy ze nowe okno dodaje nam jedna wartosc i odbiera inna musimy tylko wiedziec w ktorym kopcu usuwana wartosc sie
    znajduje oraz do ktorego kopca ma wpadac kolejna. Usuwanie elementow dziala na zasadzie leniwego usuwania po indeksach, tj jezeli zapiszemy z kazda wartoscia jej indeks i znamy poczatek i koniec naszego
    okna to w przypadku napotkania w headzie dowolnego z kopcow tej wartosci z tym indeksem mozemy wtedy ja usunac zamiast przeszukiwac caly kopiec i usuwac ja na bierzaco. w przypadku braku w min kopcu
    wiemy ze do k-1 najwiekszych wartosci trzeba dodac najwieksza z p-k innych czyli head z max_kopca.

Zlozonosc:
    poczatkowe tworzenie kopcow: O(2n)
    dodajemy zawsze maksymalnie n wartosci do jednego z kopcow: O(nlogp)
    odejmujemy zawsze maksymalnie n wartosci z jednego z kopcow: O(nlogp)

    ostatecznie : O(2n + nlogp -> nlogp -> nlogn)
"""

lt = list[tuple[int,int]]

def left(x:int): return 2*x+1
def right(x:int): return 2*x+2
def parent(x:int): return (x - 1) // 2

# min heap
def heapify(heap:lt, ind:int, bound:int): # O(logn)
    max_ind:int = ind
    left_ind = left(ind); right_ind = right(ind)

    if left_ind < bound and heap[left_ind][0] < heap[max_ind][0]:
        max_ind = left_ind
    if right_ind < bound and heap[right_ind][0] < heap[max_ind][0]:
        max_ind = right_ind

    if max_ind == ind: return
    heap[max_ind], heap[ind] = heap[ind], heap[max_ind]
    heapify(heap, max_ind, bound)

def make_heap(heap:lt): # O(n)
    n = len(heap)
    for i in range(parent(n-1), -1, -1):
        heapify(heap, i, n)

def pop_heap(heap:lt) -> tuple[int, int]: # O(logn)

    if len(heap) == 1:
        return heap.pop()

    head = heap[0]
    heap[0] = heap.pop()
    n = len(heap)
    heapify(heap, 0, n)
    return head

def insert_heap(heap:lt, el:tuple[int,int]): # O(logn)
    heap.append(el)
    curr_ind = len(heap) - 1

    while curr_ind > 0:
        parent_ind = parent(curr_ind)
        if heap[parent_ind][0] > heap[curr_ind][0]:
            heap[parent_ind], heap[curr_ind] = heap[curr_ind], heap[parent_ind]
            curr_ind = parent_ind
        else: break

def fix_heap(heap:lt, pos:int, p:int):
    while len(heap) > 0 and heap[0][1] <= pos - p:
        _ = pop_heap(heap)

def ksum(T:list[int], k:int, p:int) -> int:
    n = len(T)

    min_heap:lt = []
    max_heap:lt = []

    min_size = k

    in_min_heap:list[bool] = [False for _ in range(n)]

    for i in range(p):
        max_heap.append((-T[i], i))
    make_heap(max_heap)

    for i in range(k):
        negval, ind = pop_heap(max_heap)
        in_min_heap[ind] = True
        min_heap.append((-negval, ind))

    make_heap(min_heap)

    sum_total:int = min_heap[0][0]

    for i in range(p, n):

        left_ind = i - p
        new_el = T[i]

        if in_min_heap[left_ind]: min_size -= 1

        # insertion of new element to either of heaps
        if new_el > min_heap[0][0]:
            fix_heap(min_heap, i, p)
            insert_heap(min_heap, (new_el, i))
            in_min_heap[i] = True
            min_size += 1
        else:
            fix_heap(max_heap, i, p)
            insert_heap(max_heap, (-new_el, i))
            in_min_heap[i] = False

        # fixing heaps
        if min_size > k:
            fix_heap(min_heap, i, p)
            val, ind = pop_heap(min_heap)

            min_size -= 1

            in_min_heap[ind] = False
            insert_heap(max_heap, (-val, ind))
        elif min_size < k:
            fix_heap(max_heap, i, p)
            nval, ind = pop_heap(max_heap)

            min_size += 1

            in_min_heap[ind] = True
            insert_heap(min_heap, (-nval, ind))

        fix_heap(min_heap, i, p)
        sum_total += min_heap[0][0]


    return sum_total 

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ksum, all_tests=True)
