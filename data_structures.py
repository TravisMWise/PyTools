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
            # print("Data already entered, no duplicates.")
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
    def printAll(self, cur, type):
        if cur:
            if type == "PreOrder": 
                print(cur.data, end=" ")
            self.printAll(cur.left, type)
            if type == "InOrder": 
                print(cur.data, end=" ")
            self.printAll(cur.right, type)
            if type == "PostOrder": 
                print(cur.data, end=" ")
class AVL:
    pass
class Trie:
    pass
class dNode:
    """Node data structure for stacks, queues, and linked lists."""
    def __init__(self, data: int=None, next=None, prev=None) -> None:
        self.data = data
        self.next = next
        self.prev = prev
        pass
class LinkedList:
    """Doubly LinkedList that supports adding and removing from both ends."""
    def __init__(self) -> None:
        self.head = self.tail = None
    def addStart(self, data):
        """Add a value to the start of the list."""
        newNode = dNode(data)
        if self.head == None:
            self.head = self.tail = newNode
            pass
        elif self.head == self.tail:
            self.head = newNode
            self.head.next = self.tail
            self.tail.prev = self.head
            pass
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
    def addEnd(self, data):
        """Add a value to the end of the list."""
        newNode = dNode(data)
        if self.head == None:
            self.head = self.tail = newNode
        elif self.head == self.tail:
            self.tail = newNode
            self.head.next = self.tail
            self.tail.prev = self.head
        else:
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode
    def delStart(self):
        """Remove a value from the start of the list."""
        if self.head == None:
            return
        elif self.head == self.tail:
            temp = self.head
            self.head = self.tail = None
            del temp
        else:
            temp = self.head
            if self.head.next == self.tail:
                self.tail.prev = None
                self.head = self.tail
            else:
                self.head = self.head.next
                self.head.prev = None
            del temp
    def delEnd(self):
        """Remove a value from the end of the list."""
        if self.head == None:
            return
        elif self.head == self.tail:
            temp = self.tail
            self.head = self.tail = None
            del temp
        else:
            temp = self.tail
            if self.tail.prev == self.head:
                self.head.next = None
                self.tail = self.head
            else:
                self.tail = self.tail.prev
                self.tail.next = None
            del temp
    def export(self):
        """Return the LinkedList as a list from head to tail."""
        l = []
        temp = self.head
        while temp is not None:
            l.append(temp.data)
            temp = temp.next
        return l
class Stack:
    """Stack data type that supports adding 
    and removing from the front of the structure."""
    def __init__(self) -> None:
        self.head = None
        pass
    def isEmpty(self) -> bool:
        if self.head == None:
            return False
        return True
    def push(self, data):
        """Add a value to the front of the stack."""
        if self.head == None: # Check if the stack is empty
            self.head = dNode(data)
        else:
            newHead = dNode(data, self.head)
            self.head = newHead
    def pop(self):
        """Remove the first value to the stack if it exists
        and return it."""
        if self.head == None:
            return self.head.data
        else:
            temp = self.head
            self.head = self.head.next
            ret = temp.data
            del temp
            return ret
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
    def isEmpty(self):
        if self.head:
            return False
        return True
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
            return None
        elif self.tail == self.head:
            """If there is one element in the queue."""
            temp = self.tail
            self.tail = self.head = None
            ret = temp.data
            del temp
            return ret
        else:
            """If there is more than one element in the queue."""
            temp = self.head
            self.head = self.head.next
            self.head.prev = None
            ret = temp.data
            del temp
            return ret
    def export(self) -> list:
        """Return the queue as a list"""
        l = []
        temp = self.head
        while temp is not None:
            l.append(temp.data)
            temp = temp.next
        return l