"""
4. (Głodna żaba) Pewna żaba skacze po osi liczbowej. Ma się dostać z zera do n-1, skacząc wyłącznie w 
kierunku większych liczb. Skok z liczby i do liczby j (j > i) kosztuje ją j-i jednostek energii, a jej 
energia nigdy nie może spaść poniżej zera. Na początku żaba ma 0 jednostek energii, ale na szczęście na 
niektórych liczbach - także na zerze - leżą przekąski o określonej wartości energetycznej 
(wartość przekąski dodaje się do aktualnej energii Zbigniewa). Proszę zaproponować algorytm, który oblicza 
minimalną liczbę skoków potrzebną na dotarcie z 0 do n-1 mając daną tablicę A z wartościami energetycznymi 
przekąsek na każdej z liczb.
"""
def cap(power:int, n:int) -> int:
    if power > n-1:
        return n-1
    return power


def solution(A:list[int]):
    n = len(A)
    dp:list[list[int | float]] = [[float('inf') for _ in range(n)] for _ in range(n)]

    dp[0][ cap(A[0], n) ] = 0

    for i in range(1, n):
        for e in range(0, n):
            energy = cap(A[i] + e, n)
            for j in range(i):
                if e + i - j < n and dp[j][e + i - j] != float('inf'):
                    dp[i][energy] = min(dp[i][energy], dp[j][e + i - j] + 1)


    res = min(dp[n-1])
    if res == float('inf'): return -1
    else: return res



if __name__ == "__main__":
    #solution()
    pass
