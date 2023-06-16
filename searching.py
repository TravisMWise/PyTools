class Searcher:
    """
    At 10,000 entries the time taken to search all entries is
        binarySearch: 0.007999897003173828 | o(log(n))
        iterativeSearch: 1.0460429191589355 | o(n)
    """
    def __init__(self) -> None:
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

