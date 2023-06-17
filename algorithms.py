
class AlgoHelper():
    def __init__(self) -> None:
        pass
    def pemutation(self, nums: list[int]) -> list[list[int]]:
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