'''
Problem Name: 3005. Count Elements With Maximum Frequency
Attempted : # 23-09-2025
'''
class Solution:
    def maxFrequencyElements(self, nums: list[int]) -> int:
        s = {}
        for j in nums:
            try:
                if s.get(j) != None:
                    s[j] += 1
                else:
                    s[j] = 1
            except:
                print("Value not found")
        vals = list(s.values())
        m = max(vals)
        c = list(vals).count(m)
        return m*c

    

s = Solution()
print(s.maxFrequencyElements([1,2,2,3,1,4]))
print(s.maxFrequencyElements([1,2,3,4,5]))
