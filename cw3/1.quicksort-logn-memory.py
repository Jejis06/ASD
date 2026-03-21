"""
1. Quicksort max O(logn) pamieci
"""

# Lomuto partition
def partition(A:list[int], low:int, high:int):
    pivot = A[high]
    i = low - 1
    for j in range(low, high+1):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    return i

def quick_sort(A:list[int], low:int, high:int):
    while low < high:
        pivot = partition(A, low, high)

        if pivot - low < high - pivot:
            quick_sort(A, low, pivot - 1)
            low = pivot + 1
        else:
            quick_sort(A, pivot + 1, high)
            high = pivot - 1






def solution():
    A = [5, 4, 2, 1, 4, 5]
    quick_sort(A, 0, len(A) -1)
    print(A)
    pass

if __name__ == "__main__":
    solution()
        
