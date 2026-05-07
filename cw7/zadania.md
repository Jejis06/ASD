1. Najdluzszy wspolny podciag.
szukamy taki podciag (niekoniecznie spojny) ktory znajduje sie i w A i w B 
i jest najdluzszy mozliwy

np.
A = aabcbdadb
B = bbaabadadb

tutaj: aabcbd


2. Mnozenie maciezy.
mamy ciag maciezy (A1, A2, ... , An)( tak naprawde ich wymiarow ), 
chcemy je pomnozyc {(a1, b1), (a2, b2), ... , (an, bn)} (ai = bi+1) wymiary te spelniaja 
warunek ze mnozac je po kolei da sie to wykonac jezeli chodzi o same wymiary tych 
macierzy. Zadanie polega na tym ze trzeba znalezc takie ulozenie nawiasow ze 
teoretyczna ilosc operacji mnozenia jest najmniejsza.

np.
mamy wymiary macierzy A, B, C
100x1 , 1x100, 1x1 

potencjalne ulozenia nawiasow to:

I.  (A x B) x C     | koszt to 100
II.  A x (B x C)    | koszt to 200

czyli tutaj optymalne nawiasowanie to nawiasowanie (I.)
!!! ZWRACAMY TYLKO NAJMNIEJSZY KOSZT !!!


3. Maxi-min 
Dany jest ciąg "n" liczb naturalnych, który oznaczamy jako:
A = (a_0, a_1, ..., a_{n-1})
oraz liczba naturalna "k".

Rozważamy podział tego ciągu na dokładnie "k" spójnych (sąsiadujących ze sobą) 
i niepustych podciągów, które oznaczmy jako S_1, S_2, ..., S_k. 

Formalnie taki podział można przedstawić przy 
pomocy punktów przecięcia (indeksów l_1, l_2, ..., l_{k-1})
w następujący sposób:

S_1 = (a_0, a_1, ..., a_{l_1})
S_2 = (a_{l_1+1}, ..., a_{l_2})
...
S_k = (a_{l_{k-1}+1}, ..., a_{n-1})

Każdy wyodrębniony podciąg posiada swoją wartość (zazwyczaj jest to suma jego elementów). 
Wartość całego dokonanego podziału definiujemy jako najmniejszą z wartości tych podciągów, 
co można zapisać wzorem:

Wartość podziału = min(S_1, S_2, ..., S_k)

CEL ZADANIA:
Dla zadanego ciągu A oraz liczby "k", należy znaleźć taki podział na "k" spójnych podciągów, 
dla którego wartość całego podziału będzie jak największa (maksymalna). Innymi słowy, 
szukamy optymalnego podziału, który maksymalizuje najmniejszą wartość ze 
wszystkich utworzonych podciągów.


4.


5.


6.


7.


8.


9.


10.



