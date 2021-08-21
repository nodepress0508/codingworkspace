"""
85. Maximal Rectangle

Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Example:

Input:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
Output: 6
"""
"""
intuition:
this question is the follow up question of lc.84 Largest Rectangle in Histogram
we iterate row by row, if each element in row is 1 means height is one
in the next row, if we encounter 1 then we add the sum from from previous same loc +1
since it's similiar to lc.84 so basically we can use the same concept(function) apply in this question
"""
# class Solution(object):
#     def maximalRectangle(self, matrix):
#         """
#         :type matrix: List[List[str]]
#         :rtype: int
#         """
matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
if not matrix or not matrix[0]:
    print(0) 
maxarea = 0
dp = [0] * (len(matrix[0])+1)
# print (dp)
for row in (matrix):
  for col in range (len(matrix[0])):
      dp[col] = dp[col] + 1 if row[col] == '1' else 0
  stack = [-1]
  for i in range (len(matrix[0])+1):
    while dp[i]<dp[stack[-1]]:#top of stack
      h = dp[stack.pop()]
      w = i-1-stack[-1]
      maxarea = max(maxarea,h*w)
    stack.append(i)
print (maxarea)
    
