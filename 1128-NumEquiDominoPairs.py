'''
Problem Name: 1128. Number of Equivalent Domino Pairs
Attempted: # 03-09-2025
'''

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        normalized = [tuple(sorted(domino)) for domino in dominoes]
        count = Counter(normalized)
        result = sum(v * (v - 1) // 2 for v in count.values())
        return result
