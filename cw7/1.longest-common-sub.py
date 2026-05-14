"""
1. Najdluzszy wspolny podciag.
szukamy taki podciag (niekoniecznie spojny) ktory znajduje sie i w A i w B 
i jest najdluzszy mozliwy

np.
A = aabcbdadb
B = bbaabadadb

tutaj: aabcbd
"""

def solution(A:str, B:str):
    n = len(A); m = len(B)

    dp:list[list[int]] = [[0 for _ in range(m+1)] for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            if A[i-1] == B[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[n][m]

if __name__ == "__main__":
    #_ = solution()
    pass
