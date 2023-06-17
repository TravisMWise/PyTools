import random
from data_structures import BST, Queue, Stack

class AlgoHelper():
    def __init__(self) -> None:
        pass
    def depthFirstSearch(self, bst: BST):
        """Search through a BST going depth first and print out every node."""
        bst.print("PreOrder")

    def breadthFirstSearch(self, bst: BST):
        """Search through a BST going breadth first and print out every node.
        AKA print the level order of a BST."""
        self.bfs(bst.head)
    def bfs(self, root):
        if root == None:
            return
        q = Queue()
        q.enqueue(root)
        while not q.isEmpty():
            cur = q.dequeue()
            print(cur.data, end=" ")
            if cur.left is not None:
                q.enqueue(cur.left)
            if cur.right is not None:
                q.enqueue(cur.right)
    
    def scramble(self, nums: list[int]):
        """Randomize the list order"""
        length = len(nums)
        midvalue = nums[length // 2]
        for i in range(length):
            randValue = random.randrange(0, length-1)
            (nums[i], nums[randValue]) = (nums[randValue], nums[i])
        return (nums, midvalue)

    def permutation(self, nums: list[int]) -> list[list[int]]:
        """Return a list of permuations
        of the list of integers passed in."""
        return self.perm(nums)
    def perm(self, nums):
        l = len(nums)
        if l == 0:
            return []
        elif l == 1:
            return [nums]
        else:
            res = []
            for i in range(l):
                x = nums[i]
                xs = nums[:i] + nums[i+1:]
                for p in self.perm(xs):
                    res.append([x]+list(p))
            return res
    def combination(self, nums: list[int]) -> list[list[int]]:
        return self.comb(nums, len(nums)-1)
    def comb(self, nums, n):
        if n == 0:
            return [[]]
        l = []
        for i in range(len(nums)):
            x = nums[i]
            xs = nums[i+1:]
            xs_comb = self.comb(xs, n-1)
            for p in xs_comb:
                l.append([x, *p])
        return l