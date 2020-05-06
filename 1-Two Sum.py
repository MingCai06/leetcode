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
