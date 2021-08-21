"""
63. Unique Paths II

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?
"""
#PT:DP
"""
inutition:
1.since the robot only can go right or go left, so we iterate it from the first row, first column, second row, second column...etc
2.if the start point is an obsacle then we simply return 0
3.during the first visit we iterate first row and set it to 1 
set the robot start spot to one

TC:O(M*N)
SC:O(1)
"""
# class Solution(object):
#     def uniquePathsWithObstacles(self, obstacleGrid):
#         """
#         :type obstacleGrid: List[List[int]]
#         :rtype: int
#         """

obstacleGrid=[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
m = len(obstacleGrid)
n = len(obstacleGrid[0])
if obstacleGrid[0][0]==1:
    print (0)
else:#set set the  start point to 1 
    obstacleGrid[0][0]=1
#iterate first column 
for i in range (1,m):#move down
    obstacleGrid[i][0] = int(obstacleGrid[i-1][0] == 1 and obstacleGrid[i][0] == 0)
# print (obstacleGrid)#fd
#iterate the first row 
for j in range (1,n):#move right
    obstacleGrid[0][j] = int(obstacleGrid[0][j-1] == 1 and obstacleGrid[0][j] == 0 )
# print (obstacleGrid)#fd
# start going diagnal 
for i in range (1,m):
    for j in range (1,n):
        if obstacleGrid[i][j]==0:#check right bottom
            obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]#adding righ-top and left bottom
        else:
             obstacleGrid[i][j]=0   
# print (obstacleGrid)#fd
print (obstacleGrid[-1][-1])