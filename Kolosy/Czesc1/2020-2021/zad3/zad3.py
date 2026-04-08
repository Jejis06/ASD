from zad3testy import runtests


def dystrybutanta(x:float, P:list[tuple[float, float, float]]) -> float:
    prob = 0.0
    for a, b, c in P:
        if x > b: prob += c
        elif a <= x <= b:
            prob += c * (x - a) / (b - a)
    return prob


def insert_sort(arr:list[float]):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j + 1] = key



def SortTab(T:list[float],P:list[tuple[float, float, float]]):
    n = len(T)
    buckets:list[list[float]] = [[] for _ in range(n)]

    for el in T:
        ind = int( dystrybutanta(el, P) * n )
        if ind == n: ind -= 1
        buckets[ind].append(el)

    ind = 0
    for i in range(n):
        insert_sort(buckets[i])
        for j in range(len(buckets[i])):
            T[ind] = buckets[i][j]
            ind += 1
    return T

runtests( SortTab )
