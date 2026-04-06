from kol1atesty import runtests

'''
Algorytm:
    Na poczatku normalizujemy slowa (tj jezeli dla slowa v jego inwersja jest mniejsza leksykograficznie od tego slowa to na nia je zmieniamy), kazde takie slowo wrzucamy do kubelka 
    odpowiadajacego rozmiarze tego slowa. Nastepnie przechodzimy po kubelkach, jezeli kubelek jest pusty nic nie robimy jezeli ma tylko dwa elementy to od razu mozemy sprawdzic ze jezeli
    sa identyczne to 2 moze (ale nie musi) byc naszym maksymalnym wynikiem. W przeciwnym przypadku za pomoca radix sorta sortujemy wszystkie slowa w kubelku, po posiortowaniu przechodzimy przez
    caly kubelek i sprawdzamy ile jest w nim spojnych ciagow tych samych slow dla kazdego liczymy jego dlugosc i jezeli jest wieksza niz aktualny wynik ustawiamy wynik na ta dlugosc. Po przejsciu
    mamy juz nasz maksymalny wynik

Zlozonosc:

    znalezienie nnajdluzszego slowa - O(n)
    normalizacja kazdego slowa i wrzucanie do opdowiedniego kubelka - O(N)
    sortowanie pojedynczego kubelka (i) - O(v_i) [gdzie v_i to dlugosc sumaryczna slow w kubelku bo wszystkie takie samej dlugosci] 
    szukanie najdluzszego ciagu poszczegolnego kubelka (i) - O(v_i) [gdzie v_i zdef. jak powyzej, a zlozonosc wychodzi z tego ze kolejno porownujemy slowa ze soba tej samej dlugosci tyle razy ile ich jest]
    
    sumarycznie:
        k - ilosc kubelkow niepustych
        O(n + N + v_0 + v_1 + ... + v_k) -> O(n + N + N) -> O(N + n) [n <= N] -> O(N)

        ostateczna zlozonosc: O(N)
'''


def counting_sort(T:list[str], ind:int):
    n = len(T)
    B:list[str] = ["" for _ in range(n)]
    cnts = [0] * 27

    for i in range(n):
        x = ord(T[i][ind]) - ord('a')
        cnts[x] += 1
    for i in range(1,27):
        cnts[i] += cnts[i-1]
    for i in range(n-1, -1, -1):
        x = ord(T[i][ind]) - ord('a')
        cnts[x] -= 1
        B[cnts[x]] = T[i]

    T[0:n] = B[0:n]

def radix_sort(T:list[str], maxlen:int):
    for i in range(maxlen-1, -1, -1):
        counting_sort(T, i)


def g(T:list[str]):

    max_len = len( max(T, key= lambda x: len(x)) ) + 1
    buckets:list[list[str]] = [[] for _ in range(max_len)]
    n = len(T)

    for i in range(n):
        w = T[i]
        if w > w[::-1]: w = w[::-1]
        buckets[ len(w) ].append(w)

    res = 1
    for i in range(1, max_len):
        if len(buckets[i]) <= 1: continue
        if len(buckets[i]) == 2 and buckets[i][0] == buckets[i][1]:
            res = max(res, 2)
            continue
        
        radix_sort(buckets[i], i)
        blen = len(buckets[i])
        curr = 1
        curr_word = buckets[i][0]
        for j in range(1, blen):
            if buckets[i][j] == curr_word:
                curr += 1
            else:
                curr_word = buckets[i][j]
                res = max(res, curr)
                curr = 1
        res = max(curr, res) 

    return res


# Zamien all_tests=False na all_tests=True zeby uruchomic wszystkie testy
runtests( g, all_tests=True)
