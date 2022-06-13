# https://leetcode.com/problems/pascals-triangle/

class Solution:
    def generate(self, numRows: int):
        result=[[1]]
        for i in range(1,numRows):
            result.append([1])
            for j in range(len(result[i-1])-1):
                result[i].append(result[i-1][j]+result[i-1][j+1])
            result[i].append(1)

        return result
      
      
class Solution:
    def generate(self, n: int) -> List[List[int]]:
        ans = [[1]*i for i in range(1, n+1)]
        for i in range(1, n):
            for j in range(1, i):
                ans[i][j] = ans[i-1][j] + ans[i-1][j-1]
        return ans
      
"""
Time Complexity : O(n2)
Space Complexity : O(n2)
"""
