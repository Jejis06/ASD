'''
Zad 1______________

a) wstawianie do posortowanej listy
b) usuwanie maksimum z listy
c) insert/ select sort

Zad 2 ______________

min , max z tablicy T[n]
w 3/2n porownan

Zad 3 ______________

przesuniecie cykliczne tablicy
T[n] - w miejscu
T[i] -> T[(i+k)%n]

Zad 4 ______________

Rosnacy ciag A = {a0, a1, .... an-1} liczb naturalnych
o wartosciach nal do {0, 1, 2, ... m-1}

m > n Znajdz pierwsza brakujaca wartosc

Zad 5 ______________

Odwroc liste odsylaczowa

Zad 6 ______________ [bin search po wyniku]

Chomiki

[a1, b1], [a2, b2], ... , [an, bn]
a1 < b1 < a2 < b2 ..... < an < bn

Vi ai, bi nal do N
k chomikow

'''

class Node:
    def __init__(self, value: int):
        self.next: Node | None = None
        self.val = value 

# Zad 1 - a
def insert(head: Node, node:Node) -> Node:
    if head is None: return node

    if head.val > node.val:
        node.next = head
        return node

    curr: Node = head
    while curr is not None and curr.next.val < node.val:
        curr = curr.next

    node.next = curr.next
    curr.next = node
    return head

# Zad 1 - b
def delete_max(head) -> tuple[Node | None, Node | None]:

    if head is None:
        return (None, None)

    curr, prev = head, None
    max_node = head 
    max_val = head.val


    while curr.next:
        if curr.next.val > max_val:
            max_val = curr.next.val
            prev = curr
            max_node = curr.next
        curr = curr.next

    prev.next = max_node.next
    return (head, max_node)

# Zad 1 - c
def selection_sort(head: Node) -> Node:
    new_head = None
    while head is not None:
        head, max_val = delete_max(head)
        max_val.next = new_head
        new_head = max_val
    return new_head

# Zad 2
def max_min(T):
    n = len(T)

    mini = T[0]
    maxi = T[0]

    for i in range(0, n, 2):
        if T[i] < T[i+1]:
            if mini > T[i]:
                mini = T[i]
            if maxi < T[i + 1]:
                maxi = T[i + 1]
        else:
            if mini > T[i+1]:
                mini = T[i+1]
            if maxi < T[i]:
                maxi = T[i]
    return mini, maxi

# Zad 3
def rev(T, s, f):
    while s < f:
        T[s], T[f] = T[f], T[s]
        s += 1
        f -= 1

def move_cyclic(T, k):
    n = len(T)
    l = k % n

    rev(T, 0, n-1)
    rev(T, 0, l-1)
    rev(T, l, n-1)

# Zad 4
def first_val(T):
    n = len(T)
    left = 0
    right = n -1

    while left <= right:
        mid = (left + right) // 2
        if T[mid] == mid:
            left = mid + 1
        else:
            right = mid - 1
    return right

# Zad 5
def revlist(head):

    if head is None:
        return None
    
    prev = None
    curr = head

    while curr is not None:
        t = curr.next
        curr.next = prev
        prev = curr
        curr = t
    return prev

