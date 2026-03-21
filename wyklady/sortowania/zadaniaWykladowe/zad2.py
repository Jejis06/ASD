'''

Znalezc takie 2 liczby A[i] i A[j]
takie ze po posortowaniu bylyby obok siebie ale 
| A[i] - A[j] | jest maksymalna

W O(n)

'''

def maxgapsize(A:list[int]) -> tuple[int,int,int]:
    n = len(A)
    max_val = max(A)
    min_val = min(A)


    if max_val == min_val: return (0, 0, 0)

    used = [False] * n
    max_bucket = [-float('inf')] * n
    min_bucket = [float('inf')] * n

    for i in range(n):
        ind = (A[i] - min_val) * (n - 1) // (max_val - min_val)

        max_bucket[ind] = max(max_bucket[ind], A[i])
        min_bucket[ind] = min(min_bucket[ind], A[i])
        used[ind] = True

    max_diff = 0
    prev_max = min_val
    a, b = 0, 0 


    # roznica najwieksza bedzie tylko miedzy roznymi kubelkami a nie w srodku
    for i in range(n-1):
        if used[i] == False: continue

        curr_diff = abs(min_bucket[i] - prev_max)

        if curr_diff > max_diff:
            a = min_bucket[i]
            b = prev_max

            max_diff = curr_diff

        prev_max = max_bucket[i]

    if abs(max_val - prev_max) > max_diff:
        max_diff = abs(max_val - prev_max)
        a = max_val
        b = prev_max

    return (a, b, max_diff) 

arr = [3, 1, 10, 15, 12]
print(maxgapsize(arr))


