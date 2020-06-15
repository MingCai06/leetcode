"""
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n=len(needle)
        N = len(haystack)

        # special cases for inputs are null
        if n==0 and N==0:
            return 0
        if n==0:
            return 0

        # check wether needle in haystack
        # case 1 needle not in haystack
        if needle not in haystack:
            return -1
        # case 2 needle and haystack are identity
        elif needle in haystack and n==N:
            return 0
        # case 3 needle is in haystack, finde the index
        else:
            for i in range(N-n+1):
                temp = haystack[i:i+n]

                if temp == needle:
                    return i
                else:
                    i +=1
