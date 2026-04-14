from kol1_test import runtests

'''

Algorytm: sortujemy tablice wejsciowa quicksortem i potem dla kazdej liczby liczymy ile
ile ona posiada liczb najmniejszych ktore wygenerowala. poniewaz skoro posortowalismy tablice
to wiemy ze ita liczba wygeneruje n-i + n-i-1 liczb najmniejszych w kolejnosci rosnacej
takim sposobem wiemy ze kazda liczb z wejsciowej posortowanej tablicy ma pod soba 
przedzial rozmiaru omawianego wczesniej liczb takich ze one sa mniejsze niz pozostale
wygenerowane w tej tabliczce mnozenia. szukajac k-0tego najwiekszego idziemy od konca
i parzymy czy jestesmy akurat na brzegu a jezeli nie to w jaka inna liczba odpowiada
za kreacje naszej szukanej k-tej, wyliczamy ja i zwracamy

zlozonosc: O(nlogn)
'''

def partition(arr:list[int], lo:int, hi:int):
    x = arr[hi]
    i = lo - 1
    for j in range(lo, hi+1):
        if arr[j] <= x:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]
    return i

def qs(arr:list[int], lo:int, hi:int):
    if hi > lo:
        q = partition(arr, lo, hi)
        qs(arr, lo, q - 1)
        qs(arr, q+1, hi)


def k_big(A:list[int], k:int, b_s:bool):
    n = len(A)

    qs(A, 0, n-1)


    b_sizes = [0 for _ in range(n)]
    for i in range(n):
        b_sizes[i] = n-i + n-i-1 

    if b_s is True:
        return b_sizes

    if k == n*n:
        return A[0] * A[0]
    elif k == 1:
        return A[n-1] * A[n-1]

    ind = 0
    for i in range(n-1, -1, -1):
        ind += b_sizes[i]
        if ind == k: 
            return -1# (A[i] * A[i])
        if ind > k:
            diff = ind - k
            return (A[i] * A[i + (diff + 1) // 2 ])
    return -1

def badacz(A:list[int]):
    n = len(A)
    qs(A, 0, n-1)

    b_sizes = k_big(A, 0, True)
    print(n)

    jmps = [0] * n
    for i in range(n-2, 0, -1):
        if A[i] * A[i] < A[i-1] * A[n-1]:
            print(f"przeskok {i} -> {i-1}")
            jmps[i] -= 1

    print(jmps)


def gen_predicts(A:list[int]):
    b_sizes = k_big(A, 0, True)
    n = len(A)
    badacz(A)
    predicts = [k_big(A, i, False) for i in range(1, n*n+1)][::-1]
    print("predicts")
    print("n:",n)
    print("b_sizes:",b_sizes)
    print("predicts:")
    print(predicts)

    b_sizes = b_sizes[::-1]
    for j in range(1, len(b_sizes)):
        b_sizes[j] += b_sizes[j - 1]
    s = ""
    for i in range(n*n+1, 0, -1):
        if i in b_sizes:
            s += "*"
        else: s+="_"
    print(b_sizes)
    print(s[::-1])

    return (n, b_sizes, predicts)

def gen_table(A:list[int]):
    t = []
    n = len(A)
    for i in range(n):
        for j in range(n):
            t.append(A[i] * A[j])
    t.sort()
    return t

if __name__ == "__main__":
    A = [1, 2, 3, 4, 8, 11]
    print(A)
    print( gen_table(A) )
    _ = gen_predicts(A)

#def tx(A, k): return -1
#runtests(tx, all_tests = True)
