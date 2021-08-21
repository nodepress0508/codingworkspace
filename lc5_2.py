"""
5. Longest Palindromic Substring

Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
Example 3:

Input: s = "a"
Output: "a"
Example 4:

Input: s = "ac"
Output: "a"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters (lower-case and/or upper-case),
"""

"""
解题思路:
由回文串正序和反序的性质相同，可以得出一个性质，如果一个字符串，其中心不是回文串，那么它一定不是个回文串。
所以我们每次从中心开始，向两边延展首尾，判断是否是回文串。

代码思路
1.枚举中心 center，需要两个指针 start， end。
2.如果 s[start] == s[end]，则 start--，end++，更新答案
3.重复上一步，直到不相等就停止。
4.注意：奇数和偶数长度的回文串是不同的，奇数中心是单独的一个字符，偶数的是相邻的两个字符。

算法：背向双指针
    時:O(n^2) 枚举回文中心，复杂度 O(n)。向两边延展并 check，复杂度 O(n)。总时，时间复杂度为 O(n^2)。
    空:O(1)不需要额外变量，空间复杂度为 O(1)。

"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s: return ""
        
        #重点2：用空行区分开异常检测部分，核心代码部分，和返回值部分
        longest = ""
        for middle in range (len(s)):
            # 重点3：子函数化避免重复代码
            # 回文奇数情况
            sub = self.find_palindrome_from(s, middle, middle)
            # 重点4：通过返回值来避免使用全局变量这种不好的代码风格
            if len(sub) > len(longest):
                longest = sub
            # 回文是偶数情况
            sub = self.find_palindrome_from(s, middle, middle + 1)
            if len(sub) > len(longest):
                longest = sub


                # 重点2：用空行区分开异常检测部分，核心代码部分，和返回值部分，属于高端代码风格技巧
        return longest

    def find_palindrome_from(self, s, left, right):
        #確認邊界
        # 重点5：将复杂判断拆分到 while 循环内部，而不是放在 while 循环中，提高代码可读性
        while left >= 0 and right < len(s):
            if s[left] != s[right]:
                break
            left -= 1
            right += 1
        #return valid plainfrom which is from left+1 to right - 1
        #while sting slicing s[left + 1:right], the last index will not be included
        return s[left + 1:right]