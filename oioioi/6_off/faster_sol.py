from sys import stdin

def mul3x3(A:list[int], B:list[int]) -> list[int]:
    return [
        (A[0]*B[0] + A[1]*B[3] + A[2]*B[6]) % 67,
        (A[0]*B[1] + A[1]*B[4] + A[2]*B[7]) % 67,
        (A[0]*B[2] + A[1]*B[5] + A[2]*B[8]) % 67,
        (A[3]*B[0] + A[4]*B[3] + A[5]*B[6]) % 67,
        (A[3]*B[1] + A[4]*B[4] + A[5]*B[7]) % 67,
        (A[3]*B[2] + A[4]*B[5] + A[5]*B[8]) % 67,
        (A[6]*B[0] + A[7]*B[3] + A[8]*B[6]) % 67,
        (A[6]*B[1] + A[7]*B[4] + A[8]*B[7]) % 67,
        (A[6]*B[2] + A[7]*B[5] + A[8]*B[8]) % 67
    ]


def mul3x3_by_3x1(M:list[int], V:list[int]) -> list[int]:
    return [
        (M[0]*V[0] + M[1]*V[1] + M[2]*V[2]) % 67,
        (M[3]*V[0] + M[4]*V[1] + M[5]*V[2]) % 67,
        (M[6]*V[0] + M[7]*V[1] + M[8]*V[2]) % 67
    ]

base_M = [3, 1, 66,
          1, 0, 0,
          0, 1, 0]

pow2_M:list[list[int]]= [base_M]
for _ in range(61):
    pow2_M.append( mul3x3(pow2_M[-1], pow2_M[-1]) )

def solve(n:int) -> int:
    if n == 0: return 1
    if n == 1: return 2
    if n == 2: return 7

    p = n-2
    vec = [7, 2, 1]

    idx = 0
    while p > 0:
        if p & 1:
            vec = mul3x3_by_3x1(pow2_M[idx], vec)
        p >>= 1
        idx += 1
    return vec[0]

data = iter(stdin.read().split())
q = int(next(data))
for _ in range(q):
    t = int(next(data))
    print( solve(t - 1) )
