'''
Problem Name: 303. Range Sum Query - Immutable
Attempted : # 10-08-2025
'''


class NumArray:
    nums = []

    def __init__(self, nums: list[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        return sum(self.nums[left:right+1])


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
