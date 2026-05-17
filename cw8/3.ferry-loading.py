"""
3. (ładowanie promu) Dana jest tablica A[n] z długościami samochodów, które stoją w kolejce, 
żeby wjechać na prom. Prom ma dwa pasy (lewy i prawy), oba długości L. Proszę napisać program, 
który wyznacza, które samochody powinny pojechać na który pas, żeby na promie zmieściło się 
jak najwięcej aut. Auta muszą wjeżdżać w takiej kolejności, w jakiej są podane w tablicy A.
"""

def solution(A:list[int], L:int) -> list[tuple[int, str]]:
    n = len(A)

    if len(A) == 0: return [] 

    prefSum:list[int] = [0] * n
    prefSum[0] = A[0]
    for i in range(1, n):
        prefSum[i] = prefSum[i-1] + A[i]

    dp:list[list[bool]] = [[False for _ in range(L+1)] for _ in range(n+1)]
    dp[0][0] = True

    # 0 - brak, 1 - lewo, 2 - prawo
    backSol:list[list[int]] = [[0 for _ in range(L+1)] for _ in range(n+1)]

    max_cars = 0
    max_left = 0

    for i in range(1, n+1):
        changed = False
        for l in range(L+1):
            if dp[i-1][l]:
                if l + A[i-1] <= L:
                    max_left = l + A[i-1]
                    dp[i][l + A[i-1]] = True

                    backSol[i][l+A[i-1]] = 1
                    changed = True

                if prefSum[i-1] - l <= L:
                    max_left = l
                    dp[i][l] = True

                    backSol[i][l] = 2
                    changed = True

        if changed:
            max_cars = i
        else: break

    if max_cars == 0:
        return [] 

    res:list[tuple[int, str]] = []

    curr_car = max_cars
    curr_l = max_left


    while curr_car != 0:
        direction = backSol[curr_car][curr_l]
        car_len = A[curr_car - 1]

        if direction == 1:   # lewo
            curr_l -= car_len
            res.append((car_len, "left"))

        elif direction == 2: # prawo
            res.append((car_len, "right"))

        curr_car -= 1

    return res[::-1]



if __name__ == "__main__":
    #solution()
    pass
