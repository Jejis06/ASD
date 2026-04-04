"""
5.  Indeksowane drzewo BST
a) znajdz i-ty co do wielkosci element w drzewie
b) w ktorym co do wielosci elementem jest dany node

"""
from random import randint

class Node:
    def __init__(self, val:int):
        self.left: Node|None = None
        self.right: Node|None = None
        self.parent: Node|None = None

        self.val:int = val

        self.left_count:int = 0
        self.right_count:int = 0

class BST:
    def __init__(self):
        self.root:Node | None = None

    def insert(self, value:int):
        node = Node(value)
        if self.root is None:
            self.root = node 
            return

        curr = self.root

        while curr is not None:
            if curr.val < value:
                curr.right_count += 1
                if curr.right is None:
                    curr.right = node
                    node.parent = curr
                    break
                curr = curr.right
            else:
                curr.left_count += 1
                if curr.left is None:
                    curr.left = node
                    node.parent = curr
                    break
                curr = curr.left

    def find_kth(self, k:int) -> Node | None:
        if self.root is None: return None

        base_ind = self.root.left_count
        curr: Node = self.root

        while base_ind != k: 
            # idziemy w lewo
            if k < base_ind:
                if curr.left is None: return None

                base_ind -= (curr.left.right_count + 1)
                curr = curr.left
            # idziemy w prawo
            else:
                if curr.right is None: return None
                base_ind += (curr.right.left_count + 1)
                curr = curr.right

        return curr

    def find_node_val(self, val:int) -> Node|None:
        curr = self.root
        if curr is None: return None

        while curr is not None and curr.val != val:
            if val > curr.val:
                curr = curr.right
            else:
                curr = curr.left
        return curr

    def ind_in_order(self, val:int) -> int:
        curr = self.find_node_val(val) 

        if curr is None: return -1
        if self.root is None: return -1

        if curr == self.root: return self.root.left_count

        ind = self.root.left_count
        parent = curr.parent

        while parent is not None:
            if parent.right == curr:
                ind += (curr.left_count + 1)
            else:
                ind -= (curr.right_count + 1)
            curr = parent
            parent = parent.parent

        return ind



def solution():
    n = randint(5,20)
    arr:list[int] = []
    print(n)
    while len(arr) < n:
        x = randint(0, 2*n)
        while x in arr:
            x = randint(0, 2*n)
        arr.append(x)

    print(*sorted(arr), sep=', ')
    tree = BST()
    for x in arr:
        tree.insert(x)

    arr.sort()
    for i in range(n):
        print(tree.find_kth(i).val, end=', ')

    print()
    for x in arr:
        ind = tree.ind_in_order(x)
        print(f"val: {x}, ind:{ind}, check:{arr[ind] == x}")
    print()

    print("Checking errors:")
    non_exisitng_node = tree.find_kth(n+1)
    non_exisitng_ind = tree.ind_in_order(2*n + 1)
    print(f"Non exisitng node find result : {non_exisitng_node}")
    print(f"Non exisitng value find result : {non_exisitng_ind}")



        

if __name__ == "__main__":
    solution()
        
