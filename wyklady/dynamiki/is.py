'''
Problem zbioru wierzcholkow niezaleznych w drzewie:
 - szukamy zbioru wierzcholkow niezaleznych o maksymalnej sumie wartosci

[ O(V) ]
'''

# Zakladam ze drzewo otrzymuje w takiej postaci
class Node:
    def __init__(self, value:int):
        self.val:int = value
        self.children:list[Node] = []

        self.f_mem:int = -1
        self.g_mem:int = -1

def g(tree:Node) -> int:
    if tree.g_mem != -1: return tree.g_mem

    tree.g_mem = 0
    for child in tree.children:
        tree.g_mem += f(child)

    return tree.g_mem

def f(tree:Node) -> int:
    if tree.f_mem != -1: return tree.f_mem

    val:int = tree.val
    for child in tree.children:
        val += g(child)

    tree.f_mem = max(g(tree), val)
    return tree.f_mem

def solution(tree:Node) -> int:
    return f(tree)

