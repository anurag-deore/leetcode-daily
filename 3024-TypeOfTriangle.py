'''
Problem Name: 3024. Type of Triangle
Attempted : # 15-09-2025
'''


class Solution:
    def triangleType(self, nums: List[int]) -> str:
        s = set(nums)
        if len(s) == 1:
            return "equilateral"
        else:
            if (
                nums[0] + nums[1] > nums[2]
                and nums[0] + nums[2] > nums[1]
                and nums[1] + nums[2] > nums[0]
            ):
                return "isosceles" if len(s) == 2 else "scalene"
            return "none"
