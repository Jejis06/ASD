from kol1_test import runtests

"""

O(nlogn)
bs po wyniku ://

"""

def find_ge(A:list[int], x:int) -> int:
    n = len(A)
    l = 0; r = n-1
    cnt = 0

    while l < n and r >= 0:
        if A[l] * A[r] >= x:
            cnt += n - l
            r -= 1
        else: l += 1
    return cnt 

def k_big(A:list[int], k:int):
    A.sort()

    n = len(A)
    l = 1
    r = A[-1]  * A[-1]

    res = -1 

    while l <= r:
        mid = (l + r) // 2

        if find_ge(A, mid) >= k:
            res = mid
            l = mid + 1
        else:
            r = mid - 1

    return res 

runtests(k_big, all_tests = True)
