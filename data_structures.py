
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

class dNode:
    def __init__(self, data: int=None, next=None, prev=None) -> None:
        self.data = data
        self.next = next
        self.prev = prev
        pass
    pass
class Stack:
    """Stack data type that supports adding 
    and removing from the front of the structure."""
    def __init__(self) -> None:
        self.head = None
        pass
    def push(self, data):
        """Add a value to the front of the stack."""
        if self.head == None: # Check if the stack is empty
            self.head = dNode(data)
        else:
            newHead = dNode(data, self.head)
            self.head = newHead
    def pop(self):
        """Remove the first value to the stack if it exists."""
        if self.head == None:
            return
        else:
            temp = self.head
            self.head = self.head.next
            del temp
    def export(self) -> list:
        """Return every element in the stack as a list"""
        l = []
        temp = self.head
        while temp is not None:
            l.append(temp.data)
            temp = temp.next
        return l
class Queue:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        pass
    def enqueue(self, data):
        """Add a value to the back of the queue."""
        newNode = dNode(data)
        if self.tail == None and self.head == None:
            self.head = self.tail = newNode
        elif self.tail == self.head:
            self.head.next = newNode
            newNode.prev = self.head
            self.tail = newNode
        else: 
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
    def dequeue(self):
        """Remove an element from the front of the queue."""
        if self.tail == None and self.head == None:
            """If the queue is empty"""
            return
        elif self.tail == self.head:
            """If there is one element in the queue."""
            temp = self.tail
            self.tail = self.head = None
            del temp
        else:
            """If there is more than one element in the queue."""
            temp = self.head
            self.head = self.head.next
            self.head.prev = None
            del temp
    def export(self) -> list:
        """Return the queue as a list"""
        l = []
        temp = self.head
        while temp is not None:
            l.append(temp.data)
            temp = temp.next
        return l