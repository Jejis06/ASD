"""
Zadanie 3. Mówimy, że wierzchołek t w grafie skierowanym jest uniwersalnym
ujściem, jeśli (a) z każdego innego wierzchołka v istnieje krawędź z v do t,
oraz (b) nie istnieje żadna krawędź wychodząca z t.
a) Podać algorytm znajdujący uniwersalne ujście (jeśli istnieje) przy
reprezentacji macierzowej (O(n^2)).
b) Pokazać, że ten problem można rozwiązać w czasie O(n) w reprezentacji
macierzowej.
"""
graph_matrix = list[list[int]]

# Wierzcholek bedacy uniwersalnym wierzcholkiem to taki dla ktorego wiersz 
# w repr macierzowej jest pusty natomiast kolumna odpowiadajaca nr tego wiersza
# jest wypelniona 1 poza oczywiscie G[vert][vert]

# a) O(n^2)
def brut(G:graph_matrix):
    n = len(G)
    for vert in range(n):
        if sum(G[vert]) != 0 : continue
        proper_col = True
        for in_vert in range(n):
            if (in_vert != vert and G[in_vert][vert] != 1):
                proper_col = False
                break
        if proper_col: return vert
        else: continue

    return -1

# b) O(n) 
# zaczynamy poszukiwanie naszego kandydata metoda zachlanna tj.
# jezeli dla danego G[a][b]:
# - istnieje polaczenie to wiemy ze a na pewno nie jest naszym kandydatem wiec (a += 1)
# - nie istnieje polaczenie to musimy sprawdzic czy z kolejnym istnieje (b += 1)
# takie podejscie zawsze znajdzie dobrego kandydata poniewaz zostanie ono ograniczone na osi Y przez pasek 0 ktorym b dojdzie do n
# a na osi X znajdzie pasek 1 ktorym a dojdzie do najblizszego paska 0 i zakonczy sie w n
# trzeba jednak pamietac ze rozwiazanie moze nie istniec wiec samo dojscie a lub b do n niekoniecznie oznacza znalezione rozwiazanie
# tak wiec koncowo trzeba zweryfikowac czy dla znalezionego wierzcholka a zachodzi sum(G[a]) == 0 oraz V(b != a): G[b][a] == 1
def optimal_solution(G:graph_matrix):
    n = len(G)
    a = 0; b = 0
    # O(n)
    while a < n and b < n:
        if G[a][b] == 1: a += 1
        else: b += 1

    if a >= n: return -1

    # O(2N) -> O(N)
    if sum(G[a]) != 0: return -1
    for in_vert in range(n):
        if in_vert != a and G[in_vert][a] != 1:
            return -1

    return a




def solution():
    # TODO: Implement algorithm logic here
    pass

if __name__ == "__main__":
    solution()
