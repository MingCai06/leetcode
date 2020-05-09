#### Question ####
"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""



#### solution 1 ####
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        check = []
        max_len=0
        for i in s:
            if i in check:
                check = check[check.index(i)+1:] #pop up the previous item by duplicating
            check.append(i)
            max_len=max(max_len, len(check)) # update max length
        return max_len
#### solution 2 ####
"""
While the characters are not repeating we are updating the longest variable, once we get to repeating we update the start_idx from which we start trimming the original strin
"""
        # last_seen = {}
        # start_idx = 0
        # longest = 0
        # for i, char in enumerate(s):
        #     if char in last_seen:
        #         start_idx = max(start_idx, last_seen[char] + 1)
        #     longest = max(longest, i + 1 - start_idx)
        #     last_seen[char] = i
        # return longest
