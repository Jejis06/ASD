"""
2. k-ty najmniejszy elem w tablicy nieposortowanej w O(n)
"""
from random import randint


# lomuto partition
def partition(A:list[int], low:int, high:int) -> int:
    pivot = A[high]
    i = low - 1
    for j in range(low, high+1):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    return i


def findkth(A:list[int], low:int, high:int, k:int) -> int:
    if len(A) < k:
        return 0
    if low < high:
        pivot = partition(A, low, high)
        #print(f"l:{low}, h:{high}, piv:{pivot}")

        if pivot == k: return A[k]
        elif pivot > k: return findkth(A, low, pivot-1, k)
        else: return findkth(A, pivot+1, high, k)





def solution():
    # TODO: Implement algorithm logic here

    A = [randint(0, 30) for _ in range(randint(0, 10))]

    for k in range(len(A)):
        print(f"--------- k:{k} ---------")
        print(findkth(A, 0, len(A) - 1, k))
        print(sorted(A))
    pass

if __name__ == "__main__":
    solution()
        
