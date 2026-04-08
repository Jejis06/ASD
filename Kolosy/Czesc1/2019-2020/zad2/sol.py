

def quickselect(arr:list[int], k:int, lo:int, hi:int):
    while lo < hi:
        q = partition(arr, lo, hi)
        if q == k: return 
        elif q < k: lo = q + 1
        else: hi = q - 1

def partition(arr:list[int], lo:int, hi:int):
    x = arr[hi]
    i = lo - 1
    for j in range(lo, hi+1):
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    return i

def quicksort(arr:list[int], lo:int, hi:int):
    if hi > lo:
        q = partition(arr, lo, hi)
        quicksort(arr, lo, q-1)
        quicksort(arr, q+1 , hi)


def section(T:list[int], p:int, q:int):
    n = len(T)
    q, p = p, q
    p = n - p - 1
    q = n - q - 1
    quickselect(T, q, 0, n-1)
    quickselect(T, p, 0, n-1)

    quicksort(T, p, q)
    arr = T[p:q + 1][::-1]
    return arr

T = [1, 4, 2, 5, 3, 8, 6, 7]
print(T)
print(sorted(T, reverse=True))
print(section(T, 1, 3) )
