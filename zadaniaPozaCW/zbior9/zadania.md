Zadanie 1. (ścieżka Hamiltona w DAGu) Ścieżka Hamiltona to ścieżka 
przechodząca przez wszystkie wierzchołki w grafie, przez każdy dokładnie raz. 
W ogólnym grafie znalezienie ścieżki Hamiltona jest problemem NP-trudnym. 
Proszę podać algorytm, który stwierdzi czy istnieje ścieżka Hamiltona 
w acyklicznym grafie skierowanym.


Zadanie 2. (dobry początek) Wierzchołek v w grafie skierowanym nazywamy 
dobrym początkiem jeśli każdy inny wierzchołek można osiągnąć scieżką 
skierowaną wychodzącą z v. Proszę podać algorytm, który stwierdza czy 
dany graf zawiera dobry początek.


Zadanie 3. (najkrósze ścieżki w DAGu) Jak znaleźć najkrótsze ścieżki 
z wierzchołka s do wszystkich innych w acyklicznym grafie skierowanym?


Zadanie 4. (logarytmy) Mamy dany graf G=(V,E) z wagami w: E -> N-{0} 
(dodatnie liczby naturalne). Chcemy znalezc scieżkę z wierzchołka u 
do v tak, by iloczyn wag był minimalny. Omówic rozwiązanie 
(bez implementacji).


Zadanie 5. (problem przewodnika turystycznego) Przewodnik chce przewieźć 
grupę K turystów z miasta A do miasta B. Po drodze jest jednak wiele innych 
miast i między różnymi miastami jeżdzą autobusy o różnej pojemności. 
Mamy daną listę trójek postaci (x,y,c), gdzie x i y to miasta między 
którymi bezpośrednio jeździ autobus o pojemności c pasażerów. Przewodnik 
musi wyznaczyć wspólną trasę dla wszystkich tursytów i musi ich podzielić 
na grupki tak, żeby każda grupka mogła przebyć trasę bez rodzielania się. 
Proszę podać algorytm, który oblicza na ile (najmniej) grupek przewodnik 
musi podzielić turystów (i jaką trasą powinni się poruszać), żeby wszyscy 
dostali się z A do B.


Zadanie 6. (dwóch kierowców) Dana jest mapa kraju w postaci grafu G=(V,E), 
gdzie wierzchołki to miasta a krawędzie to drogi łączące miasta. Dla 
każdej drogi znana jest jej długość (wyrażona w kilometrach jako liczba 
naturalna). Alicja i Bob prowadzą (na zmianę) autobus z miasta x w V 
do miasta y w V, zamieniając się za kierownicą w każdym kolejnym mieście. 
Alicja wybiera trasę oraz decyduje, kto prowadzi pierwszy. Proszę zapropnować 
algorytm, który wskazuje taką trasę (oraz osobę, która ma prowadzić 
pierwsza), żeby Alicja przejechała jak najmniej kilometrów. Algorytm 
powinien być jak najszybszy (ale przede wszystkim poprawny).


Zadanie 7. (problem stacji benzynowych na grafie) Pewien podróżnik chce 
przebyć trasę z punktu A do punktu B. Niestety jego samochód spala 
dokładnie jeden litr paliwa na jeden kilometr trasy. W baku mieści się 
dokładnie D litrów paliwa. Trasa jest reprezentowana jako graf, gdzie 
wierzchołki to miasta a krawędzie to łączące je drogi. Każda krawędź 
ma długość w kilometrach (przedstawioną jako licza naturalna). W każdym 
wierzchołku jest stacja benzynowa, z daną ceną za litr paliwa. Proszę 
podać algorytm znajdujący trasę z punktu A do punktu B o najmniejszym 
koszcie. Proszę uzasadnić poprawność algorytmu.
