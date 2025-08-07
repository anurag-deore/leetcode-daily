'''
Problem Name: 541. Reverse String II
Attempted : # 07-08-2025
'''


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        result = ""
        for i in range(0, len(s), 2 * k):
            # Reverse the first k characters of the current segment
            segment = s[i: i + 2 * k]
            reversed_part = segment[:k][::-1]
            remaining_part = segment[k:]
            result += reversed_part + remaining_part
        return result


s = Solution()
print(s.reverseStr("abcdefg", 2))
