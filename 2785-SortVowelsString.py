'''
Problem Name: 2785. Sort Vowels in a String
Attempted : # 11-09-2025
'''

import bisect


class Solution:

    def sortVowels(self, s: str) -> str:
        # vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'U', 'O']
        # vowels_dict = {'A': 65, 'E': 69, 'I': 73, 'O': 79,
        #                'U': 85, 'a': 97, 'e': 101, 'i': 105, 'o': 111, 'u': 117}
        # vowelAscii = []
        # vowelIndex = []
        # for i in range(len(s)):
        #     if s[i] in vowels:
        #         vowelIndex.append(i)
        #         # print(vowels_dict[s[i]], s[i])
        #         bisect.insort(vowelAscii, vowels_dict[s[i]])
        # # print(vowelAscii, vowelIndex)

        # for i in vowelIndex:
        #     # print(vowelAscii)
        #     s = s[:i] + chr(vowelAscii.pop(0)) + s[i+1:]

        # return ''.join(s)
        vowels = set('aeiouAEIOU')
        arr = sorted([c for c in s if c in vowels])
        print(arr)
        res = []
        i = 0

        for c in s:
            if c in vowels:
                res.append(arr[i])
                i += 1
            else:
                res.append(c)
        print(res)
        return ''.join(res)


s = Solution()
print(s.sortVowels("lEetcOde"))
