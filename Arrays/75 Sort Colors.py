# https://leetcode.com/problems/sort-colors/

# Two pass
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a=b=c=0
        for i in range(len(nums)):
            if nums[i]==0:
                a+=1
            elif nums[i]==1:
                b+=1
            else:
                c+=1
        for i in range(len(nums)):
            if i<a:
                nums[i]=0
            elif i<a+b:
                nums[i]=1
            else:
                nums[i]=2


# One Pass
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low=mid=0
        high=len(nums)-1
        while(mid<=high):
            if nums[mid]==0:
                nums[low],nums[mid]=nums[mid],nums[low]
                mid+=1
                low+=1
            elif nums[mid]==1:
                mid+=1
            else:
                nums[high],nums[mid]=nums[mid],nums[high]
                high-=1
 
"""
time->O(n)
space->O(1)
"""
