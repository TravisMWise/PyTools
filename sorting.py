class Sorter():
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
        values = self.split(nums, length)
        return values
    def split(self, nums, length) -> list:
        """A helper method for merge sort."""
        if length == 1:
            return nums
        firstHalf = nums[0:length//2]
        secondHalf = nums[length//2:length]
        # print(firstHalf, secondHalf)
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
