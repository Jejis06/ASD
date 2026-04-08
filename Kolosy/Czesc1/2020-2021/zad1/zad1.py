from zad1testy import runtests

def partition(arr:list[int], lo:int, hi:int):
    x = arr[hi]
    i = lo - 1
    for j in range(lo, hi+1):
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    return i

def quickselect(arr:list[int], k:int, lo:int, hi:int):
    while hi > lo:
        p = partition(arr, lo, hi)

        if p == k: return
        elif p < k: lo = p + 1
        else: hi = p - 1


def Median(T:list[list[int]]):
    n = len(T)
    N = n * n
    A = [0] * N 

    diag_upper = (N + n) // 2
    diag_lower = (N - n) // 2

    # linearize T
    for i in range(n):
        for j in range(n):
            A[i*n + j] = T[i][j]

    quickselect(A, diag_lower, 0, N-1)
    quickselect(A, diag_upper, 0, N-1)

    # Setting diag
    ind = diag_lower
    for i in range(n):
        T[i][i] = A[ind]
        ind += 1

    # Setting lower half - lower vals
    ind = 0 
    for i in range(n):
        for j in range(i):
            T[i][j] = A[ind]
            ind += 1
    # Setting upper half - higher vals
    ind = diag_upper
    for i in range(n):
        for j in range(i+1, n):
            T[i][j] = A[ind]
            ind += 1

    return 

runtests( Median ) 
