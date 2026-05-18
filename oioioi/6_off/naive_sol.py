from sys import stdin



def solve(n:int):
    if n == 0: return 1
    if n == 1: return 2
    if n == 2: return 7

    f0 = 1
    f1 = 2
    f2 = 7

    for _ in range(2, n):
        f3 = (3 * f2 + f1 - f0) % 67 

        f0 = f1
        f1 = f2
        f2 = f3
    return f2


data = iter(stdin.read().split())
q = int(next(data))
for _ in range(q):
    t = int(next(data))
    print( solve(t - 1) )

