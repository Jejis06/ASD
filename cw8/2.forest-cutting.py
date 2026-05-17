"""
2. (Black Forest) Black Forest to las rosnący na osi liczbowej gdzieś w południowej Anglii. 
Las składa się z n drzew rosnących na pozycjach 0,...,n-1. Dla każdego i ze zbioru {0,...,n-1} 
znany jest zysk c_i, jaki można osiągnąć ścinając drzewo z pozycji i. John Lovenoses chce uzyskać 
maksymalny zysk ze ścinanych drzew, ale prawo zabrania ścinania dwóch drzew pod rząd. 
Proszę zaproponować algorytm, dzięki któremu John znajdzie optymalny plan wycinki.
"""

def solution(trees:list[int]) -> int:
    n = len(trees)

    if n == 0: return 0
    if n == 1: return trees[0]

    a1 = trees[0]
    a2 = max(trees[0], trees[1])
    for i in range(2, n):
        a3 = max(a1 + trees[i], a2)
        a1 = a2
        a2 = a3

    return a2



if __name__ == "__main__":
    #solution()
    pass
