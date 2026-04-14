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


def k_big(A:list[int], k:int) -> int:
    n = len(A)

    qs(A, 0, n-1)

    b_sizes = [0 for _ in range(n)]
    for i in range(n):
        b_sizes[i] = n-i + n-i-1 

    ind = 0
    for i in range(n-1, -1, -1):
        ind += b_sizes[i]
        if ind == k: 
            return (A[i] * A[i])
        if ind > k:
            diff = ind - k
            return (A[i] * A[i + (diff) // 2 ])
    return -1

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(k_big, all_tests = True)
