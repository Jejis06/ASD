

def convert(val:int):
    cnts = [0] * 10
    if val == 0: return 1, 0

    while val > 0:
        dig = val % 10
        cnts[dig] += 1

        val //= 10

    single_count = 0
    multiple_count = 0

    for i in range(10):
        if cnts[i] == 1: single_count += 1
        elif cnts[i] > 1: multiple_count += 1
    return single_count, multiple_count

def counting_sort(arr, key, lo, hi):
    n = len(arr)
    cnts = [0] * (hi - lo + 1)
    B = [0] * n

    for i in range(n):
        ind = arr[i][key] - lo
        cnts[ind] += 1

    for i in range(1, hi-lo+1):
        cnts[i] += cnts[i - 1]

    for i in range(n-1, -1, -1):
        ind = arr[i][key] - lo
        cnts[ind] -= 1
        B[cnts[ind]] = arr[i]

    arr[0:n] = B[0:n]
    return



def pretty_sort(T):
    n = len(T)
    max_single = 0; min_single = float('inf')
    max_multiple = 0; min_multiple = float('inf')

    for i in range(n):
        T[i] = (T[i], *convert(T[i]))
        max_single = max(max_single, T[i][1]); min_single = min(min_single, T[i][1])
        max_multiple = max(max_multiple, T[i][2]); min_multiple = min(min_multiple, T[i][2])

    counting_sort(T, 2, min_multiple, max_multiple)
    counting_sort(T, 1, min_single, max_single)

    for i in range(n//2):
        T[i], T[n-1-i] = T[n-1-i][0], T[i][0]
    if n % 2 == 1: T[n//2] = T[n//2][0]
    pass

T = [123,124141,3,4,3,4,45679,124124124, 9999999]
T1 = [124141,3,4,3,4,45679,124124124, 9999999]
print(T)
pretty_sort(T)
print(T)

print("t1")
print(T1)
pretty_sort(T1)
print(T1)

