"""
6. Posortuj n slow
w czasie liniowym wzgl sumy ich dlugosci
"""

# Sortowanie shortx --------------------------------

def sort_by_len(words:list[str]):
    n = len(words)
    max_len = len( max(words, key=len) )

    cnts = [0] * (max_len + 1)
    n_words = [''] * n

    for i in range(n):
        cnts[ len(words[i]) ] += 1

    for i in range(1, max_len + 1):
        cnts[i] += cnts[i - 1]

    for i in range(n-1, -1, -1):
        cnts[ len(words[i]) ] -= 1
        n_words[ cnts[ len(words[i]) ] ] = words[i]
    words[0:n] = n_words[0:n]


# k - indeks o jeden dalej niz koniec
# p - indeks bezposrednio startu

def counting_sort_radix(words:list[str], ind: int ,p:int, k:int): 
    max_chr = ord(max(words[p:k], key=lambda w: ord(w[ind]))[ind])
    min_chr = ord(min(words[p:k], key=lambda w: ord(w[ind]))[ind])


    cnts_len = (max_chr - min_chr + 1)

    cnts = [0] * cnts_len
    n_words = [""] * (k - p)
    for i in range(p, k):
        id = ord(words[i][ind]) - min_chr
        cnts[id] += 1

    for i in range(1, cnts_len):
        cnts[i] += cnts[i - 1]

    for i in range(k-1, p-1, -1):
        id = ord(words[i][ind]) - min_chr
        cnts[id] -= 1
        n_words[ cnts[id] ] = words[i]

    for i in range(p, k):
        words[i] = n_words[i - p]

# k - indeks o jeden dalej niz koniec
# p - indeks bezposrednio startu
def radix_sort(words:list[str], max_len:int, p:int, k:int):
    max_len -= 1
    while max_len > -1:
        counting_sort_radix(words, max_len, p, k)
        max_len -= 1

def sort_words_shortx(words:list[str]):
    sort_by_len(words)

    start_strip = 0
    end_strip = 0
    curr_len = 0

    n = len(words)

    for i in range(n):
        if len(words[i]) != curr_len or i == n:
            end_strip = i - 1
            if end_strip - start_strip > 1:
                radix_sort(words, curr_len, start_strip, end_strip+1)

            start_strip = i
            curr_len = len(words[i])

# Sortowanie leksykograficzne --------------------------------

def radix_sort_first(words:list[str], l:int, r:int, ind:int):
    if l >= r: return

    cnts = [0] * 258
    for i in range(l, r+1):
        id = ord(words[i][ind]) + 1 if ind < len(words[i]) else 0
        cnts[id + 1] += 1

    for i in range(1, 258):
        cnts[i] += cnts[i - 1]

    aux = [""] * (r - l + 1)
    for i in range(l, r + 1):
        id = ord(words[i][ind]) + 1 if ind < len(words[i]) else 0
        aux[cnts[id]] = words[i]
        cnts[id] += 1

    for i in range(l, r+1):
        words[i] = aux[i - l]

    for i in range(1, 257):
        start = l + (cnts[i-1] if i > 0 else 0)
        end = l + cnts[i] - 1

        if start < end:
            radix_sort_first(words, start, end, ind+1)


def sort_words_lex(words:list[str]):
    if not words: return
    n = len(words)
    radix_sort_first(words, 0, n-1, 0)




if __name__ == "__main__":
    A = ["skiiii", 'aaa', "aaaa", "bbbb", "cccc", "rps", "dss", "dar", "das", "qtak", "adsadad", "dasdjkahdkha"]
    B = [b for b in A]
    print(A)
    sort_words_shortx(A)
    sort_words_lex(B)
    print(f"Shortx: {A}")
    print(f"Lexig:  {B}")
    print(f"Actua:  {sorted(A)}")

