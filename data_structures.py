
class Node:
    def __init__(self, data=None, left=None, right=None) -> None:
        self.data = data
        self.left = left
        self.right = right
class BST:
    def __init__(self) -> None:
        self.head = Node()
        pass
    def add(self, data):
        if self.head.data == None:
            self.head.data = data
            return
        else:
            self.addNode(data, self.head)
    def addNode(self, data, cur):
        if data == cur.data:
            print("Data already entered, no duplicates.")
            return
        if data < cur.data:
            if cur.left == None:
                cur.left = Node(data)
            else:
                self.addNode(data, cur.left)
        else:
            if cur.right == None:
                cur.right = Node(data)
            else:
                self.addNode(data, cur.right)
    def remove(self, data):
        self.removeNode(self.head, data)
        pass
    def removeNode(self, cur, data):
        """
        1. Find the node.
        2. Check the number of children.
            - No Children == Delete Node.
            - 1 Child == Swap with child and then delete child.
            - 2 Children == Find largest value to the left of node and swap
        """
        if cur is None:
            return cur
        if data < cur.data:
            cur.left = self.removeNode(cur.left, data)
        if data > cur.data:
            cur.right = self.removeNode(cur.right, data)
        
        if cur.left is None:
            temp = cur.right
            del cur
            return temp
        elif cur.right is None:
            temp = cur.left
            del cur
            return temp
        else:
            parent = cur
            child = cur.right
            while child.left is not None:
                parent = child
                child = child.left
            
            if parent != cur:
                parent.left = child.right
            else:
                parent.right = child.right

            cur.data = child.data

            del child
            return cur
    def contains(self, data) -> bool:
        return self.containsNode(self.head, data)
    def containsNode(self, cur, data) -> bool:
        if cur == None:
            return False
        if cur.data == data:
            return True
        elif data < cur.data:
            return self.containsNode(cur.left, data)
        elif data > cur.data:
            return self.containsNode(cur.right, data)
    def print(self, type):
        print(type + ": ")
        self.printAll(self.head, type)
        print()
    def printAll(self, head, type):
        if head:
            if type == "PreOrder": print(head.data, end=" ")
            self.printAll(head.left, type)
            if type == "InOrder": print(head.data, end=" ")
            self.printAll(head.right, type)
            if type == "PostOrder": print(head.data, end=" ")
class AVL:
    pass
class Trie:
    pass