"""
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
"""

# dostajemy macierze opisane jako a1, b1, b1, c1

def solution(matricies:list[int]):

    n = len(matricies)-1
    dp:list[list[int | float]] = [[0 for _ in range(n+1)] for _ in range(n+1)]

    for l in range(2, n+1):
        for i in range(1, n-l+2):
            j = i + l - 1
            dp[i][j] = float('inf')

            for k in range(i, j):
                dp[i][j] = min(dp[i][j], 
                              dp[i][k] + dp[k+1][j] + (matricies[i-1] * matricies[k] * matricies[j])
                            )
    return dp[1][n]




if __name__ == "__main__":
    #solution()
    pass
