"""
2. T(N), Vi T[i] nal do (0, k-1)
znajdz i,j T[i:j] ze zawiera wszystkie kolory i jest najmniejszy O(N) zamort
"""
from random import randint

def solution(T:list[int], k:int):
    n = len(T)
    cols = [0] * (k + 1)
    print(cols)

    cols[T[0]] += 1
    aquired = 1

    max_j =n
    max_i = 0
    j = 1; i = 0 
    cols[T[1]] += 1
    if cols[T[1]] < 2: aquired += 1
    while j < n and max_j - max_i >= k:
        if aquired < k:
            if j == n-1: break
            j += 1
            cols[T[j]] += 1
            if cols[T[j]] - 1 == 0: aquired += 1
        else:
            cols[T[i]] -= 1
            if cols[T[i]] == 0:
                if max_j - max_i > j - i:
                    max_j = j
                    max_i = i 
                aquired -= 1
            i += 1
    return max_i, max_j


def print_pr(arr:list[int], i:int, j:int):
    n = len(arr)
    for t in range(n):
        print(arr[t], end=' ')
    print()
    for t in range(n):
        if t == i:
            while i <= j:
                print("*", end=' ')
                i += 1
            break
        else: print(" ", end=' ')
    print()


if __name__ == "__main__":
    k = randint(2, 4)
    n = randint(5,15)
    arr = [randint(1, k) for _ in range(n)]
    arr = [1, 1, 2, 1, 1, 3]
    k = 3
    print(arr)

    i, j = solution(arr, k)
    print("Solution")
    print_pr(arr, i, j)


        
