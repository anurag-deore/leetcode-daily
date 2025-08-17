'''
Problem Name: 747. Largest Number At Least Twice of Others
Attempted : # 18-08-2025
'''


class Solution:
    def dominantIndex(self, nums: list[int]) -> int:
        if (len(nums) < 1):
            return -1
        s = sorted(nums, reverse=True)
        if (s[1]*2 <= s[0]):
            return nums.index(s[0])
        return -1


s = Solution()
print(s.dominantIndex([1, 2, 3, 4]))
print(s.dominantIndex([3, 6, 1, 0]))
