from kol1testy import runtests

'''

Algorytm po otrzymaniu tablicy wejsciowej tworzy jej kopie (K) z krotkami k1,k2,k3,... takimi, ze k*[0] = wartosc i-tego elementu a k*[1] = pierwotny indeks elementu.
Nastepnie stabilnym sortowaniem mergesort sortuje tablice K rosnaco, przy okazji zwiekszajac kazdemu oryginalnemu indeksowi jego range. Dziala to tak ze kiedy mergesort dzieli
oryginalna tablice na 2 czesci to wiemy ze elementy z prawej jej czesci beda 'dalej' w tablicy niz te z lewej, wykorzystujemy to w funkcji merge w ktorej wiemy ze jezeli wartosc 
pewnej krotki K[j] jest wieksza od aktualnej wartosci K[i] to wszystkie wartosci od K[p...i] sa mniejsze od K[j] zatem ranga oryginalnego indeksu (K[j][1]) jest powiekszana o (i - p).
Po zakonczeniu sie algorytmu mergesort kazdy indeks elementu z tablicy T ma juz policzona swoja range w tablicy ranks a zatem pozostaje tylko zwrocic max(ranks)

Zlozonosc:
    Tworzenie kopii tablicy: O(n)
    Algorytm merge sort: O(nlogn)
    max wartosc z tablicy ranks: O(n)

    ostatecznie mamy: O(nlogn + 2n) -> O(nlogn)

'''


ranks = []

lt = list[tuple[int,int]]


def merge(T:lt, B:lt, p:int, q:int, r:int):
    global ranks
    i = p; j = q; k = p

    while i < q and j < r:
        if T[i][0] < T[j][0]:
            B[k] = T[i]
            i += 1
        else:
            B[k] = T[j]
            ranks[T[j][1]] += (i - p)
            j += 1
        k += 1

    while i < q:
        B[k] = T[i]
        i += 1
        k += 1

    while j < r:
        B[k] = T[j]
        ranks[T[j][1]] += (i - p)
        j += 1
        k += 1

    T[p:r] = B[p:r]


def ranker(T:lt, B:lt, p:int, r:int):
    if r - p > 1:
        q = (p + r) // 2
        ranker(T, B, p, q)
        ranker(T, B, q, r)

        merge(T, B, p, q, r)



def maxrank(T:list[int]):
    global ranks

    n = len(T)
    ranks = [0 for _ in range(n)]
    arr:lt = [(0,0) for _ in range(n)]

    for i in range(n):
        arr[i] = (T[i], i)

    n = len(T)
    B = [(0,0) for _ in range(n)] 
    ranker(arr, B, 0, n)
    return max(ranks)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maxrank, all_tests = True)
