import sys
from random import randint, seed


OIOIOI = True


cnts = []
max_count = 0

def merge(T, B, p, q, r):
    global cnts, max_count
    i = p; j = q; k = p

    while i < q and j < r:
        if T[i][0] < T[j][0]:
            B[k] = T[i]
            i += 1
        else:
            cnts[T[j][1]] += (i - p)
            max_count = max(cnts[T[j][1]], max_count)
            B[k] = T[j]
            j += 1
        k += 1

    while i < q:
        B[k] = T[i]
        i += 1
        k += 1

    while j < r:
        B[k] = T[j]
        cnts[T[j][1]] += (i - p)
        max_count = max(cnts[T[j][1]], max_count)
        j += 1
        k += 1

    for t in range(p, r):
        T[t] = B[t]

def sort_help(T, B, p, r):
    if r - p > 1:
        q = (r + p) // 2
        sort_help(T, B, p, q)
        sort_help(T, B, q, r)
        merge(T, B, p, q, r)



def solution(T: list[str]) -> int:
    global cnts, max_count
    max_count = 0
    n = len(T)
    cnts = [0] * n
    A = [None] * n
    B = [None] * n
    for i in range(n):
        A[i] = (T[i], i)

    sort_help(A, B, 0, n)

    return max_count


if __name__ == "__main__":
    def generate_random_string(length):
        return ''.join(chr(randint(97, 122)) for _ in range(length))
    
    if OIOIOI:
        n = int(sys.stdin.readline().strip())
        words = [sys.stdin.readline().strip() for _ in range(n)]
        print(solution(words))
    else:
        seed(1)
        test_def = [
            (10, 5, 10, 6),
            (100, 5, 10, 88),
            (100, 20, 100, 91),
            (10000, 10, 30, 9901)
        ]
        ok = 0
        for idx, (n, m_low, m_high, ans) in enumerate(test_def):
            print("Test", idx + 1)
            words = [generate_random_string(randint(m_low, m_high)) for _ in range(n)]
            result = solution(words)
            if result == ans:
                print("OK")
                ok += 1
            else:
                print("Błąd!")
        print("Wynik:", ok, "/", len(test_def))
