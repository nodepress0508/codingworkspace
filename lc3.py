"""
3. Longest Substring Without Repeating Characters

Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""
"""
intuition:
1. var to store seen character
2. 
"""

# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
s = "abcabcbb"
dic = {}#key would be char and value would be index
res = 0 
start = 0 
for i , c in enumerate(s):
    if c in dic:
        start = max(start,dic[c]+1)#update start  of string to the next index 
        print ("start",start)
    res = max(res,i-start+1)#check length from start to index of string
    print ("res",res)
    dic[c] = i #update char in the dict
print (res)