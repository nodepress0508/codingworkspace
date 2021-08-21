"""
76. Minimum Window Substring

Given two strings s and t, return the minimum window in s which will contain all the characters in t. If there is no such window in s that covers all characters in t, return the empty string "".

Note that If there is such a window, it is guaranteed that there will always be only one unique minimum window in s.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Example 2:

Input: s = "a", t = "a"
Output: "a"
 

Constraints:

1 <= s.length, t.length <= 105
s and t consist of English letters.
"""
"""
解題思路:
屬於滑動窗口的經典題Sliding Window
題目要求最小窗戶的子字符串,看範例似乎不用按照順序
使用同向雙指針套用模板
本题采用滑窗法，滑窗法是双指针技巧，指针left和right分别指向窗口两端，从左向右滑动，
实施维护这个窗口。我们的目标是找到source中涵盖target全部字母的最小窗口，即为最小覆盖子串。

時空複雜度:
    時:O(n)n为字符串source的长度。
    空:O(n)

"""
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #corner case
        if not s: return ""
        #get tartget hashmap 
        targethash = self.getTargetHash(t)
        #count the unique key in hash
        targetUniqueChars = len(targethash)
        matchedUniqueChars = 0

        hash = {}
        #同向雙指針模板
        j = 0
        n = len(s)
        minlen = float('inf')
        miniumwindowstring = ""
        for i in range (n):
            #當j < n ,找到的字符小於目標字符
            while j < n and matchedUniqueChars < targetUniqueChars:
                #if char is what we looking 
                if s[j] in targethash:
                    #record that char in our dict
                    hash[s[j]] = hash.get(s[j], 0) + 1
                    #if the it meets the total number of targethash
                    if hash[s[j]] == targethash[s[j]]:
                        matchedUniqueChars += 1
                #move the fast pointer to the next one 
                j += 1 


            #當exit while loop 的時候可能已經找到一解了
            #the current substring is valid and length is smaller than previous one 
            if j - i + 1< minlen and matchedUniqueChars == targetUniqueChars:
                # print (i,j)# j 會在valid substring的右手邊
                minlen = j - i + 1
                miniumwindowstring = s[i:j]
            #準備移動慢指針
            #該char in targethash
            if s[i] in targethash:
                #在當前字典內的數量等於目標的數量
                if hash[s[i]] == targethash[s[i]]:
                    matchedUniqueChars -= 1 
                hash[s[i]] -= 1 

        return miniumwindowstring

    def getTargetHash(self, t):
        hash = {}
        for i in t:
            hash[i] = hash.get(i, 0) + 1
        return hash
#===test===
s = "ADOBECODEBANC"
t = "ABC"
sol = Solution()
ans = sol.minWindow(s,t)
print (ans)