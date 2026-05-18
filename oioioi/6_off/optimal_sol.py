from sys import stdin


def mul3x3(A:list[int], B:list[int]) -> list[int]:
    C = [0] * 9
    for j in range(3):
        for k in range(3):
            C[k + 3* j] = (A[0 + 3*j ]*B[0 + k] + A[1 + 3*j]*B[ 3 + k] + A[2 + 3*j]*B[6 + k]) % 67
    return C

def pow3x3_andMul(A:list[int], p:int) -> int:
    b = list(tuple(A))

    res:list[int] = [1, 0, 0, 
                     0, 1, 0, 
                     0, 0, 1]
    while p > 0:
        if p % 2 == 1:
            res = mul3x3(res, b)
        b = mul3x3(b, b)
        p //= 2

    return (res[0] * 7 + res[1] * 2 + res[2]) % 67

def solve(n:int) -> int:
    if n == 0: return 1
    if n == 1: return 2
    if n == 2: return 7

    return pow3x3_andMul([3, 1, -1, 
                          1, 0, 0, 
                          0, 1, 0], n-2)


data = iter(stdin.read().split())
q = int(next(data))
for _ in range(q):
    t = int(next(data))
    print( solve(t - 1) )

