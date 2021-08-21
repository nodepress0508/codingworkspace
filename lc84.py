"""
84. Largest Rectangle in Histogram

Given n non-negative integers representing the histogram's bar height where the width of each bar is 1,
find the area of largest rectangle in the histogram.
"""
"""
intuition:
the stack maintain the indexes of each bar with ascending height
we are solving the question from following steps 
1. add to stack if current value is equal or bigger than top of stack
2. otherwise keep removing from stack until a number which is smaller or equal than current found
3. calculate area every time you remove 
    if (stack is empty):
        area = height[top]*i
    else:
        area height[top]*(i-stacktop-1) #top of stack would be extract from stack[-1]
TC:O(n)
SC:O(n)
ref:
https://www.youtube.com/watch?v=ZmnqCZp9bBs
"""
# class Solution:
#     def largestRectangleArea(self, heights: List[int]) -> int:
height = [2,1,5,6,2,3]
height.append(0)
stack = [-1]
ans = 0
for i in range(len(height)):
    while height[i] < height[stack[-1]]:#when the value is less than top of stack, we have to start the calculation
        h = height[stack.pop()]
        w = i - stack[-1] - 1
        ans = max(ans, h * w)
    stack.append(i)
height.pop()
print(ans)