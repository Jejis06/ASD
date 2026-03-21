import sys

def merge_sort(A, B, cnts, p, r):
    if r - p <= 1: return
    q = (p + r) // 2
    merge_sort(A, B, cnts, p, q)
    merge_sort(A, B, cnts, q, r)

    i = p; j = q; k = p
    while i < q and j < r:
        if A[i][0] < A[j][0]:
            B[k] = A[i]
            i += 1
        else:
            cnts[A[j][1]] += (i - p)
            B[k] = A[j]
            j += 1
        k += 1


    if i < q:
        B[k:r] = A[i:q]
    else:
        B[k:r] = A[j:r]
        added = q - p
        for x in range(j, r):
            cnts[A[x][1]] += added


    A[p:r] = B[p:r]


def solution(words: list[str]):
    n = len(words)
    if n == 0: return 0
    ids = sorted(set(words))
    ind_map = dict(zip(ids, range(len(ids))))

    A = [(ind_map[w], i) for i, w in enumerate(words)]
    B = [0] * n
    counts = [0] * n

    merge_sort(A, B, counts, 0, n)
    return max(counts)



if __name__ == "__main__":
    dane = sys.stdin.read().split()
    if dane:
        words = dane[1:]
        print(solution(words))
