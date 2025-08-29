'''
Problem Name: 2566. Maximum Difference by Remapping a Digit
Attempted : # 30-08-2025
'''

import re


class Solution:
    def minMaxDifference(self, num: int) -> int:
        if num < 10:
            # if num == 0 or num == 9: return 8
            # else: return 9
            return 9

        s_num = str(num)
        first = s_num[0]
        max_digit = num
        try:
            first_non_nine = re.search(r"[0-8]", s_num).group()
            max_digit = int(s_num.replace(first_non_nine, "9"))
        except AttributeError:
            first_non_nine = "0"
        # print(first, first_non_nine)

        min_digit = int(s_num.replace(first, "0"))

        return max_digit-min_digit


s = Solution()
print(s.minMaxDifference(99999))
