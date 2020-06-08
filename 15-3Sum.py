"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""
"""
Solution
Sort based algorithm

a+b = -c. 3SUM reduces to 2SUM problem.
Handling Duplicates in 2SUM

Say index s and e are forming a solution in a sorted array. Now givens nums[s], there is a unique nums[e] such that nums[s]+nums[e]=Target. Therefore, if nums[s+1] is the same as nums[s], then searching in range s+1 to e will give us a duplicate solution. Thus we must move s till nums[s] != nums[s-1] to avoid getting duplicates.
                        while s<e and nums[s] == nums[s-1]:
                            s = s+1
Handling Duplicates in 3SUM

Imagine we are at index i and we have invoked the 2SUM problem from index i+1 to end of the array. Now once the 2SUM terminates, we will have a list of all triplets which include nums[i]. To avoid duplicates, we must skip all nums[i] where nums[i] == nums[i-1].
            if i > 0 and nums[i] == nums[i-1]:
                continue
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solutions = []
        if not nums or len(nums)<3:
            return solutions
        nums.sort()
        length = len(nums)

        for i in range(length):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = nums[i]*-1
            j = i+1
            k = length -1
            while (j<k):
                if nums[j]+nums[k]==target:
                    re = [nums[i],nums[j],nums[k]]
                    solutions.append(re)
                    j +=1
                    while j<k and nums[j]==nums[j-1]:
                        j +=1
                elif nums[j]+nums[k]<target:
                    j +=1

                else :
                    k -=1

        return solutions
