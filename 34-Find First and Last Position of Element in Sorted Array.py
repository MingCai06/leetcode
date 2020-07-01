"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]


Constraints:

0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
nums is a non decreasing array.
-10^9 <= target <= 10^9
"""

"""
Solution-- Binary Search
Because the array is sorted, we can use binary search to locate the left and rightmost indices.
https://leetcode.com/articles/find-first-and-last-position-element-sorted-array/
"""

class Solution:
    def find_start_end(self, nums,target,left):
        N = len(nums)
        l,r = 0, N-1


        while r >l:
            mid = (l+r)//2

            if target < nums[mid] or(left and target == nums[mid]):
                r = mid
            else:
                l = mid +1
        return l

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # deal with special case which its' length less than 3. That means, no middle.
        if len(nums) <3 and target in nums:
            idx = []
            for i in range(len(nums)):
                if nums[i]==target:
                    if len(idx)<2:
                        idx.append(i)
                    else:
                        if i<idx[0]:
                            idx[0]=i
                        if i > idx[1]:
                            idx[1]=i

        # if there only one item in the nums
        if len(idx)==1:
            idx.append(idx[0])
        return idx

        # Normal case
        # step 1: find the left index using left==True
        left_idx = self.find_start_end(nums,target,True)

        # if left_idx is satisfied the clause?
        if left_idx == len(nums) or nums[left_idx] != target:
            return[-1,-1]
        else:
            # find the right_idx
            right_idx =  self.find_start_end(nums,target,False)
            if nums[right_idx]!=target:
                right_idx -=1

        return[left_idx,right_idx]
