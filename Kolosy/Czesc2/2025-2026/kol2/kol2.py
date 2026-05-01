from kol2_test import runtests

'''

Ignacy Buczek 

Algorytm: 
    Zadanie rozwiazuje w taki sposob, ze traktuje krawedzie poniekad jak wagi, a sam graf
    jak graf 2-warstwowy gdzie jedna warstwa to wierzcholki(wyspy) gdzie bajtek ma czapke a kolejna ze kapelusz
    Do znalezienia najkrotszego dojscia korzystam z algorytmu bfs ale tak ze jezeli chce z warstwy kapeluszowej
    przejsc do czapkowej (albo odwrotnie) to dodaje miedzy nimi pusty wierzcholek ktorego przejscie kosztuje 1 (o to chodzilo mi z tym "poniekad wagi")
    poniewaz zamiana czapki kosztuje bajtka jego cenny czas. kiedy w bfsie napotkamy poczte to wiemy ze jest ona pierwsza
    i zarowno najtansza do jakiej doszlismy takie rozwiazanie jest szybsze niz min dijkstra bo wiemy ze mozemy albo dodac 1 wierzcholek z polaczeniami albo nie

Zlozonosc: O(m)
    n - liczba wierzcholkow, m -liczba krawedzi
    policzenie n O(m)
    stworzenie grafu O(n + m)
    ustawienie sprawdzania poczt (tablica lookup) O(n)
    ustawienie tablicy visited O(2n)
    bfs O(2 * (n + m) ) [przez to ze w mamy dwie warstwy]
    sumarycznie wychodzi O(7n + 4m) natomiast z tresci zadania wiemy ze z kazdej do kazdej innej wyspy da sie dojsc albo bezposrednio albo sciezka
    co oznacza ze m minimalnie wynosi n-1 (jak w drzewie) z tad wiemy ze m jest albo tego samego rzedu co n albo wieksze (inaczej m >= n+1 bo nie wiedzialem jak to napisac)
    wiec nasza zlozonosc redukuje sie do O(7m + 4m) -> O(m)

'''
from collections import deque

def change(mosty:list[tuple[int,int,str]], poczty:list[int], s:int):

    n = 0
    for u, v, _ in mosty:
        n  = max(n, u, v)
    n += 1


    graph = [[] for _ in range(n)] 

    for u, v, c in mosty:
        c = 0 if c == 'F' else 1
        graph[u].append((v, c))
        graph[v].append((u, c))


    post_office = [False] * n
    for poczta in poczty:
        post_office[poczta] = True


    # 1 - kapelusz, 0 - czapka
    q = deque([(0, s,0, 0), (0, s, 0, 1)])
    vis = [[False for _ in range(2)] for _ in range(n)]

    while q:
        curr_cost, vert, delay, state = q.popleft()
        if delay > 0:
            q.append((curr_cost + 1, vert, 0, state))
            continue

        if vis[vert][state]: continue
        vis[vert][state] = True


        if post_office[vert]:
            return curr_cost

        for child, needed_state in graph[vert]:
            if not vis[child][state]:
                if state == needed_state:
                    q.append((curr_cost, child, 0, needed_state))
                else:
                    q.append((curr_cost, child, 1, needed_state))

    return -1

runtests(change, all_tests = True)
