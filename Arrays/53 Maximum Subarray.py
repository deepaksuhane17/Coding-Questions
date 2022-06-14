# https://leetcode.com/problems/maximum-subarray/


class Solution:
    def maxSubArray(self, nums) -> int:
        n=len(nums)
        m=nums[0]
        for i in range(n):
            s=0
            for j in range(i,n):
                s+=nums[j]
                if s>m:
                    m=s
        return m

""" TLE
time->O(n^2)
space->O(1)
"""



class Solution:
    def maxSubArray(self, nums) -> int:
        n=len(nums)
        m=nums[0]
        s=0
        for i in range(n):
            s+=nums[i]
            m=max(s,m)
            if s<0:
                s=0
            
        return m

        
class Solution:
    def maxSubArray(self, A):
        curSum = maxSum = A[0]
        for num in A[1:]:
            curSum = max(curSum, 0) + num
            maxSum = max(maxSum, curSum)

        return maxSum
        
        
"""
time->O(n)
space->O(1)
"""
