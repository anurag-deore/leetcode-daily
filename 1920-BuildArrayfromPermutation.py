'''
Problem Name : 1920. Build Array from Permutation
Attempted : # 10-09-2025
'''
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return list(map(lambda x: nums[x], nums))
