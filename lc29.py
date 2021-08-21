"""
29. Divide Two Integers
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero, which means losing its fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.

Note:

Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For this problem, assume that your function returns 231 − 1 when the division result overflows.
 

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = truncate(3.33333..) = 3.
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = truncate(-2.33333..) = -2.
Example 3:

Input: dividend = 0, divisor = 1
Output: 0
Example 4:

Input: dividend = 1, divisor = 1
Output: 1
"""
"""
算法：二分/倍增
此提要注意事先的負數上的處理以及最後整數溢出的處理不能大於2^31
这道题要求不用乘，除和模操作完成除法操作，所以我们考虑使用减法。
不断地减掉除数，直到为0为止，但是这样效率太低，我们考虑使用二分法或者说是倍增法来加速这个过程。

算法思路
不断对除数乘2，直到它恰好比被除数小为止，同时记录乘2的次数cnt。
将被除数减掉加倍后的值，答案加上cnt。

代码思路
下面先讨论一下数据处理时会遇到的一些特殊边界情况：
如果除数为0，则被除数为正时，结果为正无穷，否则为负无穷
如果被除数为0，则返回0
如果被除数为正无穷除数为1或者被除数为负无穷除数为－1，则返回正无穷
如果被除数为正无穷除数为－1或者被除数为负无穷除数为1，则返回负无穷
记录一下结果的符号，对除数和被除数取绝对值。

（python忽略）由于int的范围是-2^31 ~ 2^31-1，当对-2^31取绝对值时会溢出，所以要转换为长整型进行运算。

复杂度分析:
    時間複雜度:O(log(dividend/divisor))
    空間複雜度:O(1)


"""
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        is_negative = False
        #coner case
        #如果除數或是被除數任一方小於0那麼除出來會是負數
        if dividend < 0 and divisor > 0 or dividend > 0 and divisor < 0:
            is_negative = True
        #負數的處理
        if dividend < 0:
            dividend = -dividend
        if divisor < 0:
            divisor = -divisor
        ans = 0 
        
        while dividend >= divisor:
            tmp = divisor
            multipy_cnt = 1
            #get ready to multiple by 2
            while dividend >= tmp:
                ans += multipy_cnt
                dividend -= tmp
                tmp <<= 1#bit operation ,等於乘2
                multipy_cnt <<= 1  #multiply by 2 meaning shift one
        if is_negative:
            return -ans
        #處理溢出由于int的范围是-2^31 ~ 2^31-1，当对-2^31取绝对值时会溢出，所以要转换为长整型进行运算。
        if ans >= 1 << 31:
            ans = (1 << 31) - 1
        return ans 