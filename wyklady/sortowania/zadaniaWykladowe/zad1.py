'''

Posortowac tablice n elementowa z wartosciami od 0...n-1
w czasie O(n)

'''

from random import randint
from collections.abc import Callable



def a(x:int, n:int): return x // n 
def b(x:int, n:int): return x % n




def countsort(T:list[int], comp:Callable[[int, int], int]) -> None:
    n = len(T)
    B = [0] * n
    cnts = [0] * n

    for i in range(n):
        cnts[comp(T[i], n)] += 1
    for i in range(1, n):
        cnts[i] += cnts[i - 1]

    for i in range(n-1, -1, -1):
        ind = comp(T[i], n)
        cnts[ind] -= 1
        B[cnts[ind]] = T[i]

    for i in range(n):
        T[i] = B[i]


def solve(T:list[int]):

    modes = [b, a]

    for mode in modes:
        countsort(T, mode)


if __name__ == "__main__":
    n = randint(4, 100)
    T = [randint(0, n*n -1 ) for _ in range(n)]
    print(T)
    solve(T)
    print(T)

