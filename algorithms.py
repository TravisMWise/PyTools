import random
from data_structures import BST, Queue, Stack

class AlgoHelper:
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
    
class Searcher:
    """
    At 10,000 entries the time taken to search all entries is
        binarySearch: 0.007999897003173828 | o(log(n))
        iterativeSearch: 1.0460429191589355 | o(n)
    """
    def __init__(self) -> None:
        pass
    def depthFirstSearch(self):
        pass
    def binarySearch(self, nums, value) -> bool:
        """Take in an array of integers and a target value. 
        Search for the value in the array, return True if successful 
        and false otherwise."""
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = low + (high-low) // 2 
            if value == nums[mid]:
                return True
            elif nums[mid] < value:
                low = mid + 1
            else:
                high = mid - 1
        return False
    def iterativeSearch(self, nums, value) -> bool:
        """Iterate through the list and return true if the value is in the list"""
        for e in nums:
            if e == value:
                return True
        return False

class Sorter:
    """A class to sort integer values using multiple and separate methods."""
    def bubbleSort(self, nums) -> None:
        """If an element is smaller than the element before it swap the two elements."""
        length = len(nums)
        for i in range(length):
            for j in range(i+1, length):
                if nums[j] < nums[i]:
                    temp = nums[j]
                    nums[j] = nums[i]
                    nums[i] = temp
        return nums
    def selectionSort(self, nums) -> None:
        """Find the smallest element in the unsorted/right section of the nums and place
        it in the correct spot in the nums."""
        length = len(nums)
        for i in range(length):
            minValue = nums[i]
            minIndex = i
            for j in range(i+1, length):
                if nums[j] < minValue:
                    minValue = nums[j]
                    minIndex = j
            temp = nums[i]
            nums[i] = nums[minIndex]
            nums[minIndex] = temp
    def insertionSort(self, nums) -> None:
        """Create a sorted section of the nums at the beginning of the nums.
        While the next number in the nums is not in the correct position swap it with it's neighbor."""
        length = len(nums)
        for i in range(length - 1):
            j = i+1
            while j >= 1 and nums[j] < nums[j-1]:
                temp = nums[j-1]
                nums[j-1] = nums[j]
                nums[j] = temp
                j -= 1
    def mergeSort(self, nums) -> list:
        """Split the nums in half recursively until the halfs are sorted (1 element each).
        Sort the separate nums segments based on the first element in the two subnumss"""
        length = len(nums)
        nums = self.split(nums, length)
        return nums
    def split(self, nums, length) -> list:
        """A helper method for merge sort."""
        if length == 1:
            return nums
        firstHalf = nums[0:length//2]
        secondHalf = nums[length//2:length]
        list1 = self.split(firstHalf, len(firstHalf))
        list2 = self.split(secondHalf, len(secondHalf))
            
        # Merge and return the lists in sorted order
        ret = []; i = 0; j = 0
        lenList1 = len(list1); lenList2 = len(list2)
        while i < lenList1 and j < lenList2:
            if list1[i] <= list2[j]:
                ret.append(list1[i])
                i += 1
            elif list2[j] < list1[i]:
                ret.append(list2[j])
                j += 1
        if i < lenList1:
            for k in range(i, lenList1):
                ret.append(list1[k])
        elif j < lenList2:
            for k in range(j, lenList2):
                ret.append(list2[k])
        return ret
    def quickSort(self, nums):
        self.qS(nums, 0, len(nums)-1)
    def qS(self, nums, low, high):
        if low < high:
            partition = self.partition(nums, low, high)

            self.qS(nums, low, partition-1)
            self.qS(nums, partition+1, high)
    def partition(self, nums, low, high):
        pivot = nums[high]
        i = low - 1
        for j in range(low, high):
            if nums[j] <= pivot:
                i += 1
                (nums[i], nums[j]) = (nums[j], nums[i])
        (nums[i+1], nums[high]) = (nums[high], nums[i+1])
        return i + 1
