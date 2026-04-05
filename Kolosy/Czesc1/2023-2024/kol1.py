from kol1testy import runtests


ranks = []

lt = list[tuple[int,int]]


def merge(T:lt, B:lt, p:int, q:int, r:int):
    global ranks
    i = p; j = q; k = p

    while i < q and j < r:
        if T[i][0] < T[j][0]:
            B[k] = T[i]
            i += 1
        else:
            B[k] = T[j]
            ranks[T[j][1]] += (i - p)
            j += 1
        k += 1

    while i < q:
        B[k] = T[i]
        i += 1
        k += 1

    while j < r:
        B[k] = T[j]
        ranks[T[j][1]] += (i - p)
        j += 1
        k += 1

    T[p:r] = B[p:r]


def ranker(T:lt, B:lt, p:int, r:int):
    if r - p > 1:
        q = (p + r) // 2
        ranker(T, B, p, q)
        ranker(T, B, q, r)

        merge(T, B, p, q, r)



def maxrank(T:list[int]):
    global ranks

    n = len(T)
    ranks = [0 for _ in range(n)]
    arr:lt = [(0,0) for _ in range(n)]

    for i in range(n):
        arr[i] = (T[i], i)

    n = len(T)
    B = [(0,0) for _ in range(n)] 
    ranker(arr, B, 0, n)
    return max(ranks)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maxrank, all_tests = True)
