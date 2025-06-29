'''
Problem Name: 5. Longest Palindromic Substring
Attempted : # 28-06-2025
'''

# DID NOT UNDERSTAND CHECK AGAIN
def longestPalindrome(s):
    if not s or len(s) == 1:
        print("\n\nEdge case hit: returning input as palindrome:", s)
        return s

    start_index = 0       # Start index of the longest palindromic substring found
    max_length = 1        # Length of the longest palindromic substring

    current_index = 0
    while current_index < len(s):
        # Optimization: if the remaining characters can't produce a longer palindrome, break early
        if len(s) - current_index <= max_length // 2:
            print(f"\n\nBreaking early at index {current_index} - remaining characters insufficient")
            break

        left = current_index
        right = current_index
        print(s[:current_index]+"["+s[current_index]+"]"+s[current_index:])
        print(f"\ncurrentIndex => {current_index},char => {s[current_index]}, left => {left}, right => {right}")
        # Expand to the right to skip duplicate characters (handle even-length palindromes)
        while right < len(s) - 1 and s[right + 1] == s[right]:
            print(f"\nnext char is same, so incr right from {right} => {right+1}")
            right += 1
            print(f"\nnew right = {right}")


        # Move to the next center
        current_index = right + 1
        print(f"\n\nMoving to next center: current_index = {current_index},left => {left},right => {right}")
        print(s[:current_index]+"["+s[current_index]+"]"+s[current_index:])

        # Expand outward while characters at both ends match
        while left > 0 and right < len(s) - 1 and s[left - 1] == s[right + 1]:
            left -= 1
            right += 1
            print(f"\n\nExpanding around center: new left = {left}, new right = {right}")


        current_length = right - left + 1
        print(f"\n\nFound palindrome from index {left} to {right}, length = {current_length}")

        # Update the longest palindrome if necessary
        if current_length > max_length:
            start_index = left
            max_length = current_length
            print(f"\n\nNew longest palindrome: start_index = {start_index}, max_length = {max_length}")
        print("\n--------LOOP END-----------\n")

    result = s[start_index:start_index + max_length]
    print("\n\nLongest palindromic substring:", result)
    return result

print(longestPalindrome("xooxrr"))
# print(longestPalindrome("babad"))
# babaccababed
# berfedbaabe