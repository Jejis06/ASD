"""
5. Czy A[n] i B[n] to anagramy 
a) alf lacinski
b) unicode
"""

def check_anagrams_lat(A:str, B:str, minchr:str) -> bool:
    T = [0] * 26
    n = len(A)
    for i in range(n):
        T[ord(A[i]) - ord(minchr)] += 1
        T[ord(B[i]) - ord(minchr)] -= 1
    return ( not any(T) )

def check_anagrams_unicode(A:str, B:str, T:list[int]) -> bool:
    n = len(A)
    for i in range(n):
        T[ord(A[i])] = 0
        T[ord(B[i])] = 0

    for i in range(n):
        T[ord(A[i])] += 1
        T[ord(B[i])] -= 1

    for i in range(n):
        if T[ord(A[i])] != 0 or T[ord(B[i])] != 0: 
            return False


def solution():
    # TODO: Implement algorithm logic here
    pass

if __name__ == "__main__":
    solution()
        
