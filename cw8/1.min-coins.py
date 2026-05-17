"""
1. (wydawanie monet) Mamy daną tablicę z nominałami monet stosowanych w pewnym dziwnym kraju, oraz kwotę T. 
Proszę podać algorytm, który oblicza minimalną ilość monet potrzebną do wydania kwoty T (algorytm zachłanny, 
wydający najpierw największą monetę, nie działa: dla monet 1, 5, 8 wyda kwotę 15 jako 8+5+1+1 zamiast 5+5+5).
"""


def solution(nominaly:list[int], kwota:int) -> int:

    if kwota < 0: return -1

    dp:list[int | float] = [float('inf')] * (kwota + 1)
    dp[0] = 0

    for moneta in nominaly:
        for value in range(moneta, kwota + 1):
            dp[value] = min(dp[value], dp[value - moneta] + 1)

    if dp[kwota] == float('inf'): return -1
    return int(dp[kwota])

if __name__ == "__main__":
    #solution()
    pass
