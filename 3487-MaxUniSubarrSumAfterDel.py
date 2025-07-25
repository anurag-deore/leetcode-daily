'''
Problem Name: 3487. Maximum Unique Subarray Sum After Deletion
Attempted : # 25-07-2025
'''


class Solution:
    def maxSum(self, nums: list[int]) -> int:
        s = set(nums)
        if len(s) < 2:
            return list(s)[0]
        sum = 0
        negs = 0
        for i in s:
            if i > 0:
                sum += i
            elif i < 0:
                negs += 1
        if (negs == len(s)):
            return max(list(s))
        return sum


s = Solution()
print(s.maxSum([1, 2, 3, 4, 5]))
print(s.maxSum([1, 1, 0, 1, 1]))
print(s.maxSum([-100]))
print(s.maxSum([-17, -15]))
print(s.maxSum([1, 2, -1, -2, 1, 0, -1]))
