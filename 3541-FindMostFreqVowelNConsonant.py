'''
Problem Name: 3541. Find Most Frequent Vowel and Consonant
Attempted : # 24-09-2025
'''
class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowelMap = {"a":0,"e":0,"i":0,"o":0,"u":0}
        consonantMap = {"b":0,"c":0,"d":0,"f":0,"g":0,"h":0,"j":0,"k":0,"l":0,"m":0,"n":0,"p":0,"q":0,"r":0,"s":0,"t":0,"v":0,"w":0,"x":0,"y":0,"z":0}
        for char in s:
            if char in "aeiou":
               vowelMap[char] += 1
            else:
                consonantMap[char] += 1
        return max(vowelMap.values()) + max(consonantMap.values())

    

s = Solution()
print(s.maxFreqSum("successes"))
print(s.maxFreqSum("aeiaeia"))
