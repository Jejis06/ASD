from kol1btesty import runtests


def normalize_word(word:str):
    n = len(word)
    B:list[str] = ["" for _ in range(n)] 

    cnts = [0] * 27

    for i in range(n):
        x = ord(word[i]) - ord('a')
        cnts[x] += 1
    for i in range(1,27):
        cnts[i] += cnts[i-1]

    for i in range(n-1, -1, -1):
        x = ord(word[i]) - ord('a')
        cnts[x] -= 1
        B[cnts[x]] = word[i]

    return ''.join(B)

def counting_sort(T:list[str], ind:int):
    n = len(T)
    B:list[str] = ["" for _ in range(n)] 

    cnts = [0] * 27

    for i in range(n):
        x = ord(T[i][ind]) - ord('a')
        cnts[x] += 1
    for i in range(1,27):
        cnts[i] += cnts[i-1]

    for i in range(n-1, -1, -1):
        x = ord(T[i][ind]) - ord('a')
        cnts[x] -= 1
        B[cnts[x]] = T[i]

    T[0:n] = B[0:n]

def radix_sort(T:list[str], maxlen:int):
    for i in range(maxlen-1, -1, -1):
        counting_sort(T, i)

def f(T:list[str]):
    max_len = len( max(T, key=lambda x: len(x) )) + 1
    buckets:list[list[str]] = [[] for _ in range(max_len)]
    n = len(T)

    for i in range(n):
        w = T[i]
        buckets[len(w)].append(normalize_word(w))

    res = 1
    for i in range(1, max_len):
        if len(buckets[i]) <= 1: continue
        if len(buckets[i]) == 2 and buckets[i][0] == buckets[i][1]:
            res = max(res, 2)
            continue

        radix_sort(buckets[i], i)
        
        curr = 1
        curr_word = buckets[i][0]
        blen = len(buckets[i])
        for j in range(1, blen):
            if curr_word == buckets[i][j]:
                curr += 1
            else:
                curr_word = buckets[i][j]
                res = max(res, curr)
                curr = 1
        res = max(res, curr)
    return res


# Zamien all_tests=False na all_tests=True zeby uruchomic wszystkie testy
runtests( f, all_tests=True)
