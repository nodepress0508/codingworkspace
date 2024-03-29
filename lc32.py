"""
32. Longest Valid Parentheses

Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"
Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"
"""
# class Solution:
#     def longestValidParentheses(self, s):
s = ")()())"
if not s or len(s)<=1:
    print (0)
dp = [0]*len(s)
stack = []
for i in range (len(s)):
    if s[i] == '(':
        stack.append(i)
    else:
        if stack:
            p = stack.pop()
            dp[i + 1] = dp[p] + i - p + 1
print (dp)
print (max(dp))