"""
72. Edit Distance

Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
"""

"""
intuition:
both memoized and DP sol 
TC:O(mn)
SC:O(mn)
where m and n are the lengths of word1 and word2, respectively
ref:
https://leetcode.com/problems/edit-distance/discuss/159295/Python-solutions-and-intuition
"""
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        """
        DP solution
        """
        word1 = "intention"
        word2 = "execution"

        m = len(word1)
        n = len(word2)
        #create table
        dp = [[0] *(n+1) for _ in range(m+1)]
        #filling up first column
        for i in range (m+1):
            dp[i][0] = i
        #filling up first row 
        for j in range (n+1):
            dp[0][j] = j

        #start calculating table
        for i in range (1,m+1):
            for j in range (1,n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1+ min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])

        return (dp[-1][-1])