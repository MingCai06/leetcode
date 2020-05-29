"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
"""

"""
# IDEA:
 We compare characters from top to bottom on the same column (same character index of the strings) before moving on to the next column.
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        co = ""
        for i in zip(*strs):
            if len(set(i)) == 1:
                co = co + i[0]
            else:
                break
        return co
