"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
"""
"""
solution1: replace character

class Solution:
    def isValid(self, s: str) -> bool:
        while '()' in s or '[]'in s or '{}'in s:
            s = s.replace('()','').replace('[]','').replace('{}','')

        return s ==''
"""
"""
solution2
stack data structure
"""
class Solution:
    def isValid(self, s: str) -> bool:

        ref = {'(':')','[':']','{':'}'}
        open_par = set(['(','[','{'])
        stack = []
        for i in s:
            if i in open_par:
                stack.append(i)
            elif stack and i == ref[stack[-1]]:
                stack.pop()
            else:
                return False
        return stack == []
