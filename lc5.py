"""
5. Longest Palindromic Substring

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         ans = ''
#         for i in range(len(s)):
#             #odd case 
#             tmp = self.helper(s,i,i)
#             if len(tmp)>len(ans):
#                 ans = tmp
#             #even case
#             tmp = self.helper(s,i,i+1)
#             if len(tmp)>len(ans):
#                 ans = tmp
#         return ans 
#     def helper(self,s,l,r):
#         while l>=0 and r<len(s) and s[l]==s[r]:
#             l-=1
#             r+=1
#         return s[l+1:r]

class Solution:
    def longestPalindrome(self, s):
        ans = ""
        for i in range(len(s)):
            # odd case, like "aba"
            tmp = self.helper(s, i, i)
            print ("oddtmp",tmp)
            if len(tmp) > len(ans):
                ans = tmp
                
            # even case, like "abba"
            tmp = self.helper(s, i, i+1)
            # print ("eventmp",tmp)
            if len(tmp) > len(ans):
                ans = tmp
        return ans


    #helper will get the longest palindrome l, r are the middle indexes, from inner to outer
    def helper(self,s,l,r):
        print (l,r)
        while l >=0 and r < len(s) and s[l] == s[r]:
            l-=1
            r+=1
            print (l,r)
        return s[l+1:r]
        
# class Solution(object):
#     def longestPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """

#         res = ""
#         for i in range(len(s)):
#             res = max(self.helper(s,i,i), self.helper(s,i,i+1), res, key=len)

#         return res
       
        
#     def helper(self,s,l,r):
        
#         while 0<=l and r < len(s) and s[l]==s[r]:
#                 l-=1; r+=1
#         return s[l+1:r]
s = "babad"
a = Solution()
b = a.longestPalindrome(s)
print (b)