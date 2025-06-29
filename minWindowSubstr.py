# https://leetcode.com/problems/minimum-window-substring/

'''

DID not understand Read / Solve AGAIN

'''


def minWindow(s, t):
    len1 = len(s)
    len2 = len(t)
    if(len1 < len2):
        return ""
    hp = {}
    hs = {}
    for i in range(0, len2):
        if(hp.get(t[i]) is None):
            hp[t[i]] = 0
        hp[t[i]] += 1

    count = 0
    left = 0
    startIndex = -1
    minlen = float("inf")

    for right in range(0, len1):
        if (hs.get(s[right]) is None):
            hs[s[right]] = 0
        hs[s[right]] += 1

        if(hp.get(s[right]) is None):
            hp[s[right]] = 0
        if(hs.get(s[right]) <= hp.get(s[right])):
            count += 1

        if(count == len2):
            while hs.get(s[left]) > hp.get(s[left]):
                hs[s[left]] -= 1
                left += 1
            windowLen = right-left+1
            if(minlen > windowLen):
                minlen = windowLen
                startIndex = left
    if(startIndex == -1):
        return ""
    return s[startIndex:startIndex+minlen]


s = "ADOBECODEBANC"
t = "ABC"
print(minWindow(s, t))
