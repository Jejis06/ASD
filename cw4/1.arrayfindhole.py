"""
1. T[N], Vi T[i] nal do (0, N) oraz V i,j T[i] != T[j]
Znalezc takie i,  takie ze  po posortowaniu T |T[i+1] - T[i]| bedzie max w O(N) i zwrocic ta roznice 
"""

def solution(T:list[int]):
    n = len(T)
    min_val = min(T)
    max_val = max(T)

    used = [False] * n
    min_bucket = [n+1 for _ in range(n)]
    max_bucket = [-1 for _ in range(n)]

    for i in range(n):
        ind = (T[i] - min_val) * (n-1) // (max_val - min_val)
        min_bucket[ind] = min(min_bucket[ind], T[i])
        max_bucket[ind] = max(max_bucket[ind], T[i])
        used[ind] = True

    max_diff = 0
    prev_max = min_val

    for i in range(n-1):
        if not used[i]: continue
        curr_diff = abs(min_bucket[i] - prev_max)
        max_diff = max(max_diff, curr_diff)
        prev_max = max_bucket[i]

    max_diff = max(max_diff, max_val - prev_max)
    return max_diff

if __name__ == "__main__":
    T = [2, 1, 4, 5]
    print(solution(T))
        
