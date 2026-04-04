from random import randint
import array
import sys

input = sys.stdin.readline


def left(x:int): return 2 * x + 1
def right(x:int): return 2 * x + 2
def parent(x:int): return (x - 1) // 2


def heapify(arr:array.array[int], i:int, n:int):
    max_ind = i
    if left(i) < n and arr[left(i)] > arr[max_ind]:
        max_ind = left(i)
    if right(i) < n and arr[right(i)] > arr[max_ind]:
        max_ind = right(i)
    if max_ind != i:
        arr[i], arr[max_ind] = arr[max_ind], arr[i]
        heapify(arr, max_ind, n)

def heapsort(arr:array.array[int]):
    n = len(arr)
    for i in range(parent(n-1), -1, -1):
        heapify(arr, i, n)

    for i in range(0, n-1):
        arr[0], arr[n - i - 1] = arr[n - i - 1], arr[0]
        heapify(arr, 0, n-i-1)



def solve() -> None:
    n = int(input())
    arr = array.array('i', [0]) * n
    for i in range(n):
        arr[i] = int(input())

    q = int(input())
    heapsort(arr)

    for i in range(q):
        inq = n - int(input()) 
        print(arr[inq])



if __name__ == "__main__":
    solve()
