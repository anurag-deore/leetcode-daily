'''
Problem Name: 1863. Sum of All Subset XOR Totals
Attempted : # 04-08-2025
'''


class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        sumXOR = 0
        n = len(nums)
        for i in range(2**n):
            subsetXOR = 0
            for j in range(n):
                if (i & (1 << j)):
                    subsetXOR = subsetXOR ^ nums[j]
            sumXOR += subsetXOR
        return sumXOR


s = Solution()
# print(s.subsetXORSum([5, 1, 6]))
print(s.subsetXORSum([1, 3]))
