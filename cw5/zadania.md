Zadanie 1. Proszę zaimplementować następujące algorytmy:
a) Sprawdzanie czy graf jest dwudzielny
b) Policzyć liczbę spójnych składowych w grafie
Podzadania powinny zostać zaimplementowane z użyciem BSF i DFS (do wyboru co
gdzie "zużyć") oraz reprezentacji macierzowej i list sąsiedztwa


Zadanie 2. Znany operator telefonii komórkowej Pause postanowił zakończyć
działalność w Polsce. Jednym z głównych elementów całej procedury jest
wyłączenie wszystkich stacji nadawczych (które tworzą spójny graf połączeń).
Ze względów technologicznych urządzenia należy wyłączać pojedynczo, a operatorowi
dodatkowo zależy na tym, by podczas całego procesu wszyscy abonenci znajdujący
się w zasięgu działających stacji mogli się ze sobą łączyć (czyli by graf
pozostał spójny). Proszę zaproponować algorytm podający kolejność wyłączania
stacji.


Zadanie 3. Mówimy, że wierzchołek t w grafie skierowanym jest uniwersalnym
ujściem, jeśli (a) z każdego innego wierzchołka v istnieje krawędź z v do t,
oraz (b) nie istnieje żadna krawędź wychodząca z t.
a) Podać algorytm znajdujący uniwersalne ujście (jeśli istnieje) przy
reprezentacji macierzowej (O(n^2)).
b) Pokazać, że ten problem można rozwiązać w czasie O(n) w reprezentacji
macierzowej.


Zadanie 4. Proszę zaimplementować algorytm BFS tak, żeby znajdował najkrótsze
ścieżki w grafie i następnie, żeby dało się wypisać najkrótszą ścieżkę
z zadanego punktu startowego do wskazanego wierzchołka.


Zadanie 5. Dana jest szachownica o wymiarach n x n. Każde pole (i,j) ma koszt
(liczbę ze zbioru {1, ..., 5}) umieszczony w tablicy A (w polu A[j][i]).
W lewym górnym rogu szachownicy stoi król, którego zadaniem jest przejść do
prawego dolnego rogu, przechodząc po polach o minimalnym sumarycznym koszcie.
Prosze zaimplementować funkcję kings_path(A), która oblicza koszt ścieżki króla.
Funkcja powinna być możliwie jak najszybsza.


Zadanie 6. Dany jest graf G = (V, E), gdzie każda krawędź ma wagę ze zbioru
{1, ..., |E|} (wagi krawędzi są parami różne). Proszę zaproponować algorytm,
który dla danych wierzchołków x i y sprawdza, czy istnieje ścieżka z x do y,
w której przechodzimy po krawędziach o coraz mniejszych wagach.


Zadanie 7. Dana jest mapa kraju w postaci grafu G = (V, E). Kierowca chce
przejechać z miasta (wierzchołka) s do miasta t. Niestety niektóre drogi
(krawędzie) są płatne. Każda droga ma taką samą jednostkową opłatę. Proszę
podać algorytm, który znajduje trasę wymagającą jak najmniejszej liczby opłat.
W ogólności graf G jest skierowany, ale można najpierw wskazać algorytm dla
grafu nieskierowanego.


Zadanie 8. Ścieżka Hamiltona to ścieżka przechodząca przez wszystkie wierzchołki
w grafie, przez każdy dokładnie raz. W ogólnym grafie znalezienie ścieżki
Hamiltona jest problemem NP-trudnym. Proszę podać algorytm, który stwierdzi
czy istnieje ścieżka Hamiltona w acyklicznym grafie skierowanym.


Zadanie 9. Wierzchołek v w grafie skierowanym nazywamy dobrym początkiem jeśli
każdy inny wierzchołek można osiągnąć ścieżką skierowaną wychodzącą z v.
Proszę podać algorytm, który stwierdza czy dany graf zawiera dobry początek.


Zadanie 10. Dany jest graf nieskierowany G oraz dwa jego wierzchołki, s i t.
Proszę zaproponować algorytm, który sprawdza czy istnieje taka krawędź, po
usunięciu której długość najkrótszej ścieżki z s do t wzrośnie (lub taka
ścieżka przestaje istnieć).


Zadanie 11. (problem przewodnika turystycznego) Przewodnik chce przewieźć
grupę K turystów z miasta A do miasta B. Po drodze jest jednak wiele innych
miast i między różnymi miastami jeżdżą autobusy o różnej pojemności. Mamy
daną listę trójek postaci (x, y, c), gdzie x i y to miasta między którymi
bezpośrednio jeździ autobus o pojemności c pasażerów. Przewodnik musi
wyznaczyć wspólną trasę dla wszystkich turystów i musi ich podzielić na
grupki tak, żeby każda grupka mogła przebyć trasę bez rozdzielania się.
Proszę podać algorytm, który oblicza na ile (najmniej) grupek przewodnik
musi podzielić turystów (i jaką trasą powinni się poruszać), żeby wszyscy
dostali się z A do B.


Zadanie 12. Proszę wskazać algorytm, który mając na wejściu graf nieskierowany
G = (V, E) stwierdza, czy jego zbiór wierzchołków można podzielić na dwa
rozłączne zbiory V1 i V2 takie, że V = V1 suma V2 oraz zarówno wierzchołki
z V1 jak i wierzchołki z V2 tworzą kliki.
