"""
50. Pow(x, n)

Implement pow(x, n), which calculates x raised to the power n (i.e. xn).

 

Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000
Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100
Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
 
"""
"""
解題思路:
    令:
    注意 n 可能是负数, 需要求一下倒数, 可以在一开始把x转换成倒数, 也可以到最后再把结果转换为倒数.
    那么现在我们实现 pow(x, n), n 是正整数的版本:
    二分即可: 有 x^n=x^n/2∗x^n/2
    , 因此可以在 O(logn) 的时间复杂度内实现.
    又叫快速幂. 有递归实现和循环实现的版本.
    此題如果是用python 解題 有pow()的函數可以直接使用,不過不確定時間複雜度是什麼

算法流程：
    
時空複雜度:
    時:O(logn)
    空:O(1) 沒有開闢額外空間

"""
class Solution:
    def myPow(self, x: float, n: int) -> float:
        # 處理當N是負數的情況,按照題目給的範例去寫出
        if n < 0:
            x = 1 / x 
            n = - n
        #如果N為0直接返回1
        if n == 0:
            return 1 
        #快速幂,用遞規實現
        if n % 2 == 0:
            tmp = self.myPow(x, n // 2)
            return tmp * tmp 
        else:#n 是奇數 最後要多呈上一個自己X
            tmp = self.myPow(x, n // 2)
            return tmp * tmp * x