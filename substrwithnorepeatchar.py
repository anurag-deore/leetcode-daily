# https://leetcode.com/problems/longest-substring-without-repeating-characters/

def getLongestSubstr(s):
    left = 0
    right = 0
    ans = 0
    n = len(s)
    m = {}
    while (left<n and right <n):
        el = s[right]
        if el in m:
            left = max(left,m[el]+1)
        m[el] = right
        ans = max(ans,right-left+1)
        right+=1
    return ans
    # Alternate Solution
    '''
    window = set()
    left, res = 0, 0
    for right in range(len(s)):
        while s[right] in window:
            window.remove(s[left])
            left += 1
        window.add(s[right])
        res = max(res, len(window))
    return res
    '''

string = "abaacad"
print(getLongestSubstr(string))