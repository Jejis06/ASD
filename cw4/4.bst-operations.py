"""
4. a) wstawianie do bst
b) min/ max
c) nastepnik/ poprzednik
"""

class Node:
    def __init__(self, val:int):
        self.parent:Node|None = None
        self.left:Node|None = None
        self.right:Node|None = None
        self.val:int = val

class BST:
    def __init__(self, val:int):
        self.root:Node = Node(val)

    def insert(self, val:int):
        curr = self.root
        new_node = Node(val)

        while curr != None:
            if val > curr.val:
                if curr.right is None:
                    curr.right = new_node
                    new_node.parent = curr
                    break

                else: curr = curr.right
            else:
                if curr.left is None:
                    curr.left = new_node
                    new_node.parent = curr
                    break
                else: curr = curr.left

    def min(self, node:Node) -> Node|None:
        curr = node
        while curr.left is not None:
            curr = curr.left
        return curr

    def max(self, node:Node) -> Node|None:
        curr = node
        while curr.right is not None:
            curr = curr.right
        return curr

    def predecessor(self, node:Node) -> Node|None:
        if node.left != None:
            return self.max(node.left)
        parent = node.parent
        curr = node

        while parent is not None and curr == parent.left:
            curr = parent
            parent = parent.parent

        if parent is not None:
            return parent
        return None

    def succesor(self, node:Node) -> Node| None:
        if node.right != None:
            return self.min(node.right)
        parent = node.parent
        curr = node

        while parent is not None and curr == parent.right:
            curr = parent
            parent = parent.parent
        if parent is not None:
            return parent
        return None


def solution():
    T = [1,2,3,4,6,7,8,9,10]
    tree = BST(5)
    for i in T:
        tree.insert(i)
    print(tree.min(tree.root).val)
    print(tree.max(tree.root).val)
    pass

if __name__ == "__main__":
    solution()
        
