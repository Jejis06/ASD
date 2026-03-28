'''
1. T[N], Vi T[i] nal do (0, N) oraz V i,j T[i] != T[j]
Znalezc takie i,  takie ze  po posortowaniu T |T[i+1] - T[i]| bedzie max w O(N) i zwrocic ta roznice 

2. T(N), Vi T[i] nal do (0, k-1)
znajdz i,j T[i:j] ze zawiera wszystkie kolory i jest najmniejszy O(N) zamort

3. Kolejka na 2 stosach

4. a) wstawianie do bst
b) min/ max
c) nastepnik/ poprzednik

5.  Indeksowane drzewo BST
a) znajdz i-ty co do wielkosci element w drzewie
b) w ktorym co do wielosci co do wielkosci elementem jest dany node

6. Suma wartosci w drzewie w stalej zlozonosci pamieciowej
'''

# 4
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


def bst_insert(root:Node, x:Node):
    if x.val < root.val:
        if root.left is None:
            x.parent = root
            root.left = x
        else:
            insert(root.left, x)
    else:
        if root.right is None:
            x.parent = root
            root.right = x
        else:
            insert(root.right, x)

def bst_max(root:Node):
    t = root
    while t.right is not None:
        t = t.right
    return t.val

def bst_min(root:Node):
    while root.left not None:
        root = root.left
    return root.val




