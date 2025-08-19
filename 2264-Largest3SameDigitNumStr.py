'''
Problem Name: 2264. Largest 3-Same-Digit Number in String
Attempted : # 20-08-2025
'''


class Solution:
    def largestGoodInteger(self, num: str) -> str:
        nums = [x for x in str(num)]
        n = len(nums)
        if (n < 3):
            return ""
        s = "0"
        for i in range(n-2):
            if nums[i] == nums[i+1] and nums[i] == nums[i+2]:
                strs = nums[i]+nums[i]+nums[i]
                if (int(s) <= int(strs)):
                    s = strs
                i += 2
        return s if len(s) > 1 else ""


s = Solution()
print(s.largestGoodInteger("6777133339"))
print(s.largestGoodInteger("2300019"))
print(s.largestGoodInteger("42352338"))
