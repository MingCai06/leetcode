"""
Question
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""

"""
# IDEA:
Expand Around Center
In fact, we could solve it in O(n^2) time using only constant space.

We observe that a palindrome mirrors around its center. Therefore, a palindrome can be expanded from its center, and there are only 2n - 1such centers.

You might be asking why there are 2n - 12n−1 but not nn centers? The reason is the center of a palindrome can be in between two letters. Such palindromes have even number of letters (such as "abba") and its center are between the two 'b's.
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:

        start_str = ''

        if len(s)<1:
            return (s)
        start_str = s[0]

        def extend(i, j ,s):
            while (i>=0 and j<len(s) and s[i]==s[j]):
                i -=1
                j +=1
            return (s[i+1:j])

        for i in range(len(s)-1):
            e1 = extend(i,i,s)
            e2 = extend(i,i+1,s)
            if max(len(e1), len(e2))>len(start_str):
                start_str = e1 if len(e1)>len(e2) else e2
        return start_str
