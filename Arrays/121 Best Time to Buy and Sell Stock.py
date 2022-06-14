# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices) -> int:
        m=0
        for i in range(len(prices)):
            for j in range(i,len(prices)):
                if prices[j]-prices[i]>m:
                    m=prices[j]-prices[i]
        return m
      
"""TLE
time->O(n^2)
space->O(1)
"""

class Solution:
    def maxProfit(self, prices) -> int:
        min_left = prices[0]
        profit=0
        for i in range(len(prices)):
            if min_left>prices[i]:
                min_left=prices[i]
            cost = prices[i]-min_left
            if profit<cost:
                profit = cost
        return profit
      
      
"""TLE
time->O(n)
space->O(1)
"""

class Solution:
    def maxProfit(self,prices):
        left = 0
        right = 1
        max_profit = 0
        while right < len(prices):
            currentProfit = prices[right] - prices[left]
            if prices[left] < prices[right]:
                max_profit =max(currentProfit,max_profit)
            else:
                left = right
            right += 1
        return max_profit
      
"""TLE
time->O(n)
space->O(1)
"""
