"""
4. Posortowac tablice N elementowa ale wiemy ze w tej tablicy jest log(n) unikalnych wartosci
    w O(n loglog(n))
"""
from random import randint

def bs(A:list[int], val:int) -> int:
    l = 0
    r = len(A) - 1
    while l <= r:
        m = (l + r) // 2
        if A[m] == val: return m
        elif A[m] > val: r = m - 1
        else: l = m + 1
    return l

def solution(T:list[int]):
    B = []
    n = len(T)

    # unique sorted
    for i in range(n):
        ind = bs(B, T[i])
        if ind < len(B) and B[ind] == T[i]: continue
        B.append(0)
        for j in range(len(B) - 1, ind, -1):
            B[j] = B[j-1]
        B[ind] = T[i]

    # counting sort
    cnts = [0] * len(B)
    C = [0] * n

    for i in range(n):
        ind = bs(B, T[i])
        cnts[ind] += 1

    for i in range(1, len(B)):
        cnts[i] += cnts[i - 1]

    for i in range(n-1, -1, -1):
        ind = bs(B, T[i])
        cnts[ind] -= 1
        C[ cnts[ind] ] = T[i]

    return C
    #for i in range(n):
    #    T[i] = C[i]

        

if __name__ == "__main__":
    T = [randint(0, 1000) for _ in range(randint(0, 100))]
    print(solution(T))
    print(sorted(T))
        
