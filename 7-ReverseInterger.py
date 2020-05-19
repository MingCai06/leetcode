"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""

class Solution:
    def reverse(self, x: int) -> int:
        r_x = ''
        if x > -10 and x<10:
            return x
        elif x > pow(2,31)-1 or x < -pow(2,31):
            return 0
        else:
            str_x =str(x)
            if x>0:
                r_x = r_x
            elif x<0:
                str_x = str_x[1:]
                r_x += '-'
            for i in reversed(range(len(str_x))):
                if i== len(str_x)-1 and str_x[i]==0:
                    r_x = r_x
                else:
                    r_x = r_x + str_x[i]
            if int(r_x)> pow(2,31)-1 or int(r_x) < -pow(2,31):
                return 0
            else:
                return int(r_x)
