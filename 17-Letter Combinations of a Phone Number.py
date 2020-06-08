"""
17. Letter Combinations of a Phone Number
Medium

3693

400

Add to List

Share
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.



Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.
"""
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ref = {
               "2": ['a','b','c'],
               "3": ['d','e','f'],
               "4": ['g','h','i'],
               "5": ['j','k','l'],
               "6": ['m','n','o'],
               "7": ['p','q','r','s'],
               "8": ['t','u','v'],
               "9": ['w','x','y','z']
              }
        if not digits:
            return []

        strlist = ref[digits[0]]
        if len(digits)<2:
            return strlist

        for i in digits[1:]:
            string = []
            for letter in ref[i]:
                string += list(map(lambda x:x+letter, strlist))
            strlist = string
        return strlist
