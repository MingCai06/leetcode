#Given an array of integers, return indices of the two numbers such that they add up to a specific target.

#You may assume that each input would have exactly one solution, and you may not use the same element twice.
"""
Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1]

"""

import numpy as np
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
###### solution 1########
#         for i in range(0,len(nums)):
#             for j in range(i+1,len(nums)):
#                 if nums[i]+nums[j] != target: continue
#                 return [i,j]

###### solution 2 use hash map ########
        dic = {}
        for i in range(0,len(nums)):
            n = target - nums[i]
            if n in dic.keys():
                return [dic[n],i]
            dic[nums[i]]=i
