# https://leetcode.com/problems/next-permutation/

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        i2=0
        for i in range(len(nums)-1,-1,-1):
            if nums[i]>nums[i-1] and i>0:
                i2=i
                for j in range(i+1,len(nums)):
                    if nums[i-1]<nums[j]<=nums[i2]:
                        i2=j
                nums[i-1],nums[i2]=nums[i2],nums[i-1]
                nums[i:]=nums[len(nums)-1:i-1:-1]
                return
        nums.reverse()
        return
      
"""
Time complexity : O(n)O(n). In worst case, only two scans of the whole array are needed.
Space complexity : O(1)O(1). No extra space is used. In place replacements are done.
"""
