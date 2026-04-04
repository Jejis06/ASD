from kol1testy import runtests
from random import randint


def select_sort(A:list[float]):
    n = len(A)
    for i in range(1, n):
        key = A[i]
        j = i - 1
        while j >=0 and A[j] > key:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = key

# [p, k+1]
def bucket_sort(A:list[float], p:int, k:int, min_val:float, max_val:float):
    buckets:list[list[float]] = [[] for _ in range(k - p)]

    multiplier = (max_val - min_val)  / (k-p-1)
    for i in range(p, k):
        ind = int( (A[i] - min_val) / multiplier )
        buckets[ind].append(A[i])

    ind = p
    for i in range(k-p):
        select_sort(buckets[i])
        for j in range(len(buckets[i])):
            A[ind] = buckets[i][j]
            ind += 1

def find_kth(A:list[float], beg:int, en:int, k:int):
    while beg <= en:
        piv = pivot(A, beg, en)

        if piv == k:
            return A[piv]
        elif piv > k:
            en = piv - 1
        else:
            beg = piv + 1

def pivot(A:list[float], beg:int, en:int):
    x = randint(beg, en)
    A[x], A[en] = A[en], A[x]
    x = A[en]
    i = beg - 1
    for j in range(beg, en + 1):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    return i
        

def ogrodzenie(M:float, D:float, T:list[float]) -> int:
    n = len(T)

    mid = n // 2

    p:float = find_kth(T, 0, n-1, mid)
    bucket_sort(T, 0, mid, 0, p)
    bucket_sort(T, mid, n, p, M)


    res = 0
    for i in range(1,n):
        if T[i] - T[i-1] >= D:
            res += 1
        i += 1

    return res
                

# zmien all_tests na True zeby
runtests( ogrodzenie, all_tests = True )
