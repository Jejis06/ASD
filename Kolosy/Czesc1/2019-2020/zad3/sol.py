from random import randint

def snail(arr:list[int], ind:int) -> bool:
    n = len(arr)
    i = 0; j = n-1

    while i < j:
        if i == ind: 
            i += 1
            continue
        if j == ind: 
            j -= 1
            continue

        s = arr[i] + arr[j]
        if s == arr[ind]: return True
        elif s < arr[ind]:
            i += 1
        else:
            j -= 1
    return False

def partition(arr:list[int], lo:int, hi:int) -> int:
    x = arr[hi]
    i = lo - 1
    for j in range(lo, hi + 1):
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    return i

def qsort(arr:list[int], lo:int, hi:int):
    while hi > lo:
        q = partition(arr, lo, hi)
        qsort(arr, lo, q - 1)
        lo = q + 1


        

def check_sum(T:list[int]) -> bool:

    n = len(T)
    qsort(T, 0, n-1)
    for i in range(n):
        if snail(T, i) == False:
            return False
    return True



def rand_sgn():
    i = randint(0, 1)
    if i == 1: return -1
    else: return 1


def so():
    #T = [-18, -24, 6, 15, 21, 12, -17, -30, 29, -12, 27, 30, 13, 17]
    # T = [-9, -20, -27, 27, -29, 9, 18, -18]
    # print(T)
    # print(sorted(T))
    #
    # print(check_sum(T))
    # return
    n = 5
    b = False
    while b == False:
        print("-------")
        arr = [rand_sgn() * randint(5,30) for _ in range(n)]
        print(arr)
        b = check_sum(arr)

if __name__ == "__main__":
    so()

