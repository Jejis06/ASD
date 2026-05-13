'''
maksymalnie dlugi podciag rosnacy, niekoniecznie spojny 

[ O(n^2) ]
'''


def lis(arr:list[int]) -> list[int]:
    n = len(arr)

    dp = [1] * n
    parent = [-1] * n

    for k in range(1, n):
        for i in range(k):
            if arr[i] < arr[k] and dp[i] + 1 > dp[k]:
                dp[k] = dp[i] + 1
                parent[k] = i
    
    max_subseq_ind = -1
    curr_subseq = -1

    for i in range(n):
        if dp[i] > curr_subseq:
            max_subseq_ind = i
            curr_subseq = dp[i]

    if max_subseq_ind == -1: return []

    max_subseq:list[int] = []

    while max_subseq_ind != -1:
        max_subseq.append(arr[max_subseq_ind])
        max_subseq_ind = parent[max_subseq_ind]

    return max_subseq[::-1]



