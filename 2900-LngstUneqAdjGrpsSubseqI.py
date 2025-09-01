'''
Problem Name: 2900. Longest Unequal Adjacent Groups Subsequence I
Attempted : # 02-09-2025
'''


class Solution:
    def getLongestSubsequence(self, words: list[str], groups: list[int]) -> list[str]:
        currChar = groups[0]
        selected = [words[0]]
        for i in range(1, len(groups)):
            if currChar != groups[i]:
                currChar = groups[i]
                selected.append(words[i])
        return selected


s = Solution()
print(s.getLongestSubsequence(["e", "a", "b"], [0, 0, 1]))
print(s.getLongestSubsequence(["a", "b", "c", "d"], [1, 0, 1, 1]))
