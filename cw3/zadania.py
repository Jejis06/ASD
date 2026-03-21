'''

1. Quicksort max O(logn) pamieci

2. k-ty najmniejszy elem w tablicy nieposortowanej w O(n)

3. Pojemniki z woda:
    - duzo rozneg rozmiaru 2d prosokatow w ukladzie wspolrzednych
    - wszystkie pojemniki polaczone rurami (wiec napelnione tak ze jak jest podany poziom to tak jakby w 2d 
                                            tam gdzie linia poziomu to ponizej kazdy istniejacy pojemnik napelniony do danego pojemnika)
    - nalalismy k litrow wody i interesuje nas ile pojemnikow bedzie w pelni napelnione

4. Posortowac tablice N elementowa ale wiemy ze w tej tablicy jest log(n) unikalnych wartosci
    w O(n loglog(n))

5. Czy A[n] i B[n] to anagramy 
a) alf lacinski
b) unicode

6. Posortuj n slow
w czasie liniowym wzgl sumy ich dlugosci

'''

# zad 1
def partition(A, p, r):
    # ...
    return 0

def qsort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        if q - p > r - q:
            qsort(A, q+1, r)
            qsort(A, p, q-1)
        else:
            qsort(A, p, q-1)
            qsort(A, q+1, r)

# zad 2
# n + n/2 + n/4 + .... = 2*n
def findkth(A, p, r, k):
    if k > len(A): return 0
    if p < r:
        q = partition(a, p, r)
        if q == k:
            return A[k]
        elif q > k:
            return findkth(A, p, q-1, k)
        else:
            return findkth(A, q+1, r, k)

# zad 3

# zdazeniowka po posortowanych wysokosciach pudelek
# do napisania w domu
# binsecz po wyniku

# zad 4
# do domu

# zad 5 a)
def czyanagram(A, B, k):
    cnts = [0] * k
    n = len(A)

    for i in range(n):
        cnts[ord(A[i]) - ord('a')] += 1
        cnts[ord(B[i]) - ord('a')] -= 1

    return (not any(cnts))

# zad 5 b)
def anananangram(A, B, cnts):
    n = len(A)
    for i in range(n):
        cnts[A[i]] = 0
        cnts[B[i]] = 0


    for i in range(n):
        cnts[ord(A[i]) - ord('a')] += 1
        cnts[ord(B[i]) - ord('a')] -= 1

    for i in range(n):
        if cnts[A[i]] != 0 or cnts[B[i]] != 0:
            return False
    return True


