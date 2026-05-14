"""
3. Max i min 
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

Każdy wyodrębniony podciąg posiada swoją wartość (suma jego elementów). 
Wartość całego dokonanego podziału definiujemy jako najmniejszą z wartości tych podciągów, 
co można zapisać wzorem:

Wartość podziału = min(S_1, S_2, ..., S_k)

CEL ZADANIA:
Dla zadanego ciągu A oraz liczby "k", należy znaleźć taki podział na "k" spójnych podciągów, 
dla którego wartość całego podziału będzie jak największa (maksymalna). Innymi słowy, 
szukamy optymalnego podziału, który maksymalizuje najmniejszą wartość ze 
wszystkich utworzonych podciągów.
"""

# O(k * n^2)

def solution(nums:list[int], k:int):

    n = len(nums)
    sums = [0] * n

    sums[0] = nums[0]
    for i in range(1, n):
        sums[i] = sums[i-1] + nums[i]

    dp:list[list[int]] = [[0 for _ in range(k+1)] for _ in range(n)]

    for i in range(n):
        dp[i][1] = sums[i]

    for i in range(n):
        for j in range(2, k+1):

            if j > i + 1: 
                continue

            for m in range(i):
                dp[i][j] = max( dp[i][j], min(dp[m][j-1], sums[i] - sums[m]))
    return dp[n-1][k]




if __name__ == "__main__":
#    solution()
    pass
