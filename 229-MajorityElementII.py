'''
Problem Name: 229. Majority Element II
Attempted : # 10-08-2025
'''


class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        s = []
        n = len(nums)
        n3 = n/3
        for i in nums:
            if i not in s:
                if nums.count(i) > n3:
                    s.append(i)
        return list(s)


s = Solution()
print(s.majorityElement([3, 2, 3]))
print(s.majorityElement([3]))
print(s.majorityElement([1, 2]))
