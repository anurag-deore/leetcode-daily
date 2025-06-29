# https://leetcode.com/problems/group-anagrams/
'''
'''


def groupAnagrams(strs):
    o = {}
    ans = []

    def findHash(s):
        return ''.join(sorted(s))
    for s in strs:
        h = findHash(s)
        if h not in o:
            o[h] = []
        o[h].append(s)
    for m in o.values():
        ans.append(m)
    return ans


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))
