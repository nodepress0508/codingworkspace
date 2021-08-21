"""
7. Reverse Integer

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. 
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""
"""
Time Complexity: O(log(x)). There are roughly log 10(x) digits in x.
Space Complexity: O(1).
"""
class Solution:
    def reverse(self, x: int) -> int:
        ans = int(str(abs(x))[::-1])
        if ans.bit_length() < 32:#check the lengh after transfer the int number into binary
            return (-ans if x < 0 else ans)  
        else:#if overflow return 0
            return (0)