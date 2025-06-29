'''
Problem Name: 2311. Longest Binary Subsequence Less Than or Equal to K
Attempted : # 27-06-2025
'''

def longestSubsequence(self, s: str, k: int) -> int:
    subs = ""
    print("checking s = ",s)
    for i in range(len(s) - 1, -1, -1):
        print("subs",subs)
        if (s[i]=='0'):
          subs = s[i] + subs
        elif(s[i] == '1'):
          print(s[i]+subs,"=>",int(s[i]+subs,2))
          if int(s[i] + subs,2) <= k:
            subs = s[i] + subs

    print(subs)
    return len(subs)

if __name__ == "__main__":
  s = "1001010"
  k = 5
  print('\n\n',longestSubsequence(None, s, k))


  s = "00101001"
  k = 1
  print("\n\n",longestSubsequence(None, s, k))
#   # Explanation: The longest subsequence is "001010" which is less than or equal to 5.
#   s = "1111"
#   k = 1
#   print("\n\n",longestSubsequence(None, s, k))        