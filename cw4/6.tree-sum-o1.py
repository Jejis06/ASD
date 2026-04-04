"""
6. Suma wartosci w drzewie w stalej zlozonosci pamieciowej

"""

class Node:
    def __init__(self, val:int):
        self.left:Node|None = None
        self.right:Node|None = None
        self.parent:Node|None = None

        self.val:int = val 

class BST:
    def __init__(self):
        self.root:Node|None = None

    def insert(self, val:int):
        node = Node(val)

        if self.root is None:
            self.root = node
            return

        curr = self.root

        while curr is not None:
            if curr.val < val:
                if curr.right is None:
                    curr.right = node
                    node.parent = curr
                    break
                else:
                    curr = curr.right
            else:
                if curr.left is None:
                    curr.left = node
                    node.parent = curr
                    break
                else:
                    curr = curr.left

    def min(self, node:Node) -> Node|None:
        curr = node 
        while curr.left is not None:
            curr = curr.left
        return curr

    def succesor(self, node:Node) -> Node|None:
        if node.right is not None:
            return self.min(node.right)
        
        curr = node
        parent = node.parent

        while parent is not None and curr == parent.right:
            curr = parent
            parent = parent.parent

        if parent is not None:
            return parent
        return None

    def sum(self) -> int:
        res = 0
        if self.root is None: return 0


        min_node = self.min(self.root)
        while min_node is not None:
            res += min_node.val
            min_node = self.succesor(min_node) 

        return res

    def print_tree(self, node:Node|None=None):
        if node is None: node = self.root
        if node is None: return
        print("printing treee")
        level:list[Node] = [node]
        next_level:list[Node] = []
        while True: 
            for node in level:
                if node.left is not None:
                    next_level.append(node.left)
                if node.right is not None:
                    next_level.append(node.right)
            for node in level:
                print(node.val, end = ' ')
            print()
            if len(next_level) == 0: break
            level = next_level
            next_level = []





def solution():
    T = [1,2,3,4,6,7,8,9,10]
    tree = BST()
    tree.insert(5)
    for x in T:
        tree.insert(x)
    print("sum", tree.sum())
    tree.print_tree()

if __name__ == "__main__":
    solution()
        
